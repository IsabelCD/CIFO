from charles.charles import Population, Individual
from charles.crossover import *
from charles.mutation import *
from charles.selection import *
from pop_created import *
from pop_creation import *
import csv


def get_fitness(self):
    # Create a dictionary with days as keys and exams as values
    # using a dictionary comprehension is more efficient than with an if statement  on a list

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
        students = check_students(exams, [], list_students=True)

        # Calculate the difference between the number of students who took the exams and the number of unique students
        diff_d = len(students) - len(set(students))
        diff_o = 0

        if day not in mondays:
            today_students = list(set(students))

            # Get the key for the day before the current day
            previous_day = list(exam_by_day.keys())[list(exam_by_day.keys()).index(day) - 1]

            yesterday_students = check_students(exam_by_day[previous_day], [], list_students=True)

            diff_o = len(today_students + yesterday_students) - len(set(today_students + yesterday_students))

        # Add the result to the student_counts list
        student_counts.append(diff_d)
        student_counts_ovenight.append(diff_o)

    # Calculate the fitness as the sum of the student counts
    fitness = sum(student_counts) + 0.5 * sum(student_counts_ovenight)
    # print(fitness)
    return fitness


# Monkey patching
Individual.get_fitness = get_fitness


# the following function takes the alternatives we are testing and the factor we are testing (tournament, mutation or crossover)
# and runs the algorithm 10 times for each, saving it in a csv file.
def comparison(alternatives_list, factor):
    for alternative in alternatives_list:
        algorithm_fit = []
        for i in range(10):
            print(30 * "-", f"In iteration {i} of {alternative.__name__}", 30 * "-")
            pop = Population(size=30, replacement=False, optim='min', valid_set=None, initial_pop=population)
            if factor == "mutation":
                best = pop.evolve(gens=30, select=tournament_sel, mutate=alternative, crossover=cycle_xo,
                                  mut_prob=0.05, xo_prob=0.6, elitism=True)
            elif factor == "crossover":
                best = pop.evolve(gens=30, select=tournament_sel, mutate=day_swap, crossover=alternative,
                                  mut_prob=0.05, xo_prob=0.6, elitism=True)
            else:
                best = pop.evolve(gens=30, select=alternative, mutate=day_swap, crossover=cycle_xo,
                                  mut_prob=0.05, xo_prob=0.6, elitism=True)
            algorithm_fit.append(best)

        with open(f"{alternative.__name__}.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(algorithm_fit)


# Mutation
# alternatives_mutation=[timeslot_swap, inversion, day_swap]
# comparison(alternatives_mutation, "mutation")

# Selection
# alternatives_sel=[cycle_xo, single_point_slots_co, order_timeslots_crossover]
# comparison(alternatives_sel, "crossover")

# Selection
# alternatives_xo=[tournament_sel, fps, ranking_sel]
# comparison(alternatives_sel, "selection")

## Best model fine-tuning
"""algorithm_fit= []
for i in range(10):
            print(30*"-", f"In iteration {i} of best", 30*"-")
            pop= Population(size =30, replacement=False, optim= 'min', valid_set= None, initial_pop=population)
            best = pop.evolve(gens=60, select=tournament_sel, mutate=inversion, crossover=cycle_xo,
                mut_prob=0.05, xo_prob=0.6, elitism=True)             
            algorithm_fit.append(best)
        
with open(f"best.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(algorithm_fit)"""
