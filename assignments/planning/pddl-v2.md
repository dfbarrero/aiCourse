# PDDL v2 exercises

## Objectives

* Practice PDDL v2 syntax.

* Implement a PDDL domain and problem.

## Introduction

In order to help in the resolution of problems, one can check the International Planning Competitions (IPC) where the student can find to ns of domains. Some links are:

* [CSU Planning Repository: AIPS 2002 Planning Competition Problems and Domains](http://www.cs.colostate.edu/meps/repository/aips2002.html)

* [IPC 2011 domains](http://www.plg.inf.uc3m.es/ipc2011-deterministic/Domains)

The student should generate one domain file and at least 3 problem files for each exercise.

## Exercise 1: Mars rover domain with multiple tasks

Suppose we have a rover on Mars, and we want it to move from an initial position to a final one. It can perform several taks at various points, such as take pictures, drilling, earth communication, analyse samples, or extend solar panels to  recharge the battery. The positions where those tasks have to be taken should be specified on the goal section. The rover can peform more than one of those activities (e.g. it can take 10 pictures in 10 different positions) and while those activities are performed the rover CANNOT move. In addition, it will be considered that the rover can go at two speeds: fast and slow. The resource to be modelled is the battery. Initially, we can consider that each activity consumes a fixed amount of battery, then it will be changed according to some parameters (for example, distance or speed). Also consider that each task has an initially constant duration and then variable. The plan will have to take into account the consumption of the battery, and when it is low (define a threshold value) should recharge the battery. 

If you want to visualize the output, please go to the following link to use the R2P2 simulator.

https://github.com/dfbarrero/aiCourse/blob/master/assignments/planning/r2p2-pddl.md

## Exercise 2 

Propose a domain where planning could be useful.

