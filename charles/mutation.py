from random import randint, sample
from pop_creation import *
import datetime

def swap_mutation(individual):
    #check students e lotação
    #só posso trocar se forem salas da mesma lotação

    #create copy of individual
    mut_indiv= individual.copy()

    #choose two dates and swap
    day_indexes = sample(range(0, len(mut_indiv)),2)

    #Chose a room to swap
    room_index= sample(range(individual[1]))
    sec_range= [i for i in range(0, len(mut_indiv)) if i != mut_indexes]

    mut_indiv[mut_indexes[0]], mut_indiv[mut_indexes[1]] = mut_indiv[mut_indexes[1]], mut_indiv[mut_indexes[0]]

    #aux variable that adds every time there are no students signed up for two exams at the same time
    time_check=0
    for exams in individual:
        time_check += check_students(exams, [], list_students=False)

    #should be equal to the length of students (nº of existing timeslots). If not, return original individual
    if time_check!=len(individual):
        return individual
    else:
        return mut_indiv


def day_swap(individual):
    #Use as range of choice all days except saturdays, as they have a different number of exams
    sample_range= []
    for day, j in hours_keys.items():
        if datetime.datetime.strptime(day, '%d-%m-%Y').weekday() != 5:
            sample_range.append(day)

    chosen_days= sample(sample_range, 2)
    days_indexes=[]
    for index, time in hours.items():
        if time['day'] in chosen_days:
            days_indexes.append(index)

    #choose two timeslots of exams and swap their exams
    individual[days_indexes[0]], individual[days_indexes[1]], individual[days_indexes[2]], individual[days_indexes[3]], individual[days_indexes[4]], individual[days_indexes[5]] = individual[days_indexes[3]], individual[days_indexes[4]], individual[days_indexes[5]], individual[days_indexes[0]], individual[days_indexes[1]], individual[days_indexes[2]]

    return individual


def timeslot_swap(individual):
    #choose two timeslots of exams and swap their exams
    mut_indexes = sample(range(0, len(mut_indiv)),2)
    individual[mut_indexes[0]], individual[mut_indexes[1]] = individual[mut_indexes[1]], individual[mut_indexes[0]]

    return individual


def inversion(individual):
    #Choose the timeslots between which we want the inversion to happen
    day_indexes = sample(range(0, len(individual)),2)
    day_indexes.sort()

    #Inverse the order of the sub-lists (the timeslots of exams inverse order)
    start_index, end_index = day_indexes
    individual[start_index:end_index+1] = individual[start_index:end_index+1][::-1]
    return individual





if __name__ == '__main__':
    test = population[sample(0, len(population))]
    test = day_swap(test)

