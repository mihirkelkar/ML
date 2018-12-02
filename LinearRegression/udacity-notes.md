Linear Regression.

Basic concepts:
A model in this case is to find a line that can best fit your dataset.
Assuming that the data that you have follows a linear patterns.

 ŷ = wx + b

Square Trick
The square trick here is to get a learning rate (α) and to find
the distance between a point you're trying to fit in the model

 ŷ = wx + b is the model. In order to move this model fit a point better.

We can change it to (w + α(|y -  ŷ|)) + (b + α|y -  ŷ|)

Regulatization
A single line can fit two data points in a linear regression model. However
infinte polynomial regression models can fit those two points. We need to find
a way to incentivize generalized algorithms and simple models. We do this
by adding the co-efficients of the model to the error. So the higher the
co-efficients the more the error.


L1 Regulatization:
Adding the absolute value of co-efficients to the error calculation

L2 Regulatization:
Adding the square of the value of co-efficients to the error calculations.


Feature Scaling :
Normalizing the features to one standardized range. 
