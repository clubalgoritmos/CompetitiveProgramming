generar_sucesion = lambda n: 1 if n<=0 else 1+(n)*4+generar_sucesion(n-1)
for _ in range(int(input())):
  print(*[generar_sucesion(i) for i in range(int(input()))])