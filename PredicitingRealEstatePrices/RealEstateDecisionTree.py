#Author: Nishank Raisinghani###
#Project: Predicting the price of a house in Taiwan using a Decision Tree Regressor model
#We will be training the model using data from UCI
#Link to the dataset: https://archive.ics.uci.edu/ml/datasets/Real+estate+valuation+data+set


#Step 1: Import all needed libraries/frameworks
from __future__ import print_function
from pyspark.ml.regression import DecisionTreeRegressor
from pyspark.sql import SparkSession

from pyspark.ml.feature import VectorAssembler

#Step 2: Create a spark instance
spark = SparkSession.builder.appName("PredicitingRealEstate").getOrCreate()

#Step3: Read the dataset using spark and turn it into a dataframe
#Since the dataset already has headers there is no need for us to use a custom schema, instead we can infer the schema with a built in spark function
inputDF = spark.read.option("header", "true").option("inferSchema", "true").csv("realestate.csv")

#Step 3: Format the dataframe so that we can run the regressor model on it
#This is a very important step because without the right formatted data the regressor will not be able to run
#This combines all of the parameters into one column called "features"
assemble = VectorAssembler().setInputCols(["TransactionDate", "HouseAge", "DistanceToMRT", "NumberConvenienceStores", "Latitude","Longitude"]).setOutputCol("features")
formattedDF = assemble.transform(inputDF).select("PriceOfUnitArea", "features")

##Step 4: split your data into training and testing data
##You always want some data to test with to make sure you have made an accurate model
data = formattedDF.randomSplit([0.5,0.5])
trainData = data[0]
testData = data[0]

#Step 4: Here we actually create and apply the model
#The Decision Tree Regressor doesn't require any hyperparameters so we just pass in the features and the label
DT = DecisionTreeRegressor().setFeaturesCol("features").setLabelCol("PriceOfUnitArea")
model = DT.fit(trainData)

#Step 5: We run the model on the test data and we cache the results for a faster speed next time around
predictions = model.transform(testData).cache()

#Step 6: We convert the data into an rdd so it is printable
#We are going to put the prediction side by side with the actual data to compare the accuracy
extractPredictions = predictions.select("prediction").rdd.map(lambda x: x[0])
actualResults = predictions.select("PriceOfUnitArea").rdd.map(lambda x: x[0])

#Step 7: Zip the results together
finalPredictions = extractPredictions.zip(actualResults).collect()

#Step 8: print out the results
for prediction in finalPredictions:
    print(prediction)
    
spark.stop()
