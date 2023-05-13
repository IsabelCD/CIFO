import random
from data_import import *
import itertools

#variables to be used
size = 30 #pop
pop = []
hours = {
    0: {'day': '23-01-1995', 'time': '9:00', 'duration': 3},
    1: {'day': '23-01-1995', 'time': '13:30', 'duration': 2},
    2: {'day': '23-01-1995', 'time': '16:30', 'duration': 2},
    3: {'day': '24-01-1995', 'time': '9:00', 'duration': 3},
    4: {'day': '24-01-1995', 'time': '13:30', 'duration': 2},
    5: {'day': '24-01-1995', 'time': '16:30', 'duration': 2},
    6: {'day': '25-01-1995', 'time': '9:00', 'duration': 3},
    7: {'day': '25-01-1995', 'time': '13:30', 'duration': 2},
    8: {'day': '25-01-1995', 'time': '16:30', 'duration': 2},
    9: {'day': '26-01-1995', 'time': '9:00', 'duration': 3},
    10: {'day': '26-01-1995', 'time': '13:30', 'duration': 2},
    11: {'day': '26-01-1995', 'time': '16:30', 'duration': 2},
    12: {'day': '27-01-1995', 'time': '9:00', 'duration': 3},
    13: {'day': '27-01-1995', 'time': '13:30', 'duration': 2},
    14: {'day': '27-01-1995', 'time': '16:30', 'duration': 2},
    15: {'day': '28-01-1995', 'time': '9:00', 'duration': 3},
    16: {'day': '30-01-1995', 'time': '9:00', 'duration': 3},
    17: {'day': '30-01-1995', 'time': '13:30', 'duration': 2},
    18: {'day': '30-01-1995', 'time': '16:30', 'duration': 2},
    19: {'day': '31-01-1995', 'time': '9:00', 'duration': 3},
    20: {'day': '31-01-1995', 'time': '13:30', 'duration': 2},
    21: {'day': '31-01-1995', 'time': '16:30', 'duration': 2},
    22: {'day': '01-02-1995', 'time': '9:00', 'duration': 3},
    23: {'day': '01-02-1995', 'time': '13:30', 'duration': 2},
    24: {'day': '01-02-1995', 'time': '16:30', 'duration': 2},
    25: {'day': '02-02-1995', 'time': '9:00', 'duration': 3},
    26: {'day': '02-02-1995', 'time': '13:30', 'duration': 2},
    27: {'day': '02-02-1995', 'time': '16:30', 'duration': 2},
    28: {'day': '03-02-1995', 'time': '9:00', 'duration': 3},
    29: {'day': '03-02-1995', 'time': '13:30', 'duration': 2},
    30: {'day': '03-02-1995', 'time': '16:30', 'duration': 2},
    31: {'day': '04-02-1995', 'time': '9:00', 'duration': 3},
    32: {'day': '06-02-1995', 'time': '9:00', 'duration': 3},
    33: {'day': '06-02-1995', 'time': '13:30', 'duration': 2},
    34: {'day': '06-02-1995', 'time': '16:30', 'duration': 2},
    35: {'day': '07-02-1995', 'time': '9:00', 'duration': 3},
    36: {'day': '07-02-1995', 'time': '13:30', 'duration': 2},
    37: {'day': '07-02-1995', 'time': '16:30', 'duration': 2},
    38: {'day': '08-02-1995', 'time': '9:00', 'duration': 3},
    39: {'day': '08-02-1995', 'time': '13:30', 'duration': 2},
    40: {'day': '08-02-1995', 'time': '16:30', 'duration': 2},
    41: {'day': '09-02-1995', 'time': '9:00', 'duration': 3},
    42: {'day': '09-02-1995', 'time': '13:30', 'duration': 2},
    43: {'day': '09-02-1995', 'time': '16:30', 'duration': 2},
    44: {'day': '10-02-1995', 'time': '9:00', 'duration': 3},
    45: {'day': '10-02-1995', 'time': '13:30', 'duration': 2},
    46: {'day': '10-02-1995', 'time': '16:30', 'duration': 2},
    47: {'day': '11-02-1995', 'time': '9:00', 'duration': 3}
}




def get_hours(duration):
    hour, minute = map(int, duration.split(':'))
    return hour + (minute / 60)

