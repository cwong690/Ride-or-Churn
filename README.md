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

![Precision](images/precision.png)

![Recall](images/recall.png)

Where,
TP = True Positive
TN = True Negative  
FP = False Positive
FN = False Negative


**Deliverables:**<br>

How did we compute the target? <br>

The data was taken on July 1, 2014. If a user has not taken a ride in the past 30 days (since June 1, 2014), we consider that user as "churn". We used a pandas dataframe to make a new column called 'churn', where the value 1 is if that user has churned.

![churned](images/churn_calculation.png)

Using this computation, we found that there were about 62% of the sample data that were considered "churn".

We started with some classic exploratory data analysis. We examined the distribution plots of some numerical columns.

![avg_dist](images/avg_dist_distplot.png)

![avg_raing_by_pct](images/avg_rating_by_driver_distplot.png)

![avg_rating_of_pct](images/avg_rating_of_driver_distplot.png)

![surge_pct](images/surge_pct_distplot.png)

![avg_surge_pct](images/avg_surge_distplot.png)

![trips_30](images/trips_in_first_30_days_distplot.png)


What model did you use in the end? Why? <br>

We used a Voting Classifier. All of our models were found to have not-so-great accuracies, so we combined them in a voting classifier to try to increase our scores.

For the Voting Classifier, on the final testing set:

![Voting Classifier](images/voting_classifier.png)

ROC curve and area under curve:

![Voting Classifier ROC](images/voting_classifier_roc.png)


![Voting Classifier AOC](images/voting_class_aoc.png)

Alternative models you considered? Why are they not good enough? <br>

Considered a Random Forest Classifier and using a 10 K-Fold split with the training data:

![Random Forest](images/random_forest.png)

The Random Forest ROC Curve was plotted and ROC area under curve was found. The ROC Score was found to be 0.711.

![Random Forest ROC](images/random_forest_roc.png)

Considered a Logistic Regression Classifier and using a 3 K-Fold split with the training data:

![Logistic Regression](images/logistic_regression.png)

Not great.

Considered a Bagging Classifier and using a 3 K-Fold split with the training data:

![Bagging Classifier](images/bagging.png)

Also considered a gradient boosting classifier. The gradient boosting classifier performed poorly when compared to the random forest classifier. Using gridsearch, more optimal hyperparameters were found, but this method is CPU intensive and time consuming. Looking at the MSE for two different learning rates for the testing and training data as function of the number of decision trees, it is clear that a learning rate of 0.08 performed better than 0.02:

![gb_lr](images/gbc_lr.png)

And comparing this to the random forest classifier, it appears that the MSE is slightly better.

![gb_rf](images/gbc_rf.png)

Compared to the bagging classifier, the accuracy is the same,but precision went up a bit and recall went down slightly.

![gb scores](images/gb_scores.png)




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




Future Work:

Drop some of very unimportant columns that we find

Do some feature engineering and look into linear regression

Dive into more of the reprussions of precision, accuracy, and recall for this problem.

Clean up files within project.