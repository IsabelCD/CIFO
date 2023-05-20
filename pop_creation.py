import random
from data_import import *
import itertools

# variables to be used
size = 30  # pop
pop = []


def get_hours(duration):
    hour, minute = map(int, duration.split(':'))
    return hour + (minute / 60)


# function that checks if there are no students making exams at the same time
def check_students(row, exam):
    total_students = []
    for i in row:
        if (i is not None) and i.startswith("COMBO"):
            indx = int(i.split()[1])
            for i in coincidences[indx]:
                students_for_exam = df_en[df_en['exam'] == i]['student'].tolist()
                total_students = total_students + students_for_exam
        elif (i is not None):
            students_for_exam = df_en[df_en['exam'] == i]['student'].tolist()
            total_students = total_students + students_for_exam

    for i in exam:
        total_students = total_students + df_en[df_en['exam'] == i]['student'].tolist()
    if len(total_students) == len(set(total_students)):
        return True
    else:
        return False


# function that will check if there are rooms available that check the condition required
def is_there_any_rooms_left(timetable, examhours, examcapacity):
    roomsAvailable = []
    hoursAvailable = []
    roomshours = []
    for key, value in rooms.items():
        if value[1] > examcapacity:
            roomsAvailable.append(key)

    for key, value in hours.items():
        if value['duration'] >= examhours:
            hoursAvailable.append(key)

    for i in roomsAvailable:
        for j in hoursAvailable:
            if timetable[j][i] is None:
                roomshours.append([j, i])
    return roomshours


# function that defines which groups of 2 rooms are posssible
def multiple_rooms(timetable, examhours, examcapacity, numrooms, exam):
    hoursAvailable = []
    possible_combos = {}
    for key, value in hours.items():
        if value['duration'] >= examhours and (check_students(timetable[key], exam)):
            hoursAvailable.append(key)
    print('this are the hours available', hoursAvailable, examhours)

    for i in hoursAvailable:
        # matrix that has all the index that are none of hour i
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

    return possible_combos


def check_exam_coincidences(exam, coincidences):
    # Check if exam is in coincidences
    for i in coincidences:
        if exam in i:
            return True
    return False


def check_combo_timetable(exam, coincidences, timetable, name=False):
    for i, sublist in enumerate(coincidences):
        if exam in sublist:
            # Generate the corresponding "COMBO [index]" string
            combo_string = f"COMBO {i}"
            if any(combo_string in timeslot for timeslot in timetable):
                return True
            else:
                if name:
                    print(combo_string)
                    return combo_string, i
                else:
                    return False


# creates population
def create_individual(rooms, hours, df_exam, df_en, coincidences):
    combo_count = 0
    
    # initialization
    timetable = [[None for r in range(len(rooms))] for h in range(len(hours))]

    # all exams in the time table
    for i in range(df_exam.shape[0]):
        hours_room = True
        exam_name = df_exam.loc[i][0]
        exam_collection = []
        exam_hours = get_hours(df_exam.loc[i]['duration'])
        room_capacity = df_en['exam'].value_counts()[df_exam.loc[i][0]]

        if check_exam_coincidences(df_exam.loc[i][0], coincidences):
            if check_combo_timetable(df_exam.loc[i][0], coincidences, timetable):
                continue
            else:
                print('MODIFY')
                exam_name, combo_index = check_combo_timetable(df_exam.loc[i][0], coincidences, timetable, name=True)
                for exam in coincidences[combo_index]:
                    exam_collection.append(exam)
                    if get_hours(df_exam[df_exam['exam'] == exam]['duration'].values[0]) > exam_hours:
                        exam_hours = get_hours(df_exam[df_exam['exam'] == exam]['duration'].values[0])
                room_capacity = 0
                for exam in coincidences[combo_index]:
                    room_capacity = room_capacity + df_en['exam'].value_counts()[
                        df_exam[df_exam['exam'] == exam]['exam'].values[0]]
                combo_count = combo_count + 1

            if not exam_collection:
                exam_collection.append(exam_name)

        roomhoursAvailable = is_there_any_rooms_left(timetable, exam_hours, room_capacity)

        while hours_room:
            if roomhoursAvailable:
                print('exam', i)
                hr = random.choice(roomhoursAvailable)
                # r = random.choice(roomsAvailable)
                roomhoursAvailable.remove(hr)

                print("condition:", check_students(timetable[hr[0]], exam_collection))

                if check_students(timetable[hr[0]], exam_collection) and timetable[hr[0]][hr[1]] is None:
                    print("--------------------------------------------------------------------------------------")
                    timetable[hr[0]][hr[1]] = exam_name
                    hours_room = False
                    # print(timetable)

            else:
                num_rooms = 2
                morethanone = multiple_rooms(timetable, exam_hours, room_capacity, num_rooms, exam_name)
                while all(not value for value in morethanone.values() if value):
                    print(num_rooms)
                    morethanone = multiple_rooms(timetable, exam_hours, room_capacity, num_rooms, exam_name)
                    print(morethanone)
                    num_rooms = num_rooms + 1

                print('exam', i)
                r = []
                while (not r and hours_room):
                    print(num_rooms)
                    print(morethanone)
                    h = random.choice(list(morethanone.keys()))
                    try:
                        r = random.choice(morethanone[h])
                        morethanone[h].remove(r)
                    except:
                        r = []
                        morethanone.pop(h)

                    print('h', h, 'r', r)

                print("condition:", check_students(timetable[h], exam_collection))
                print("--------------------------------------------------------------------------------------")

                if check_students(timetable[h], exam_collection):
                    for i in r:
                        timetable[h][i] = exam_name
                    hours_room = False
                    # print(timetable)
    print(combo_count)
    return timetable


#ind = create_individual(rooms, hours, df_exam, df_en, coincidences)

#for i in ind:
#    print(i)
