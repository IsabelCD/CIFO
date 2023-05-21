from random import uniform, choice, sample
from operator import attrgetter


def fps(population):
    """Fitness proportionate selection implementation.

    Args:
        population (Population): The population we want to select from.

    Returns:
        Individual: selected individual.
    """

    # Invert the fitness values since its a minimization problem
    inverted_fitness = [1 / i.fitness for i in population]
    # Sum total inverted fitness
    total_inverted_fitness = sum(inverted_fitness)
    # Get a position on the wheel
    spin = uniform(0, total_inverted_fitness)
    position = 0
    # Find individual in the position of the spin
    individual: object
    for individual, inverted_fitness_value in zip(population, inverted_fitness):
        position += inverted_fitness_value
        if position > spin:
            return individual


def tournament_sel(population, size=4):
    """Tournament selection implementation.

    Args:
        population (Population): The population we want to select from.
        size (int): Size of the tournament.

    Returns:
        Individual: The best individual in the tournament.
    """

    # Select individuals based on tournament size
    # with choice, there is a possibility of repetition in the choices,
    # so every individual has a chance of getting selected
    tournament = [choice(population.individuals) for _ in range(size)]
    return min(tournament, key=attrgetter("fitness"))

def ranking_sel(population):
    """Ranking selection implementation.

    Args:
        population (Population): The population we want to select from.

    Returns:
        Individual: Selected individual.
    """

    #Rank individuals by fitness (from worst to best/higher fitness to lower fitness)
    inverted_fitness = [1 / i.fitness for i in population]
    sorted_population = sorted(inverted_fitness)
    rank = list(range(1, len(sorted_population) + 1))
    #Sum all ranks
    total_ranks = sum(rank)
    # Get a position on the wheel
    spin = uniform(0, total_ranks)
    position = 0
    # Find individual in the position of the spin
    individual: object
    for individual, rank_value in zip(population, rank):
        position += rank_value
        if position > spin:
            return individual