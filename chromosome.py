"""
    By Armando Canul - 29/10/2024

    Abstract Class for Chromosome
    Chromosome class help us for create with SGA class
    Concrete SGA implementations, this is just the base
    and structure for code a especific chromosome child
    class for ours implementations.
"""
# this help us for implement a abstract class
from abc import ABCMeta, abstractmethod

class Chromosome(metaclass=ABCMeta):
    def __init__(self, sga):
        self.sga = sga
        pass
    @abstractmethod
    def random(self):
        """
            Metodo para inicializar el chromosoma con
            valores aleatorios
        """
        pass
    @abstractmethod
    def assign(self, new_data):
        """
            Asignar un valor especifico al chromosoma
        """
        pass
    @abstractmethod
    def crossover(self, other_chromosome):
        """
            Cruza (crossover) con otro chromosoma
            Define aqui como será tu cruzamiento
        """
        pass
    @abstractmethod
    def mutation(self, mutation_prob=0.3):
        """
            Mutacion del cromosoma apartir de una probabilidad
            Define aqui como será tu mutación
        """
        pass
    @abstractmethod
    def fitness(self):
        """
            Metodo que nos ayuda a saber que tan apto o
            bueno es el individuo (chromosoma)
            Define aqui como será tu función de Fitness
        """
        pass