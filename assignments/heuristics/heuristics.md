# Comparison of heuristics for path-planning with the R2P2 simulator

## Objectives

* Understand the impact of the heuristic selection in path-planning

## Dependencies

Install the [R2P2](https://github.com/ISG-UAH/R2P2) simulator, which depends on the libraries numpy and matplotlib. Read the README.md file in the project's root folder for instructions about the simulator installation and usage.

## Practical assignment

Perform the following tasks:

1. Get familiar with the simulator running the example scenarios available in the project.

2. Consider the following grid map (10 X 10) where the robot is located at the cell labeled with R, and the target is located at the cell labeled with T. All the cells labeled with X are considered as occupied cells and the white cells are considered free to pass. Run the algorithms and see the results.  
 
<img align="right" src="r2p2-mapgrid.png" width="250">

4. Implement the following heuristics for A*: Octile, Manhattan, Euclidean and Chebyschev.

5. Run A* with the different heuristics.

7. What is the better algorithm and/or heuristic? Why?
