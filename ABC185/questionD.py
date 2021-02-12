import sys
n, m = map(int, input().split())
a = [0] + list(map(int, input().split())) + [n+1]
a.sort()
m += 2
k = sys.maxsize
between = []
for i in range(1,m):
    tmp = a[i] - a[i-1] - 1
    if tmp <= 0:
        continue
    k = min(k, tmp)
    between.append(tmp)

ans = 0
for b in between:
    ans += b//k
    if b%k != 0:
        ans += 1

print(ans)
