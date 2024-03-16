# https://jv.umsa.bo/oj/problem.php?id=2535
#  EL PROBLEMA DE LA SANDÍA
#  Enviar
#  Estado
#  Descripción
#    Un caluroso día de verano, Dereck y su amigo Alex, decidieron comprar una sandía. Eligieron la más grande y la más madura, a su juicio. Después de eso, se pesó la sandía y la balanza mostró W kilos. Corrieron a casa, muriendo de sed, y decidieron dividir la sandía, sin embargo, se enfrentaron a un problema difícil.
#    Dereck y Alex, son grandes aficionados a los números pares, por eso quieren dividir la sandía de tal forma que cada una de las dos partes, tenga su peso como un número par de kilos, a la vez que, no es obligatorio que las partes sean iguales. Los niños están extremadamente cansados y quieren comenzar su comida lo más antes posible, por eso debes ayudarlos y averiguar si pueden dividir la sandía de la manera que ellos quieren. Por supuesto, cada uno de ellos debería tener una parte del peso positivo.
#   Entrada
#    La primera (y única) línea de entrada contiene el número entero W (1≤W≤100) — que corresponde al peso de la sandía comprada por los niños.
#    La primera (y única) línea de entrada contiene el número entero W (1≤W≤100) — que corresponde al peso de la sandía comprada por los niños.
#   Salida
#    Escriba en mayúscula SI, si los niños pueden dividir la sandía en dos partes, cada una de ellas con un peso par de kilos; y NO en el caso contrario.
#    Escriba en mayúscula SI, si los niños pueden dividir la sandía en dos partes, cada una de ellas con un peso par de kilos; y NO en el caso contrario.
#   Ejemplo Entrada
#    8
#   Ejemplo Salida
#    SI
#   Ayuda

W = int(input())
if (W/2)%2==0:
 print('SI')
else:
 print('NO')