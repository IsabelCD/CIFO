from charles.charles import Population, Individual
from data.tsp_data import distance_matrix
from random import choices
from copy import deepcopy
from charles.crossover import cycle_xo
from charles.mutation import swap_mutation
from charles.selection import tournament_sel, fps
from data_import import *

def get_fitness(self):
    """A simple objective function to calculate distances
    for the TSP problem.

    Returns:
        int: the total distance of the path
    """
    # Create a dictionary with days as keys and exam codes as values
    #using a dictionary comprehension is more efficient than with an if statement  on a list
    exams_by_day = {}
    for exam in self.representation:
        day = exam[0]["day"]
        code = exam[1]
        exams_by_day.setdefault(day, []).append(code)

    # Convert the dictionary values to a list
    exams_by_day = list(exams_by_day.values())

    # Create an empty list to hold nº students with multiple exams in each day
    student_counts = []

    # Iterate over each sub-list in the result list
    for exam_list in exams_by_day:
        
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
    
    return fitness 


def get_neighbours(self):
    """A neighbourhood function for the TSP problem. Switches
    indexes around in pairs.

    Returns:
        list: a list of individuals
    """
    n = [deepcopy(self.representation) for i in range(len(self.representation) - 1)]

    for count, i in enumerate(n):
        i[count], i[count + 1] = i[count + 1], i[count]

    n = [Individual(i) for i in n]
    return n


# Monkey patching
Individual.get_fitness = get_fitness
Individual.get_neighbours = get_neighbours


pop = Population(
    size=50,
    sol_size=len(distance_matrix[0]),
    valid_set=[i for i in range(len(distance_matrix[0]))],
    replacement=False,
    optim="min")

pop.evolve(gens=500, select=tournament_sel, mutate=swap_mutation, crossover=cycle_xo,
           mut_prob=0.05, xo_prob=0.9, elitism=True)


#hill_climb(pop)
#sim_annealing(pop)

