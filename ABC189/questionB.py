n, x = map(int, input().split())
l = [list(map(int, input().split())) for l in range(n)]
idx = 1
s = 0
for i in l:
    s += i[0] * i[1]
    if x * 100 < s:
        print(idx)
        break
    idx += 1
if idx > n:
    print('-1')