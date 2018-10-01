from travelRoute import TravelRoute
from individual import Individual
from population import Population

import sys
sys.path.insert(0,'utils')
import alexTools

FILE_NAME = '..\data\cities.txt'
STREAM_FILE = '..\data\AlexTol_GA_TS_Info.txt'
SOLUTION_FILE = '..\data\AlexTol_GA_TS_Result.txt'
ITERATION_FILE = 'iterations.txt'
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

def writeIteration(pop,file,selected):
    file.write('Population Size: ' + str(len(pop.individuals)) + '   for iteration ' + str(pop.generations) + '\n')
    file.write('Average Fitness Score: ' + str(pop.getAverage()) + '\n')
    file.write('Median Fitness Score: ' + str(pop.getMedian()) + '\n')
    file.write('STD of Fitness Scores: ' + str(pop.getStandardDeviation()) + '\n')
    file.write('Size of selected subset: ' + str((selected)) + '\n')
    file.write('\n')

def writeResults(pop,symbolMap):
    rsMap = {v:k for k,v in symbolMap.items()}
    file = open(SOLUTION_FILE, "w+")
    bestInd = ''

    for ind in pop.individuals:
        if(bestInd == ''):
            bestInd = ind
        elif(ind.fitness < bestInd.fitness):
            bestInd = ind
        
        counter = 1
    for c in bestInd.representation:
        file.write('City ' + str(counter) + ' / ' + rsMap[c] + '\n')
        counter = counter + 1
    



def GA(pop,repetitions=1000):
    file2 = open(STREAM_FILE, "w+")

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
        pop.generations = pop.generations + 1
        writeIteration(pop,file2,5)

    
if __name__ == "__main__":
    itFile = open(ITERATION_FILE)
    iterations = 0

    for line in itFile:
        iterations = int(line)

    global mCities
    mCities = parseCities()
    global sMap
    sMap = getSymbolMap()
    
    mPop = generatePopulation()

    GA(mPop,iterations)
    writeResults(mPop,sMap)

    
    
    

