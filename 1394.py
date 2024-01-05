c = 0
primos = ["2", "3", "5", "7"]
for _ in range(int(input())):
  n = input()
  xn = [int(ni) for ni in n if ni in primos]
  if len(xn)>=3 and sum(xn)%2==0:
    c+=1
print(c)