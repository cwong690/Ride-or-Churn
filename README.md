## Battle of the Churns

Can we predict a user will 'churn' better than you?


![Ride Share Header](images/ride_share_logo.jpg)


### Contributors
|  [Cindy Wong](https://github.com/cwong690)  |
 [Tyler Woods](https://github.com/tylerjwoods)  |
 [Nathan Rasmussen](https://github.com/rasbot)  |
   
---

**Main Goal:** <br>
Predict if a ride-share user will churn (that is, not be active within the past 30 days). <br>

*Note: This info is sourced from a ride-sharing company (Company X) and is interested in predicting rider retention*

**Evaluation:**<br>
The evaluation of our model will be based on Accuracy, Recall, and Precision.<br>
![Accuracy](images/accuracy1.png)

![Recall](images/recall.png)

![Precision](images/precision.png)

**Deliverables:**<br>

How did we compute the target? <br>

The data was taken on July 1, 2014. If a user has not taken a ride in the past 30 days (since June 1, 2014), we consider that user as "churn". We used a pandas dataframe to make a new column called 'churn', where the value 1 is if that user has churned.

![churned](images/churn_calculation.png)

Using this computation, we found that there were about 62% of the sample data that were considered "churn".


What model did you use in the end? Why? <br>



Alternative models you considered? Why are they not good enough? <br>

Considered a Random Forest Classifier and using a 10 K-Fold split with the training data:

![Random Forest](images/random_forest.png)

The Random Forest ROC Curve was plotted and ROC area under curve was found. The ROC Score was found to be 0.711.

![Random Forest ROC](images/random_forest_roc.png)


Based on insights from the model, what plans do you propose to reduce churn?

Using feature importance of the random forest model, we found the following feature importances:

![Random Forest Feature Importances](images/random_forest_feature_importance.png)

It appears that Average Rating by Driver, Average Surge, and Surge Percentage have the most importance. 

Diving into Average Surge, it appears that if the user had a higher average surge, then they were more likely to churn.

![Average Surge](images/average_surge.png)

The most obvious way to limit the amount of churning: STOP SURGING!!!
Also, could limit surges on people; i.e., if a user is continually being surged, give them a break here and there.

What are the potential impacts of implementing these plans or decisions? 

If you implement limiting surging on specific individuals, you're obviously going to be generating less money.

What performance metrics did you use to evaluate these *decisions*, why?