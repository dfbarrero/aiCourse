# Optimization of the trajectory of a spacecraft to the Moon (no coding)

## Objectives

* Set the parameters of a EA to solve a non-trivial problem

* Optimize a real-number function

<!-- (It is based on the problem exposed in the inspyted tutorial, do not read it!) -->

## Summary

You will be provided with the implementation of a EA that optimizes the trajectory of a spacecraft to transit the Moon and come back to Earch. You will have to set its parameters and obtain the best solution.

## Problem statement

This exercise deals with an optimization problem of a real-valued function. The objective is to design the trajectory of a spacecraft in orbit on Earth to the Moon and come back to Earth (see the figure below). For simplicity, the problem is reduced to 2D, and there is only one boost at the begining of the journey. 

<img src="figs/moonshot.jpg" width="400" alt="Example of evolved trajectory to the Moon and return">

With those considerations, the parameters to optimize are:

* *Orbital height*. The spacescraft begins in a circular orbit over the Earth. This parameter sets its height.
* *Satellite mass*. It is self-explicatory.
* *Boost velocity*. Velocity after the engine boost. It is a bidimensional vector in form (x, y).
* *Initial y velocity*. Initially, the spacecraft moves in the Y axis with the velocity given by this parameter. It does not move in X.

The spacecraft must go to the Moon, transit it as close as possible, and return to land on Earth. It must not crash to the Moon (given by a distance equal to 0). To this end, we have the following fitness function:

f = (d_m/1000) + d + c - l

Where *d_m* is the mimimum distance from Moon, *d* the total distance traveled, *c* Moon crash penalty (+1000) and *l* Earth landing reward (-1000). Therefore, this is a **minimization** problem of function *f* with five variables.

The simulation ends if the spacescraft losses radio communication with Earth. 

## moonshot-nocoding.py

In order to ease this assignment, a complete implementation of the evolutionary algorithm is [provided](https://gist.github.com/dfbarrero/e47016acf557354882f0ad6a19f0dda9), it includes orbital dynamics computations, fitness assessment and the evolutionary algorithm itself. 

The algorithm parameters can be set from the command line, to obtain a complete list of the arguments it accepts, please execute the following command:

~~~Bash
paul@arrakis:~$ python moonshot-nocoding.py -h

usage: moonshot-nocoding [-h] [--population POP] [--tournament TOUR]
                         [--evaluations EVALUATIONS] [--elite ELITE]
                         [--crossover PROB] [--mutation PROB]
                         [--gaussianmean MEAN] [--gaussianstd STD] [--orbit]
                         [--plot]

Optimization of a transit orbit from Earth to Moon.

optional arguments:
  -h, --help            show this help message and exit
  --population POP, -p POP
                        population size [default=20]
  --tournament TOUR, -t TOUR
                        tournament size [default=2]
  --evaluations EVALUATIONS, -e EVALUATIONS
                        maximum number of evaluations [default=200]
  --elite ELITE, -l ELITE
                        crossover probability [default=0]
  --crossover PROB, -c PROB
                        crossover probability [default=1]
  --mutation PROB, -m PROB
                        mutation rate [default=0.01]
  --gaussianmean MEAN   gaussian mutation mean [default=0]
  --gaussianstd STD     gaussian mutation standard deviation [default=1]
  --orbit, -o           plot orbit in pdf file [default false]
  --plot                plot statistics [default false]

~~~

The script implements a Genetic Algorithm with the following components:

- Float codification with five genes, one per argument to optimize.
- Tournament selection.
- Gaussian mutation.
- Blend crossover. It is a variation of an arithmetic crossover where a small mutation is added.

Each time the script runs the evolutionary algorithm, it stores in the working directory two files, *moonshot_ec_individuals.csv* and *moonshot_ec_statistics.csv*,  containing data about all the individuals in the population and statistics grouped by generation.

The format of each line of the individuals file is as follows:

~~~
generation number, individual number, fitness, string representation of candidate
~~~

The format of each line of the statistics file is as follows:

~~~
generation number, population size, worst, best, median, average, standard deviation
~~~

Please, observe that you can save a PDF file with a plot of the best orbit passing the argument *--orbit*. The file name will have the format `solution-{fitness}.pdf'.

# Tasks

Execute the following tasks.

1. Download the script that implements the Genetic Algorithm [from here](https://gist.github.com/dfbarrero/e47016acf557354882f0ad6a19f0dda9).
2. Check out the EA parameters available (running it with the *-h* argument).
3. Execute the script enabling orbit visualization.
4. Look for the best solution you can trying different parameters. How do you know that you have got *the best* solution? (to be discussed in class).
5. Search the best combination of parameters using any tool in your hand. Write down the problems you will find in this search (to be discussed in class).





