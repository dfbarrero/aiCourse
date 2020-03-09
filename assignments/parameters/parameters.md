# Understanding parameters settings in Evolutionary Algorithms

## Objectives

* Introduce *inspyred*

* Understand the parameter settings of a basic GA

* Observe the basic behaviour of an EA

* Customize the parameter settings

* Gather and process the main statistics

## Preliminary steps

First of all, if you are using Windows, you will need to install Python 3.X. Just [download it](https://www.python.org/downloads/) and install it as any other software. In case you where using Linux or Mac, you already has Python in your machine.

Install *inspyred* following the instructions available on http://pythonhosted.org/inspyred/. Basically, *inspyred* is a Python module that can be installed like any other module. From an Unix or PowerShell console, just type ```pip install inspyred```.


## One-max problem with inspyred

Download [this script](https://gist.github.com/dfbarrero/ea3f81cd9a7847147e48490dd0b44b50), which implements the one-max problem with a basic Genetic Algorithm implemented with inspyred. Once it is in your machine, you need to open a shell and, from the same folder than the script is stored, run the following command:

```
python onemax-ga.py
```

If everything works, the script must be printing information about the evolutionary process. You can get all the information about the script parameters running:

```
python onemax-ga.py -h
```

For instance, if you want to run the algorithm with a population of 100 chromosomes, type 

```
python onemax-ga.py --population 100
```

To increase the number of generations run by the algorhtm just put it in the corresponding parameters.

```
python onemax-ga.py --population 100 --generations 50
```

## Initial questions

Answer the following questions:

1. Which is the default configuration?

2. Execute the script several times, did it always find the solution? Why?

3. Observe how average and best fitness evolve along the time. Explain their behavior.

4. Execute the algorithm with mutation and crossover probability set to 0. Do you observe any evolution?

5. Execute the algorithm with crossover probability set to 0 and mutation probability to 0.5. Do you observe any evolution?

6. Change the chromosome length to 100 and run the algorithm. Do you observe any difference?

7. Which is the function implemented by the argument 'jobs'?

## Impact of the parameters setting 

The main objective of the assignment is to assess the impact of the parameter settings into the Genetic Algorithm dynamics. To this end we will execute the algorithm controlling each parameter. Please, take into account that a GA has a stochastic nature, so each time you execute it you usually obtain a different result, so you will need to run it several time in order to assess its variability.

Using the default parameter settings as a starting point, change the following parameter settings and plot the fitness against the generation number of different values of the given parameter:

1. Set crossover probability to 0, 0.5, 0.75 and 1.

2. Set mutation probability to 0, 0.01, 0.05 and 0.1.

3. Set population size to 10, 30, 50 and 100.

4. Set tournament size to 2, 3, 4 and 5.

5. Set chromosome length to 10, 20, 30, 50 and 100.

The final goal is to obtain a collecion of figures like the one showed here, along with an interpretation of the results.

<img align="center" src="plot.png" width="400">

You may need to change the maximum number of generations (some configurations may need a longer time to converge), but this number *does not* affect the evolutionary process, it just defines when to stop it.

## Final remarks

Take into account that you can easely store the algorithm output to futher processing. Evolution statistics is printed in stderr, while additional information is printed in stderr, it means that you can store the run statistics simply

```
python onemax-ga.py > output.csv
```

you can append data to that file with the command 

```
python onemax-ga.py >> output.csv
```

It is also possible to store both, statistics and messages, with

```
python onemax-ga.py > output.csv 2> messages.txt
```

Remember that CSV is a common file format to store structured data; you can process it with any data processing software such as Excel or SPSS.
