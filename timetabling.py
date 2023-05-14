from charles.charles import Population, Individual
from charles.search import hill_climb, sim_annealing
from data.tsp_data import distance_matrix
from random import choices
from copy import deepcopy
from charles.crossover import cycle_xo
from charles.mutation import swap_mutation
from charles.selection import tournament_sel, fps
from data_import import *

# Sample input data
representation = [
    [{'day': 'Monday', 'time': '10:00am'}, 'exam1'],
    [{'day': 'Monday', 'time': '2:00pm'}, 'exam2'],
    [{'day': 'Tuesday', 'time': '9:00am'}, 'exam3'],
    [{'day': 'Tuesday', 'time': '1:00pm'}, 'exam4'],
    [{'day': 'Wednesday', 'time': '11:00am'}, 'exam5'],
    [{'day': 'Wednesday', 'time': '3:00pm'}, 'exam6'],
]

exams_by_day = {}
for exam in representation:
    day = exam[0]["day"]
    code = exam[1]
    if day in exams_by_day:
        exams_by_day[day].append(code)
    else:
        exams_by_day[day] = [code]

result = list(exams_by_day.values())


print(result)
# Output: [['exam1', 'exam2'], ['exam3', 'exam4'], ['exam5', 'exam6']]


room_capacity = df_en['exam'].value_counts()[df_exam.loc[i][0]]

def get_fitness(self):
    """A simple objective function to calculate distances
    for the TSP problem.

    Returns:
        int: the total distance of the path
    """
    fitness = 0
    for time, room in self.representation:
        

        fitness= i + j

    
    for i in range(len(self.representation)):
        fitness += distance_matrix[self.representation[i - 1]][self.representation[i]]
    return int(fitness)


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

