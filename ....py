import csv

# Take in 3 wellness indicators
money_wellness = int(input("On a scale of 1-10, from poorly to well, how well do you follow a monthly budget? "))
save_wellness = int(input("On a scale of 1-10, from nothing to a lot, how much of your money do you want to save? "))
mental_wellness = int(input("On a scale of 1-10, from poor to well, how does money affect your mental wellbeing? "))

# Calculate average mood
avg_mood = round((money_wellness + save_wellness + mental_wellness) / 3, 2)

# Writing the data to a CSV file
file_path = 'wellness_data.csv'

with open(file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Writing headers
    csv_writer.writerow(["Money Wellness", "Save Wellness", "Mental Wellness", "Average Mood"])
    
    # Writing data
    csv_writer.writerow([money_wellness, save_wellness, mental_wellness, avg_mood])

print("Data has been saved to", file_path)

file_path = 'wellness_data.csv'

with open(file_path,'r' , newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    
    for row in csv_reader:
        print(row)