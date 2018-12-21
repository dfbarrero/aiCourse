# Contents

## Introductory

* [Introduction to Artificial Intelligence](introduction/)

* [Search](search/search.pdf) (PPT, Russel & Norvig slides)

## Evolutionary Computation

* [Introduction to Evolutionary Computation](ecintro/)

* [Evolutionary Algorithms](ea/)

* [Neuroevolution](neuroevolution/)

## Planning & Scheduling

* [Planning representation](planningrepresentation/planningrepresentation.pptx)

* [Path-planning](plathplanning/pathplanning.pptx) (PPTX)

* [Misiones espaciales basadas en control autónomo](aicontrolmissions/aicontrolmissions) (PPT, Spanish)

## Misc

* [Artificial Intelligence in Videogames](aivideogames/)

* [Introduction to Robotics](robotics/)

* [Artificial Neural Networks](ann/)

* [Artificial Neural Networks with PyBrain](pybrain/)

# Practical assignments

## Classic search

## Task and path planning

* [Integración de planificación PDDL con simulación robótica](https://github.com/munozp/pddl-sim)

* [PDDL v1 exercises](assignments/planning/pddl-v1.md)

* [PDDL v2 exercises](assignments/planning/pddl-v2.md)

## Evolutionary Computation

* [One-max problem with a basic Genetic Algorithm](assignments/onemax/onemax.md)

* [Understanding parameters settings in Evolutionary Algorithms](assignments/parameters/parameters.md)

* [Programming Evolutionary Algorithms with Inspyred](assignments/inspyred/inspyred.md)

* [Symbolic regression with Genetic Programming](assignments/regression/regression.md)

* [Optimization of the trajectory of a spacecraft to the Moon](assignments/moonshot/moonshot.md)

# Compilation

Use xelatex or lualatex as latex processors, otherones would raise a compilation error. Custom UAH fonts are needed to properly compile the project. The original template used to format the slides, including the fonts, can be downloaded from [this repository](https://github.com/dfbarrero/UAH-beamer-template). By default, the theme will use UAH fonts installed in the system, edit the theme to easily change this behaviour.

*Manual execution of xelatex or lualatex would generate a compilation error*, since the tex documents require a variable containing the course for which the slides are compiled. You should use instead the command make which calls xelatex with the proper variable definition.

Several Makefiles are provided to ease repository management. Make executed from the root folder would compile the entire collections of slides for all the courses, while "make view" would open a PDF viewer with all the complided slides. On the contrary, if make is executed within a subfolder, it would only compile the slided contained in that folder. By default, make compiles the slides for all the courses, while "make course" would build the slides for that course. 

The courses for which the slides are compiled are defined in the TARGET variable, in the begining of the Makefiles. The courses details such their names are defined in [gsi-parametros.sty](gsi-parametros.sty), in the root folder.
