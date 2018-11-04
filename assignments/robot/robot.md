# Machine-based robot motion control

## Objectives

* Implement a realistic Machine Learning workflow

* Integrate classification and Principal Component Analysis

* Implement a 10 cross-validation classifier evaluation

* Get an insight to the application of Machine Learning methods to Robotics

## Introduction

The goal of this assignment is to develop a robot controller able to follow a wall based on a set of sonar measurements. We will address this problem as a classification task in which the input is composed by several sonar measurements and the output a class is the next robot motion.

Of course, we need a labeled dataset to train the classifier. To this end we will use the UCI [Wall-Following Robot Navigation Data Data Set](https://archive.ics.uci.edu/ml/datasets/Wall-Following+Robot+Navigation+Data). This dataset contains data for three robot contigurations:

* 2 sonars placed looking forward and backwards (sensor_readings_2.data).
* 4 sonars placed looking forward, backwards, left and right (sensor_readings_4.data).
* 24 sonars (sensor_readings_24.data).

The dataset provides an additional attribute with the expected robot motion, which is one label out of four: "Move-Forward", "Slight-Right-Turn", Sharp-Right-Turn" and "Slight-Left-Turn"

## Preliminary steps

Download the UCI [Wall-Following Robot Navigation Data Data Set](https://archive.ics.uci.edu/ml/datasets/Wall-Following+Robot+Navigation+Data) and store it in a convenient location.

Open one of the data files with a text editor of your choice and inspect it.

## Robot motion control with two sonars

Firstly, we will train a classifier to predict the best next motion with the 2 sonars dataset. Using a single workflow, implement the following tasks:

1. Read the file sensor_readings_2.data.

2. Exploratory analysis. Visualize the dataset to have a first contact with the data. Explore the dataset in search of outliers and missing values. Count the number of instances of each class, does it have any impact for the classification?
