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


# Return True if point q lies on segment pr
def on_segment(p, q, r):

    if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
        q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
        return True

    return False


# Determine if two segments intersect
def do_intersect(seg1, seg2):

    p1, q1 = seg1
    p2, q2 = seg2

    o1 = get_orientation(p1, q1, p2)
    o2 = get_orientation(p1, q1, q2)
    o3 = get_orientation(p2, q2, p1)
    o4 = get_orientation(p2, q2, q1)

    # General case
    if o1 != o2 and o3 != o4:
        return True

    # Special Cases
    if o1 == 0 and on_segment(p1, p2, q1):
        return True

    if o2 == 0 and on_segment(p1, q2, q1):
        return True

    if o3 == 0 and on_segment(p2, p1, q2):
        return True

    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False


# Example usage
if __name__ == "__main__":

    p1 = (1.0, 1.0)
    p2 = (4.0, 4.0)
    p3 = (2.0, 4.0)
    p4 = (4.0, 2.0)

    seg1 = (p1, p2)
    seg2 = (p3, p4)

    print(do_intersect(seg1, seg2))  # Should print True