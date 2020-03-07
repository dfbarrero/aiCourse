# PDDL v1 exercises

## Objectives

* Practice PDDL v1 syntax.

* Implement a PDDL domain and problem.

## Introduction

In order to help in the resolution of problems, one can check the International Planning Competitions (IPC) where the student can find a variety of domains. Some links are:

* [CSU Planning Repository: AIPS 2002 Planning Competition Problems and Domains](http://www.cs.colostate.edu/meps/repository/aips2002.html)

* [IPC 2011 domains](http://www.plg.inf.uc3m.es/ipc2011-deterministic/Domains)


## Exercise 1: Robot motion planning

This domain is about a robot that can move between two rooms and pick up or drop balls with either of its two arms. 

The planning model (domain and problem) will consist of:
 -  Objects: the two rooms, balls and two robot arms (problem)
 -  Predicates: Is x a room? Is x a ball? Is ball x inside room y? Is robot arm x empty? (domain)
 -  Initial state: all balls and the robot are in the first room. All robot arms are empty (problem)
 -  Goal specification: all balls must be in the second room (problem)
 -  Actions/Operators: the robot can move between rooms, pick up a ball or drop a ball (domain)

Initially, all balls and the robot are in the first room. We want the balls to be in the second room. The figure shows the initial state:

<img align="center" src="gripper-i.png" width="200">

And the next figure shows the goal state:

<img align="center" src="gripper-g.png" width="200">


Do the following steps:
 1. Implement the planning model using the on-line editor, and check the results:
 [http://editor.planning.domains/](http://editor.planning.domains/)
 2.  Place two of the balls and the gripper in roomb. The goal is that all balls are in rooma. Run the new model.
 3. Add two more balls and place them when you decide. The goal is that 5 balls are in the same room and the one remaining, in the other room. Run the new model.
 4. Extend the gripper domain to allow the definition of types. For that:
    - Add in the domain the types as follow: 
      `(:requirements :strips :typing)` 
      `(:types room ball)` 
    - In the operators, specify the type:
       `:parameters (?b - ball)`
    - In the problem, define the type of the objects:
    `(:objects rooma roomb - room)`
