from charles.charles import Population, Individual
from charles.crossover import *
from charles.mutation import *
from charles.selection import *
from pop_created import *
from pop_creation import *
import csv


def get_fitness(self):
    # Create a dictionary with days as keys and exams as values
    #using a dictionary comprehension is more efficient than with an if statement  on a list

    # Create an empty list to hold nº students with multiple exams in each day
    student_counts = []
    student_counts_ovenight = []
    exam_by_day = {}

    # Iterate over each sub-list in the result list
    for day, day_keys in hours_keys.items():
        exam_by_day[day] = []
        for key_day in day_keys:
            exam_by_day[day] = exam_by_day[day] + (self.representation[key_day])

    for day, exams in exam_by_day.items():

        # Get the list of students who took the exams on the current day
        students = check_students(exams, [], list_students= True)
        
        # Calculate the difference between the number of students who took the exams and the number of unique students
        diff_d = len(students) - len(set(students))
        diff_o = 0

        if day not in mondays:
            today_students = list(set(students))

            # Get the key for the day before the current day
            previous_day = list(exam_by_day.keys())[list(exam_by_day.keys()).index(day) - 1]

            yesterday_students = check_students(exam_by_day[previous_day], [], list_students = True)

            diff_o = len(today_students+yesterday_students) - len(set(today_students+yesterday_students))


        
        # Add the result to the student_counts list
        student_counts.append(diff_d)
        student_counts_ovenight.append(diff_o)

    # Calculate the fitness as the sum of the student counts
    fitness = sum(student_counts) + 0.5*sum(student_counts_ovenight)
    print(fitness)
    return fitness 


# Monkey patching
Individual.get_fitness = get_fitness


# Step 3: Assign the created Individual instances to the individuals list of the Population instance
pop= Population(size =30, replacement=False, optim= 'min', valid_set= None, initial_pop=population)

alternatives_mutation=[day_swap, timeslot_swap, inversion]
for alternative in alternatives_mutation:
    algorithm_fit= []
    for i in range(30):
        best=[]
        pop.evolve(gens=5, select=tournament_sel, mutate=alternative, crossover=cycle_xo,
            mut_prob=0.05, xo_prob=0.6, elitism=True)
        algorithm.append(best)
    
    with open(f"{alternatives_mutation}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(algorithm)




