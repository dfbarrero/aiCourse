# Neuroevolutive robot control with the r2p2 robotic simulator

## Objectives

* Implement a full neuroevolutive controller

* Design an ANN topology and an evolutionary algorithm.

This assignment assumes a basic knowledge of ANN and EA and Python programming (Inspyred and numpy).

## Preliminary steps

This assignment requires the [r2p2 robotic simulator](https://github.com/ISG-UAH/r2p2) properly installed. The [r2p2](https://github.com/ISG-UAH/r2p2) project website contains detailed installation instructions, follow them. The simulator depends on Python 3.x.

## Assignment goal

The goal of this assignment is to develop a neuronal controller for a mobile robot. Basicly, there are to linked task to perform:

1. Design an ANN topology.
2. Train the network thought an evolutionary algorithm.

In order to ease the development of this assignment and focus on the important concepts (algorithm design), most of the code is given.

## R2p2 contents

The r2p2 simulator provides almost a full implementation of the neuroevolutive controller with the exception of the critical parts that define the ANN topology and its training.

<img align="center" src="track_2.png" width="300">

R2p2 provides some configuration files:

* **scenario-neuro.json**: Scenario with a minimalistic track as shown in the figure. Please observe that you can enable or disable the GUI with the parameter *gui*.
* **robot-neuro.launch**: Description of the robot used for neuroevolution, by default it contains 5 sonar sensors.
* **controller-neuro.launch**: Neuronal controller. You can use it to evolve the controller and fix a network weights as well. The network must accept **five inputs** (which correspond to five sonars) and **two outputs** (linear and angular velocities).
* **scenario-neuro-simple.json**: Scenario to test a fixed ANN.
* **controller-neuro-simple.launch**: Neuronal controller with fixed weights, for testing purposes. Please check out that *neurocontroller.py* has the proper ANN topology.

You will not need to touch these files, with the exception of the GUI parameter in the scenario configuration and the weights in *controller-neuro-simple.launch*.

The folder *r2p2* contains the simulator code along with two files of interest in this assignment:

* **neurocontroller.py**: Script that partially implements the controller and fitness assessment. The script takes an array of floats with the ANN weights from a temporal file (do not worry by the implementation details), builds the ANN, feeds it with the normalized sensors measures and controls the motion with its output. This scripts already has implemented the input and output layers with five and two neurons. You must modify this file to setup the ANN topology, i.e., the number of hidden layers and the number of neurons in each one. 

* **evolution.py**: It must implement the evolutive algorithm which will optimize the ANN weights. This file contains the implementation of the fitness function that must be used, *evaluate_ann()*. You must complete this file to implement the optimization algorithm.

A potential source of problems is that the neuronal controller **must receive a vector with the same number of values than weights has the ANN**, otherwise it will raise an error (numpy will comply that it is unable to reshape an array). Do not forget that the number of weights in the ANN must include the neurons bias.

## Fitness assessment

The fitness is computed as the sum of the distance traveled by the robot, as measured by the odometry. In case of collision with a wall, the evolution is stopped.

A tricky issue is how to map the array of weights given to *evaluate_ann()* to the actual weights in the ANN. Fortunately, that is almost irrelevant because the the ANN will eventually learn where each input and output neuron is connected. However, it is critical to keep consistency between the genotype encoding and the order in which the weights are sent to *evaluate_ann()*, i.e., use always the same mapping.

## Neuroevolution execution

In order to train the network you must execute the simulator along with the evolutionary algorithm. From the r2p2 folder, execute the following command:

```Bash
python r2p2.py --scenario ../conf/scenario-neuro.json
```

In another tab, execute the evolutionary algorithm:

```Bash
python evolution.py
```

You should be able to view in real-time the behaviour of the robot if enabled in the configuration file (which is activated by default). Remember that both scripts must work properly in order to evolve the robot behaviour, but the order in which they are run does not matter.

## Evolving the neurocontroller

In order to develop a neurocontroller, there are basically three different tasks:

1. Implement the ANN. This is done by editing the file *neurocontroller.py*. Just check out the "TODO" in that file. 
2. Implement the evolutionary algorithm. This is done by editing the file *neurocontroller.py*. Inspyred source code and documentation contains lots of examples to begin with. Remember that the functions *evaluate_ann()* already contains the implementation of the fitness functions.
3. Train the ANN. Try different parameters in order to determine which ones provides better performance.

Once all the previous tasks are completed, you should be able to perform the robot trainning with the following steps from the folder r2p2:

1. Run the simulation (*python r2p2.py --scenario ../conf/scenario-neuro.json*).
3. Run the script that implements the evolutionary trainning (*python evolution.py*). By defaul, this script generates random weights, so do not expect a champion robot.

There are some issues you must address.

* ANN topology: Number of layers and number of neurons per layer.

* Init values of network weights.

* Type of EA to implement. You can use any optimization algorithm: GA, ES, SA, or any other.

* EA parameters settings.

## Tips 

- Disable the GUI to get the best from your (scarce) computational resources.

- Test your ANN and evolutionary algorithm individually with some naive scenario, only then try to join them.

- Visualization of the robot behaviour may provide a valuable insight to how the controller is learning, but it requires a lot of computational resources. Use it wisely.

- Once you get a suitable network, you can test it setting its weights in the field *weights* of the file *controller-neuro.json*.

- Try to understand the number of weights needed in the ANN with paper and pencil.

## Bonus track

Modify the robot perception design (i.e., the number of sonars and their location) to improve the robot behaviour.
