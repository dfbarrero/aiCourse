# Optimization of the trajectory of a spacecraft to the Moon

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

Where d_m is the mimimum distance from Moon, d the total distance traveled, c Moon crash penalty (1000) and l Earth landing reward (1000). Therefore, this is a minimization problem. Execute the following tasks.

1. Download the code that implements the fitness function (moonshot) [from here](code/moonshotshort.py) and test it. Remember that the Boost velocity must be given in vectorial form (x, y).
2. Design and implement an EA that solves the given problem.
3. Modify the algorithm to consider the following constrains (Hint: Use Bounders): Orbital height in (6e6, 8e6); Satellite mass in (10.0, 40.0); Boost velocity (x, y) in ((3e3, 9e3), (-10000.0, 10000.0)); Initial y velocity in (4000, 6000).

Once you had finished, compare your solution with the one proposed by the tutorial in http://pythonhosted.org/inspyred/tutorial.html#lunar-explorer. You can also use the template in https://gist.github.com/dfbarrero/93400a4c1974c9fff73cf48b96e1b77d.


