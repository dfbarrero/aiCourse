# Regression analysis of exoplanets masses

## Objectives

* Deal with a realistic Machine Learning application 

* Extract and preprocess a real dataset

* Perform a realistic exploratory analysis

* Implement a realistic Machine Learning workflow

This assignment assumes a basic knowledge of descriptive Statistics.

## Preliminary steps

First, it is advisable to get a basic knowledge about exoplanets detection methods and orbital elements. The following two readings are a good introduction to some concepts that we will be handling in this assignment.

* [Five Ways to Find a Planet](https://exoplanets.nasa.gov/5-ways-to-find-a-planet/)

* [Orbital elements](https://en.wikipedia.org/wiki/Orbital_elements)

It is usefull to remember the basic ML steps:

1. Adquire data.
2. Select data.
3. Exploratory analysis of data.
4. Train the model
5. Evaluate the model.
6. Go to 2 until a good enough model is found.

## Assignment goal

The goal of this assignment is to write a report developing an exoplanet mass predictor. To achieve this goal it is required to perform a descriptive analysis of the dataset complemented with the development of regression models able to predict an exoplanet mass.

## Data adquisition and selection

Download the exoplanet dataset from the [NASA Exploplanet Archive](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=planets). This dataset contains a collection of confirmed exoplanets along with several attributes about them. Download the dataset in *CSV format* and *values-only*. *You might need to configure your browser to allow the website to open pop-ups*.

Once the dataset was downloaded (consider only the default attributes), visualize its header using any tool of your choice (Linux command, text editor, etc) to get info about the dataset attributes names codification. If your are interested in getting a more detailed info about the attributes, [read this link](https://exoplanetarchive.ipac.caltech.edu/docs/API_exoplanet_columns.html).

The first step in any ML project is to get a basic understanding of the data at hand. To this end, apply any technique at your disposal (Statistics, histograms, etc) to answer the following questions:

1. How many instances and attributes does the dataset contain? (Hint: Use the Statistics node to get an insight to the data statistics)

2. How many exoplanets were discovered? How many exoplanets were discovered with each detection method? Which detection methods does the dataset contain? (Hint: The groupBy node is handy in to answer that kind of questions)

3. Does the dataset contain missing values?

## Univariable exploratory analysis

This assignment is interested in predicting the exoplanet mass, so many of the information contained in the dataset is irrelevant. However, distinguishing between relevant and irrelevant features is, itself, a challenging task most of the times.

In a first attempt to better understand our data, we will consider only those attributes which are directly associated with mass. Insert a KNIME node to drop all the attributes, with the exception of the following ones:

* pl_dens
* pl_mass
* pl_radj

Perform a exploratory univariable analysis of those attributes, and in particular identify maximum and minimum values, average value and median value. Identify missing values and outliers. If any, remove missing values and outliers.

Analyze the results.

## Bivariable exploratory analysis

Compute the correlation matrix and visualize a scatterplot matrix to identify correlations among the variables. 

Analyze the results.

## Regression analysis

The final goal of this assignment is to predict the exoplanet mass, which in ML terminology means training a regression model.

Implement a linear regression with *pl_mass* as target attribute. Train the model with the 70% of the data, and validate it with the remaining 30% of the data. Compute, on the validation set, the [R2](https://en.wikipedia.org/wiki/Coefficient_of_determination) using a [Numeric Scorer](https://nodepit.com/node/org.knime.base.node.mine.scorer.numeric.NumericScorerNodeFactory) node. A complementary tool to assess the model fit is a plot comparing the predicted mass to the actual mass, as the following figure shows. A proper interpretation of the plot should suggest how to improve the regression model.

<img align="center" src="regression.png" width="300">

The objective of model evaluation is to determine whether the model fit well the data. For the purpose of this assignment, we will consider a satisfactory model that one with R2>0.65.

Introduce any change to the model to increase the model fit. You can change the regression model, add or remove attributes (perhaps orbital measures?), or build new attributes. Take into account that the model interpretation could provide you valuable information, for instance, the p-values or coefficients values.

Analyze the results.
