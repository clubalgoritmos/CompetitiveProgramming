n = int(input())
s = n//5
n = n%5
s = s + n//4
n = n%4
s = s + n//3
n = n%3
s = s + n//2
n = n%2
s = s + n
print(s)