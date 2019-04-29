# Use PDDL with the R2P2 simulator

## Objectives

* Integrate the output of PDDL into the R2P2 simulator to execute the actions.

## Dependencies

Install the [R2P2](https://github.com/ISG-UAH/R2P2) simulator, which depends on the libraries numpy and matplotlib. Read the README.md file in the project's root folder for instructions about the simulator installation and usage.

## Practical assignment

Perform the following tasks:

1. Get familiar with the simulator for PDDL. Use the "scenario-planning.json" file in the "conf" folder for running it as follows:

   python r2p2.py --scenario ../conf/scenario-planning.json

2. Edit the "robot.json" file in the "conf" folder and modify the values according to the predicates used in your problem. For example:
  
   "battery" : 100      --> (= (battery-capacity robot) 100)
   
   "charging_rate": 5   --> (= (charging-rate-battery robot) 5)

3. Variables "x" and "y" on the "robot.json" file represent the initial state of the robot. In our case is set to (202, 256).

4. Fix the duration value of your actions as follow: 

	 "movement_cost": 7   --> (:durative-action move (= ?duration 7) ...
	 
	 "reading_cost": 10   --> (:durative-action ReadingCo2  (= ?duration 10) ...
	 
	 "picture_cost": 5    --> (:durative-action Take-picture (= ?duration 5) ...
	 
	 "generic_cost": 13    --> any other action, (= ?duration 13)

5. The Take_Picture action will take a picture and store it in  the logs/ Folder. 

6. Ignore the rest of the variables since they are not needed for this assignment.

7. Edit the "controller-planning.json" file in the "conf" folder and adjust the output of your PDDL domain. By default the output is 
   stored in a file called "planning.txt" in the "res/" folder. See the definition of "plan_path" in that file.
   
   That is, when you run you problem and domain you do the following:
   
   ./sgplan -o domain.pddl -f problem.pddl > planning.txt

    
