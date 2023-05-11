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


#function that checks if there are no students making exams at the same time
def check_students(row):
    total_students = []
    for i in row:
        if (i is not None):
            students_for_exam = df_en[df_en['exam'] == i]['student'].tolist()
            total_students = total_students + students_for_exam
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
        if value['duration'] > examhours:
            hoursAvailable.append(key)

    for i in roomsAvailable:
        for j in hoursAvailable:
            if timetable[j][i-1] is None:
                roomshoursYes = True
                roomshours.append([j, i-1])
    return roomshoursYes, roomshours


# function that defines which groups of 2 rooms are posssible
def multiple_rooms(timetable, examhours, examcapacity):
    hoursAvailable = []
    possible_combos = []
    for key, value in hours.items():
        if value['duration'] > examhours:
            hoursAvailable.append(key)
    for i in hoursAvailable:
        none_indexes = [j for j, item in enumerate(timetable[i]) if item is None]
        # Generate combinations of the indexes
        all_combinations = list(itertools.combinations(none_indexes, 2))
        for k in all_combinations:
            full_capacity = 0
            for l in k:
                full_capacity = full_capacity + rooms[(l+1)][1]
            if full_capacity < examcapacity:
                all_combinations.remove(k)
        possible_combos.append(all_combinations)

    return possible_combos


#creates population
while len(pop) <1:
    #initialization
    timetable = [[None for r in range(len(rooms))] for h in range(len(hours))]

    #all exams in the time table
    for i in range(df_exam.shape[0]):
        hours_room = True
        hour, minute = map(int, df_exam.loc[0]['duration'].split(':'))
        exam_hours = hour + (minute / 60)
        room_capacity = df_en['exam'].value_counts()[df_exam.loc[i][0]]
        runit, roomhoursAvailable = is_there_any_rooms_left(timetable, exam_hours, room_capacity)


        if runit:

                # assign hours and room to exam but also making sure it respects the limites of the exam
            while hours_room:
                if roomhoursAvailable:
                    hr = random.choice(roomhoursAvailable)
                #r = random.choice(roomsAvailable)
                    roomhoursAvailable.remove(hr)

                else:
                    morethanone = multiple_rooms(timetable, exam_hours, room_capacity)
                    hr = random.choice(morethanone)
                    print(hr)

                print("condition 4:", check_students(timetable[hr[0]]))
                print("--------------------------------------------------------------------------------------")

                if check_students(timetable[hr[0]]):
                    timetable[hr[0]][hr[1]] = df_exam.loc[i][0]
                    hours_room = False
                    print(timetable)

        pop.append(timetable)

print(pop)







