import math

def prime_generator(limit):
    """Genera números primos hasta limit usando yield"""
    yield 2
    for n in range(3, limit + 1, 2):
        is_prime = True
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n

def factorize(n):
    """Factoriza n y retorna lista de (primo, exponente)"""
    factors = {}
    
    # Límite para la búsqueda de primos
    limit = int(math.sqrt(n)) + 1
    
    # Usar generador de primos
    for p in prime_generator(min(limit, 10**6)):
        if p * p > n:
            break
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
    
    # Si queda un número mayor que 1, es primo
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    
    return list(factors.items())

def solve():
    X = int(input().strip())
    
    # Para números pequeños (factorizables), factorizamos exactamente
    if X <= 10**15:
        factors = factorize(X)
        print(len(factors))
        for p, e in factors:
            print(p, e)
        return
    
    # Para números muy grandes, usamos aproximación con potencias de primos pequeños
    if X <= 10**18:
        # Intentar factorizar o aproximar con potencias de primos pequeños
        small_primes = list(prime_generator(50))
        
        best_factorization = None
        best_error = float('inf')
        
        for p in small_primes:
            # Encontrar e tal que p^e ≈ X
            e = round(math.log(X) / math.log(p))
            if e > 0:
                Y = p ** e
                error = abs(X - Y) / X
                if error <= 1e-9 and error < best_error:
                    best_error = error
                    best_factorization = [(p, e)]
        
        if best_factorization:
            print(len(best_factorization))
            for p, e in best_factorization:
                print(p, e)
            return
    
    # Para números extremadamente grandes (> 10^18), usar aproximación logarítmica
    if X > 10**300:
        # Aproximar usando conteo de dígitos
        num_digits = len(str(X))
        # log₂(X) ≈ num_digits * log₂(10)
        log2_X = num_digits * math.log(10) / math.log(2)
    else:
        log2_X = math.log(X) / math.log(2)
    
    e = round(log2_X)
    
    # Salida: 2^e
    print(1)
    print(2, e)

solve()