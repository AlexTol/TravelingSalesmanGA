from individual import Individual

def travelRouteToIndividual(tr,symbolMap):
    representation = ''
    for city in tr.route:
        representation = representation + symbolMap[city]

    ind = Individual()
    ind.setRepresentation(representation)
    return ind

def determineFitnessOfTravelRoute(symbolMap,weightMap,ind):
    reverseSymbols = {symbol:city for city,symbol in symbolMap.items()}

    fitness = 0
    for i in range(1,len(ind.representation)):
        fitness = fitness + int(weightMap[reverseSymbols[ind.representation[i-1]]][reverseSymbols[ind.representation[i]]])

    ind.fitness = fitness

def selectionOfTravelRoutes(pop,numSelected):
    prevPopNum = len(pop.individuals)
    selected = []
    for i in range(0,numSelected):
        highest = ''
        for ind in pop.individuals:
            if(highest == ''):
                highest = ind
            elif(highest.fitness < ind.fitness):
                highest = ind
        pop.individuals.remove(highest)

