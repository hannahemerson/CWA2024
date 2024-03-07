import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the wellbeing dataset
df = pd.read_csv('ar.csv')

# Perform exploratory data analysis
print(df.head())
print(df.describe())

# Preprocess the data (handle missing values, encode categorical variables, etc.)
# For demonstration purposes, let's assume the dataset is already preprocessed

# Split the data into training and testing sets
X = df.drop('weekly_save', axis=1)  # Features
y = df['prediction']  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print("Training R^2 Score:", train_score)
print("Testing R^2 Score:", test_score)

# Predict wellbeing scores for the test set
y_pred = model.predict(X_test)

"""
# Visualize actual vs. predicted wellbeing scores
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Wellbeing Score")
plt.ylabel("Predicted Wellbeing Score")
plt.title("Actual vs. Predicted Wellbeing Scores")
plt.show()
"""
"""
# 'What If' Scenario 1: What if average sleep duration increases by 1 hour?
# Update the test data accordingly and predict the new wellbeing scores
X_test_scenario1 = X_test.copy()
X_test_scenario1['double_prediction'] += 1 
y_pred_scenario1 = model.predict(X_test_scenario1)
print("Scenario 1 - What I double the amount I save per week?:", y_pred_scenario1)
"""
