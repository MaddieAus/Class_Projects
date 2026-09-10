"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment # class 08 main.py
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""

def greedy_scheduling(tasks):
    """
    tasks: list of tuples (start_time, end_time, profit)
    returns: maximum total profit from non-overlapping tasks
    """

    tasks_sorted = tasks[:]     # copying 

    # sorttting by ending time
    n = len(tasks_sorted)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if tasks_sorted[j][1] < tasks_sorted[min_index][1]:     # all of this is making the tasks sort by ending time and swapping if need be
                min_index = j
        # Swapping tasks
        tasks_sorted[i], tasks_sorted[min_index] = (
            tasks_sorted[min_index],
            tasks_sorted[i],
        )

    total_profit = 0
    last_end_time = 0

    # Greedy selection for non overlapping 
    for start, end, profit in tasks_sorted:
        if start >= last_end_time:
            total_profit += profit      # this is for the overlapping if you are a busy bee that day
            last_end_time = end

    return total_profit


# test run from slides it should be 16 
tasks = [(1, 3, 5), (2, 5, 6), (4, 6, 5), (6, 7, 4), (5, 8, 11), (7, 9, 2)]
max_profit = greedy_scheduling(tasks)
print(max_profit)
