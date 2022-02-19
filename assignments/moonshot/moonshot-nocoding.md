# Optimization of the trajectory of a spacecraft to the Moon (no coding)

## Objectives

* Set the parameters of a EA to solve a non-trivial problem

* Optimize a real-number function

<!-- (It is based on the problem exposed in the inspyted tutorial, do not read it!) -->

## Summary

You will be provided with the implementation of a EA that optimizes the trajectory of a spacecraft to transit the Moon; you will have to set its parameters and get the best solution.

## Assignment

This exercise deals with an optimization problem of a real-valued function. The objective is to design the trajectory of a spacecraft in orbit on Earth to the Moon using a gravity assist maneuver (see the figure below). For simplicity the problem is reduced to 2D, and there is only one boost at the begining of the journey. 

<img src="figs/moonshot.jpg" width="400" alt="Example of evolved trajectory to the Moon and return">

With those considerations, the parameters to optimize are:

* *Orbital height*. The spacescraft begins in a circular orbit over the Earth. This parameter sets its height.
* *Satellite mass*. It is self-explicatory.
* *Boost velocity*. Velocity after the engine boost. It is a bidimensional vector in form (x, y).
* *Initial y velocity*. Initially, the spacecraft moves in the Y axis with the velocity given by this parameter. It does not move in X.

The spacecraft must go to the Moon, transit it as close as possible, and return to land on Earth. It must not crash to the Moon (given by a distance equal to 0). To this end, we have the following fitness function:

f = (d_m/1000) + d + c - l

Where *d_m* is the mimimum distance from Moon, *d* the total distance traveled, *c* Moon crash penalty (+1000) and *l* Earth landing reward (-1000). Therefore, this is a **minimization** problem. 

The format of each line of the statistics file is as follows:

~~~
generation number, population size, worst, best, median, average, standard deviation
~~~

The format of each line of the individuals file is as follows:

~~~
generation number, individual number, fitness, string representation of candidate
~~~


Execute the following tasks.

1. Download the script that implements the Genetic Algorithm [from here](code/moonshotshort.py).
2. Check out the EA parameters available (running it with the *-h* argument).
3. Execute the script enabling orbit visualization.
4. Look for the best solution you can trying different parameters. How do you know that you have got *the best* solution?
5. Search the best combination of parameters. Which problems did you find?


The format of each line of the statistics file is as follows:

generation number, population size, worst, best, median, average, standard deviation

The format of each line of the individuals file is as follows:

generation number, individual number, fitness, string representation of candidate


