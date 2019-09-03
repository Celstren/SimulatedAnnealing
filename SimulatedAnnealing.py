import math
import random

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SimulatedAnnealing:
    def __init__(self, elements, temp, cooling):
        self.elements = elements
        self.temp = temp
        self.cooling = cooling
        self.current = self.calculateDistance(elements)
        self.new = self.current
        self.best = self.current
    
    def calculateDistance(self, elements):
        value = 0
        prev = Player(-1, -1)
        for element in elements:
            if (prev.x == -1):
                prev = element
            else:
                value += math.sqrt(pow(element.x - prev.x, 2) + pow(element.y - prev.y, 2))
        return value

    def accept_solution(self, delta_energy):
        if delta_energy < 0:
            return True
        elif random.random() <= math.exp(-(delta_energy/self.temp)):
            return True
        return False

    def run(self):
        while self.temp > 0:
            self.evolve_tour()
            self.temp *= 1-self.cooling

    def evolve_tour(self):
        tour_evolved = self.elements

        pos1 = random.randrange(len(self.elements))
        pos2 = pos1
        while(pos1 == pos2):
            pos2 = random.randrange(len(self.elements))
        city1 = self.elements[pos1]
        city2 = self.elements[pos2]
        self.elements[pos1] = city2
        self.elements[pos2] = city1

        new_energy = self.calculateDistance(tour_evolved)
        delta = new_energy - self.current

        if self.accept_solution(delta):
            self.current = new_energy
            self.elements = tour_evolved
        
        if self.current < self.best:
            self.best = self.current