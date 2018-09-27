import random

class TravelRoute:
    route = []
    
    def f(self, rep):
        return 0

    def setRoute(cities):
        if(cities is list):
            route = cities
        else:
            print('Error! Only acceptable input is a list!')

    def genRoute(cityList):
        for city in cityList:
            route.append(city)

        random.shuffle(route)

