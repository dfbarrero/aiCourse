# Optimization of a robotic controller through an Evolutionary Algorithm

## Objectives

* Practice real-numbers optimization.

* Implement an Evolutionary Algorithm.

* Learn to use the Inspyred package.


## Prerrequisites

First of all, download and install R2P2 following the instructions given in the [R2P2 GitHub repository](https://github.com/ISG-UAH/r2p2), please, pay attention to install [Anaconda](https://www.anaconda.com/distribution/) first (a Python distribution that makes everything easier) and R2P2 dependencies. 

Check out the installation running a basic scenario with the following command from the folder r2p2:

```
(r2p2) paul@arrakis:~/r2p2$ python r2p2.py
```

If everything is working properly, you shoud be now watching a basic scenario with a robot that can be teleoperated with the arrows keys, as the following picture depicts.

<img align="center" src="r2p2-stage.png" width="400">

The scenario is stored in a JSON file under the conf folder, you can change it with the argument *--scenario*. A very convenient sandbox scenario is provided in R2P2, run it with

```
(r2p2) paul@arrakis:~/r2p2/r2p2$ python r2p2.py --scenario ../conf/scenario-sandbox.json
```
Check out the scenarios contained in conf and try to run some of them.

You can get all the arguments to R2P2 passing the argument *--help*.

## Objective

The main objective of this assignment is to develop a robot controller based on a classical controller. This controller uses a collection of fixed rules to determine the robot behaviour. Those rules are based on several constants whose values are not known a priory. We need to run an optimization algorithm (based on an Evolutionary Algorithm of your choice) to set those values.

The goal to optimize is the distance in a scenario simulated with R2P2.

## Initial considerations

We will use the `scenario-inspyred.json`, which is based on the `track_2.png` layout, as depicted in the figure.

<img align="center" src="track_2.png" width="400">

The control logic is given by the controller `r2p2/controllers/inspyred.py`. This controller is straitforward, it computes linear and angular velocities as linear combinations of the distance measures. 

<img src="https://latex.codecogs.com/svg.latex?\text{v}_l=\sum_{i=1}^{N}\alpha_{i}d_{i}" title="\text{v}_l=\sum_{i=1}^{N}\alpha_{i}d_{i}" />

<img src="https://latex.codecogs.com/svg.latex?\text{v}_a=\sum_{i=1}^{N}\beta_{i}d_{i}" title="\text{v}_a=\sum_{i=1}^{N}\beta_{i}d_{i}" />

where <img src="https://latex.codecogs.com/svg.latex?\alpha_{i}" title="\alpha_{i}"/> and <img src="https://latex.codecogs.com/svg.latex?\beta_{i}" title="\beta_{i}"/> denotes a weight of sensor *i* and <img src="https://latex.codecogs.com/svg.latex?d_{i}" title="d_{i}"/> the distance measured by sensor *i*. The chromosome includes two additional genes to optimize the maximum linear and angular velocities that are not used by the controller. Please, check out the source code (*set_network_params()* and *control()*) to have a better understanding. The point here, of course, is setting the values of the weights, which is the responsability of the Evolutionary Algorithm. 

## Task 1: Design and code the Evolutionary Algorithm

Design an Evolutionary Algorithm to perform the optimization of the weights in the controller. 

When the controller is called, it waits until a list of weights is written in the file `res/weights.json` by an external logic, such as a script running the Evolutionary Algorithm (*ga-inspyred.py*). The evolution is run in a script while the fitness assessment is done by R2P2. 

Take the following fitness function that send to R2P2 a list of network weights:

```Python
import os
import inspyred

history = open('../logs/history_'+str(int(time.time()))+'.log', 'a+')
cur_best = 0

def write_params(string):
	f = open('../res/weights.json', 'w+')
	f.write('{"params": ' + string + '}')
	f.close()


@inspyred.ec.evaluators.evaluator
def evaluate(candidate, args):
	global history, cur_best
	string = ''.join(str(candidate)).replace(" ", "")
	#print("Evaluating: " + string)
	try:
		write_params(string)
		original_time = os.path.getmtime('../res/fitness.txt')
		while os.path.getmtime('../res/fitness.txt') == original_time:
			write_params(string)
			time.sleep(0.5)
		f = open('../res/fitness.txt', 'r')
		output = f.read()
		f.close()
		output = float(output)
		print("Fitness: " + str(output))
		if output >= cur_best:
			history.write('\n\n['+str(output)+']: '+string)
			cur_best = output
		return output
	except Exception as e:
		print(__file__)
		print(e)
		return(0)
```

You may want to read the [Inspyred examples](https://pythonhosted.org/inspyred/examples.html). The given function ``evaluate`` implements the fitness evaluation, including the communication between Inspyred and R2P2. The function *write_params()* is required by *evaluate()* and you will not to invoke it. The function *evaluate()* should be used as fitness function by the evolutionary algorithm. Please pay special attention to define a chromosome size with the size that R2P2 expects, otherwise the code will fail.

## Task 2: Train the robot controller

Set up the evolutionary parameter settings and run it until you find a satisfactory behaviour. Do not forget to obtain the weights of the best solution.

## Task 3: Implement the controller

Based on the weights obtained in the previous task, hard code your own controller (*eccontroller.py*). You may want to use code from the controller `r2p2/controllers/inspyred.py`.

<!--
Based on the weights obtained in the previous task, run the robot with the optimized weights. To this end use the scenario defined by the file ``scenario-inspyred-simple.json``, which uses the ``controller-inspyred-simple.json`` controller. Look for the field ``weights`` and fill a list with your weights, as the example contained in the example shows. Run the scenario and verify that the robot repeats the behaviour.-->

Please take into account that the robot sensors contain a small amount of noise, and therefore the behaviours might not be exactly equal in different executions.

## Task 4 (optional): Improve the controller

Based on ``Inspyred_controller``, create a new controller with a different behaviour able to outperform the previous controller. For instance, you may set different coefficients for different distance ranges. You can modify the controller as much as you want, but do not modify the robot. Develop a new controller (*GA_Extended_Controller.py*) and a new implementation of the evolutionary algorithm (*ga-inspired-extended.py*)

