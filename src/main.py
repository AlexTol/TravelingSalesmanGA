
FILE_NAME = '..\data\cities.txt'

def parseCities():
    cities = {}

    mFile = open(FILE_NAME)
    cityNames = mFile.readline().split(',')

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
    

if __name__ == "__main__":
    mCities = parseCities()
    print(mCities)

