n = int(input())
s = 0
x = []
for i in range(n):
	a, b = map(int, input().split())
	s += a
	x.append(a + a + b)
x.sort()
ans = 0
while s >= 0:
	s -= x.pop()
	ans  += 1

print(ans)