import math
import random

class City:
    name = ""

class TourManager:
    x = y = 0

class Tour:
    def __init__(self, tour_manager = TourManager()):
        self.tour_manager = tour_manager

    def generate_individual(self):
        print("individual")
    
    def get_city(self, pos):
        print("get city")

    def tour_size(self):
        return 0

class SimulatedAnnealing():
    def __init__(self, tour_manager, initial_temperature, cooling_rate):
        self.tour_manager = tour_manager

        self.tour = Tour(tour_manager)
        self.tour.generate_individual()

        self.temperature = initial_temperature
        self.cooling_rate = cooling_rate

    def accept_solution(self, delta_energy):
        if delta_energy < 0:
            return True
        elif random.random() <= math.exp(-(delta_energy/self.temperature)):
            return True
        return False

    def evolve_tour(self):
        tour_evolved = Tour(self.tour_manager, self.tour)

        pos1 = random.randrange(self.tour.tour_size())
        pos2 = random.randrange(self.tour.tour_size())
        city1 = tour_evolved.get_city(pos1)
        city2 = tour_evolved.get_city(pos2)
        tour_evolved.set_city(pos2, city1)
        tour_evolved.set_city(pos1, city2)

        current_energy = self.tour.get_distance()
        new_energy = tour_evolved.get_distance()
        delta = new_energy - current_energy

        if self.accept_solution(delta):
            self.tour = tour_evolved

    def run(self):
        while self.temperature > 0:
            self.evolve_tour()
            self.temperature *= 1-self.cooling_rate