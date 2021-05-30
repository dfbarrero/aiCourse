# PDDL 2.1 & 3.1 exercise

## Objectives

* Practice PDDL 2.1 and 3.1 syntax.

* Implement a domain and problem in that syntax.



## Exercise 1: Airport Domain  

The [Airport domain](https://github.com/dfbarrero/aiCourse/blob/master/assignments/planning/airport.md) is partially modelled. 

## Exercise 2: Extended Gripper

We are going to extend the [GRIPPER domain](https://github.com/Malola2015/planningCourse/blob/master/assignments/Gripper.md) to use time and preferences. 

Do the following steps:
 1. Consider that the rooms where the robot of the GRIPPER domain moves are kitchen and living room; and that the robot is initially in the kitchen, together with two balls Z1 and Z2. We want as a goal that the two balls are in the living room. Model this new situation in the corresponding file.
 2. Extend the `pick-up` and `drop` actions to have a duration that depends on the weight of the ball. Name that predicate as `dur-ball`. 
 3. Add a preference that expresses that the robot is at the end in the living room.
 4. Comment the previous preference and add another preference that expresses that the robot is sometime in another room called `bathroom`. 

## Exercise 3: [Extended Pizzeria](https://github.com/Malola2015/planningCourse/blob/master/assignments/ExtPizza.md)

## Exercise 4: Extended Planetary exploration on Mars 

Extend the PDDL rover domain to consider time and resources. Let's consider that the rover can go at two speeds: fast and slow. The resource to be modelled is the battery. 
The consumption of the battery will change according to some parameters (for example, distance or speed). Then, add a new action that extends solar panels to recharge the battery. Each task will have a variable duration. The plan will have to take into account the consumption of the battery, and when is low (defined as a threshold value) recharge the battery.

Define also one preference:
* At the END, the battery of the rover is in the position it was in the initial state.
 
 Then, define a constrain that uses that preference.


## Exercise 5: Use the R2P2 simulator (Optional)

You can use the R2P2 simulator to visualize the previous plan. 

Install the [R2P2](https://github.com/ISG-UAH/R2P2) simulator, which depends on the libraries numpy and matplotlib. Read the README.md file in the project's root folder for instructions about the simulator installation and usage.

Remember to install R2P2 dependencies by executing ```pip install -r requirements.txt``` from the folder that contains R2P2.

Run your domain and problem and save the plan solution into a file called <em>planning.txt</em>. Then, replace the file with the same name located in ```../res/planning.txt```. You can modify the path but it will be simpler to just replace that file.

Run the Planning domain scenario as follows:

   ```
   python r2p2.py --scenario ../conf/scenario-planning.json
   ``` 

Hope it helps to visualize the results.
