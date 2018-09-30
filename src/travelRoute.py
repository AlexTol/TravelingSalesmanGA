import random

class TravelRoute(object):
    #route

    def __init__(self):
        self.route = []

    def setRoute(self,cities):
        if(cities is list):
            self.route = cities
        else:
            print('Error! Only acceptable input is a list!')

    def genRoute(self,cityList):
        for city in cityList:
            self.route.append(city)

        random.shuffle(self.route)

