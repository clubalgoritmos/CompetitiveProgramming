from math import gcd

n = int(input())

def find_position(n):
    block = 1
    total = 0
    while total + block < n:
        total += block
        block += 1
    
    pos = n - total - 1
    integer_part = block
    
    if pos == 0:
        return integer_part, 0, 1
    
    numerator, denominator = pos, block
    g = gcd(numerator, denominator)
    
    return integer_part, numerator // g, denominator // g

integer_part, num, denom = find_position(n)
print(integer_part if num == 0 else f"{integer_part} {num}/{denom}")
