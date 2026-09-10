"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment # class 10 main10.py
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""

def reconstruct_cuts(n, first_cut): # helper function: looks for best cut for current length and saves it

    cuts = []

    while n > 0:
        cut = first_cut[n]
        cuts.append(cut)
        n -= cut

    return cuts


def RodCutting(n, prices):

    if n == 0:      # this is incase you have empty rod (edge case)
        return 0, []

    revenue = [0] * (n + 1)
    first_cut = [0] * (n + 1)

    # the bottom up approch
    for length in range(1, n + 1):  # starting with smallest value
        max_val = float("-inf")     #lowest possible 

        for cut in range(1, length + 1):    # try every possible cut for current rod
            current_val = prices[cut - 1] + revenue[length - cut]

            if current_val > max_val:   # if the cut gives better revenue, update
                max_val = current_val   # then saving that
                first_cut[length] = cut

        revenue[length] = max_val   # saving the best value

    cuts = reconstruct_cuts(n, first_cut)
    return revenue[n], cuts

if __name__ == "__main__":
    # testting if it's actually doing what I want it to do
    rod_length = 8
    prices = [1, 5, 8, 9, 10, 17, 17, 20]

    max_revenue, cuts = RodCutting(rod_length, prices)

    print("Rod Length:", rod_length)
    print("Prices:", prices)
    print("Maximum Revenue:", max_revenue)
    print("Cuts:", cuts)