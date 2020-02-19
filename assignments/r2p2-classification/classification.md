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

## Assignment objective

The main objective of this assignment is to develop a robot controller that imitates the behaviour of a teleoperated robot. The teleoperation will only consider five outputs: STOPPED, UP, DOWN, LEFT and RIGHT, which corresponds to the cursor keys. We will perform three different tasks in this assignment.

1.- Build a dataset that maps the robot sensons and its output.

2.- Train a classification model.

3.- Integrate the model into the robot controller.

## Task 1: Build a dataset

1.- Modify the teleoperation controler to display the robot sensors measures and its motion ("UP", "DOWN", "LEFT", "RIGHT", STOPPED"). The output must be in [CSV format](https://en.wikipedia.org/wiki/Comma-separated_values), which is straitforward. You can add a header with the columns names, which will ease futher steps.

2.- Build the dataset. Teleoperate the robot while storing its perception and actions. Remember that this is what the controller will learn, so try to be consistent and do not develop complex behaviours. A very easy way to store the CSV file into disk is to redirect the simulator output (```python r2p2.py --scenario scenario.json > output.csv```).

## Task 2: Train a classification model

