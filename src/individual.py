class Individual:
    representation = []
    fitness = 0

    def f(self):
        return 0

    def setRepresentation(self,rep):
        self.representation = rep

    def setFitness(self,val):
        self.fitness = val