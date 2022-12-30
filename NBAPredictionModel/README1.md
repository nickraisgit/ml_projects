Author: ***Nishank Raisinghani***

Project: ***Predicting the NBA Finals Champion using a regression tree algorithm***

This is a project to predict the final rankings of the NBA using regular season data. I trained a decision tree regression model to learn data from the past 5 years, since the 2014-2015 season. I didn't go back any farther because 2014-2015 was the season when most teams starting attempting about 30 threes a game, and if I went back any farther my model would have preferred teams with a better mid range game rather than teams who shoot better from 3. I then used an ensemble method in XGBoost to make my predictions and model more accurate. This ended up working really well, and helped me figure out the recipe to a championship winning team.