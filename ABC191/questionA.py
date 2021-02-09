V, T, S, D = map(int, input().split())

M_t = V*T
M_s = V*S

if not(M_t<=D and D <= M_s):
    print('Yes')
    exit()

print('No')