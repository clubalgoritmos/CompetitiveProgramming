# https://jv.umsa.bo/oj/problem.php?cid=2826&pid=14
## https://jv.umsa.bo/oj/problem.php?id=1768
#  La secuencia de Santi
#  Enviar
#  Estado
#  Descripción
#    Santi es un chico como tú, él tiene una afición por las secuencias y el metodo que emplea no es eficiente, él necesita de tu ayuda para terminar su tarea y jugar clash royal, ¡Ayúdalo! es por una buena causa.Dado dos secuencias de caracteres, imprimir LCS (longest common subsequence) de ambas secuencias.Por ejemplo, la subsecuencia común más larga (LCS) de las siguientes dos secuencias 'abcdgh' y 'aedfhr' es 'adh' de tamaño 3.
#   Entrada
#    La entrada consiste en pares de linea. El primer par de linea contiene a la primera cadena y la segunda linea contiene a la segunda cadena. Cada cadena está en una línea separada y consta de un máximo de 1,000 caracteres.
#   Salida
#    Para cada par subsiguiente de líneas de entrada, genere una línea que contenga un número entero que satisfaga lo descrito anteriormente.
#   Ejemplo Entrada
#    bcacbcabbaccbabbccabccbbabacbca1b2c3d4ezz1yy2xx3ww4vvabcdghaedfhrabcdefghijklmnopqrstuvwxyza0b0c0d0e0f0g0h0i0j0k0l0m0n0o0p0q0r0s0t0u0v0w0x0y0z0abcdefghijklmnzyxwvutsrqpoopqrstuvwxyzabcdefghijklmn
#   Ejemplo Salida
#    11432614
#   Ayuda

while True:
    try:
        X = input()
        Y = input()
        m = len(X)
        n = len(Y)
        dp = [[None] * (n + 1) for i in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif X[i - 1] == Y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])      
        print(dp[m][n])
    except EOFError:
        break
