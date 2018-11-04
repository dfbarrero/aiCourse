# Machine-based robot motion control

## Objectives

* Implement a realistic Machine Learning workflow

* Integrate classification and Principal Component Analysis

* Implement a 10 cross-validation classifier evaluation

* Get an insight to the application of Machine Learning methods to Robotics

## Introduction

The goal of this assignment is to develop a robot controller able to follow a wall based on a set of sonar measurements. We will address this problem as a classification task in which the input is composed by several sonar measurements and the output a class is the next robot motion.

Of course, we need a labeled dataset to train the classifier. To this end we will use the UCI [Wall-Following Robot Navigation Data Data Set](https://archive.ics.uci.edu/ml/datasets/Wall-Following+Robot+Navigation+Data). This dataset contains data for three robot contigurations:

* 2 sonars placed looking forward and backwards.
* 4 sonars placed looking forward, backwards, left and right.
* 24 sonars.

The dataset provides an additional attribute with the expected robot motion, which is one label out of four: "Move-Forward", "Slight-Right-Turn", Sharp-Right-Turn" and "Slight-Left-Turn"
