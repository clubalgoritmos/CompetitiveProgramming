

for _ in range(int(input())):
    i,n = map(int, input().split()) #elem, tipo
    fibo = [1]*n
    def fibonacci(i):
        if i < len(fibo):
            return fibo[i]
        fibo.append(sum(fibo[-n:]))
        return fibonacci(i)
    print(fibonacci(i))
