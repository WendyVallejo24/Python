# Import the train_test_split function and uncomment
from sklearn.model_selection import train_test_split


# ----- Step 1: Split Your Data -----
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

# ----- Step 2: Specify and Fit the Model -----
# You imported DecisionTreeRegressor in your last exercise
# and that code has been copied to the setup code above. So, no need to
# import it again
from sklearn.tree import DecisionTreeRegressor

# Specify the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit iowa_model with the training data.
iowa_model.fit(train_X, train_y)


# ----- Step 3: Make Predictions with Validation data -----
# Predict with all validation observations
val_predictions = iowa_model.predict(val_X)

# print the top few validation predictions
print(val_predictions[0:5])

# print the top few actual prices from validation data
print(val_y[0:5])

# ----- Step 4: Calculate the Mean Absolute Error in Validation Data -----

from sklearn.metrics import mean_absolute_error
val_mae = mean_absolute_error(val_y, val_predictions)
print(val_mae)
