from deap import base
from deap import creator
from deap import tools
from deap import algorithms

import random
import numpy

import matplotlib.pyplot as plt
#import seaborn as sns

from ks import Knapsack01Problem
from process_data import get_data

# Genetic Algorithm constants:
P_CROSSOVER = 0.85  # probability for crossover
P_MUTATION = 0.15   # probability for mutating an individual
MAX_GENERATIONS = 150
HALL_OF_FAME_SIZE = 1
POPULATION_SIZE = 50


# set the random seed:
RANDOM_SEED = 42
random.seed(RANDOM_SEED)


# Genetic Algorithm flow:
def main():
    str_n = ['n00050', 'n00100' ,'n00200', 'n00500', 'n01000']
    problem_types = [
        '00Uncorrelated',
        '01WeaklyCorrelated',
        '02StronglyCorrelated',
        '03InverseStronglyCorrelated',
        '04AlmostStronglyCorrelated',
        '05SubsetSum',
        '06UncorrelatedWithSimilarWeights',
        '07SpannerUncorrelated',
        '08SpannerWeaklyCorrelated',
        '09SpannerStronglyCorrelated',
        '10MultipleStronglyCorrelated',
        '11ProfitCeiling',
        '12Circle'
    ]

    problems = []
    for t in problem_types:
        tmp = []
        for k in str_n:
            tmp.append(f"D:/HOC/Tri Tue Nhan Tao/KnapsackProblems/kplib-master/kplib-master/{t}/{k}.kp")
        problems.append(tmp)

    for files in problems:
        for file in files:
            items, maxCapacity = get_data(file)

            knapsack = Knapsack01Problem(items, maxCapacity)

            toolbox = base.Toolbox()

            # create an operator that randomly returns 0 or 1:
            toolbox.register("zeroOrOne", random.randint, 0, 1)

            # define a single objective, maximizing fitness strategy:
            creator.create("FitnessMax", base.Fitness, weights=(1.0,))

            # create the Individual class based on list:
            creator.create("Individual", list, fitness=creator.FitnessMax)

            # create the individual operator to fill up an Individual instance:
            toolbox.register("individualCreator", tools.initRepeat,
                             creator.Individual, toolbox.zeroOrOne, len(knapsack))

            # create the population operator to generate a list of individuals:
            toolbox.register("populationCreator", tools.initRepeat,
                             list, toolbox.individualCreator)

            # fitness calculation

            def knapsackValue(individual):
                return knapsack.getValue(individual),  # return a tuple

            toolbox.register("evaluate", knapsackValue)

            # genetic operators:mutFlipBit

            # Tournament selection with tournament size of 3:
            toolbox.register("select", tools.selTournament, tournsize=3)

            # Single-point crossover:
            toolbox.register("mate", tools.cxTwoPoint)

            # Flip-bit mutation:
            # indpb: Independent probability for each attribute to be flipped
            toolbox.register("mutate", tools.mutFlipBit,
                             indpb=1.0/len(knapsack))

            # create initial population (generation 0):
            population = toolbox.populationCreator(n=len(knapsack))

            # prepare the statistics object:
            stats = tools.Statistics(lambda ind: ind.fitness.values)
            stats.register("max", numpy.max)
            stats.register("avg", numpy.mean)

            # define the hall-of-fame object:
            hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

            # perform the Genetic Algorithm flow with hof feature added:
            population, logbook = algorithms.eaSimple(population, toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTATION,
                                                      ngen=MAX_GENERATIONS, stats=stats, halloffame=hof, verbose=True)

            # print best solution found:
            best = hof.items[0]
            with open('result.txt', 'a') as writer:
                writer.write(f"Solution for {file}\n")
                writer.write(f"-- Best Ever Individual = {best}\n")
                writer.write(
                    f"-- Best Ever Fitness = {best.fitness.values[0]}\n")
                writer.write(f"{knapsack.result(best)}\n")


if __name__ == "__main__":
    main()
