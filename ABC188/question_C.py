from time import time


n = int(input())
A=input().split()
A_ = A.copy()

start = time()
while True:
    for i in range(len(A)//2):
        if int(A[i * 2 - i]) > int(A[i * 2 + 1 - i]):
            A.pop(i * 2 + 1 - i)
        else:
            A.pop(i * 2 - i)
    if len(A) == 2:
        break

if int(A[0]) > int(A[1]):
    A.pop(0)
else:
    A.pop(1)

print(A_.index(A[0]) + 1)

elapsed_time = time() - start

print(elapsed_time)