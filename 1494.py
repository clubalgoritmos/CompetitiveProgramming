fibo = [0, 1]
def fibonacci(n):
    if n < len(fibo):
        return fibo[n]
    else:
        fibo.append(fibonacci(n-1) + fibonacci(n-2))
        return fibo[n]

primes = [2]
def nth_prime(n):
    if n <= len(primes):
        return primes[n-1]
    else:
        num = primes[-1] + 1
        while len(primes) < n:
            if all(num % p > 0 for p in primes):
                primes.append(num)
            num += 1
        return primes[-1]

while True:
    try:
        n,x = map(int, input().split())
        s = 0
        for i in range(1,n+1):
            s+=fibonacci(i)/(nth_prime(i)*x)
        print("{:.2f}".format(s))
    except EOFError:
        break