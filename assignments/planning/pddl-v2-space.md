# PDDL 2.1 & 3.1 exercise

## Objectives

* Practice PDDL 2.1 and 3.1 syntax.

* Implement a domain and problem in that syntax.


## Exercise 1: Extend the Planetary exploration on Mars 

Extend the PDDL rover domain to consider time and resources. Let's consider that the rover can go at two speeds: fast and slow. The resource to be modelled is the battery. 
The consumption of the battery will change according to some parameters (for example, distance or speed). Then, add a new action that extends solar panels to recharge the battery. Each task will have a variable duration. The plan will have to take into account the consumption of the battery, and when is low (defined as a threshold value) recharge the battery.

Define also one preference:
* At the END, the battery of the rover is recharged.
 
 Then, define a constrain that uses that preference.
