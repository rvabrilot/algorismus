# The longest common subsequence in Python

# X and Y be two given sequences
# Initialize a table LCS of dimension X.length * Y.length
# X.label = X
# Y.label = Y
# LCS[0][] = 0
# LCS[][0] = 0
# Start from LCS[1][1]
# Compare X[i] and Y[j]
#     If X[i] = Y[j]
#         LCS[i][j] = 1 + LCS[i-1, j-1]   
#         Point an arrow to LCS[i][j]
#     Else
#         LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
#         Point an arrow to max(LCS[i-1][j], LCS[i][j-1])

# Applications
# in compressing genome resequencing data
# to authenticate users within their mobile phone through in-air signatures

# Function to find lcs_algo
def lcs_algo(S1, S2, m, n):
    L = [[0 for x in range(n+1)] for x in range(m+1)]

    # Building the mtrix in bottom-up way
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i-1] == S2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    index = L[m][n]

    lcs_algo = [""] * (index+1)
    lcs_algo[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if S1[i-1] == S2[j-1]:
            lcs_algo[index-1] = S1[i-1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    # Printing the sub sequences
    print("S1 : " + S1 + "\nS2 : " + S2)
    print("LCS: " + "".join(lcs_algo))


S1 = "ACADB"
S2 = "CBDA"
m = len(S1)
n = len(S2)
lcs_algo(S1, S2, m, n)