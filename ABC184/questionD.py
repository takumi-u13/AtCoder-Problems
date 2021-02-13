from functools import lru_cache

@lru_cache(maxsize=None)
def expected_value(a, b, c):
    res = 0
    if any([a==100, b==100, c==100]): return res
    if a != 0:
        res += a * (expected_value(a+1, b, c)+1)
    if b != 0:
        res += b * (expected_value(a, b+1, c)+1)
    if c != 0:
        res += c * (expected_value(a, b, c+1)+1)
    return res/(a+b+c)

a, b, c = map(int, input().split())

print(expected_value(a, b, c))