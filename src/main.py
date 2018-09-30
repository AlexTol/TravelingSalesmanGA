from travelRoute import TravelRoute
from individual import Individual
from population import Population

import sys
sys.path.insert(0,'utils')
import alexTools

FILE_NAME = '..\data\cities.txt'
STREAM_FILE = '..\data\iterations.txt'
SOLUTION_FILE = '..\data\solution.txt'
cityNames = []

def parseCities():
    global cityNames
    cities = {}

    mFile = open(FILE_NAME)
    cityNames = mFile.readline().rstrip().split(',')
    
    for city in cityNames:
        cities[city.rstrip()] = {}
    
    with mFile as f:
        for line in f:
            temp = line.split(',')
            xcity = temp[0]

            index = 0
            for distance in temp[1:]:
                cities[xcity][cityNames[index].rstrip()] = distance.rstrip()
                index = index + 1            
    f.close()
    return cities

def getSymbolMap():
    file = open('..\data\citiesToSymbols.txt')
    symbolMap = {}

    for line in file:
        temp = line.split(',')
        symbolMap[temp[0].rstrip()] = temp[1].rstrip()

    return symbolMap

def generatePopulation(size=10):
    pop = Population()

    for i in range(0,size):
        tR =TravelRoute()
        tR.genRoute(cityNames)

        ind = alexTools.travelRouteToIndividual(tR,sMap)
        alexTools.determineFitnessOfTravelRoute(sMap,mCities,ind)

        pop.addIndividual(ind)

    return pop
def writeIteration

def GA(pop,repetitions=1000):
    file1 = open(STREAM_FILE)
    file2 = open(STREAM_FILE)

    for ind in pop.individuals:
        print(ind.representation)
        print(ind.fitness)
    
    pop.evaluateFitness()
    print(pop.totalFitness)
    print('\n ++++++++++++++++++++++++++ \n')
    for i in range(0,repetitions):
        alexTools.selectionOfTravelRoutes(pop,5)
        pop.orderOneCrossover(5,4)
        pop.nonRepeatMut(15)

        for ind in pop.individuals:
            alexTools.determineFitnessOfTravelRoute(sMap,mCities,ind)

        for ind in pop.individuals:
            print(ind.representation)
            print(ind.fitness)

        pop.evaluateFitness()
        print(pop.totalFitness)
        print('\n ++++++++++++++++++++++++++ \n')

    
if __name__ == "__main__":
    global mCities
    mCities = parseCities()
    global sMap
    sMap = getSymbolMap()
    
    mPop = generatePopulation()

    GA(mPop)

    
    
    

