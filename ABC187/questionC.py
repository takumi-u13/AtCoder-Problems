n = int(input())
s = set(input() for _ in range(n))

for i in s:
    if '!' + i in s:
        print(i)
        exit()

print('satisfiable')