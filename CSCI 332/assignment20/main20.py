"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment class 20
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""

import math

# helper functions--------------------------------

def polar_angle(p0, p1):
    return math.atan2(p1[1] - p0[1], p1[0] - p0[0])

def dist(p0, p1):
    return (p1[0] - p0[0])**2 + (p1[1] - p0[1])**2          # just a bunch of math

def orientation(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

#end helper functions-----------------------------

def graham_scan(points):
    p0 = min(points, key=lambda p: (p[1], p[0]))       # finding the anchor point: the lowest y point
    points.sort(key=lambda p: (polar_angle(p0, p), dist(p0, p)))    # we have the anchor: we look at the points in CCW order

    hull = [] # my stack

    for i in range(len(points)):   # going through in left turns only
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], points[i]) <= 0: # checking the direction of the turn from the last 2 turns
            hull.pop() # removes right turn
        hull.append(points[i]) # adds point

    return hull

if __name__ == "__main__": # messing around
        points = [(0, 0), (2, 0), (2, 2), (0, 2), (1, 1)]
        expected = [(0, 0), (2, 0), (2, 2), (0, 2)]
        result = graham_scan(points)
        print(result, expected)