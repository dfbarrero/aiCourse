# Use PDDL with the R2P2 simulator

## Objectives

* Integrate the output of the PDDL rover example into the R2P2 simulator to execute the actions.

## Dependencies

Install the [R2P2](https://github.com/ISG-UAH/R2P2) simulator, which depends on the libraries numpy and matplotlib. Read the README.md file in the project's root folder for instructions about the simulator installation and usage.

## Practical assignment

From the folder ''r2p2'', perform the following tasks:

1. Get familiar with the simulator for PDDL. Use the "scenario-planning.json" file in the "conf" folder for running it as follows:

   python r2p2.py --scenario ../conf/scenario-planning.json

2. Edit the "robot.json" file in the "conf" folder and modify the values according to the predicates used in your problem. For example:
  
   "battery" : 100      --> (= (battery-capacity robot) 100)
   
   "charging_rate": 5   --> (= (charging-rate-battery robot) 5)

3. Variables "x" and "y" on the "robot.json" file represent the initial state of the robot. In our case is set to (202, 256).

4. Modify the battery value of your actions as follow: 

	 "movement_cost": 7   --> (decrease (battery-capacity ?r) (move-cost)) where in the problem  (= (move-cost) 7)
	 
	 "reading_cost": 10   --> (decrease (battery-capacity ?r) (read-cost)) where in the problem  (= (read-cost) 10)
	 
	 "picture_cost": 5    --> (decrease (battery-capacity ?r) (picture-cost)) where in the problem  (= (picture-cost) 5)
	 
	 "generic_cost": 1    --> any other action, (decrease (battery-capacity ?r) (generic-cost)) 
	  
    where in the problem  (= (generci-cost) 1)

5. The action to take a picture should be named "take_picture" action and store a picture in  the "logs/" Folder. 

6. Revise that your "move" action as follows:

   (:action move
    
    :parameters ?r - rover ?lorig ?ldest - coord ...
    
    Where "coord" should be defined as follows: P0811 --> X = 08 Y = 11

7. Ignore the rest of the variables since they are not needed for this assignment.

8. Edit the "controller-planning.json" file in the "conf" folder and adjust the output of your PDDL domain. By default the output is 
   stored in a file called "planning.txt" in the "res/" folder. See the definition of "plan_path" in that file.
   
   That is, when you run you problem and domain you do the following:
   
   ./sgplan -o domain.pddl -f problem.pddl > planning.txt

    
