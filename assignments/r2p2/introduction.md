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

<img align="center" src="stage.jpg" width="400">

The scenario is stored in a JSON file under the conf folder, you can change it with the argument --scenario. A very convenient sandbox scenario is provided in R2P2, run it with

```
(r2p2) david@arrakis:~/r2p2$ python r2p2.py --scenario ../conf/scenario-sandbox.json
```

You can get all the arguments to R2P2 passing the argument ```--help```.

(Image taken from [here](http://file.scirp.org/Html/1-8302163_41175.htm).)

Once the algorithm is implemented, perform the following tasks:

1. Show the best fitness found in each generation. Execute the algorithm. How does the best fitness evolve?
2. Compare the execution time with n=10, n=20 and n=100. (Hint: Use the Unix command *time*).
