## Battle of the Churns

Can we predict a user will 'churn' better than you?


![Ride Share Header](images/ride_share_logo.jpg)


### Contributors
|  [Cindy Wong](https://github.com/cwong690)  |
 [Tyler Woods](https://github.com/tylerjwoods)  |
 [Nathan Rasmussen](https://github.com/rasbot)  |
   
---

## Introduction

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


What model did you use in the end? Why? <br>



Alternative models you considered? Why are they not good enough? <br>

Considered a Random Forest Classifier and using a 10 K-Fold split with the training data:

![Random Forest](images/random_forest.png)