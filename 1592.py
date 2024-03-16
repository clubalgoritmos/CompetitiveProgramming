n = input()
A = list(map(int,input().split()))
mx = A[0]
mxn = A.count(mx)
for i in set(A):
    if A.count(i) > mxn:
        mx = i
        mxn = A.count(i)
print(abs(len(A)-mxn))