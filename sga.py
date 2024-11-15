"""
    By Armando Canul - 29/10/2024

    Abstract Class for Simple Genetic Algorithm (SGA)
    This abstract class, give us a structure to implement
    a SGA.
"""
# this help us for implement a abstract class
from abc import ABCMeta, abstractmethod
# import Chromosome abstract class
from chromosome import Chromosome

class SGA(metaclass=ABCMeta):
    def __init__(self, N=10, fitness_range=[0,0], maxGenerations=1000):
        self.N = N
        self.found = False
        self.population = []
        self.fitness_range = fitness_range
        self.maxGenerations = maxGenerations
    @abstractmethod
    def generatePopulation(self):
        """
            Define como será tu generación de individuos
            (chromosomas)
        """
        pass
    @abstractmethod
    def selection(self):
        """
            Metodo de seleccion de Individuos
        """
        pass

    # indicamos que ya se encontro un individuo optimo
    def founded(self):
        self.found = True
        return
    
    # optimiza el proceso del sga
    def optimize(self):
        self.found = False
        generations = 1
        self.generatePopulation()
        print("Generation: ", generations)
        while not self.found or generations > self.maxGenerations:
            generations += 1
            self.selection()
            print("Generation: ", generations)
        self.found = False