h, w = map(int,input().split()) 
a = []
for i in range(h):
    a += list(map(int, input().split()))

minimum = min(a)
ans = 0
for i in range(h*w):
    ans += a[i] - minimum

print(ans)