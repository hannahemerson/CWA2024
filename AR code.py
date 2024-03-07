# This program takes three values from a CSV file and compares them to predict a fourth value
# This is given the fancy name "Multiple Linear Regression".
# It's like a bunch of linear trendlines mashed up together to allow a few more extra variables.

# HOW TO USE:
# Thonny>Tools>Manage Packages and install sklearn, pandas
# Open the CSV file called "your_dataset" in the same folder as this python file
# Replace my columns of data with your data
# Change the titles of each of my columns to your own titles
# Do the same in the code below

# The model which given ABC to predict X then works like this:

# predicted_X_Value = predict_mood(A,B,C)
# print("The predicted value is", predicted_X_Value)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# Training the model

# Load your dataset
data = pd.read_csv('ar.csv')

# Define your independent variables (features) and dependent variable (target)
X = data[['total_income', 'save_goal', 'weekly_save']]
Y = data['prediction']

# Splitting the dataset into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Creating the Linear Regression model
model = LinearRegression()

# Fitting the model with the training data
model.fit(X_train, Y_train)

# Predicting mood scores for the test set
Y_pred = model.predict(X_test)


print("Multiple Linear Regression Model Complete!")


# Checking how well it worked
mse = mean_squared_error(Y_test, Y_pred)
print(f"Mean Squared Error: {mse}")

income = int(input("Enter your income: "))
save = int(input("Enter how much you would like to save: "))
weekly = int(input("Enter how much you will save per week: "))

# Calculation for prediction
prediction = save / weekly

print("Prediction:", prediction)


"""

# WHAT-IF Question 1
# How long will i?
print("-----------------------------------------------------------")
print("WHAT-IF QUESTION 1")
print("Let's test what the mood will be if the sunlight is very low")

# Low values for all 3 parameters
sunlight_hours = 2
average_sunlight = 100
peak = 200

mood_if_littleSun = predict_mood(sunlight_hours, average_sunlight, peak)  # Example values
print("\n The low sun score mood is", mood_if_littleSun)



# WHAT-IF Question 2
# What is will your mood be with high values of all three parameters?
print("-----------------------------------------------------------")
print("WHAT-IF QUESTION 2")
print("Let's test what the mood will be if the sunlight is very high")

# High values for all 3 parameters
sunlight_hours = 15
average_sunlight = 600
peak = 800

mood_if_LoadsaSun = predict_mood(sunlight_hours, average_sunlight, peak)  # Example values
print("\n The higher sun score mood is", mood_if_LoadsaSun)



# WHAT IF QUESTION 3
# What variable is more important
print("-----------------------------------------------------------")
print("WHAT-IF QUESTION 3")
print("Let's test if average sunlight is more important than peak sunlight")
print("We will keep the hours (A) the same and double the others (B) and (C) one at a time")
print("")

print("Let's get a baseline from fairly average values...")

# Baseline 
sunlight_hours = 6
average_sunlight = 300
peak = 300

baseline_mood = predict_mood(sunlight_hours, average_sunlight, peak)  # Example values
print("\n The baseline Score mood is", baseline_mood)
print("")


# Double the average sunlight
print("Let's double the average sunlight...")
sunlight_hours = 6
average_sunlight = 600
peak = 300

doubleAverageOutcome = predict_mood(sunlight_hours, average_sunlight, peak)  # Example values
print("The double sunlight mood is", doubleAverageOutcome)
print("")

# Double the peak sunlight
print("Let's double the peak sunlight...")
sunlight_hours = 6
average_sunlight = 300
peak = 600

doublePeakOutcome = predict_mood(sunlight_hours, average_sunlight, peak)  # Example values
print("The double peak mood is", doublePeakOutcome)
print("")


# PRINTED FEEDBACK

print("OUTCOME:")
if doubleAverageOutcome > doublePeakOutcome:
    print("It's the average that improves mood the most")
else:
    print("It's the peak that improves mood the most")


#------------------------------------
# AR3 Show Results of WHAT IF on a graph for Questions 1 & 2
import matplotlib.pyplot as plt

# Data: names of the variables and their values
variable_names = ['Mood if Little Sun', 'Mood if Loadsa Sun',]
values = [mood_if_littleSun, mood_if_LoadsaSun]

# Creating the bar chart
plt.bar(variable_names, values)

# Adding labels and title
plt.xlabel('Ammount of Sun')
plt.ylabel('Moodiness')
plt.title('Bar Chart of WHAT-IF Q1, Q2 Outcomes')

# Show the plot
plt.show()

#------------------------------------
# AR3 Show Results of WHAT IF on a graph for Question 3
import matplotlib.pyplot as plt

# Data: names of the variables and their values
variable_names = ['How long would it take to save if I double the amount I save per week', 'Mood if Double Peak',]
values = [doubleAverageOutcome, doublePeakOutcome]

# Creating the bar chart
plt.bar(variable_names, values)

# Adding labels and title
plt.xlabel('Ammount of Sun')
plt.ylabel('Moodiness')
plt.title('Bar Chart of WHAT-IF Q3 Outcome')

# Show the plot
plt.show()
"""