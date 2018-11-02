# PDDL v2 exercises

## Objectives

* Practice PDDL v2 syntax.

* Implement a PDDL domain and problem.

## Introduction

In order to help in the resolution of problems, one can check the International Planning Competitions (IPC) where the student can find to ns of domains. Some links are:

* [CSU Planning Repository: AIPS 2002 Planning Competition Problems and Domains](http://www.cs.colostate.edu/meps/repository/aips2002.html)

* [IPC 2011 domains](http://www.plg.inf.uc3m.es/ipc2011-deterministic/Domains)


## Exercise 1: Mars rover with multiple tasks

Add to the Mars rover domain developed in the assignment [PDDL v1 exercises](https://github.com/dfbarrero/aiCourse/blob/master/assignments/planning/pddl-v1.md) several tasks that the rover can perform at various points, such as take pictures, drilling, earth communication, analyse samples, or extend solar panels to  recharge the battery. Assume that the rover does not move when these tasks are performed. In addition, it will be considered that the rover can go at two speeds: fast and slow. The resource to be modelled is the battery. Initially, we can consider that each activity consumes a fixed amount of battery, then it will be changed according to some parameters (for example, distance or speed). Also consider that each task has an initially constant duration and then variable. The plan will have to take into account the consumption of the battery, and when it is low (define a threshold value) should recharge the battery.

## Exercise 2 

Propose a domain where planning could be useful.

