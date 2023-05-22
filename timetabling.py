from charles.charles import Population, Individual
from charles.crossover import cycle_xo
from charles.mutation import binary_mutation
from charles.selection import tournament_sel
from pop_created import *
from pop_creation import *


def get_fitness(self):
    # Create a dictionary with days as keys and exams as values
    #using a dictionary comprehension is more efficient than with an if statement  on a list

    # Create an empty list to hold nº students with multiple exams in each day
    student_counts = []
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
        diff = len(students) - len(set(students))
        
        # Add the result to the student_counts list
        student_counts.append(diff)

    # Calculate the fitness as the sum of the student counts
    fitness = sum(student_counts)
    
    return fitness 


# Monkey patching
Individual.get_fitness = get_fitness





# Step 2: Iterate over your list of lists and create Individual instances
for i, inner_list in enumerate(population):
    individual = Individual(representation=inner_list)
    print(i)

# Step 3: Assign the created Individual instances to the individuals list of the Population instance
pop= Population(size =30, replacement=False, optim= 'min')

pop.evolve(gens=50, select=tournament_sel, mutate=binary_mutation, crossover=cycle_xo,
           mut_prob=0.05, xo_prob=0.9, elitism=True)


#hill_climb(pop)
#sim_annealing(pop)

