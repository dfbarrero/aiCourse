# Neuroevolutive robot control with the r2p2 robotic simulator

## Objectives

* Implement a full neuroevolutive controller

* Design an ANN topology and optimization evolutionary algorithm.

This assignment assumes a basic knowledge of ANN and EA and Python programming (Inspyred and numpy).

## Preliminary steps

This assignment requires the [r2p2 robotic simulator](https://github.com/ISG-UAH/r2p2) properly installed. The [r2p2](https://github.com/ISG-UAH/r2p2) project website contains detailed installation instructions, follow them. The simulator depends on Python 3.x.

## Assignment goal

The goal of this assignment is to develop a neuronal controller for a mobile robot. Basicly, there are to linked task to perform:

1. Design an ANN topology.
2. Train the network thought an evolutionary algorithm.

In order to ease the development of this assignment and focus on the important concepts (algorithm design), most of the code is given.

## R2p2 contents

The r2p2 simulator provides almost a full implementation of the neuroevolutive controller with the exception of the critical parts that define the ANN topology and its training, along with some utility features that eases development. It is important to understand what features the simulator provides, how it is implemented and what is needed to develop the neurocontroller.

R2p2 provides some configuration files:

* **scenario-neuro.json**: Scenario with a minimalistic track as shown in the figure. Please observe that you can enable or disable the GUI with the parameter *gui*.
* **robot-neuro.launch**: Description of the robot used for neuroevolution, by default it contains 5 sonar sensors.
* **controller-neuro.launch**: Neuronal controller. You can use it to evolve the controller and fix a network weights as well.

<img align="center" src="track_2.png" width="300">

The folder *r2p2* contains the simulator code along with two files of interest in this assignment:

* **neurocontroller.py**: Script that partially implements the controller and fitness assessment. The script takes an array of floats with the ANN weights from a temporal file (do not worry by the implementation details), builds the ANN, feeds it with the normalized sensors measures and controls the motion with its output. By default, it runs the simulation for 20 seconds and returns the fitness value. You must modify this file to setup the ANN topology.

* **evolution.py**: It must implement the evolutive algorithm which will optimize the ANN parameters. This file contains the implementation of the fitness function that must be used, *evaluate_ann()*. You must modify this file to implement the optimization algorithm.

A potential source of problems is that the neuronal controller **must receive a vector with the same number of weights than the ANN**, otherwise it will rise an error (numpy will comply that it is unable to reshape an array). Do not forget that the number of weights in the ANN must include the neurons bias.

## Neuroevolution execution

In order to train the network you must execute the simulator along with the evolutionary algorithm. From the r2p2 folder, execute the following command:

```Bash
python r2p2.py --scenario ../conf/scenario-neuro.json
```

In another tab, execute the evolutionary algorithm:

```Bash
python evolution.py
```
Remember that both scripts must work properly in order to evolve the robot behaviour.

## Fitness assessment

The fitness is computed as the sum of the distance traveled by the robot, as measured by the odometry. 

A tricky issue is how to map the array of weights given to *evaluate_ann()* to the actual weights in the ANN. Fortunately, that is almost irrelevant because the the ANN will eventually learn where each input and output neuron is connected. However, it is critical to keep consistency between the genotype encoding and the order in which the weights are sent to *evaluate_ann()*, i.e., use always the same mapping.

## Evolving the neurocontroller

In order to develop a neurocontroller, there are basically two different tasks:

1. Implement the ANN. This is done by editing the file *neurocontroller.py*. Just check out the two "TODO" comments in that file. 
2. Implement the evolutionary algorithm. This is done by editing the file *neurocontroller.py*. 
3. Train the ANN. Run both scripts

We describe those tasks in more detail.

There are three issues to implement the ANN:

1. Initialize the ANN. Fill the function *initANN()* in *neurocontroller.py*. The part of the script you must customized is marked with ``TODO''. Take into account that the ANN must have N_SONAR (which actually values 4) and two outputs.
2. Set the ANN weights.
3. Feed the network with the sonar measures (stored in the global variable ranges), propagate the input and store its output in the out global variable (remember, just two values, linear and angular velocities).

In this stage, you should be able to use testFitness.py to test the previous steps with random (or zero) weights. Do not expect a good robot behaviour at this point, just random motion, if any. Take into account that you must send the same number of weights that the ANN expects.

Once all the previous tasks are completed, you should be able to perform the robot trainning with the following steps from the folder r2p2:

1. Run the simulation (*roslaunch launch/road.launch*).
2. Run the robot controller (*neurocontroller.py*).
3. Run the script that implements the evolutionary trainning (*evolution.py*). You should be able to view in real-time the behaviour of the robot in the STDR window.

There are some issues you must address.

* ANN topology.

* Initialization of network weights.

* Type of EA to implement. Inspyred source code and documentation contains lots of examples to begin with.

* EA parameters settings.

## Bonus track

Modify the robot perception design (i.e., the number of sonars and their location) to improve the robot behaviour.
