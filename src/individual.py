class Individual(object):
    #representation
    #fitness

    def __init__(self):
        self.representation = []
        self.fitness = 0

    def setRepresentation(self,rep):
        self.representation = rep

    def setFitness(self,val):
        self.fitness = val