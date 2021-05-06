# PDDL 2.1 & 3.1 exercise

## Objectives

* Practice PDDL 2.1 and 3.1 syntax.

* Implement a domain and problem in that syntax.

* (Optionally) Run R2P2 simulator.


## Exercise 1: Localization of a CO2 source

Suppose we have a rover on Mars, and we want the rover to move from an initial position to a final one. 
We define the following actions:
 - Recharge the batteries by extending the solar panels.
 - Move between locations with a defined navigation mode. There are two possible values: N0 and N1. When the value is N1 the speed is double than when the value is N0.
 - Take pictures with the camera. 
 - Drill some areas for knowing the composition of the surface. 
 - Perform reading measures of CO2 in the atmosphere. 

The positions where those tasks have to be taken should be specified on the goal section using waypoints. The rover can perform more than one of those activities (e.g. it can take 10 pictures in 10 different positions) and while those activities are performed the rover CANNOT move. In addition, it will be considered that the rover can go at two speeds: fast and slow. The resource to be modelled is the battery. The consumption of the battery will change according to some parameters (for example, distance or speed). Each action will have a variable duration. The plan will have to take into account the consumption of the battery, and when is low (defined as a threshold value) recharge the batteries.

Define also one preference:
 -  At the END the battery of the rover is recharged.
 
 Then, define a constrain that uses that preference.


## Exercise 2: Use the R2P2 simulator (Optional)

You can use the R2P2 simulator to visualize the previous plan. 

Install the [R2P2](https://github.com/ISG-UAH/R2P2) simulator, which depends on the libraries numpy and matplotlib. Read the README.md file in the project's root folder for instructions about the simulator installation and usage.

Remember to install R2P2 dependencies by executing ```pip install -r requirements.txt``` from the folder that contains R2P2.

Run your domain and problem and save the plan solution into a file called <em>planning.txt</em>. Then, replace the file with the same name located in ```../res/planning.txt```. You can modify the path but it will be simpler to just replace that file.

Run the Planning domain scenario as follows:

   ```
   python r2p2.py --scenario ../conf/scenario-planning.json
   ``` 

Hope it helps to visualize the results.
