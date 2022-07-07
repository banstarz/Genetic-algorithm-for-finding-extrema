import random

class Chromosome():
    def __init__(self, Func, x = None, y = None):
        self.x = x
        self.y = y
        self.Func = Func
        self.fitness = None
    
    def Crossover(self, other):
        child1 = Chromosome(self.Func, self.x, other.y)
        child2 = Chromosome(self.Func, other.x, self.y)
        return (child1, child2)
    
    def Mutate(self, threshold):
        self.x = self.x + random.uniform(-threshold, threshold) if random.random() > 0.9 else self.x
        self.y = self.y + random.uniform(-threshold, threshold) if random.random() > 0.9 else self.y
    
    def RandInst(self, xmin, xmax, ymin, ymax):
        self.x = random.uniform(xmin, xmax)
        self.y = random.uniform(ymin, ymax)
    
    def FF(self):
        if self.fitness is None:
            self.fitness = self.Func(self.x, self.y)
        return self.fitness