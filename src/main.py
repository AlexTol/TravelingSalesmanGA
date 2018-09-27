from travelRoute import TravelRoute
from individual import Individual
from population import Population

import sys
sys.path.insert(0,'utils')
import alexTools

FILE_NAME = '..\data\cities.txt'
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

def generatePopulation(size=10):
    pop = Population()
    for i in range(0,size):
        print(i)

    
if __name__ == "__main__":
    mCities = parseCities()
    print(cityNames)

    citiesToSymbolsFile = open('..\data\citiesToSymbols.txt')
    route = TravelRoute()
    route.genRoute(cityNames)
    print(route.route)
    ind = alexTools.travelRouteToIndividual(route,citiesToSymbolsFile)
    print(ind.representation)
    
    

