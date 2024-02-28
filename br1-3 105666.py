#import statements here
import pandas as pd
from statistics import mean
import csv
import serial
from time import sleep


#function to give a remark on my mood based on avg_mood value
def interpret_mood(avg_mood):
    if avg_mood >= 9:
        return "Excellent mood today, thank god"
    elif avg_mood <  5:
        return "Okay today, thanks for asking"
    elif 5 <= avg_mood < 9:
        return "Improving thanks."
    else:
        return "Not really sure, not enough info \n"



#Take in 3 wellness indicators
#Take them in as integers, as all inputs default to strings
money_wellness = int(input("On a scale of 1-10, from poorly to well, how well do you follow a monthly budget? "))
save_wellness = int(input("On a scale of 1-10, from nothing to a lot, how much of your money do you want to save? "))
mental_wellness = int(input("On a scale of 1-10, from poor to well, how does money effect your mental wellbeing? "))
avg_mood = round(mean([money_wellness,save_wellness,mental_wellness]),2)
mood_remark = interpret_mood(avg_mood)
print("My Average mood today is ",mood_remark, " ", avg_mood)

file_path = '105666.csv'

with open(file_path,'r' , newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    
    for row in csv_reader:
        print(row)
        
""" 
df = pd.read_csv('hannah.csv')
print(df)
# Convert 'Timestamp' column to datetime, is it necessary
#df['time (seconds)'] = pd.to_datetime(df['time (seconds)'], errors='coerce')
light_min = df['Light'].min()
light_max = df['Light'].max()
light_mean = df['Light'].mean()
print (light_min,light_max,light_mean, avg_mood)

f = open("hannah.csv", "a", newline='')
csver = csv.writer(f)
#csver.writerow(["light_min", "light_max", "light_mean", "avg_mood"])
csver.writerow([light_min, light_max, light_mean, avg_mood])

f.close()
"""