import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


print(combinations_count(int(input())-1, 11))