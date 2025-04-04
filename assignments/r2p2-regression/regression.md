# Robot control based on a neural regression model

## Objectives

* Implement a full Machine Learning process.

* Build and preprocess a dataset based on robotic control.

* Train different neural network architectures for regression.


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

The main objective of this assignment is to develop a robot controller that imitates the behaviour of a teleoperated robot. The teleoperation will consider the output given by a joystick, a linear velocity and an angular velocity. Therefore the controller will be a multivariable regression model. We will perform three different tasks in this assignment.

1.- Build a dataset that maps the robot sensors readings and its action.

3.- Train a regression model based on a neural network.

4.- Integrate the model into the robot controller.

Use the scenario defined by the file ```scenario-track.json``` for this lab assignment.

## Task 1: Build a dataset

You may want to check out this [Scikit-learn notebook](https://github.com/dfbarrero/dataCourse/blob/master/mlfoundations/scikit-learn.ipynb) as an example.

1.- Use the teleoperation controler as a template for a new controller (*Telecom_Controller_ML*) to display the robot velocities. The output must be in [CSV format](https://en.wikipedia.org/wiki/Comma-separated_values), which is straitforward. You can add a header with the columns names, which will ease futher steps.

2.- Build the dataset. Teleoperate the robot while storing its perception and actions. Remember that this is what the controller will learn, so try to be consistent and do not develop complex behaviours. A very easy way to store the CSV file into disk is to redirect the simulator output (```python r2p2.py --scenario scenario.json > output.csv```). The success of this assignment highly depends on how you drive the robot in this step, so do it carefully.

3.- Preprocess the dataset. Add a header and perform any task needed to correctly format the CSV. This might need a manual edition of the file with a text editor or Excel.

## Task 2: Train a classification model

For this task, we recommend using a Jupyter notebook.

1.- Explore your dataset. Do you need any futher preprocessing in your data? You will need preprocessing if not all the instances in the dataset are relevant for the training. 

2.- Preprocess your data for the training, if needed. Automatic preprocessing could be a better option in this step. Take into account the sonar range and robot radius. Remember that the input of an artificial neural network should always be normalized or standarized.

3.- Train a neural network for regression. Try different numbers of layers and architectures.

Do not forget to assess the performance of all your models. You will need to persist (i.e., store) your trained models, use this [Scikit-learn notebook](https://github.com/dfbarrero/dataCourse/blob/master/mlfoundations/scikit-learn.ipynb) or read [this link](https://wiki.python.org/moin/UsingPickle) for futher information on this topic.

4.- Tune your hyperparameters. Try different values for k (k=1,2,3,4 and 5) in K-NN and plot its performance. Which value of k gives the best performance?

5.- Select one of the previous algorithms to integrate it into the robot controller. You will need to persist the model in disk.

## Task 3: Integrate the model into the robot controller

1.- Develop a new robot controller (*MLP_Controller*) that reads the classification model from disk, and then integrate it with the sensor outputs and actions output.

2.- Assess the robot behaviour. Is it as expected?
