import time
import sys
import math
from person import Person
import random
from mpi4py import MPI

sports = ["martial_arts", "football", "basketball", "powerlifting"]

chosen_sport = "basketball"
chosen_sport = str(sys.argv[1])
crossing_rate = 0.7
mutation_rate = 0.3
max_population = 200
best_population = 150
tasks_number = 10
task_size = max_population/tasks_number
persons_to_add_per_task = (max_population-best_population)/tasks_number
WORK = 1
DIE = 2


def get_tasks(population, task_size, tasks_number):
    tasks = []
    for i in range(tasks_number):
        start = int(i*task_size)
        end = int(start + task_size)
        #print(start," ",end)
        task = population[start:end]
        #task = (start, end)
        tasks.append(task)
        i = i+1
    return tasks


def give_tasks(tasks, comm, N, persons_to_add_per_task, task_size, chosen_sport, tasks_number):

    w = 0
    r = 0
    extra_population = []
    for i in range(1, N):
        if w < tasks_number:
            work = tasks[w]
            comm.send(work, dest=i, tag=WORK)
            w += 1

    while (w < tasks_number):
        status = MPI.Status()
        population_from_worker = comm.recv(
            source=MPI.ANY_SOURCE, status=status)
        #print(len(population_from_worker))
        extra_population.extend(population_from_worker)
        id = status.Get_source()
        comm.send(tasks[w], dest=id, tag=WORK)
        r += 1
        w += 1

    while (r < tasks_number):
        status = MPI.Status()
        population_from_worker = comm.recv(
            source=MPI.ANY_SOURCE, status=status)
        #print(len(population_from_worker))
        extra_population.extend(population_from_worker)
        id = status.Get_source()
        r += 1

    for i in range(1, N):
        comm.send(-1, dest=i, tag=DIE)
    return extra_population


def worker(comm):
    while(True):
        id = comm.Get_rank()
        status = MPI.Status()
        population_from_worker = comm.recv(
            source=0, tag=MPI.ANY_TAG, status=status)
        #population_from_worker = population[ranges[0]:ranges[1]]
        if population_from_worker != -1:
            population_from_worker = process_population(
                population_from_worker, chosen_sport, task_size+persons_to_add_per_task)

        if (status.Get_tag() == DIE):
            return
        comm.send(population_from_worker, dest=0)


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
        new_person = Person(age, height, weight, strength,
                            endurance, agility, speed, explosivness)
        population.append(new_person)
    return population


def get_best_persons(population, chosen_sport, n):
    population.sort(key=lambda x: x.evaluate_fitness(
        chosen_sport), reverse=True)
    return population[0:n]


def process_population(population, chosen_sport, n):
    size = len(population)
    while size < n:
        idx = random.uniform(0, 1)
        if idx < crossing_rate:
            i1 = random.randrange(size)
            i2 = random.randrange(size)
            person1 = population[i1]
            person2 = population[i2]
            if person1.valid_person == True and person2.valid_person == True:
                new_person = person1.crossing(person2)
                population.append(new_person)
                size += 1
        if idx < mutation_rate:
            i3 = random.randrange(size)
            person3 = population[i3]
            if person3.valid_person == True:
                person3.mutate()
                population[i3] = person3
    return population


def print_population_fitness(population, chosen_sport):
    for person in population:
        print(person.evaluate_fitness(chosen_sport)," | ",person.the_best, flush=True)


def get_the_best(population, chosen_sport):
    the_best = population[0]
    best_score = 0
    idx = 0
    for person in population:
        score = person.evaluate_fitness(chosen_sport)
        if score > best_score:
            best_score = score
            the_best = person
        idx += 1
    return the_best


population = generate_random_population(max_population)

the_best = population[0]
population_number = 1
comm = MPI.COMM_WORLD
id = comm.Get_rank()
N = comm.Get_size()
start = time.time()
the_best_index = 0
while the_best.evaluate_fitness(chosen_sport) < 90:
    if id == 0:
        tasks = get_tasks(population, task_size, tasks_number)
        population = get_best_persons(population, chosen_sport, best_population)
        #print_population_fitness(population, chosen_sport)
        extra_population = give_tasks(tasks, comm, N, persons_to_add_per_task, task_size, chosen_sport, tasks_number)
        population.extend(extra_population)
        # rozdzielamy
        #population = process_population(population, chosen_sport, max_population)
        # zbieramy do kupy
        the_best = get_the_best(population, chosen_sport)
        #print("----------")
        #print_population_fitness(population, chosen_sport)
        #population[the_best_index].set_the_best()
        print("Population ", population_number, ": ",the_best.evaluate_fitness(chosen_sport), flush=True)
        #time.sleep(0.2)
        population_number += 1
        #if population_number == 10:
        #    break
    else:
        worker(comm)
end = time.time()
print("Time: ", end-start, flush=True)
print("The best person:", flush=True)
print(the_best.print_stats(), flush=True)