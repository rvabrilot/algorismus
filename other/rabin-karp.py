# Limitations of Rabin-Karp Algorithm
# Spurious Hit
# When the hash value of the pattern matches with the hash value of a window of the text but the window is not the actual pattern then it is called a spurious hit.

# Spurious hit increases the time complexity of the algorithm. In order to minimize spurious hit, we use modulus. It greatly reduces the spurious hit.

# Rabin-Karp Algorithm Complexity
# The average case and best case complexity of Rabin-Karp algorithm is O(m + n) and the worst case complexity is O(mn).

# The worst-case complexity occurs when spurious hits occur a number for all the windows.

# Rabin-Karp Algorithm Applications
# For pattern matching
# For searching string in a bigger text

# PSEUDO
# n = t.length
# m = p.length
# h = dm-1 mod q
# p = 0
# t0 = 0
# for i = 1 to m
#     p = (dp + p[i]) mod q
#     t0 = (dt0 + t[i]) mod q
# for s = 0 to n - m
#     if p = ts
#         if p[1.....m] = t[s + 1..... s + m]
#             print "pattern found at position" s
#     If s < n-m
#         ts + 1 = (d (ts - t[s + 1]h) + t[s + m + 1]) mod q

# Rabin-Karp algorithm in python


d = 10

def search(pattern, text, q):
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0

    for i in range(m-1):
        h = (h*d) % q

    # Calculate hash value for pattern and text
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q

    # Find the match
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break

            j += 1
            if j == m:
                print("Pattern is found at position: " + str(i+1))

        if i < n-m:
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q

            if t < 0:
                t = t+q


text = "ABCCDDAEFG"
pattern = "CDD"
q = 13
search(pattern, text, q)