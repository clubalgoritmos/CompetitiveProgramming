A,B,C,D = map(int,input().split())
s = min(A,B,C,D)
print(sum([abs(A-s),abs(B-s),abs(C-s),abs(D-s)]))