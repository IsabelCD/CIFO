from charles.charles import Population, Individual
from charles.crossover import single_point_slots_co
from charles.mutation import binary_mutation
from charles.selection import tournament_sel
from pop_created import *
from pop_creation import *


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






population_size = len(population)
pop = Population(size=population_size, optim="min", sol_size=len(population[0]), replacement=False, valid_set=population[0])
pop.individuals = [Individual(representation=representation) for representation in population]
print(pop)


pop.evolve(gens=50, select=tournament_sel, mutate=binary_mutation, crossover=single_point_slots_co,
           mut_prob=0.05, xo_prob=0.9, elitism=True)


#hill_climb(pop)
#sim_annealing(pop)

