# https://jv.umsa.bo/oj/problem.php?id=1248
#  Números armonicos
#  Enviar
#  Estado
#  Descripción
#    Los números armónicos se definen como:
#    Hn=1/1+1/2+1/3+.....+1/n
#    Donde Hn es el n-simo número armonico.
#   Entrada
#    La entrada consiste en un número "n".
#   Salida
#    Imprima el n-simo número armonico, con 4 decimales de precisión.
#   Ejemplo Entrada
#    2
#   Ejemplo Salida
#    1.5000
#   Ayuda
#    Pueden imprimir con 4 decimales usando System.out.printf("%.4f\n",numero); (en java)
#    print('{:.4f}'.format(numero)) en python

n = int(input())
S=0
for i in range(1,n+1):
 S=S+(1/i)
print('{:.4f}'.format(S))