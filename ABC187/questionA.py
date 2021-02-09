a, b = map(str, (input().split()))

a_ans=b_ans=0
for i in range(len(a)):
    a_ans += int(a[i])
    b_ans += int(b[i])

print(max(a_ans, b_ans))
