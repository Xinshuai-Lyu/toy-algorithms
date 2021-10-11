
"""
 The area of a circle is defined as πr^2. 
 Estimate π to 3 decimal places using a Monte Carlo method.
 
 Hint: The basic equation of a circle is x2 + y2 = r2.

points in square/ points in circle
r = 1
Pi r2 / r2 = Pi
"""
N = 10000
from random import random
def estimate_PI(N):
    points_in_square = 0
    points_in_circle = 0
    for i in range(N):
        random_x = random()
        random_y = random()
        # points in square 0<=x<0.5, 0=<y<0.5
        if random_x < 0.5 and random_y < 0.5:
            points_in_square += 1
        # points in circle
        y = (1 - random_x**2)**0.5
        if random_x < 1 and random_y < y:
            points_in_circle += 1
    return points_in_circle / points_in_square
    
print(estimate_PI(N))
print(estimate_PI(N*10))
print(estimate_PI(N*100))
print(estimate_PI(N*1000))
        
        
