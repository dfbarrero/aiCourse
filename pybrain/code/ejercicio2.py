#!/usr/bin/python

import numpy as np
import scipy.io
import math

print "Loading MATLAB data..."    
data = scipy.io.loadmat("ex3data1.mat")
X = data["X"]
y = data["y"]
y[y == 10] = 0 # '0' is encoded as '10' in data, fix it
