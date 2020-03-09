from random import Random
from time import time
import inspyred

# Do not touch this value
maxEvaluations=8000

# Customize these parameters
popSize = X
mutRate = X
elitism = X
tourSize = X
xoverPoints = X

def showStatistics(population, num_generations, num_evaluations, args):
    stats = inspyred.ec.analysis.fitness_statistics(population)
    print('Generation {0}, best fit {1}, avg. fit {2}'.format(
			num_generations, stats['best'], stats['mean']))

def main(prng=None, display=False): 
    if prng is None:
        prng = Random()
        prng.seed(time()) 
    
    problem = inspyred.benchmarks.Binary(inspyred.benchmarks.Schwefel(2), 
                                         dimension_bits=30)
    ea = inspyred.ec.GA(prng)
    ea.terminator = inspyred.ec.terminators.evaluation_termination 
    ea.observer = showStatistics
    ea.selector = inspyred.ec.selectors.tournament_selection
    final_pop = ea.evolve(generator=problem.generator,
                          evaluator=problem.evaluator,
                          pop_size=popSize,
                          maximize=problem.maximize,
                          bounder=problem.bounder,
                          max_evaluations=maxEvaluations, 
                          num_elites=elitism,
						  tournament_size=tourSize,
						  mutation_rate=mutRate,
						  num_crossover_points=xoverPoints)
                          
    if display:
        best = max(final_pop)
        print('Best Solution: \n{0}'.format(str(best)))
    return ea
            
if __name__ == '__main__':
    main(display=True)
