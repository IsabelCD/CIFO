import random

from pop_created import population
from pop_creation import *
import itertools
import copy
import numpy as np


def check_all_exams_scheduled(parent, offspring):
    parent_exams = set(itertools.chain(*parent))
    offspring_exams = set(itertools.chain(*offspring))

    return parent_exams == offspring_exams

def get_missing_exams(parent, offspring):
    parent_exams = set(itertools.chain(*parent))
    offspring_exams = set(itertools.chain(*offspring))
    missing_exams = parent_exams - offspring_exams

    return missing_exams


def remove_duplicates(offspring):
    unique_exams = set()
    duplicates = set()

    for timeslot in offspring:
        for i, exam in enumerate(timeslot):
            if exam in unique_exams and exam is not None:
                timeslot[i] = None
        unique_exams.update(timeslot)
    


    return offspring






def single_point_slots_co(parent1, parent2):
    offspring1 = copy.deepcopy(parent1)  # Create copies of parents
    offspring2 = copy.deepcopy(parent2)

    timeslots = len(parent1)
    crossover_point = random.randint(1, timeslots - 1)  # Select crossover point

    # Swap room assignments after the crossover point
    for time in range(crossover_point, timeslots):
            offspring1[time], offspring2[time] = parent2[time], parent1[time]

    # repair system
    if not check_all_exams_scheduled(parent1, offspring1):
        offspring1 = remove_duplicates(offspring1)
        missing_exams = get_missing_exams(parent1, offspring1)
        for exam in missing_exams:
            offspring1 = create_individual(rooms,hours, df_exam, df_en, coincidences, assign=True, timetable= offspring1, examstoschedule=exam)
            if offspring1 == "Crossover not possible":
                print("Crossover not possible")
                return parent1, parent2
    if not check_all_exams_scheduled(parent2, offspring2):
        offspring2 = remove_duplicates(offspring2)
        missing_exams = get_missing_exams(parent2, offspring2)
        for exam in missing_exams:
            offspring2 = create_individual(rooms,hours, df_exam, df_en, coincidences, assign=True, timetable= offspring2, examstoschedule=exam)
            if offspring2 == "Crossover not possible":
                print("Crossover not possible")
                return parent1, parent2


    return offspring1, offspring2

def cycle_xo(p1, p2):

    # offspring placeholders
    offspring1 = [[] for _ in range(len(p1))]
    offspring2 = [[] for _ in range(len(p1))]
    offspring1_index = random.sample(range(len(p1)), len(p1))
    offspring2_index = random.sample(range(len(p1)), len(p1))


    index_off = 0

    val_inside1 = offspring1_index[index_off]
    val_inside2 = offspring2_index[index_off]
    val1_incial = 60
    count=0

    while val_inside1 != val1_incial and count<len(offspring1_index):
        #assign of the parents to the offsprings
        offspring1[index_off] = p2[index_off]
        offspring2[index_off] = p1[index_off]

        #index of the val2 in the offspring1
        index_off = offspring1_index.index(val_inside2)
        count = count + 1
        #print(count)

        #new values for the inside
        val_inside1 = offspring1_index[index_off]
        val_inside2 = offspring2_index[index_off]

    #assign the correponding parent timeslot
    for index,element in enumerate(offspring1):
        if not element:
            offspring1[index] = p1[index]
            offspring2[index] = p2[index]

    #print("Repair system", not check_all_exams_scheduled(p1, offspring1))

    if not check_all_exams_scheduled(p1, offspring1):
        offspring1 = remove_duplicates(offspring1)

        missing_exams = get_missing_exams(p1, offspring1)
        for exam in missing_exams:
            offspring1 = create_individual(rooms,hours, df_exam, df_en, coincidences, assign=True, timetable= offspring1, examstoschedule=exam)
            if offspring1 == "Crossover not possible":
                print("Crossover not possible")
                return p1, p2
    #print("Repair system 2")

    if not check_all_exams_scheduled(p2, offspring2):
        offspring2 = remove_duplicates(offspring2)
        missing_exams = get_missing_exams(p2, offspring2)
        for exam in missing_exams:
            offspring2 = create_individual(rooms,hours, df_exam, df_en, coincidences, assign=True, timetable= offspring2, examstoschedule=exam)
            if offspring2 == "Crossover not possible":
                print("Crossover not possible")
                return p1, p2

    return offspring1, offspring2

def order_timeslots_crossover(p1, p2):
    #create empty offspring
    offspring1 = [[None] * len(p1[0]) for _ in range(len(p1))]
    offspring2 = [[None] * len(p1[0]) for _ in range(len(p1))]

    #get the interval points tha will be conserved
    timeslots = len(p1)
    crossover_point1 = random.randint(1, timeslots)
    crossover_point2 = random.randint(1, timeslots)

    #pass the segment that will be conserved to the offspring
    for i in range(min([crossover_point1,crossover_point2]), max([crossover_point1, crossover_point2])):
        offspring1[i] = p1[i]
        offspring2[i] = p2[i]

    for i in range(min([crossover_point1, crossover_point2])):
        offspring1[i] = p2[i]
        offspring2[i] = p2[i]

    for i in range( max([crossover_point1, crossover_point2]), len(p1)):
        offspring1[i] = p2[i]
        offspring2[i] = p2[i]

    #repair system
    if not check_all_exams_scheduled(p1, offspring1):
        offspring1 = remove_duplicates(offspring1)

        missing_exams = get_missing_exams(p1, offspring1)
        for exam in missing_exams:
            offspring1 = create_individual(rooms,hours, df_exam, df_en, coincidences, assign=True, timetable= offspring1, examstoschedule=exam)
            if offspring1 == "Crossover not possible":
                print("Crossover not possible")
                return p1, p2
    #print("Repair system 2")

    if not check_all_exams_scheduled(p2, offspring2):
        offspring2 = remove_duplicates(offspring2)
        missing_exams = get_missing_exams(p2, offspring2)
        for exam in missing_exams:
            offspring2 = create_individual(rooms,hours, df_exam, df_en, coincidences, assign=True, timetable= offspring2, examstoschedule=exam)
            if offspring2 == "Crossover not possible":
                print("Crossover not possible")
                return p1, p2

    return offspring1, offspring2





