from random import Random
from time import time
import inspyred

chrLength = 15	# Chromosome length
popSize = 50	# Population size
maxGenerations = 15	# Max. generations
mutRate = 0.1	# Mutation rate
elite=0		# Elitism size

def onemax_fitness(candidates, args):
	fitness = [] 
	for cs in candidates: 
		fit = sum(cs)
		fitness.append(fit)
	print("Best fit: {0}, avg. fit: {1}".format(max(fitness), 
		float(sum(fitness))/len(fitness)))
	return fitness

def generator(random, args):
    return [random.choice([0, 1]) for _ in range(chrLength)]


prng = Random()
prng.seed(time()) 
    
ea = inspyred.ec.GA(prng)
ea.terminator = inspyred.ec.terminators.generation_termination

final_pop = ea.evolve(generator=generator, 
				evaluator=onemax_fitness,
				pop_size=popSize, 
				num_elites=elite, 
				max_generations=maxGenerations, 
				mutation_rate=mutRate)

best = max(final_pop)                          
print('Best solution: \n{0}'.format(str(best)))
if (best.fitness == chrLength): 
	print("Solution found!") 
else: 
	print("Solution NOT found")

