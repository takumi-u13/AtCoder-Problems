import  itertools

N, M = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(M)]
K = int(input())
cd = [tuple(map(int, input().split())) for _ in range(K)]

ans = 0

for balls in itertools.product(*cd):
    balls = set(balls)
    cnt = sum(A in balls and B in balls for A, B in ab)
    if ans < cnt:
        ans = cnt

print(ans)