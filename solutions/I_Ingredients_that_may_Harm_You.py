#Time limit
MOD = 10**9 + 7

def sieve(n):
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
    return prime_numbers

def prime_factors(n, primes):
    factors = set()
    for p in primes:
        if p * p > n:
            break
        while n % p == 0:
            factors.add(p)
            n //= p
    if n > 1:
        factors.add(n)
    return factors

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    
    N = int(data[index])
    index += 1
    foods = list(map(int, data[index:index + N]))
    index += N
    
    Q = int(data[index])
    index += 1
    allergies = list(map(int, data[index:index + Q]))
    
    max_value = 10**6
    primes = sieve(max_value)
    
    food_factors = [prime_factors(food, primes) for food in foods]
    
    results = []
    for allergy in allergies:
        allergy_factors = prime_factors(allergy, primes)
        safe_food_count = 0
        for factors in food_factors:
            if not factors & allergy_factors:
                safe_food_count += 1
        results.append(pow(2, safe_food_count, MOD))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()