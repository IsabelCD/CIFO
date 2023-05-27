import random
from data_import import *
import itertools


# function that checks if there are no students making exams at the same time
def check_students(row, exam, list_students = False):
    total_students = []
    for i in set(row):
        # if the exam is actually a combination of exams
        if (i is not None) and i.startswith("COMBO"):
            # get the index of the combination
            indx = int(i.split()[1])
            # add the students of each exam in the combination to the total
            for i in coincidences[indx]:
                students_for_exam = df_en[df_en['exam'] == i]['student'].tolist()
                total_students = total_students + students_for_exam

        # if it is a single exam
        elif (i is not None):
            students_for_exam = df_en[df_en['exam'] == i]['student'].tolist()
            total_students = total_students + students_for_exam

    # add the exam for which we are checking
    for i in exam:
        total_students = total_students + df_en[df_en['exam'] == i]['student'].tolist()
    if list_students: # for when we want the list of the students that are doing exam at that time slot
        return total_students

    return len(total_students) == len(set(total_students))


# function that will check if there are rooms available that check the condition required
def is_there_any_rooms_left(timetable, examcapacity):
    roomsAvailable = []
    roomshours = []
    #get all the rooms that meet the need capacity
    for key, value in rooms.items():
        if value[1] > examcapacity:
            roomsAvailable.append(key)
    #remove the biggest rooms for small exams
    if examcapacity <= 40:
        for i in [0, 8, 13, 14, 15]:
            try:
                roomsAvailable.remove(i)
            except:
                continue
    #check if the room is available
    for i in roomsAvailable:
        for j in range(len(timetable)):
            if timetable[j][i] is None:
                roomshours.append([j, i])
    return roomshours


# function that defines which groups of 2 rooms are posssible
def multiple_rooms(timetable, examcapacity, numrooms, exam):
    hoursAvailable = []
    possible_combos = {}

    #get the possible hours, that the student don't have another exam
    for key, value in hours.items():
        #print("key", key, 'value', value, check_students(timetable[key], exam, help=True), 'exam', exam)
        if check_students(timetable[key], exam):
            hoursAvailable.append(key)
    #if more than 6 trys, then stop
    if not hoursAvailable or numrooms > 6:
        return "Crossover not possible"

    for i in hoursAvailable:

        # matrix that has all the index that are none of hour i (rooms that are not occupied)
        none_indexes = [j for j, item in enumerate(timetable[i]) if item is None]
        combinations = []

        # Generate combinations of the indexes for hour i
        all_combinations = list(itertools.combinations(none_indexes, numrooms))

        # filter all the combinations to get only the ones that fullfill the capacity requirement
        for index, k in enumerate(all_combinations):
            full_capacity = 0
            for l in k:
                full_capacity = full_capacity + rooms[(l)][1]

            if full_capacity >= examcapacity:
                combinations.append(k)
        possible_combos[i] = combinations

    #return the rooms that can be combined to meet the needed capacity
    return possible_combos


# verify if an exam is part of a combo of exams
def check_exam_coincidences(exam, coincidences):
    # Check if exam is in coincidences
    for i in coincidences:
        if exam in i:
            return True
    return False


# verify if the combo of exams is already in the timeline
def check_combo_timetable(exam, coincidences, timetable, name=False):
    for i, sublist in enumerate(coincidences):
        if exam in sublist:
            # Generate the corresponding "COMBO [index]" string
            combo_string = f"COMBO {i}"
            if any(combo_string in timeslot for timeslot in timetable):
                return True
            else:
                if name:
                    #print(combo_string)
                    return combo_string, i
                else:
                    return False


