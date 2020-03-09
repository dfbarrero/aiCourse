# Optimization of a classical robotic controller through an Evolutionary Algorithm

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

<img src="https://latex.codecogs.com/svg.latex?\text{v}_l=\sum_{i=1}^{N}\beta_{i}d_{i}" title="\text{v}_l=\sum_{i=1}^{N}\beta_{i}d_{i}" />

where <img src="https://latex.codecogs.com/svg.latex?\alpha_{i}" title="\alpha_{i}"/> and <img src="https://latex.codecogs.com/svg.latex?\beta_{i}" title="\beta_{i}"/> denotes a weight of sensor *i* and <img src="https://latex.codecogs.com/svg.latex?d_{i}" title="d_{i}"/> the distance measures by sensor *i*. Please, check out the source code to have a better understanding. 


## Task 1: Build a dataset

You may want to check out this [Scikit-learn notebook](https://github.com/dfbarrero/dataCourse/blob/master/mlfoundations/scikit-learn.ipynb) as an example.

1.- Use the teleoperation controler as a template for a new controller (Telecom_Controller_ml) to display the robot sensors measures and its motion ("UP", "DOWN", "LEFT", "RIGHT", STOPPED"). The output must be in [CSV format](https://en.wikipedia.org/wiki/Comma-separated_values), which is straitforward. You can add a header with the columns names, which will ease futher steps.

2.- Build the dataset. Teleoperate the robot while storing its perception and actions. Remember that this is what the controller will learn, so try to be consistent and do not develop complex behaviours. A very easy way to store the CSV file into disk is to redirect the simulator output (```python r2p2.py --scenario scenario.json > output.csv```). The success of this assignment highly depends on how you drive the robot in this step, so do it carefully.

3.- Preprocess the dataset. Add a header and perform any task needed to correctly format the CSV. This might need a manual edition of the file with a text editor or Excel.

## Task 2: Train a classification model

For this task, we recommend using a Jupyter notebook.

1.- Explore your dataset. Do you need any futher preprocessing in your data? You will need preprocessing if not all the instances in the dataset are relevant for the training. 

2.- Plot the two main components of the PCA. Is your data separable? 

3.- Preprocess your data for the training, if needed. Automatic preprocessing could be a better option in this step. Take into account the sonar range and robot radius.

4.- Train a classification model. Try the following algorithms:
  - K-Nearest Neighbors (K-NN) with k=1.
  - Classification Tree.
  - Logistic Regression.
  - Multilayer Perceptron.
  - Support Vector Machine.

Do not forget to assess the performance of all your models. You will need to persist (i.e., store) your trained models, use this [Scikit-learn notebook](https://github.com/dfbarrero/dataCourse/blob/master/mlfoundations/scikit-learn.ipynb) or read [this link](https://wiki.python.org/moin/UsingPickle) for futher information on this topic.

7.- Tune your hyperparameters. Try different values for k (k=1,2,3,4 and 5) in K-NN and plot its performance. Which value of k gives the best performance?

8.- Select one of the previous algorithms to integrate it into the robor controller. You will need to persist the model in disk.

## Task 3: Integrate the model into the robot controller

1.- Develop a new robot controller that reads the classification model from disk, and then integrate it with the sensor outputs and actions output.

2.- Assess the robot behaviour. Is it as expected?
