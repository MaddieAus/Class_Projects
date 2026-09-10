"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment class 25
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""

import math
from queue import PriorityQueue

def OrthoSeg(segments):
    s = {}
    pq = PriorityQueue()   # sorted by x-coordinates

    # Build event list
    for seg in segments:
        if seg[0] == "H": # horizontal segments
            _, x1, x2, y = seg
            pq.put((x1, "start", y, x2))   
            pq.put((x2, "end", y, x1))     

        elif seg[0] == "V": # vertical segments
            _, x, y1, y2 = seg
            pq.put((x, "vertical", y1, y2))  

    intersections = [] # store all intersection points

    # Process events
    while not pq.empty():   

        event = pq.get() # get next event sorted order
        x = event[0] # current x position of swwep line
        etype = event[1] # type of event

        if etype == "start": # starts horizontal
            y = event[2]
            x2 = event[3]
            s[y] = (x, x2)

        elif etype == "end": # ends horizontal
            y = event[2]
            if y in s:
                del s[y] # remove segment from active set

        elif etype == "vertical": # vertical segment
            y1 = event[2]
            y2 = event[3]

            for y in s: # checking if the horizontal segments intersect. if lies within [y1, y2] then vertical segment
                if y1 <= y <= y2:
                    intersections.append((x, y))

    return intersections # return all intersection points 

if __name__ == "__main__": # testing
    segments = [
        ("H", 1, 5, 3),
        ("H", 2, 6, 5),
        ("V", 4, 2, 6)
    ]

    print(OrthoSeg(segments))