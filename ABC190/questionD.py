import itertools

N = int(input())
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

divisors = make_divisors(2*N)

cnt = 0
for n in divisors:
    m = (2*N)//n
    if (n%2 != m%2):
        cnt += 1

print(cnt)