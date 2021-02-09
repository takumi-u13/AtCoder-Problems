H, W = map(int, input().split())

a = [input() for l in range(H)]

directions = (
    (0,1),
    (1,1),
    (1,0),
    (0,0)
)
cnt = 0

for i in range(H-1):
    for j in range(W-1):
        tmp = 0
        for d in directions:
            if a[i+d[0]][j+d[1]] == '#':
                tmp += 1
        cnt += tmp%2 
print(cnt)