## Airport domain

The domain consists of planes and passengers that travel from one city to another.

Create a file called *airport.pddl* and copy the following domain description:
```
(define (domain airport)
(:requirements :durative-actions :typing :fluents)
(:types aircraft person city - object)

(:predicates (at ?x - (either person aircraft) ?c - city)
             (in ?p - person ?a - aircraft))
(:functions (fuel ?a - aircraft)
            (distance ?c1 - city ?c2 - city)
            (slow-speed ?a - aircraft)
            (slow-burn ?a - aircraft)
            (capacity ?a - aircraft)
            (refuel-rate ?a - aircraft)
            (total-fuel-used)
            (boarding-time)
            (debarking-time)
            )

(:durative-action board
:parameters (?a - aircraft  ?p - person  ?c - city)
:duration (= ?duration (boarding-time))
:condition (and (at start (at ?p ?c))
                          (over all (at ?a ?c)))
:effect (and (at start (not (at ?p ?c)))
                       (at end (in ?p ?a))))
                       
 (:durative-action debark
 
 )

(:durative-action fly 
 :parameters (?a - aircraft ?c1 ?c2 - city)
 :duration (= ?duration )
 :condition 
 
)

(:durative-action refuel
 :parameters (?a - aircraft ?c - city)
 :duration
)                      
                       
                       
```
Create a new file called *air-problem.pddl* and copy the following problem description:
```
(define (problem air-problem) 
(:domain airport)
(:objects
	; define people 
	city0 city1 city2 city3 city4 - CITY
	pl0 pl1 pl2 - AIRCRAFT)
(:init 
;; distances between cities
	(= (distance city1 city0) 1316.6534)
	(= (distance city0 city1) 1316.6534)
	(= (distance city2 city0) 1408.3523)
	(= (distance city0 city2) 1408.3523)
	(= (distance city0 city3) 2403.2266)
	(= (distance city3 city0) 2403.2266)
	(= (distance city0 city4) 2688.4637)
	(= (distance city4 city0) 2688.4637)
	(= (distance city1 city2) 1256.3465)
	(= (distance city2 city1) 1256.3465)
	(= (distance city1 city3) 1003.4996)
	(= (distance city3 city1) 1003.4996)
	(= (distance city1 city4) 986.6789)
	(= (distance city4 city1) 986.6789)
	(= (distance city2 city3) 6453.8961)
	(= (distance city3 city2) 6453.8961)
	(= (distance city2 city4) 7103.6434)
	(= (distance city4 city2) 7103.6434)
	(= (distance city3 city4) 598.6671)
	(= (distance city4 city3) 598.6671)
  
	; place people and planes in different cities
	; Define speed of planes
  ; fuel  capacity of each plane
  ; fuel level
  ; duration of debarking and borading

)
(:goal (and 
	(at pepe2 city0)
	(at pepe1 city4)
	(at pepe0 city1)
	)
)
(:metric minimize ... ))  ; fuel used
)

```
