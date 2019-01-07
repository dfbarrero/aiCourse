# PDDL v1 exercises

## Objectives

* Practice PDDL v1 syntax.

* Implement a PDDL domain and problem.

## Introduction

In order to help in the resolution of problems, one can check the International Planning Competitions (IPC) where the student can find a variety of domains. Some links are:

* [CSU Planning Repository: AIPS 2002 Planning Competition Problems and Domains](http://www.cs.colostate.edu/meps/repository/aips2002.html)

* [IPC 2011 domains](http://www.plg.inf.uc3m.es/ipc2011-deterministic/Domains)

The student should generate one domain file and at least 3 problem files for each exercise.


## Exercise 1: Robot motion planning

The original STRIPS program was designed to control Shakey, a robot that roamed the halls of SRI in the early 1970s. It turns out that most of the work on STRIPS involved simulations where the actions performed were just printing to a terminal, but occasionally Shakey would actually move around, grab, and push things based on the plans created by STRIPS. The figure shows a version of Shakey’s world consisting of four  rooms lined up along a corridor, where each room has a door and a light switch.

<img align="center" src="shakey.png" width="400">

Shakey can move from place to place, push movable objects (such as boxes), climb on and off of rigid objects (such as boxes) and turn light switches in and off. There are 6 actions:

* Go from current location x to location y: Go (x,y) moves from x to y (that cannot be the same room). By convection there is a room between rooms.
* Push an object b from location x to location y: Push(b,x,y).
* Climb up/down onto a box: Climb(b).
* Switch on/off  the  light. Because Shakey is short, this can only be done when Shakey is on top of a box that is at the room location.

Define the domain and the problem for the Shakey world and generate the **same problem** of the figure. Extend the domain to include the actions Open and Close.  As preconditions for the Go action, add that the door should be open. Assume that when pushing or switching the interruptor is enough that they are in the same place (don't subdivide the map on cells since it will complicate the modelling). 
Generate another problem(s) with higher/lesser number of rooms and boxes randomly distributed. Note that rooms can be (or not) connected with a corridor.

## Exercise 2: Rocket domain

A rocket can mean a type of engine or a vehicle that uses that engine. Like most engines, rockets burn fuel. Most rocket engines turn the fuel into hot gas. The engine pushes the gas out its back. The gas makes the rocket move forward. A rocket engine doesn't need air. It carries with it everything it needs. A rocket engine works in space, where there is no air. NASA uses rockets to launch satellites. It also uses rockets to send probes to other worlds. These rockets include the Atlas V, the Delta II, the Pegasus and Taurus. NASA uses smaller "sounding rockets" for scientific research.  NASA also is working on a powerful new rocket called a heavy lift vehicle that will be able to take big loads into space. Together, these new rockets will make it possible to explore other worlds. Someday they may send humans to Mars (https://www.nasa.gov/audience/forstudents/k-4/stories/nasa-knows/what-is-a-rocket-k4.html).

Consider the problem where you have rockets to load and unload things or astronauts and send them back and forth space/Earth. Rockets can fly from a start location to a destination but only once (they run out of fuel). Use PDDL to model the problem of moving cargos and people from different locations. Differentiate the cargos that are things from humans. Use types in PDDL to do that.

