import itertools

n, k = map(int,input().split()) 
t = [list(map(int, input().split())) for l in range(n)]

res = []

for p in itertools.permutations(range(1,n), n-1):
    p = [0] + list(p) + [0]
    tmp = 0
    now = 0
    for i in p:
        tmp += t[i][now]
        now = i
    res.append(tmp)

ans = 0
for i in res:
    if k == i:
        ans += 1
print(ans)