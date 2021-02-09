n = int(input())
a = list(map(int, input().split()))

ans = 0
for l in range(n):
    x = a[l]
    for r in range(l,n):
        cnt = r-l+1
        x = min(x,a[r])
        ans = max(ans, x*cnt)

print(ans)

