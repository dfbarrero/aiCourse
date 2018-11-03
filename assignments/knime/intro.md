# Introduction to KNIME Analytics Platform

## Objectives

* Install KNIME

* First contact with KNIME

* Implement basic Machine Learning workflows with KNIME

* Data exploration with KNIME

## Videos sequence

1 [What is a Node, What is a Workflow](https://www.knime.com/knime-introductory-course/chapter1/section2/what-is-a-node-what-is-a-workflow)

2 [Node Repository](https://www.knime.com/knime-introductory-course/chapter1/section2/node-repository)

3 [Workflows and Workflow Groups](https://www.knime.com/knime-introductory-course/chapter1/section3/workflows-and-workflow-groups)

4 [Node Status and Operations](https://www.knime.com/knime-introductory-course/chapter1/section3/node-status-and-operations)

5 [Data Table Structure](https://www.knime.com/knime-introductory-course/chapter1/section3/data-table-structure)

6 [Document your workflow: Annotations & Comments](https://www.knime.com/knime-introductory-course/chapter1/section3/document-your-workflow-annotations-and-comments)

## Dataset preliminary steps

Perhaps the most famous dataset in Machine Learning is one introduced by Fisher in 1936. The dataset contains measures of three different species of a flower named Iris (petal width, petal height, sepal width and sepal height), along with the species name (Iris setosa, Iris versicolor, Iris virginica). In order to better understand what petal and sepal stands for, please, observe the figure below. 

The iris dataset is widely used in Machine Learning literature as an example. To follow up this tradition, we will use this data set in this introductory assignment.

<img align="center" src="iris_petal_sepal.png" width="400">

(Image taken from [here](http://blog.kaggle.com/2015/04/22/scikit-learn-video-3-machine-learning-first-steps-with-the-iris-dataset/).)

Download the famous [iris dataset](iris.csv) and store it in an accesible location. Please observe that the file has CSV format, which is a widely used format in Machine Learning because of its simplicity; read [this](https://en.wikipedia.org/wiki/Comma-separated_values#Example) in case you need additional information about CSV.

Open the CSV file with a text editor of your choice to have a look. Count the number of attributes and instances in the dataset and observe the attributes data types.

## Exercises

Create a new workflow group named "exercises" to store the exercises, create a new workflow for each one of the following exercises.

1 Load the Iris dataset with a "File Reader" node and compute its main statistics (such as mean, median, standard deviation, etc) with the "Statistics" node.

## Working environment setup

Blablabla

## Issues to take into account

Data types (http://marcoghislanzoni.com/blog/2016/05/06/knime-for-beginners-part-2/)

Node ports

## Practical assignment

```
n := Chromosome length
p := Population size
pm := Mutation probability

Initialize population with random values

While solution not found
	i := 0
	While i < p
		Select randomly two individuals in the population
		Compute their fitness
		Select fittest individual

		If random_number() < pm 
			Flip a random position of the selected individual

		Store individual in the next population

```

The following figure outlines the algorithm to implement.


Once the algorithm is implemented, perform the following tasks:

1. Show the best fitness found in each generation. Execute the algorithm. How does the best fitness evolve?
2. Compare the execution time with n=10, n=20 and n=100. (Hint: Use the Unix command *time*).

