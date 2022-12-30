***Author: Nishank Raisinghani***
***Project: Creating Average Yards Over Expected(YOE) and using it to look at how good each offense is***


For this project I am using the nflfastr dataset and using down, yardline, yards to go, time remaining, and score differential as features for this model. We will create a data point called Yards Over Expected by predicting the amount of yards a team would get based on those features using a simple Deep Learning model. We will use this data point to compare it with the amount of yards gained, creating a final point of Yards Over Expected. This will show how good an offense is compared to league average. I am using data from the past 3 years to train this model.

The article corresponding to this code can be found on my Medium at https://nishank-r.medium.com/creating-yards-over-expected-and-using-it-to-measure-offenses-in-the-nfl-64b12faada41. Please take some time to read it as it will make more sense of the code and the purpose behind this project

The article mentioned above was written after week 8 of the NFL Season. This notebook will keep updating over time meaning that the results in this notebook will not completely correspond with the article, but there will obviously be continuation as it continues to process data from the season