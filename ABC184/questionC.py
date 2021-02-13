a, b = map(int, input().split())
c, d = map(int, input().split())

r = abs(a-c)
q = abs(b-d)

if (r, q) == (0, 0):
    print(0)
elif (a+b == c+d) or (a-b == c-d) or abs(r)+abs(q) <= 3:
    print(1)
elif ((a+b+c+d)%2 == 0) or (abs(r)+abs(q) <= 6) or abs((a+b)-(c+d)) <= 3 or abs(r - q) <= 3:
    print(2)
else:
    print(3)