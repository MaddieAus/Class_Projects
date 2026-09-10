"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment # class 16 main.py
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""

# Function to compute orientation of three points
def get_orientation(p, q, r):

    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    if val == 0:
        return 0
    elif val > 0:
        return 1      # counterclockwise
    else:
        return 2      # clockwise


def convex_hull_jarvis(points):

    n = len(points)

    if n < 3:
        return points

    hull = []

    # Find the leftmost point
    leftmost = 0
    for i in range(1, n):
        if points[i][0] < points[leftmost][0]:
            leftmost = i

    p = leftmost

    while True:

        hull.append(points[p])

        q = (p + 1) % n

        for r in range(n):

            if get_orientation(points[p], points[q], points[r]) == 2:
                q = r

        p = q

        if p == leftmost:
            break

    return hull

# Example usage
if __name__ == "__main__":

    points = [
        (0,3),
        (2,2),
        (1,1),
        (2,1),
        (3,0),
        (0,0),
        (3,3)
    ]

    hull = convex_hull_jarvis(points)

    print("Convex Hull:")
    for p in hull:
        print(p)