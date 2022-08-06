import random

class Chromosome():
    def __init__(self, Func, x = None, y = None):
        self.x = x
        self.y = y
        self.Func = Func
        self.fitness = None
    
    def crossover(self, other):
        child1 = Chromosome(self.Func, self.x, other.y)
        child2 = Chromosome(self.Func, other.x, self.y)
        return (child1, child2)
    
    def mutate(self, max_mutate_shift):
        self.x = self.x + random.uniform(-max_mutate_shift, max_mutate_shift) if random.random() > 0.9 else self.x
        self.y = self.y + random.uniform(-max_mutate_shift, max_mutate_shift) if random.random() > 0.9 else self.y
    
    def random_initialization(self, x_bounds, y_bounds):
        self.x = random.uniform(*x_bounds)
        self.y = random.uniform(*y_bounds)
    
    @property
    def fitness_value(self):
        if self.fitness is None:
            self.fitness = self.Func(self.x, self.y)
        return self.fitness

    @property
    def genes(self):
        return (self.x, self.y)