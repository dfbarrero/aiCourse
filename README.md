# Contents

## Introductory

* [Introduction to Artificial Intelligence](introduction/)

* [Search](search/search.pdf) (PPT, Russel & Norvig slides)

* [Uninformed Search](search/Uniformed%20Search.pdf) (PPT, Russel & Norvig slides)

* [Informed Search](search/Informed%20Search.pdf) (PPT, Russel & Norvig slides) 

## Evolutionary Computation

* [Introduction to Evolutionary Computation](ecintro/)

* [Evolutionary Algorithms](ea/)

## Planning & Scheduling

* [Planning representation](planningrepresentation/planningrepresentation.pdf)

* [PDDL v1](planningrepresentation/PDDL.Master.pdf) 

* [PDDL v2-v3](planningrepresentation/PDDL2.x-3.X.Master.pdf)

* [Planning techniques](planningtechniques/planningtechniques.master.pdf)

* [Path-planning](pathplanning/pathplanning.pdf)

* [Space missions based on autonomous control](controlmissions/spacemissions.master.pdf)

## Robotics

* [Introduction to Robotics](robotics/)

* [Control Architectures](controlarchitectures/controlarchitectures.pdf) 

## Misc

* [Artificial Intelligence in Videogames](aivideogames/)

* [Artificial Neural Networks with PyBrain](pybrain/)

# Practical assignments

## Classic search

* [8-queens with informed search](assignments/search/informed.md)

* [8-queens with non-informed search](assignments/search/noninformed.md)

* [Examples for practicing search algorithms](assignments/search/Exercises-Tree/examplesSearch.md)

## Task and path planning

* [Integración de planificación PDDL con simulación robótica](https://github.com/munozp/pddl-sim)

* [PDDL with the R2P2 simulator](assignments/planning/r2p2-pddl.md)

* [Path-planning exercises](assignments/pathplanning/pathplanning.md)

* [Comparison of heuristics for path-planning in the R2P2 simulator](assignments/heuristics/heuristics.md)

* [PDDL exercises](assignments/planning/pddl-v1.md)

* [PDDL2.x/3.x exercises](assignments/planning/pddl-v2.md)

## Robotics

* [Introduction to the R2P2 robotic simulator](assignments/r2p2/introduction.md)

* [Optimization of a robotic controller through an Evolutionary Algorithm](assignments/r2p2-optimization/optimization.md)

* [Robot control based on a classification model](assignments/r2p2-classification/classification.md)

* [Robot control based on a neural regression model](assignments/r2p2-regression/regression.md)

## Evolutionary Computation

* [One-max problem with a basic Genetic Algorithm](assignments/onemax/onemax.md)

* [Real number optimization with Inspyred](assignments/realoptimization/realoptimization.md)

* [Understanding parameters settings in Evolutionary Algorithms](assignments/parameters/parameters.md)

* [Understanding parameters settings in Evolutionary Algorithms (Google Colab)](https://colab.research.google.com/drive/1HOzOUuTYJOGQ5JvFww40u2NC7FNXf1SV?usp=sharing)

* [Programming Evolutionary Algorithms with Inspyred](assignments/inspyred/inspyred.md)

* [Symbolic regression with Genetic Programming](assignments/regression/regression.md)

* [Neuroevolutive robot control with the r2p2 robotic simulator](assignments/neuroevolution/neuroevolution.md)

* [Optimization of the trajectory of a spacecraft to the Moon](assignments/moonshot/moonshot.md)

* [Optimization of the trajectory of a spacecraft to the Moon (no coding)](assignments/moonshot/moonshot-nocoding.md)

* [Optimization of the trajectory of a spacecraft to the Moon (no coding, Google Colab)](https://colab.research.google.com/drive/1u5g9wm7q44OKgBEAqfowiAtm7j3r7mAC?usp=sharing)

* [Paper 'Automated Design of CubeSats and Small Spacecrafts'](assignments/papers/cubesats.md)

# Compilation

Use xelatex or lualatex as latex processors, otherones would raise a compilation error. Custom UAH fonts are needed to properly compile the project. The original template used to format the slides, including the fonts, can be downloaded from [this repository](https://github.com/dfbarrero/UAH-beamer-template). By default, the theme will use UAH fonts installed in the system, edit the theme to easily change this behaviour.

*Manual execution of xelatex or lualatex would generate a compilation error*, since the tex documents require a variable containing the course for which the slides are compiled. You should use instead the command make which calls xelatex with the proper variable definition.

Several Makefiles are provided to ease repository management. Make executed from the root folder would compile the entire collections of slides for all the courses, while "make view" would open a PDF viewer with all the complided slides. On the contrary, if make is executed within a subfolder, it would only compile the slided contained in that folder. By default, make compiles the slides for all the courses, while "make course" would build the slides for that course. 

The courses for which the slides are compiled are defined in the TARGET variable, in the begining of the Makefiles. The courses details such their names are defined in [gsi-parametros.sty](gsi-parametros.sty), in the root folder.
