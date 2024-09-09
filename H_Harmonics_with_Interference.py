#Solucion
def generate_combinations(s):
    if '*' not in s:
        return [s]
    combinations = []
    for c in '01':
        combinations.extend(generate_combinations(s.replace('*', c, 1)))
    return combinations

def find_valid_message(M_prime, N_prime):
    M_combinations = generate_combinations(M_prime)
    N_combinations = generate_combinations(N_prime)
    
    for M in M_combinations:
        M_int = int(M, 2)
        for N in N_combinations:
            N_int = int(N, 2)
            if N_int != 0 and M_int % N_int == 0:
                return M
    return None
M_prime = input().strip()
N_prime = input().strip()
valid_message = find_valid_message(M_prime, N_prime)
if valid_message:
    print(valid_message)
else:
    print(-1)