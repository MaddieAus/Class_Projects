"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment # class main12.py
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""

def longest_common_subsequence(string1, string2):

    m = len(string1)
    n = len(string2)

    # Creating a zero table 
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)] # variable doesn't matter so just using "_"

    # for filling up the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[m][n]

    # going back to reconstruct sequence
    lcs_sequence = []
    i = m
    j = n

    while i > 0 and j > 0:

        if string1[i - 1] == string2[j - 1]:
            lcs_sequence.append(string1[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_sequence.reverse() # we used the bottom up approach so this is just flipping it

    return lcs_length, "".join(lcs_sequence) # just bringing the stings together

if __name__ == "__main__":
    # Testting that its working
    string1 = "ABCDGH"
    string2 = "AEDFHR"
    length, sequence = longest_common_subsequence(string1, string2)

    print("Testting")
    print("String 1:", string1)
    print("String 2:", string2)
    print("LCS Length:", length)
    print("LCS Sequence:", sequence)
    print()