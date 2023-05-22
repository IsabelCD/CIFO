from copy import deepcopy
from pop_creation import *
import itertools


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
    select_index = list(np.where(df_exam["exam"] == True)[0])
    examcapacity = df_en['exam'].value_counts()[exam]

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
    for i in object:
        try:
            indx_rooms = i.index(item)
            indx_time = object.index(i)
            return indx_time, indx_rooms
        except:
            continue


def single_point_slots_co(parent1, parent2):
    offspring1 = deepcopy(parent1)  # Create copies of parents
    offspring2 = deepcopy(parent2)

    timeslots = len(parent1)
    crossover_point = random.randint(1, timeslots - 1)  # Select crossover point

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
    #repair system

    if not check_all_exams_scheduled(p1, offspring1):
        missing_exams = get_missing_exams(p1, offspring1)
        for exam in missing_exams:
            offspring1 = assign_exam(exam, offspring1)
    if not check_all_exams_scheduled(p2, offspring2):
        missing_exams = get_missing_exams(p2, offspring2)
        for exam in missing_exams:
            offspring2 = assign_exam(exam, offspring2)

    return offspring1, offspring2







from pop_created import *
print(get_item(population, "C42304E1"))


