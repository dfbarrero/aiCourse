# PDDL 2.1 & 3.1 exercise

## Objectives

* Practice PDDL 2.1 and 3.1 syntax.

* Implement a domain and problem in that syntax.


## Exercise 1: Extend the Planetary exploration on Mars 

Extend the PDDL rover domain to consider time and resources. Let's consider that the rover can go at two speeds: fast and slow. The resource to be modelled is the battery. 
The consumption of the battery will change according to some parameters (for example, distance or speed). Then, add a new action that extends solar panels to recharge the battery. Each task will have a variable duration. The plan will have to take into account the consumption of the battery, and when is low (defined as a threshold value) recharge the battery.

Define also one preference:
* At the END, the battery of the rover is recharged.
 
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
