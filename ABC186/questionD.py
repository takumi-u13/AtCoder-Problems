import itertools

n = int(input())
a = list(map(int, input().split()))
a.sort()
cumsum = list(itertools.accumulate(a))

ans = 0
for i in range(1, n):
    ans += i * a[i] - cumsum[i-1]


print(ans)