# Programming Evolutionary Algorithms with Inspyred

## Objectives

* Implement EAs with a proper framework

* Solve non-trivial problems with EAs

## Preliminar note: Pseudo random numbers generation

Evolutionary Algorithms (EAs), like any other stochastic search algorithm heavily depend on randomness to solve problems. As a consequence, the algorithm needs to generate a large number of random numbers, which is itself a serious problem. Fortunately, Python's default random number generator works well, and is suitable for using in EC. Given that a computer is a deterministic system, getting randomness from it is complex. For this reason random number are not random, but instead pseudorandom.

In order to properly use a pseudorandom numbers generator we need to feed the algorithm with a seed, i.e., a number that is used to initialize the algorithm. The seed should be as much random as possible, so a common practice is to use the current time, in milliseconds. From an EC perspective, it is important to note that two equal seeds will generate the same pseudoranom number sequence, it means that *two executions of an EA with the same seed will give the same results*. It is a very important feature, because eases the repetivity of the execution.

For this reason, any well-implemented EA will contain some code to initialize the pseudorandom numbers generator. In the case of *Inspyred*, you will always find something like

```Python
from random import Random
from time import time

# Code here

# Properly initialize pseudorandom numbers generator
prng = Random()
prng.seed(time())

# More code here
```

## Getting into Inspyred API

Inspyred is a well-documented project. Go to the project website in http://pythonhosted.org/inspyred/index.html and read the following texts:

* Read the "Overview". Pay special attention to the section "Design Methodology";
* *Do not* read the tutorial (the following exercises are inspired in those examples);
* Examine the examples "Genetic Algorithm" and "Evolution Strategy" within the "Examples" section. You might need futher information about [Schewefel](https://duckduckgo.com/?q=Schwefel+genetic&t=ffab&iar=images&iax=images&ia=images&iai=https%3A%2F%2Fjenyay.net%2Fblog%2Fwp-content%2Fuploads%2F2019%2F11%2Fschwefel_2d-1536x842.png) and [Rosenbrock](https://duckduckgo.com/?q=rosenbrock+function&t=ffab&iar=images&iax=images&ia=images), both are two well-known functions commonly used to test optimization algorithms;
* Read carefully the subsection "Customized Algorithms",  within the "Examples" section.

Once you got a general understanding on the structure of Inspyred, you should get used to handle its reference manual and source code. Much of the features are not documented, and many times there are doubs that requires reading the source code. Based on the reference library (located in http://pythonhosted.org/inspyred/reference.html), answer the following questions:

1. Identify all the *mutation* methods available by default.
2. Identify all the *recombination* methods available by default.
3. Identify all the *parent selection* methods available by default.
4. Identify all the *survivor selection* methods available by default.
5. Identify all the *termination* methods available by default.
6. Identify all the methods available to inspect the population throughout the evolutionary process.

## Playing with Inspyred

Based on the code of the one-max problem introduced in the previous practical assigment, perform the following tasks.

1. Change the selection method to fitness proportionale.
2. Change the crossover to uniform crossover.
3. Change the mutation to scramble mutation.
4. Show the basic statistics (best, worst and average fitness) for each generation. Use the proper observer.
5. Store all the individuals in a CSV file for futher analysis. Use the proper observer.
6. Bonus track: Visualize in real-time the basic fitness statistics in a plot. Use the proper observer.

## Genetic operators customization

We are going to use a variant of the one-max problem. Instead of an all-ones chromosomes, we want to generate a chromosome with the pattern [0,1,1,1] repeated k times, for instance, [0,1,1,1,0,1,1,1,0,1,1,1] with k=3. 

Implement a GA to solve the previously described problem and store it in a file named *ga-custom.py*. Divide this task into the following steps.

1. Implement an skeleton of the algorithm with *Inspyred* with default components.
2. Define and implement the fitness function.
3. Implement a customized crossover operator that only splits chromosomes in the boundaries of the repeated pattern [0,1,1,1]. Compare this operator with one-point crossover (optional).