#function that checks if there are no students making exams at the same time
def check_students(row, exam):
    total_students = []
    for i in row:
        if (i is not None):
            students_for_exam = df_en[df_en['exam'] == i]['student'].tolist()
            total_students = total_students + students_for_exam
    total_students = total_students + df_en[df_en['exam'] == exam]['student'].tolist()


    if len(total_students) == len(set(total_students)):
        return True
    else:
        return False


#function that will check if there are rooms available that check the condition required
def is_there_any_rooms_left(timetable, examhours, examcapacity):
    roomsAvailable = []
    hoursAvailable = []
    roomshoursYes = False
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
                roomshoursYes = True
                roomshours.append([j, i-1])
    return roomshoursYes, roomshours

# function that defines which groups of 2 rooms are posssible
def multiple_rooms(timetable, examhours, examcapacity, numrooms, exam):
    hoursAvailable = []
    possible_combos = {}
    for key, value in hours.items():
        if value['duration'] >= examhours and (check_students(timetable[key], exam)):
            hoursAvailable.append(key)
    print('this are the hours available', hoursAvailable, examhours)

    for i in hoursAvailable:
        #matrix that has all the index that are none of hour i
        none_indexes = [j for j, item in enumerate(timetable[i]) if item is None]
        combinations = []

        # Generate combinations of the indexes for hour i
        all_combinations = list(itertools.combinations(none_indexes, numrooms))

        #filter all the combinations to get only the ones that fullfill the capacity requirement
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

def check_combo_timetable(exam, coincidences, timetable, name = False):
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


countrow = 0
combolist = []
#creates population
while len(pop) <1:
    #initialization
    timetable = [[None for r in range(len(rooms))] for h in range(len(hours))]

    #all exams in the time table
    for i in range(df_exam.shape[0]):
        hours_room = True
        exam_name = df_exam.loc[i][0]
        exam_hours = get_hours(df_exam.loc[i]['duration'])
        room_capacity = df_en['exam'].value_counts()[df_exam.loc[i][0]]


        if check_exam_coincidences(df_exam.loc[i][0], coincidences):
            if check_combo_timetable(df_exam.loc[i][0], coincidences, timetable):
                continue
            else:
                print('MODIFY')
                exam_name, combo_index = check_combo_timetable(df_exam.loc[i][0], coincidences, timetable, name= True )
                for exam in coincidences[combo_index]:
                    if get_hours(df_exam[df_exam['exam']==exam]['duration'].values[0])> exam_hours:
                        exam_hours = get_hours(df_exam[df_exam['exam']==exam]['duration'].values[0])
                room_capacity = 0
                for exam in coincidences[combo_index]:
                    room_capacity = room_capacity + df_en['exam'].value_counts()[df_exam[df_exam['exam']==exam]['exam'].values[0]]
                countrow = countrow + 1
                combolist.append(exam_name)

        runit, roomhoursAvailable = is_there_any_rooms_left(timetable, exam_hours, room_capacity)



        while hours_room:
            if roomhoursAvailable:
                print('exam', i)
                hr = random.choice(roomhoursAvailable)
                #r = random.choice(roomsAvailable)
                roomhoursAvailable.remove(hr)

                print("condition:", check_students(timetable[hr[0]], exam_name))
                print("--------------------------------------------------------------------------------------")

                if check_students(timetable[hr[0]], exam_name):
                    timetable[hr[0]][hr[1]] = exam_name
                    hours_room = False
                    #print(timetable)

            else:
                print('exam', i)
                num_rooms = 2
                r = []
                while not r:
                    morethanone = multiple_rooms(timetable, exam_hours, room_capacity,num_rooms, exam_name)
                    num_rooms = num_rooms + 1
                    if not all(not value for value in morethanone.values() if value):
                        while not r:
                            h = random.choice(list(morethanone.keys()))
                            try:
                                r = random.choice(morethanone[h])
                            except:
                                r = []




                print("condition 4:", check_students(timetable[h], exam_name))
                print("--------------------------------------------------------------------------------------")

                if check_students(timetable[h], exam_name):
                    for i in r:
                        timetable[h][i] = exam_name
                    hours_room = False
                    #print(timetable)

    pop.append(timetable)

for i in pop:
    for indx, horario in enumerate(i):
        print('horario', hours[indx])
        print(horario)
        print()

print(countrow)
print(len(coincidences), 'how many coincidences there are')
print(sorted(combolist))





