# PDDL 1.2 exercise

## Objectives

* Practice PDDL 1.2 syntax.

* Implement a PDDL domain and problem.

## Introduction

In order to help in the resolution of problems, one can check the International Planning Competitions (IPC) where the student can find a variety of domains. Some links are:

* [CSU Planning Repository: AIPS 2002 Planning Competition Problems and Domains](http://www.cs.colostate.edu/meps/repository/aips2002.html)

* [IPC 2011 domains](http://www.plg.inf.uc3m.es/ipc2011-deterministic/Domains)

## Exercise 1: [Gripper domain](https://github.com/Malola2015/planningCourse/blob/master/assignments/Gripper.md)

This domain is already given. 

## Exercise 2: [Blocks World](https://github.com/Malola2015/planningCourse/blob/master/assignments/Blocksworld.md)

This domain is partially provided.

## Exercise 3: Planetary exploration on Mars 

Suppose we have a rover on Mars, and we want the rover to move from an initial position to a final one. It can perform several tasks at various points, such as:
* Taking a picture 
* Drilling 
* Earth communication 
* Analyse samples 

The positions where those tasks have to be taken should be specified on the goal section using points that will be declared as an object of type "point". 
The rover can perform more than one of those activities (e.g. it can take 3 pictures in 3 different positions) and while those activities are performed the rover CANNOT move. 
