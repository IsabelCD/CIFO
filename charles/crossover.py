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

def check_exam_timeslots(offspring):
    scheduled_exams = set()
    duplicates = set()
    for ind, timeslot in enumerate(offspring):
        if ind == 0:
            scheduled_exams.update(timeslot)
        else:
            for exam in timeslot:
                if exam in scheduled_exams:
                    duplicates.add(exam)
            scheduled_exams.add(exam)

    return duplicates

def assign_exam(timetable, exam):

    roomsAvailable = []
    hoursAvailable = []
    examcapacity =
    if exam.startswith("COMBO"):
        indx = int(exam.split()[1])
        for code in coincidences[indx]:
            examcapacity = examcapacity + df_en['exam'].value_counts()[
                        df_exam[df_exam['exam'] == code]['exam'].values[0]]
    else:
        examcapacity = df_en['exam'].value_counts()[exam]

    print('assing exam', exam, examcapacity)
    for key, value in rooms.items():
        if value[1] > examcapacity:
            roomsAvailable.append(key)

    for key, value in hours.items():
        hoursAvailable.append(key)

    

    exam_inside = True
    while exam_inside:

        room = random.choice(roomsAvailable)
        timeslot = random.choice(hoursAvailable)
        if (timetable[timeslot][room] is None) and check_students(timetable[timeslot], exam):
            timetable[timeslot][room] = exam
            exam_inside = False

    return timetable

def get_item(object, item):
    indx_rooms = []

    for i in object:
        if item in i:
            indx_time = object.index(i)
            indx_rooms = [index for index, value in enumerate(i) if value == item]


    return indx_time, indx_rooms


def single_point_slots_co(parent1, parent2):
    offspring1 = parent1.copy()  # Create copies of parents
    offspring2 = parent2.copy()

    timeslots = len(parent1)
    crossover_point = random.randint(1, num_rooms - 1)  # Select crossover point

    # Swap room assignments after the crossover point
    for time in range(crossover_point, timeslots):
            offspring1[time], offspring2[time] = parent2[time][i], parent1[time][i]

    # repair system
    if not check_all_exams_scheduled(parent1, offspring1):
        missing_exams = get_missing_exams(parent1, offspring1)
        for exam in missing_exams:
            offspring1 = assign_exam(exam, offspring1)
    if not check_all_exams_scheduled(parent2, offspring2):
        missing_exams = get_missing_exams(parent2, offspring2)
        for exam in missing_exams:
            offspring2 = assign_exam(exam, offspring2)


    return offspring1, offspring2

