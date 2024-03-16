primes = set([2,3,5,7])

def filter_primes(n):
    digits = map(int, str(n))
    filtered = list(filter(primes.__contains__, digits))
    return filtered if filtered else [0]

for _ in range(int(input())):
    print(*filter_primes(input()), sep='', end='\n'):