##################
import pandas as pd
from random import randint, sample
from pop_creation import *
from pop_created import *
import datetime
from charles.crossover import *
from charles.mutation import *
from charles.selection import *
import csv

alternatives_mutation=[day_swap, timeslot_swap, inversion]
for alternative in alternatives_mutation:
    algorithm_fit= []
    best=[]
    for i in range(30):
        best.append(i)
        algorithm_fit.append(best)
    
    with open(f"{alternative.__name__}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(algorithm_fit)




# Sample input data

representation = [
    [{'day': 'Monday', 'time': '10:00am'}, 'exam1'],
    [{'day': 'Monday', 'time': '2:00pm'}, 'exam2'],
    [{'day': 'Tuesday', 'time': '9:00am'}, 'exam3'],
    [{'day': 'Tuesday', 'time': '1:00pm'}, 'exam4'],
    [{'day': 'Wednesday', 'time': '11:00am'}, 'exam5'],
    [{'day': 'Wednesday', 'time': '3:00pm'}, 'exam6'],
]

# Create a dictionary with days as keys and exam codes as values
exams_by_day = {}
for exam in representation:
    day = exam[0]["day"]
    code = exam[1]
    exams_by_day.setdefault(day, []).append(code)

# Convert the dictionary values to a list
result = list(exams_by_day.values())
#print(exams_by_day)

#print("result", result)



# Sample dataframe
df_en = pd.DataFrame({
    'student': ['Alice','Alice', 'Bob', 'Bob','Charlie','Charlie', 'Dave', 'Eve', 'Frank', 'Grace', 'Harry'],
    'exam': ['exam1','exam2', 'exam2', 'exam6','exam3', 'exam4','exam4', 'exam5', 'exam6', 'exam1', 'exam3']
})

# Create an empty list to hold the results
student_counts = []

# Iterate over each sub-list in the result list
for exam_list in result:
    
    # Filter the dataframe to only include rows with the current day's exams
    day_en = df_en[df_en['exam'].isin(exam_list)]
    
    # Get the list of students who took the exams on the current day
    students = list(day_en['student'])
    
    # Calculate the difference between the number of students who took the exams and the number of unique students
    diff = len(students) - len(set(students))
    
    # Add the result to the student_counts list
    student_counts.append(diff)

# Calculate the fitness as the sum of the student counts
fitness = sum(student_counts)

#print(fitness)



representation = [
    [{'day': 'Monday', 'time': '10:00am'}, 'exam1'],
    [{'day': 'Monday', 'time': '2:00pm'}, 'exam2'],
    [{'day': 'Tuesday', 'time': '9:00am'}, 'exam3'],
    [{'day': 'Tuesday', 'time': '1:00pm'}, 'exam4'],
    [{'day': 'Wednesday', 'time': '11:00am'}, 'exam5'],
    [{'day': 'Wednesday', 'time': '3:00pm'}, 'exam6'],
]


#SWAP MUTATION
mut_indiv= representation.copy()
days_indexes = sample(range(0, len(representation)), 2)

# Extract the exam codes to swap
exam_code_1 = mut_indiv[days_indexes[0]][1]
exam_code_2 = mut_indiv[days_indexes[1]][1]

# Swap the exam codes
mut_indiv[days_indexes[0]][1] = exam_code_2
mut_indiv[days_indexes[1]][1] = exam_code_1

#print(mut_indiv)

#DAY SWAP
import datetime
mut_indiv= representation.copy()
[item[0]['day'] for item in representation]
days_indexes = sample([item[0]['day'] for item in representation], 2)
#print(days_indexes)




days_indexes= ['23-01-1995', '24-01-1995', '25-01-1995']

# Convert the date string to a datetime object
for i in days_indexes:
    date_weekday = datetime.datetime.strptime(i, '%d-%m-%Y').weekday()

    if date_weekday==1:
        print('aqui')

