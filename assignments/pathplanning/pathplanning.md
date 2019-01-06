# Path-planning exercises


## Objectives

* Implement path-planning algorithms

* Increase knowledge about path-planning

## Preliminary steps

Blablabla

## The 8-queens problem

Blablabla

## One-max problem with inspyred

Copy or [download](code/onemax.py) the following script, which implements the one-max problem with a basic Genetic Algorithm implemented with inspyred. All the relevant algorithm parameters are contained in variables defined in the begining of the script.

```Python
from random import Random
from time import time
import inspyred

chrLength = 15	# Chromosome length
popSize = 50	# Population size
maxGenerations = 15	# Max. generations
mutRate = 0.1	# Mutation rate
elite=0		# Elitism size
tourSize=2      # Tournament size

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
ea.selector = inspyred.ec.selectors.tournament_selection

final_pop = ea.evolve(generator=generator, 
	evaluator=onemax_fitness,
	pop_size=popSize, 
        tournament_size=tourSize,
	num_elites=elite, 
	max_generations=maxGenerations, 
	mutation_rate=mutRate)

best = max(final_pop)                          
print('Best solution: \n{0}'.format(str(best)))
if (best.fitness == chrLength): 
	print("Solution found!") 
else: 
	print("Solution NOT found")
```

The parameter setting used is the following one:

* Representation: Binary

* Chromosome length: 15

* Crossover: 1-point crossover

* Mutation: Flip mutation

* Mutation probability: 0.1

* Population size: 50

* Termination: 15 generations

* Selection: Tournament with size 2

Perform the following tasks:

1. Execute the script to validate the installation of *Inspyred*.

2. Observe how average and best fitness evolve along the time. Explain their behavior.

3. Execute the script several times, did it always find the solution? Why?

4. Change the chromosome length to 30 and repeat the previous questions.

5. Customize the algorithm settings to increase the probability of finding a solution.

6. Set p_m=0.5. What happen?

7. Set p_m=1.0. What happen?

8. Set the chromosome length to 50 and customize the algorithm to increase the probability of finding a solution.

## Real number function optimization with Inspyred

This exercise deals with the optimization of a function. We will optimize the parameters of a function named the Schwefel function, that can be formally stated as follows:

<img src="figs/eqn.png">

where *n* represents the number of dimensions and x_i \in [-500, 500] for all i=1,...,n. The input values that optimizes the function is [420.9687, 420.9687, ..., 420.9687], this a minimization task and the best fitness is 0. A graphical representation of this problem for n=2 (two dimensions) follows.

<img src="figs/schwefel.png" width="400">

The code that implemens a GA that solves the Schwefel problem is the next listing. You can download the (code here)[code/ga_example.py]. 

```Python
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
```

Please observe that the main algorithm parameters have been deleted. The remaining parameters are as follows:

* Representation: Binary

* Chromosome length: 30

* Crossover: n-point crossover

* Mutation: Flip mutation

* Mutation probability: X

* Population size: X

* Termination: 8,000 evaluations

Perform the following tasks:

1. Set the parameters to get a perfect solution (fitness=0).

2. Set the parameters to get the solution as soon as possible.

3. Execute the algorithm 10 times and show a graph relating generation, best fitness and average fitness. To obtain the graph values, average across all the 10 runs. If necessary, change the code and use any external tool (Excel, Matlab, R, Gnuplot, ...) at your convenience.

