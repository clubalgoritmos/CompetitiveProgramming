# https://jv.umsa.bo/oj/problem.php?id=1003
#  Rumores
#  Enviar
#  Estado
#  Descripción
#   Entrada
#   Salida
#   Ejemplo Entrada
#    14 31 22 33 41 4
#   Ejemplo Salida
#    SI
#   Ayuda

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        matris = [[0]*m for _ in range(2)]
        for j in range(m):
            u, v = map(int, input().split())
            matris[0][j] = u
            matris[1][j] = v
        x, y = map(int, input().split())
        funcion(m, x, y, matris)

def funcion(m, x, y, matris):
    lista = []
    for _ in range(m):
        for i in range(m):
            if x == matris[0][i]:
                lista.append(matris[1][i])
        if lista: 
            num = len(lista)
            x = lista[num-1]
    num = len(lista)
    for i in range(num):
        var = lista[i]
        if var == y:
            print("SI")
            return
    print("NO")

if __name__ == "__main__":
    main()
        