import time
import sys
import math
from person import Person
import random

sports = [ "martial_arts", "football", "basketball", "powerlifing"]

chosen_sport = "basketball"
crossing_rate = 0.7
mutation_rate = 0.1

def generate_random_population(n):
    population = []
    for i in range(n):
        age = 15 + random.randrange(45)
        height = 160 + random.randrange(60)
        weight = 50 + random.randrange(70)
        strength = random.randrange(16)
        endurance = random.randrange(16)
        agility = random.randrange(16)
        speed = random.randrange(16)
        explosivness = random.randrange(16)
        new_person = Person(age, height, weight, strength, endurance, agility, speed, explosivness)
        population.append(new_person)
    return population


def get_best_persons(population, chosen_sport, n): 
    population.sort(key=lambda x: x.evaluate_fitness(chosen_sport), reverse=True)
    return population[0:n]

def process_population(population, chosen_sport, n):
    size = len(population)
    while size < n:
        idx = random.uniform(0,1)
        if idx < crossing_rate:
            i1 = random.randrange(size)
            i2 = random.randrange(size)
            person1 = population[i1]
            person2 = population[i2]
            if person1.valid_person == True and person2.valid_person == True:
                new_person = person1.crossing(person2)
                population.append(new_person)
                size+=1
        if idx < mutation_rate:
            i3 = random.randrange(size)
            person3 = population[i3]
            if person3.valid_person == True:
                person3.mutate()
                population[i3] = person3
    return population

def print_population_fitness(population, chosen_sport):
    for person in population:
        print(person.evaluate_fitness(chosen_sport))

def get_the_best(population, chosen_sport):
    the_best = population[0]
    return the_best

population = generate_random_population(100)

the_best = population[0]
population_number = 1
start = time.time()
while the_best.evaluate_fitness(chosen_sport) < 95:
    population = get_best_persons(population, chosen_sport, 80)
    population = process_population(population, chosen_sport, 100)
    the_best = get_the_best(population, chosen_sport)
    print("Population ",population_number,": ",the_best.evaluate_fitness(chosen_sport))
    time.sleep(0.2)
    population_number += 1
end = time.time()
print("Time: ",end-start)
print("The best person:")
print(the_best.print_stats())