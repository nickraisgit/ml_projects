Author: ***Nishank Raisinghani***


Project: ***Using multiple machine learning techniques to predict and classify the quality of wine***

This project is just using the same dataset in a number of different ways to basically try and get the same answer and see which answer is the best. I am splitting up the quality into good and bad and I tried multiple classification systems to predict this. I used a sigmoid classification in XGBoost as well as a softmax model as well. I noticed that both basically had the same amount of accuracy, which was expected. 

I also used a supervised support vector cluster to examine this data as well, and the sigmoid kernel in this case turned out to be a much lower accuracy than the rbf kernel or even the polynomial kernel. In conclusion, when using support vector machines, even on binary labels, it is better to use a rbf or a polynomial kernel due to the fact that the sigmoid kernel underfits a lot. I do think that in most cases it is better to use XGBoost, especially when using supervised data, but when you have higher dimension features either one is good.   