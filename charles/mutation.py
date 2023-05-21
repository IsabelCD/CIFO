from random import randint, sample


def binary_mutation(individual):
    mut_indiv= individual.copy()
    days_indexes = random.sample(range(0, len(representation)), 2)

    # Extract the exam codes to swap
    exam_code_1 = mut_indiv[days_indexes[0]][1]
    exam_code_2 = mut_indiv[days_indexes[1]][1]

    # Swap the exam codes
    mut_indiv[days_indexes[0]][1] = exam_code_2
    mut_indiv[days_indexes[1]][1] = exam_code_1

    #check students e lotação
    #só posso trocar se forem salas da mesma lotação
    return mut_indiv


def swap_mutation(individual):
    mut_indexes = sample(range(0, len(individual)), 2)
    individual[mut_indexes[0]], individual[mut_indexes[1]] = individual[mut_indexes[1]], individual[mut_indexes[0]]
    return individual


if __name__ == '__main__':
    test = [1, 2, 3, 4, 5, 6]
    test = swap_mutation(test)

