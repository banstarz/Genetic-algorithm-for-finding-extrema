import random
from chromosome import Chromosome

class GeneticAlgorithm():
    def __init__(self, Func, PopSize = 50, GenLimit = 100, TournamentSize = 2, Elite = 5,
                 xmin = -50, xmax = 50, ymin = -50, ymax = 50):
        self.Func = Func
        self.PopSize = PopSize
        self.TournamentSize = TournamentSize
        self.Elite = Elite
        self.GenLimit = GenLimit
        self.Population = []
        self.TemporaryPopulation = [0 for i in range(2*PopSize)]
        self.PopulationInit(xmin, xmax, ymin, ymax)
        self.History = []
    
    def Run(self):
        self.EvaluateFF(self.Population)
        self.History.append(self.MeanFF())
        for i in range(self.GenLimit):
            self.Offsprings()
            self.Mutation()
            self.EvaluateFF(self.TemporaryPopulation)
            self.NewPopulation()
            self.History.append(self.MeanFF())
    
    def PopulationInit(self, xmin, xmax, ymin, ymax):
        for i in range(self.PopSize):
            self.Population.append(Chromosome(self.Func))
            self.Population[i].RandInst(xmin, xmax, ymin, ymax)
    
    def EvaluateFF(self, Pop):
        for i in range(len(Pop)):
            Pop[i].FF()
    
    def Selection(self):
        Candidates = random.choices(self.Population, k=self.TournamentSize)
        best = 0
        for i in range(len(Candidates)):
            if Candidates[i].FF() < Candidates[best].FF():
                best = i
        return Candidates[best]
        
    def Offsprings(self):
        for i in range(self.PopSize):
            parent1 = self.Selection()
            parent2 = self.Selection()
            child1, child2 = parent1.Crossover(parent2)
            self.TemporaryPopulation[i] = child1
            self.TemporaryPopulation[i+self.PopSize] = child2
            
    def Mutation(self):
        for i in range(len(self.TemporaryPopulation)):
            self.TemporaryPopulation[i].Mutate(1)
    
    def NewPopulation(self):
        sorted(self.Population, key = lambda x: x.FF())
        sorted(self.TemporaryPopulation, key = lambda x: x.FF())
        j=0
        for i in range(self.Elite):
            if self.Population[i].FF() > self.TemporaryPopulation[j].FF():
                self.Population[i] = self.TemporaryPopulation[j]
                j+=1
        for i in range(self.Elite, self.PopSize):
            self.Population[i] = self.TemporaryPopulation[j]
            j+=1
            
    def MeanFF(self):
        SumFF = 0
        for i in range(len(self.Population)):
            SumFF = self.Population[i].FF()
        return SumFF/len(self.Population)