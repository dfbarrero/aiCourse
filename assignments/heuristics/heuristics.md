# Comparison of heuristics for path-planning with the R2P2 simulator

## Objectives

* Understand the impact of the heuristic selection in path-planning

## Dependencies

Install the [R2P2](https://github.com/ISG-UAH/R2P2) simulator, which depends on the libraries numpy and matplotlib. Read the README.md file in the project's root folder for instructions about the simulator installation and usage.

## Practical assignment

Perform the following tasks:

1. Get familiar with the simulator. Use the "conf/configPathPlanning.json" file for running it.

2. Consider the grid map "res/test_2.png". The robot should be located at the position X=27 Y=27 and the goal X=12 Y=12. For setting those values, go to file "conf/controllerPathPlanning.json" and modify "start" and "goal" fields. 

3. Try other maps available in the res/ folder. Try other goals and start positions.

4. Change the algorithm (A* or Dijkstra) by setting "A*" or "Dijkstra" in the algorithm field of "conf/controllerPathPlanning.json". 

5. Implement the following heuristics for A*: Octile, Manhattan and Euclidean.

6. Go to the "r2p2/heuristic.py" file, define the heuristic you want to use, and then, register it. After that, go to "conf/controllerPathPlanning.json" and update the field "heuristic" with the heuristic you want to use. 

7. For the heuristic function, you can use the grid point or the absolute point representation. Compare if anything changes depending on the representation. Carefully look at "r2p2/node.py" to analyze how to access to the coordinates of each point (represented as a node).

8. What is the better algorithm and/or heuristic? Why?
