

n = int(input())
A=input().split()

A = [int(n) for n in A]
A_ = A[:len(A)//2]
B_ = A[len(A)//2:]

if max(A_) > max(B_):
    print(A.index(max(B_))+1)
else:
    print(A.index(max(A_))+1)
