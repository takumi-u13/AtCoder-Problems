n = int(input())
A = input().split(' ')
B = input().split(' ')

ans = 0
for i in range(n):
    ans += int(A[i])*int(B[i])

if ans == 0:
    print('Yes')
else:
    print('No')