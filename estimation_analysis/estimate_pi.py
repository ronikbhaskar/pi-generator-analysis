from random import uniform
from math import sqrt

#pi estimation function using random
def estimate_pi(trials):
    "doesn't use the sqrt"
    points_in_circle = 0
    points_total = 0

    for t in range(trials):
        x = uniform(0,1)
        y = uniform(0,1)
        distance = x**2 + y**2
        #no need for sqrt b/c doesn't change in context of < or > 1
        if distance <= 1:
            points_in_circle += 1
        points_total += 1

    return 4 * points_in_circle / points_total

def estimate_pi_w_sqrt(trials):
    "uses the sqrt"
    points_in_circle = 0
    points_total = 0

    for t in range(trials):
        x = uniform(0,1)
        y = uniform(0,1)
        distance = sqrt(x**2 + y**2)
        if distance <= 1:
            points_in_circle += 1
        points_total += 1

    return 4 * points_in_circle / points_total


