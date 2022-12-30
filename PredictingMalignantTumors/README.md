***Author: Nishank Raisinghani***

Date: ***04/2021***

***Project: Using Multiple Machine Learning Methods to see which one has the best Accuracy***
In this project I am using 7 different machine learning methods to try and accurately predict whether a tumor is malignant or benign using descriptive data of the tumor, such as size, shape, margin, and density.

I am using a decision tree classifier, random forest classifier, XGBoost classifier, K Nearest Neighbors method, Naive Bayes Method, Support Vector Clustering and finally a deep learning neural network with Keras.

I use K fold cross validation on all of these to see the accuracy of these models and to see which method is the most accurate. At the end we come up with a conclusion that there is no clear cut best model for this data, but instead a clear cut worst, which is the basic decision tree. Obviously, the other methods are much better suited for higher dimension vectors and we can see that in this experiment. 