# Introduction to KNIME Analytics Platform

## Objectives

* Install KNIME

* First contact with KNIME

* Implement basic Machine Learning workflows with KNIME

* Data exploration with KNIME

## Working environment setup

Blablabla

## Practical assignment

```
n := Chromosome length
p := Population size
pm := Mutation probability

Initialize population with random values

While solution not found
	i := 0
	While i < p
		Select randomly two individuals in the population
		Compute their fitness
		Select fittest individual

		If random_number() < pm 
			Flip a random position of the selected individual

		Store individual in the next population

```

The following figure outlines the algorithm to implement.

<img align="center" src="ga.jpg" width="400">

(Image taken from [here](http://file.scirp.org/Html/1-8302163_41175.htm).)

Once the algorithm is implemented, perform the following tasks:

1. Show the best fitness found in each generation. Execute the algorithm. How does the best fitness evolve?
2. Compare the execution time with n=10, n=20 and n=100. (Hint: Use the Unix command *time*).

