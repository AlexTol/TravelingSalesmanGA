from individual import Individual

def travelRouteToIndividual(tr,file):
    symbolMap = {}

    for line in file:
        temp = line.split(',')
        symbolMap[temp[0].rstrip()] = temp[1].rstrip()

    representation = ''
    for city in tr.route:
        representation = representation + symbolMap[city]

    ind = Individual()
    ind.setRepresentation(representation)
    return ind