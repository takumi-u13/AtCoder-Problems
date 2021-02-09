s = input().split(' ')

X = int(s[0])
Y = int(s[1])
ans = abs(X-Y)

if ans < 3:
    print('Yes')
else:
    print('No')