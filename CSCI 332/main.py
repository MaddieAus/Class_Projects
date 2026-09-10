"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment # class (structured python project) main.py
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""


### This Assignment Brute_force_matching: is about using python to make a pattern matching algorithm. Taking a string and having the code tell us how many times it shows up ###

# def brute_force_match(text:str,pattern:str)-> list[int]:
#     matches = [] # empty list to store
#     n = len(text) # the length of the text putting in n
#     m = len(pattern) # the length of the pattern putting in m
#     for i in range(n-m+1): # looking in both m and n
#         j = 0
#         while j < m and text[i+j] == pattern[j]: # this is navagating the list
#             j = j+1
#         if j == m: # if it finds a match it will move to matched text
#             matches.append(i) # this adds it to the list matches
#     return matches
    
    
# if __name__ == "__main__":
#     text = "Mississippi"
#     pattern = "iss"
#     print (brute_force_match(text,pattern))


### This Assignment Boyer-Moore: is the same concept as the last assignment but we will be using a differnet implementation. using "the bad character heuristic" ###

# def build_bad_character_table(pattern: str) -> dict: # this is the helper function
#     table = {} # building the bad table
#     for i in range(len(pattern)):
#         table[pattern[i]] = i
#     return table


# def boyer_moore_match(text: str, pattern: str) -> list[int]:
#     if not pattern or not text or len(pattern) > len(text):
#         return []

#     bad_char_table = build_bad_character_table(pattern)
#     matches = []

#     n = len(text)
#     m = len(pattern)
#     shift = 0  # aligning the text

#     while shift <= n - m:
#         j = m - 1  # looking at the end of the pattern

#         # Comparing the pattern and text from the right to the left
#         while j >= 0 and pattern[j] == text[shift + j]:
#             j -= 1

#         # If the pattern matches
#         if j < 0:
#             matches.append(shift)

#             # this shifts the pattern 
#             if shift + m < n:
#                 next_char = text[shift + m]
#                 shift += m - bad_char_table.get(next_char, -1)
#             else:
#                 shift += 1
#         else:
#             # sends it to the bad character heuristic
#             bad_char = text[shift + j]
#             last_occurrence = bad_char_table.get(bad_char, -1)
#             shift += max(1, j - last_occurrence)

#     return matches

# text = "ABAAABCD"
# pattern = "ABC"
# print(boyer_moore_match(text, pattern))

### this assignment: Knuth-Morris-pratt algorithm, this is another matching problem but a different algorithm. trying to keep the run time faster ###

# def knuth_morris_pratt_match(text: str, pattern: str) -> list[int]:
    
#      # making the LPS array
#     if pattern == "":     # If pattern is empty
#         return []

#     lps = [0] * len(pattern)

#     prevLPS = 0      # length of previous longest prefix suffix
#     i = 1            # starting from second place in text

#     while i < len(pattern):
#         if pattern[i] == pattern[prevLPS]: # if there is match it extends 
#             prevLPS += 1
#             lps[i] = prevLPS
#             i += 1
#         else:
#             if prevLPS == 0: # if there is no prefix match
#                 lps[i] = 0
#                 i += 1
#             else:
#                 prevLPS = lps[prevLPS - 1] # trying shorter prev prefix

#     matches = []  # matches found
#     i = 0   # texts
#     j = 0   # patterns

#     while i < len(text):
#         if text[i] == pattern[j]: # if the characters match we move both pointers
#             i += 1
#             j += 1
#         else:
#             if j == 0: # if no partial match it moves to the next pointer
#                i += 1
#             else:
#                 # Use the LPS to skip unnecessary stuff
#                 j = lps[j - 1]
#         if j == len(pattern): # If matched the entire pattern
#             matches.append(i - j) # Record starting letter of match
#             j = lps[j - 1] # Continues searching for next match

#     return matches

# if __name__ == "__main__":
#     text = "abracadabra"
#     pattern = "abra"
#     result = knuth_morris_pratt_match(text, pattern)
#     print("Text:", text)
#     print("Pattern:", pattern)
#     print("Matches:", result) # it should be [0,7]


### this assignment: knapsack problem algorithm,  ###

def fractional_knapsack(items: list[tuple[float, float]], capacity: float) -> tuple[float, list[tuple[int, float]]]:
    """
    items: list of tuples (value, weight)
    capacity: maximum capacity of the knapsack
    returns: tuple of total value, list of tuples (item_index, fraction_taken)
    """

    # Pair each item
    indexed_items = [
        (i, value, weight, value / weight)
        for i, (value, weight) in enumerate(items)
    ]

    # Sorting items ---> descending
    indexed_items.sort(key=lambda x: x[3], reverse=True)

    total_value = 0.0
    result = []

    # greedy selection
    for index, value, weight in indexed_items:
        if capacity <= 0:
            break

        if weight <= capacity:
            # Take the whole item
            total_value += value
            capacity -= weight
            result.append((index, 1.0))
        else:
            # Take fraction of the item
            fraction = capacity / weight 
            total_value += value * fraction     # math for getting fraction of item
            result.append((index, fraction))
            capacity = 0

    return total_value, result

if __name__ == "__main__":
    items = [(60, 10), (100, 20), (120, 30)]
    capacity = 50

    total_value, fractions = fractional_knapsack(items, capacity)

    print(f"Total value: {total_value}")
    print(f"Items taken (index, fraction): {fractions}")