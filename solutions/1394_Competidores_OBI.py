# https://jv.umsa.bo/oj/problem.php?id=1394
#  Competidores OBI
#  Enviar
#  Estado
#  Descripción
#    A la Fase Nacional de la Olimpiada Científica Estudiantil, han llegado estudiantes de muchos departamentos de Bolivia.Todos los estudiantes tienen una credencial y en ella un código único, y por alguna extraña razón el código de los competidores del área de informática tienen una particularidad: Tienen al menos 3 números primos de un dígito y la suma de tres de esos numeros (digitos primos) es par. Mishell, una competidora del área de matemáticas se ha dado cuenta de ello y por eso va contando competidores en el área de informática en cada grupo que ella conoce, ella anota y hace sus cálculos de manera manual ya que no sabe programar. Por ello te pide ayuda, ya que vio tu credencial.Realiza un programa donde ingresas $n$ números que representan los códigos de las credenciales y cuente los competidores en el área de informática.
#   Entrada
#    La primera línea tendrá un número $n<4000$, que es la cantidad de casos de prueba. Seguido de $n$ líneas. En cada línea se tiene un número $x>1$ y $x< 100000000$. Cada $x$ corresponde al código de una credencial.
#   Salida
#    Imprimir sólo un número, el cual indica la cantidad de competidores en el área de informática.
#   Ejemplo Entrada
#    31234168956791223456
#   Ejemplo Salida
#    2
#   Ayuda
#    Puede tener más de tres primos.

c = 0
primos = ["2", "3", "5", "7"]
for _ in range(int(input())):
  n = input()
  xn = [int(ni) for ni in n if ni in primos]
  if len(xn)>=3 and sum(xn)%2==0:
    c+=1
print(c)