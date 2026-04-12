# https://jv.umsa.bo/oj/problem.php?id=2559
#  Restas Sucesivas Especiales
#  Enviar
#  Estado
#  Descripción
#    Dado N y K, donde N ( 2 ≤N≤109 ) y K ( 1≤K≤50), se realizan las restas sucesivas especiales, bajo el siguiente algoritmo:
#    Dado N y K, donde N ( 2
#    ≤
#    N
#    ≤
#    109 ) y K ( 1
#    ≤
#    K
#    ≤
#    50), se realizan las restas sucesivas especiales, bajo el siguiente algoritmo:
#    - Si el último dígito es diferente de cero, entonces simplemente le restas uno.
#    - Si el último dígito es diferente de cero, entonces simplemente le restas uno.
#    - Si el último dígito es igual a cero, entonces dividimos entre 10 (eliminamos el último dígito)
#    - Si el último dígito es igual a cero, entonces dividimos entre 10 (eliminamos el último dígito)
#    Por ejemplo: 512 4
#    Por ejemplo:
#    512 4
#    Iteración 1: Restar uno. Resultado = 511
#    Iteración 1: Restar uno. Resultado = 511
#    Iteración 2: Restar uno. Resultado = 510
#    Iteración 2: Restar uno. Resultado = 510
#    Iteración 3: Divide entre 10. Resultado = 51
#    Iteración 3: Divide entre 10. Resultado = 51
#    Iteración 4: Restar uno. Resultado = 50
#    Iteración 4: Restar uno. Resultado = 50
#    Imprime como resultado final: 50
#    Imprime como resultado final:
#    50
#   Entrada
#    Lee dos número seguidos por un espacio, donde el primero corresponde a N y el segundo corresponde a K.
#    Lee dos número seguidos por un espacio, donde el primero corresponde a N y el segundo corresponde a K.
#   Salida
#    Imprime el valor final de N resultante,
#    Imprime el valor final de N resultante,
#   Ejemplo Entrada
#    512 4
#   Ejemplo Salida
#    50
#   Ayuda

N, K = (int(x) for x in input().split(' '))
for _ in range(K):
  if N%10==0:
    N = N//10
  else:
    N = N-1
print(N)