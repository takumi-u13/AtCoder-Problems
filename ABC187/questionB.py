import itertools

n = int(input())
p = [list(map(int, input().split())) for l in range(n)]

ans = 0
for l in itertools.combinations(p,2):
    if abs((l[0][1]-l[1][1])/(l[0][0]-l[1][0])) <= 1:
        ans += 1
print(ans)