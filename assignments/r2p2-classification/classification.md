# Robot control based on a classification model

## Objectives

* Implement a full Machine Learning process.

* Build and preprocess a dataset based on robotic control.

* Train different classification models.


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

## Basic configuration files

R2P2 stores all its configuration under the folder "conf/". There are three types of configuration files:

- Scenarios, which contain the physical environment in which the robot is placed in.

- Robots, which describes the robots, including its morphology and sensors.

- Controllers, which configures a robot controller.

R2P2 comes with a collection of scenarios, robots and controllers, each one is stored in a JSON file, which is plain text format with a straightforward syntax, as can be seen in the next example with the default scenanio:

```
{
	"stage": "../res/stage.png",
	"robot": ["../conf/robot_2.json"],
	"controller": "../conf/controller-telecom.json",
	"gui": true
}

```

The file syntax is self-explicative.

Perform the following tasks:

1. Change the initial location of the robot in the default scenario to the top-right corner. Take into account that the coordinates origin is the top-left corner and coordinates are always positive.

2. Change the robot used in the default scenario to *robot.json*.

3. Create a new scenario based on the default scenario or any other of your choice. Please, observe that the scenario map is just an image located in the folder *res/*, so you can use any image editor such as Gimp to do it.

## Basic robot control

The basics of robot control with R2P2 is straightforward, there is a control function that receives a vector of distances and return a tuple with linear and angular velocities. This function is invoked from within the control loop, wich is transparent to the programmer. Read the R2P2 developer manual to get more details about its API.

Perform the following tasks:

1.- Change the controller in the default scenario to the naïve controller and identify which behaviour this controller implements.

2.- Open the naîve controller source code (*r2p2/controllers/naive_controller.py*) and understand its code. You can browse the code with GitHub or any other tool of your choice.

3.- Open the telecom controller source code (*r2p2/controllers/telecom_controller.py*) and understand its code.

4.- Modify the telecom controller and print in the screen the distance measures.

5.- Modify the telecom controller and print in the screen the odometry.

## Wall following behaviour

1. Implement a new controller (*wallfollowing_controller.py*) that searches and follows a wall. Use the sandbox scenario for this exercise. You can use the naïve controller (just copy the file) as a template.

<img align="center" src="sandbox.png" width="400">

## Wall following behaviour  with a FSM (optional)

1. Implement a new controller (*wallfollowing_fsm_controller.py*) that searches and follows a wall using the following Finite State Machine (FSM).

<img align="center" src="fsm.svg" width="400">
