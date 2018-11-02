# Title:  Moon probe evolution example
# Author: Mike Vella

#start_imports
import os
import math
import pylab
import itertools

from random import Random
from time import time
import inspyred
from inspyred.ec.analysis import *
#end_imports

# All units are in SI unless stated otherwise.

# Global constants
#start_globals
G = 6.67300e-11 # Universal gravitational constant
earth_mass = 5.9742e24
earth_radius = 6.378e6
moon_mass = 7.36e22
moon_radius = 1.737e6
moon_position = (384403e3, 0)
earth_position = (0, 0)
#end_globals

def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)
    
def distance_between(position_a, position_b):
    return math.sqrt((position_a[0] - position_b[0])**2 + (position_a[1] - position_b[1])**2)
    
def gravitational_force(position_a, mass_a, position_b, mass_b):
    """Returns the gravitational force between the two bodies a and b."""
    distance = distance_between(position_a, position_b)

    # Calculate the direction and magnitude of the force.
    angle = math.atan2(position_a[1] - position_b[1], position_a[0] - position_b[0])
    magnitude = G * mass_a * mass_b / (distance**2)

    # Find the x and y components of the force.
    # Determine sign based on which one is the larger body.
    sign = -1 if mass_b > mass_a else 1
    x_force = sign * magnitude * math.cos(angle)
    y_force = sign * magnitude * math.sin(angle)
    return x_force, y_force

def force_on_satellite(position, mass):
    """Returns the total gravitational force acting on the body from the Earth and Moon."""
    earth_grav_force = gravitational_force(position, mass, earth_position, earth_mass)
    moon_grav_force = gravitational_force(position, mass, moon_position, moon_mass)
    F_x = earth_grav_force[0] + moon_grav_force[0]
    F_y = earth_grav_force[1] + moon_grav_force[1]
    return F_x, F_y

def acceleration_of_satellite(position, mass):
    """Returns the acceleration based on all forces acting upon the body."""
    F_x, F_y = force_on_satellite(position, mass)
    return F_x / mass, F_y / mass

def moonshot(orbital_height, satellite_mass, boost_velocity, initial_y_velocity, 
             time_step=60, max_iterations=5e4):
    fitness = 0.0
    distance_from_earth_center = orbital_height + earth_radius
    eqb_velocity = math.sqrt(G * earth_mass / distance_from_earth_center)
    
    # Start the simulation.
    # Keep up with the positions of the satellite as it moves.
    position = [(earth_radius + orbital_height, 0.0)] # The initial position of the satellite.
    velocity = [0.0, initial_y_velocity]
    time = 0
    min_distance_from_moon = distance_between(position[-1], moon_position) - moon_radius

    i = 0 
    keep_simulating = True
    rockets_boosted = False

    while keep_simulating:
        # Calculate the acceleration and corresponding change in velocity.
        # (This is effectively the Forward Euler Algorithm.)
        acceleration = acceleration_of_satellite(position[-1], satellite_mass)
        velocity[0] += acceleration[0] * time_step
        velocity[1] += acceleration[1] * time_step 

        # Start the rocket burn:
        # add a boost in the +x direction of 1m/s
        # closest point to the moon
        if position[-1][1] < -100 and position[-1][0] > distance_from_earth_center-100 and not rockets_boosted: 
            launch_point = position[-1]
            velocity[0] += boost_velocity[0]
            velocity[1] += boost_velocity[1]
            rockets_boosted = True

        # Calculate the new position based on the velocity.
        position.append((position[-1][0] + velocity[0] * time_step, 
                         position[-1][1] + velocity[1] * time_step))
        time += time_step

        if i >= max_iterations:
            keep_simulating = False

        distance_from_moon_surface = distance_between(position[-1], moon_position) - moon_radius
        distance_from_earth_surface = distance_between(position[-1], earth_position) - earth_radius
        if distance_from_moon_surface < min_distance_from_moon:
            min_distance_from_moon = distance_from_moon_surface
            
        # See if the satellite crashes into the Moon or the Earth, or
        # if the satellite gets too far away (radio contact is lost).
        if distance_from_moon_surface <= 0:
            fitness += 100000 # penalty of 100,000 km if crash on moon
            keep_simulating = False
        elif distance_from_earth_surface <= 0:
            keep_simulating = False
            fitness -= 100000 # reward of 100,000 km if land on earth
        elif distance_from_earth_surface > 2 * distance_between(earth_position, moon_position): 
            keep_simulating = False #radio contact lost
        i += 1

    # Augment the fitness to include the minimum distance (in km) 
    # that the satellite made it to the Moon (lower without crashing is better).
    fitness += min_distance_from_moon / 1000.0 
    
    # Augment the fitness to include 1% of the total distance
    # traveled by the probe (in km). This means the probe
    # should prefer shorter paths.
    total_distance = 0
    for p, q in pairwise(position):
        total_distance += distance_between(p, q)
    fitness += total_distance / 1000.0 * 0.01

    return fitness
