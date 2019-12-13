# Introduction to the R2P2 robotic simulator

## Objectives

* Install and run R2P2.

* Understand and customize R2P2 configuration files.

* Develop basic robot controllers in R2P2.

## First steps

First of all, download and install R2P2 following the instructions given in the [https://github.com/ISG-UAH/r2p2](R2P2 GitHub repository), please, pay attention to install [https://www.anaconda.com/distribution/](Anaconda) first (a Python distribution that makes everything easier) and R2P2 dependencies. 

Check out the installation running a basic scenario with the following command from the folder r2p2:

```
(r2p2) david@arrakis:~/r2p2$ python r2p2.py
```

If everything is working properly, you shoud be now watching a basic scenario with a robot that can be teleoperated with the arrows keys, as the following picture depicts.

<img align="center" src="r2p2-stage.png" width="400">

The scenario is stored in a JSON file under the conf folder, you can change it with the argument --scenario. A very convenient sandbox scenario is provided in R2P2, run it with

```
(r2p2) david@arrakis:~/r2p2$ python r2p2.py --scenario ../conf/scenario-sandbox.json
```
Check out the scenarios contained in conf and try to run some of them.

You can get all the arguments to R2P2 passing the argument ```--help```.

# Basic configuration files manipulation

R2P2 stores all its configuration under the folder ```conf```. There are three types of configuration files:

- Scenarios, which contain the physical environment in which the robot is placed in.

- Robots, which describes the robots, including its morphology and sensors.

- Controllers, which configures a robot controller.

R2P2 comes with a collection of scenarios, robots and controllers, each one is stored in a JSON file, which is plain text format with a straightforward syntax, as can be seen in the next example with the default scenarnio:

```
{
	"stage": "../res/stage.png",
	"robot": ["../conf/robot_2.json"],
	"controller": "../conf/controller-telecom.json",
	"gui": true
}

```

The file syntax is self-explicative.

Once the algorithm is implemented, perform the following tasks:

1. Change the initial location of the robot in the default scenario to the coordinate ().
2. Compare the execution time with n=10, n=20 and n=100. (Hint: Use the Unix command *time*).