# creates population or schedule exams in a existem time timetable
def create_individual(rooms, hours, df_exam, df_en, coincidences, assign = False, timetable = None, examstoschedule= None):
    #get the exams that have to be scheduled
    if timetable is not None:
        exam_count = [examstoschedule]
    else:
        exam_count = df_exam['exam']


    if not assign:
        # initialization if creating new timetabling
        timetable = [[None for r in range(len(rooms))] for h in range(len(hours))]


    # all exams in the time table
    for i in exam_count:
        hours_room = True #loop control
        exam_name = i
        exam_collection = []

        #initialization of the roomcapacity variable
        if i.startswith("COMBO"):
            room_capacity = []
        else:
            room_capacity = df_en['exam'].value_counts()[i]
        num_rooms = 2

        #check if we are scheduling a coincidence or an exam that belongs to one
        if check_exam_coincidences(i, coincidences) or i.startswith('COMBO'):
            #check if said coincidence is not already scheduled
            if check_combo_timetable(i, coincidences, timetable):
                continue
            else:
                #print('MODIFY')
                if i.startswith("COMBO"):
                    exam_name = i #make the exam name a combo
                    combo_index = int(i.split()[1])
                else:
                    #make the exam name a combo when scheduling an exam that is part of a combo
                    exam_name, combo_index = check_combo_timetable(i, coincidences, timetable, name=True)
                room_capacity = 0
                #get the room capacity for the COMBO and put the exams names in a collection
                for exam in coincidences[combo_index]:
                    exam_collection.append(exam)
                    room_capacity = room_capacity + df_en['exam'].value_counts()[
                        df_exam[df_exam['exam'] == exam]['exam'].values[0]]

        #in the case that we are not scheduling an exam combo
        if not exam_collection:
            exam_collection.append(exam_name)
        #get the combinations of hours and rooms possible for each exam
        roomhoursAvailable = is_there_any_rooms_left(timetable, room_capacity)

        while hours_room:
            #if it is possible to schedule the exam in one room
            if roomhoursAvailable:
                #print('exam', i)
                hr = random.choice(roomhoursAvailable) #choose a random hour/room
                # r = random.choice(roomsAvailable)
                roomhoursAvailable.remove(hr)  #so the algorithm does not repeat it in case it is not possible to do it
                #print("condition:", check_students(timetable[hr[0]], exam_collection))

                #check if coinstraints are met
                if check_students(timetable[hr[0]], exam_collection) and timetable[hr[0]][hr[1]] is None:
                    #if room_capacity <= 15:
                        #print('small exam', hr[1])
                    #print("--------------------------------------------------------------------------------------")
                    timetable[hr[0]][hr[1]] = exam_name #assignement of exam
                    hours_room = False
                    # print(timetable)
            #when more than one room is needed
            else:
                #print('começou')
                #get the possible combinations of two rooms
                morethanone = multiple_rooms(timetable, room_capacity, num_rooms, exam_collection)
                #print(morethanone)

                if morethanone == "Crossover not possible":
                    return "Crossover not possible"
                #to do if not possible to use two rooms only
                while all(not value for value in morethanone.values() if value):
                    morethanone = multiple_rooms(timetable, room_capacity, num_rooms, exam_collection)
                    if morethanone == "Crossover not possible":
                        return "Crossover not possible"
                    num_rooms = num_rooms + 1
                num_rooms = num_rooms + 1
                #print('exam', i)
                r = []

                while hours_room:
                    #print(num_rooms)
                    #print(morethanone)
                    #choose a random hour from the possible hours
                    h = random.choice(list(morethanone.keys()))
                    try:
                        #choose a random combination of rooms if it is there is one
                        r = random.choice(morethanone[h])
                        morethanone[h].remove(r)
                        #print('what?', morethanone[h])
                    except:
                        r = []
                        morethanone.pop(h)

                    #print('h', h, 'r', r)

                    #print("condition:", check_students(timetable[h], exam_collection), room_capacity)
                    #print("--------------------------------------------------------------------------------------")

                    #if constraints are meet
                    if check_students(timetable[h], exam_collection) and r:
                        for exam in r: #assing the exam for all rooms
                            timetable[h][exam] = exam_name
                        hours_room = False
                        # print(timetable)
    return timetable

#pop = []
#while len(pop)<10:
#    print('POPULATION', len(pop))
#    print('############################################################################################################')
#    ind = create_individual(rooms, hours, df_exam, df_en, coincidences)
#    pop.append(ind)
#    print('############################################################################################################')
#
#for i in pop:
#    print(i)
