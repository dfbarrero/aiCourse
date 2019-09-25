# Comparison of heuristics for path-planning with the R2P2 simulator

## Objectives

* Understand the impact of the heuristic selection in path-planning

## Dependencies

Install the [R2P2](https://github.com/ISG-UAH/R2P2) simulator, which depends on the libraries numpy and matplotlib. Read the README.md file in the project's root folder for instructions about the simulator installation and usage.

## Practical assignment

Perform the following tasks:

1. Get familiar with the simulator. Run the simulator with the command `python r2p2.py`. it will create a plain scenario with a robot teleoperated by the arrows keys.

2. Run the Path Planning scenario as follows:

   ```
   python r2p2.py --scenario ../conf/configPathPlanning.json
   ```

   Observe that the robot is initially located at the position (19,15) and the goal (12,12). The simulator visualizes the computed path. 
   
3. Given that the configuration of the robot controller is located in the file ```conf/controller-pathplanning.json```, change the initial point from (19,15) to (27,19).

4. Which path-planning algorithm is being executed by default? Which heuristic is used by default?

5. Change the algorithm (A* or Dijkstra) by setting "A*" or "Dijkstra" in the ```algorithm``` field of ```conf/controller-pathplanning.json``` (caution, the simulator is case sensitive). Can you observe any difference in the resulting path?

5. Implement the following heuristics for A*: Octile, Manhattan and Euclidean.

6. Go to the ```r2p2/heuristic.py``` file, define the heuristic you want to use, and then, register it. After that, go to "conf/controllerPathPlanning.json" and update the field "heuristic" with the heuristic you want to use. 

7. For the heuristic function, you can use the grid point or the absolute point representation. Compare if anything changes depending on the representation. Carefully look at "r2p2/node.py" to analyze how to access to the coordinates of each point (represented as a node).

8. What is the better algorithm and/or heuristic? Why?
