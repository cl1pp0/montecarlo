#!/usr/bin/python2
import random
from time import clock
import math
import cmath

t_start = clock()
n_it = 10000
random.seed()
n_circ = 0.0

for i in range(n_it):
    x = random.random()
    y = random.random()
    r = math.sqrt(x**2 + y**2)
        
    if r < 1:
        n_circ += 1

t_delta = clock() - t_start

pi_approx = n_circ / (n_it+1) * 4
error = (cmath.pi - pi_approx) / cmath.pi
print "%d iterations:" % n_it
print "pi (approx) =", pi_approx
print "pi (exact) =", cmath.pi
print "error = %.2f" % (error*100), "%"
print "elapsed time: %3.3f s" % t_delta