def cycle_xo(p1, p2):
    """Implementation of cycle crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    # offspring placeholders
    offspring1 = [[None] * len(p1[0]) for _ in range(len(p1))]
    offspring2 = [[None] * len(p1[0]) for _ in range(len(p1))]
    parents_exam = list(set(list(itertools.chain(*p1)) + list(itertools.chain(*p2))))
    print(parents_exam)

    parents_exam.remove(None)
    counter = 0

    while parents_exam:
        index_time, index_rooms = get_item(offspring1, None)
        val1 = p1[index_time][index_rooms]
        val2 = p2[index_time][index_rooms]
        print('iniciais', index_time, index_rooms)
        parents = True

        if counter % 2 == 0:
            # copy the cycle elements
            while parents:
                offspring1[index_time][index_rooms] = val1
                offspring2[index_time][index_rooms] = val2
                if val1 in parents_exam:
                    parents_exam.remove(val1)
                else:
                    parents = False
                val1 = p2[index_time][index_rooms]
                index_time, index_rooms = get_item(p1, val1)
                val2 = p2[index_time][index_rooms]

        else:
            while parents:
                offspring1[index_time][index_rooms] = val2
                offspring2[index_time][index_rooms] = val1
                if val1 in parents_exam:
                    print(counter, 'valor', val1)
                    parents_exam.remove(val1)
                else:
                    parents = False
                val1 = p2[index_time][index_rooms]
                index_time, index_rooms = get_item(p1, val1)
                val2 = p2[index_time][index_rooms]


        counter = counter + 1

        # copy the rest54
        for element in offspring1:
            if element is None:
                index = offspring1.index(None)
                if offspring1[index] is None:
                    offspring1[index] = p2[index]
                    offspring2[index] = p1[index]

    if not check_all_exams_scheduled(p1, offspring1):
        missing_exams = get_missing_exams(p1, offspring1)
        for exam in missing_exams:
            offspring1 = assign_exam(exam, offspring1)
    if not check_all_exams_scheduled(p2, offspring2):
        missing_exams = get_missing_exams(p2, offspring2)
        for exam in missing_exams:
            offspring2 = assign_exam(exam, offspring2)

    return offspring1, offspring2

def order_timeslots_crossover(p1, p2):
    offspring1 = [[None] * len(p1[0]) for _ in range(len(p1))]
    offspring2 = [[None] * len(p1[0]) for _ in range(len(p1))]

    timeslots = len(p1)
    crossover_point1 = random.randint(1, timeslots)
    crossover_point2 = random.randint(1, timeslots)

    for i in range(min([crossover_point1,crossover_point2]), max([crossover_point1, crossover_point2])):
        offspring1[i] = p1[i]
        offspring2[i] = p2[i]

    missing_exams1 = get_missing_exams(p1,offspring1)
    missing_exams2 = get_missing_exams(p2,offspring2)
    scheduled = []
    for i in missing_exams1:
        time, rooms = get_item(p2, i)
        for j in rooms:
            room = []
            if offspring1[time][j] is None and check_students(offspring1[time], i):
                room.append(True)
            else:
                room.append(False)
            if sum(room) == len(room):
                offspring1[time][j] = i
                scheduled.append(i)

    missing_exams1 = [exam for exam in missing_exams1 if exam not in scheduled]
    scheduled = []

    for i in missing_exams2:
        time, rooms = get_item(p1, i)
        for j in rooms:
            room = []
            if offspring1[time][j] is None and check_students(offspring1[time], i):
                room.append(True)
            else:
                room.append(False)
            if sum(room) == len(room):
                offspring2[time][j] = i
                scheduled.append(i)

    missing_exams2 = [exam for exam in missing_exams2 if exam not in scheduled]
    scheduled = []

    #exams that are between the points on the other parent
    for i in missing_exams1:
        time, rooms = get_item(p1, i)
        for j in rooms:
            room = []
            if offspring1[time][j] is None and check_students(offspring1[time], i):
                room.append(True)
            else :
                room.append(False)
            if sum(room) == len(room):
                offspring1[time][j] = i
                scheduled.append(i)

    missing_exams1 = [exam for exam in missing_exams1 if exam not in scheduled]
    scheduled = []
    # exams that are between the points on the other parent
    for i in missing_exams2:
        time, rooms = get_item(p1, i)
        for j in rooms:
            room = []
            if offspring1[time][j] is None and check_students(offspring1[time], i):
                room.append(True)
            else:
                room.append(False)
            if sum(room) == len(room):
                offspring2[time][j] = i
                scheduled.append(i)

    missing_exams2 = [exam for exam in missing_exams2 if exam not in scheduled]

    scheduled = []
    for exam in missing_exams1:
        off1 = copy.deepcopy(offspring1)
        offspring1 = assign_exam(offspring1, exam)
        if off1 != offspring1:
            scheduled.append(exam)

    missing_exams1 = [exam for exam in missing_exams1 if exam not in scheduled]
    scheduled = []

    for exam in missing_exams2:
        off2 = copy.deepcopy(offspring2)
        offspring2 = assign_exam(offspring2, exam)
        if off2 != offspring2:
            scheduled.append(exam)
    missing_exams2 = [exam for exam in missing_exams2 if exam not in scheduled]
    return missing_exams2, missing_exams1

one, two = order_timeslots_crossover(population[0], population[1])
print(one)
print(len(one))
print(two)
print(len(two))


