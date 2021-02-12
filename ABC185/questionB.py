n, m, t = map(int, input().split())
cafe_time = [list(map(int, input().split())) for _ in range(m)]
ans = n
before = 0
for i in range(m):
    arrived, leaved = cafe_time[i]
    ans -= arrived - before
    if ans <= 0:
        break
    ans = min(n, ans+leaved-arrived)
    before = leaved
    
ans -= t - leaved

if ans > 0:
    print('Yes')
else:
    print('No')


