import random
from chromosome import Chromosome

class GeneticAlgorithm():

    def __init__(self, fitness_function, population_size = 50, GenLimit = 100, tournament_size = 2, elite = 5,
                 xmin = -50, xmax = 50, ymin = -50, ymax = 50):
        self.fitness_function = fitness_function
        self.population_size = population_size
        self.tournament_size = tournament_size
        self.elite = elite
        self.GenLimit = GenLimit
        self.population = []
        self.temporary_population = [0 for i in range(2*population_size)]
        self.initialize_population(xmin, xmax, ymin, ymax)
        self.history = {
            'chromosomes': [],
            'fitness_function': []
        }
    
    def run(self):
        self.evaluate_fitness_for_each_chromosome_in(self.population)
        self.add_to_history()
        for i in range(self.GenLimit):
            self.generate_child_population()
            self.mutate_child_population()
            self.evaluate_fitness_for_each_chromosome_in(self.temporary_population)
            self.produce_next_generation()
            self.add_to_history()

    def add_to_history(self):
        mean_ff = self.calculate_mean_fitness_in_population()
        top_ten_chromosomes = tuple(chromo.genes for chromo in self.population[:10])
        self.history['fitness_function'].append(mean_ff)
        self.history['chromosomes'].append(top_ten_chromosomes)
    
    def initialize_population(self, xmin, xmax, ymin, ymax):
        for i in range(self.population_size):
            self.population.append(Chromosome(self.fitness_function))
            self.population[i].random_initialization((xmin, xmax), (ymin, ymax))
    
    def evaluate_fitness_for_each_chromosome_in(self, population):
        for chromosome in population:
            chromosome.fitness_value
    
    def select_parent(self):
        Candidates = random.choices(self.population, k=self.tournament_size)
        best = 0
        for i in range(len(Candidates)):
            if Candidates[i].fitness_value < Candidates[best].fitness_value:
                best = i
        return Candidates[best]
        
    def generate_child_population(self):
        for i in range(self.population_size):
            parent1 = self.select_parent()
            parent2 = self.select_parent()
            child1, child2 = parent1.crossover(parent2)
            self.temporary_population[i] = child1
            self.temporary_population[i+self.population_size] = child2
            
    def mutate_child_population(self):
        for i in range(len(self.temporary_population)):
            self.temporary_population[i].mutate(1)
    
    def produce_next_generation(self):
        sorted(self.population, key = lambda x: x.fitness_value)
        sorted(self.temporary_population, key = lambda x: x.fitness_value)
        j=0
        for i in range(self.elite):
            if self.population[i].fitness_value > self.temporary_population[j].fitness_value:
                self.population[i] = self.temporary_population[j]
                j+=1
        for i in range(self.elite, self.population_size):
            self.population[i] = self.temporary_population[j]
            j+=1
            
    def calculate_mean_fitness_in_population(self):
        total_fitness = sum([chromosome.fitness_value for chromosome in self.population])
        return total_fitness/len(self.population)