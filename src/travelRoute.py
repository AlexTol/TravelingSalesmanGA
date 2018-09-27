import random

class TravelRoute:
    route = []
    
    def f(self):
        return 0

    def setRoute(self,cities):
        if(cities is list):
            self.route = cities
        else:
            print('Error! Only acceptable input is a list!')

    def genRoute(self,cityList):
        for city in cityList:
            self.route.append(city)

        random.shuffle(self.route)

