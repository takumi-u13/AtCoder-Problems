n = int(input())
s = [input() for _ in range(n)]
ans = 0
def logical_expression(s):
    ans = 0
    if len(s) == 0: return 1
    if s[-1] == 'AND':
        ans += logical_expression(s[:-1])
    else:
        ans += 2**(len(s)) + logical_expression(s[:-1])

    return ans

print(logical_expression(s))