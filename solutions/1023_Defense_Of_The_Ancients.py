# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=1
## https://jv.umsa.bo/oj/problem.php?id=1023
#    Copiado al portapapeles
#  Defense Of The Ancients
#  Enviar
#  Estado
#  Descripción
#   Entrada
#   Salida
#   Ejemplo Entrada
#    13ABCD XYTS ABCWBACD OPCW POIU
#   Ejemplo Salida
#    2
#   Ayuda
#    Un heroe se puede enfrentar a otro si comparten al menos una habilidad

def count_battles(N, A, B):
    adj_matrix = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if any(skill in B[j] for skill in A[i]):
                adj_matrix[i][j] = 1

    def bpm(u, matchR, seen):
        for v in range(N):
            if adj_matrix[u][v] and not seen[v]:
                seen[v] = True
                if matchR[v] == -1 or bpm(matchR[v], matchR, seen):
                    matchR[v] = u
                    return True
        return False

    matchR = [-1] * N

    result = 0
    for i in range(N):
        seen = [False] * N
        if bpm(i, matchR, seen):
            result += 1

    return result

for _ in range(int(input())):
    N = int(input())
    A = input().split()
    B = input().split()
    print(count_battles(N, A, B))