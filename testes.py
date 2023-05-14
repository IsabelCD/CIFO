"""import pandas as pd

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

# Sample dataframe
df_en = pd.DataFrame({
    'student': ['Alice','Alice', 'Bob', 'Bob','Charlie','Charlie', 'Dave', 'Eve', 'Frank', 'Grace', 'Harry'],
    'exam': ['exam1','exam2', 'exam2', 'exam6','exam3', 'exam4','exam4', 'exam5', 'exam6', 'exam1', 'exam3']
})

# Create a dictionary that maps each exam to a set of unique students who took that exam
students_by_exam = {exam: set(students) for exam, students in df_en.groupby('exam')['student']}

# Create an empty list to hold the results
student_counts = []

# Iterate over each sub-list in the result list
for exam_list in result:
    
    # Get the list of students who took the exams on the current day
    students = [student for exam in exam_list for student in students_by_exam[exam]]
    
    # Calculate the difference between the number of students who took the exams and the number of unique students
    diff = len(students) - len(set(students))
    
    # Add the result to the student_counts list
    student_counts.append(diff)

# Calculate the fitness as the sum of the student counts
fitness = sum(student_counts)

print(fitness)"""



##################
import pandas as pd

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

print("result", result)



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

print(fitness)
