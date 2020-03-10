# Comparison of heuristics for path-planning with the R2P2 simulator

## Objectives

* Understand the impact of the heuristic selection in path-planning

## Dependencies

Install the [R2P2](https://github.com/ISG-UAH/R2P2) simulator, which depends on the libraries numpy and matplotlib. Read the README.md file in the project's root folder for instructions about the simulator installation and usage.

Remember to install R2P2 dependencies by executing ```pip install -r requirements.txt``` from the folder that contains R2P2.

## Practical assignment

Perform the following tasks:

1. Get familiar with the simulator. Run the simulator with the command `python r2p2.py`. it will create a plain scenario with a robot teleoperated by the arrows keys.

2. Run the Path Planning scenario as follows:

   ```
   python r2p2.py --scenario ../conf/scenario-pathplanning.json
   ```

   Note that the robot is initially located at the position (18,19) and the goal at position (12,12). The simulator visualizes the computed path. 
   
3. Given that the configuration of the robot controller is located in the file ```conf/controller-pathplanning.json```, change the initial point to  (27,19) and the goal point to (8,20).

4. Change the algorithm (A* or Dijkstra) by setting "A*" or "Dijkstra" in the ```algorithm``` field of ```conf/controller-pathplanning.json``` (caution, the simulator is case sensitive). Can you observe any difference in the resulting path? Take into account that the default heuristic is naive, which returns a constant (and unrealistic) heuristic.

5. Which path-planning algorithm is being executed by default? Which heuristic is used by default? If needed, use the path-planning visualizer in https://qiao.github.io/PathFinding.js/visual/ to reconstruct the scenario and observe the node expansion using different algorithms.

6. Implement the Manhattan and Euclidean heuristics for A*: Go to the ```r2p2/heuristic.py``` file and fill out the functions ```euclidean``` and ```manhattan```. Both functions take the initial and final points as tuples (X, Y) and must return a float with the heuristic value.
