import math
from random import *
from individual import Individual

class Population(object):
    #generations
    #totalFitness
    #individuals

    def __init__(self):
        self.generations = 0
        self.totalFitness = 0
        self.individuals = []
        

    def evaluateFitness(self):
        self.totalFitness = 0
        for ind in self.individuals:
            self.totalFitness = self.totalFitness + ind.fitness

    def addIndividual(self,i):
        self.individuals.append(i)

    def orderOneCrossover(self,amountOfCrossovers,regionLength):
        previousPairs = []
        for i in range(0,amountOfCrossovers):
            space1 = randint(0,len(self.individuals)-1)
            space2 = randint(0,len(self.individuals)-1)
            while(str(space1) + str(space2) in previousPairs or space1 == space2):
                space1 = randint(0,len(self.individuals)-1)
                space2 = randint(0,len(self.individuals)-1)
            previousPairs.append(str(space1) + str(space2))

            P1 = self.individuals[space1]
            P2 = self.individuals[space2]

            childRep = ''
            loc = randint(0,len(P1.representation)-1)
            region = P1.representation[loc:loc + regionLength]

            right = ''
            left = ''

            for c in P2.representation[loc + regionLength:]:
                if(c not in region):
                    right = right + c
            for c in P2.representation[:loc + regionLength]:
                if(c not in region):
                    left = left + c

            childRep = left + region + right
            mInd = Individual()
            mInd.setRepresentation(childRep)
            self.individuals.append(mInd)

    def nonRepeatMut(self,mutationCoefficient):
        for ind in self.individuals:
            someNum = randint(1,100)
            if(someNum <= mutationCoefficient):
                space1 = randint(0,len(ind.representation)-1)
                space2 = randint(0,len(ind.representation)-1)
                while(space1 == space2):
                    space2 = randint(0,len(ind.representation)-1)
        
                newInd = ''
                for i in range(0,len(ind.representation)):
                    if(i == space1):
                        newInd = newInd + ind.representation[space2]
                    elif(i == space2):
                        newInd = newInd + ind.representation[space1]
                    else:
                        newInd = newInd + ind.representation[i]
                ind.representation = newInd
    
    def getAverage(self):
        return self.totalFitness/len(self.individuals)

    def getMedian(self):
        fitnessList = []
        for ind in self.individuals:
            fitnessList.append(ind.fitness)

        fitnessList.sort()

        return fitnessList[int(len(fitnessList)/2)]

    def getStandardDeviation(self):
        mean = self.getAverage()
        amount = 0
        for ind in self.individuals:
            temp = ind.fitness - mean
            temp = temp * temp
            amount = amount + temp

        amount = amount/len(self.individuals)
        return math.sqrt(amount)
        
