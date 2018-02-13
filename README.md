# Train-DS-project

Overview
The data has been split into two groups:<br>
   <ul> <li> training set (train.csv)</li>
    <li>test set (test.csv)</li></ul>
The training set should be used to build your machine learning models. For the training set, we provide the outcome (also <br>known as the “ground truth”) for each passenger. Your model will be based on “features” like passengers’ gender and class.<br> You can also use feature engineering to create new features.<br>
The test set should be used to see how well your model performs on unseen data. For the test set, we do not provide the <br>ground truth for each passenger. It is your job to predict these outcomes. For each passenger in the test set, use the model <br>you trained to predict whether or not they survived the sinking of the Titanic.<br>
We also include gender_submission.csv, a set of predictions that assume all and only female passengers survive, as an example <br>of what a submission file should look like.<br>
Data Dictionary<br>
Variable<br>
Definition<br>
Key<br>
survival<br>
Survival<br>
0 = No, 1 = Yes<br>
pclass<br>
Ticket class<br>
1 = 1st, 2 = 2nd, 3 = 3rd<br>
sex<br>
Sex<br>

Age<br>
Age in years<br>

sibsp<br>
of siblings / spouses aboard the Titanic<br>
<br>
parch<br>
of parents / children aboard the Titanic<br>
<br>
ticket<br>
Ticket number<br>
<br>
fare<br>
Passenger fare<br>
<br>
cabin<br>
Cabin number<br>
<br>
embarked<br>
Port of Embarkation<br>
C = Cherbourg, Q = Queenstown, S = Southampton<br>
Variable Notes<br>
pclass: A proxy for socio-economic status (SES)<br>
1st = Upper<br>
2nd = Middle<br>
3rd = Lower<br>
<br>
age: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5<br>
<br>
sibsp: The dataset defines family relations in this way...<br>
Sibling = brother, sister, stepbrother, stepsister<br>
Spouse = husband, wife (mistresses and fiancés were ignored)<br>
<br>
parch: The dataset defines family relations in this way...<br>
Parent = mother, father<br>
Child = daughter, son, stepdaughter, stepson<br>
Some children travelled only with a nanny, therefore parch=0 for them.<br>
