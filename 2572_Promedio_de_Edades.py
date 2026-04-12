# https://jv.umsa.bo/oj/problem.php?id=2572
#  Promedio de Edades
#  Enviar
#  Estado
#  Descripción
#    Son muy comunes los problemas sobre las edades y el cálculo de promedios, de hecho es uno de los problemas clásicos cuando se enseña programación, este problema es algo parecido al clásico problema de leer edades y calcular el promedio de las edades, pero con una ligera variante, debes extraer las edades de una cadena de caracteres donde estan todas las edades juntas y de las cuales debes calcular el promedio, para facilitar tu análisis, cada edad es un numero entre 1 y 10 y tu tarea es ver la forma de extraer las edades de la cadena y calcular el promedio de ellas.Por ejemplo, para la cadena ’310110’, las posibles edades entre 1 y 10 son: 3, 10, 1, 10 y el promedio de ellas es 6Visto de esta manera consideremos la siguiente cadena y la restricción de edades de 1 a 10 ‘30101102020’ las edades validas son 3, 10, 1, 10, 2, 2 y el promedio de ellas es 4.67
#    Son muy comunes los problemas sobre las edades y el cálculo de promedios, de hecho es uno de los problemas clásicos cuando se enseña programación, este problema es algo parecido al clásico problema de leer edades y calcular el promedio de las edades, pero con una ligera variante, debes extraer las edades de una cadena de caracteres donde estan todas las edades juntas y de las cuales debes calcular el promedio, para facilitar tu análisis, cada edad es un numero entre 1 y 10 y tu tarea es ver la forma de extraer las edades de la cadena y calcular el promedio de ellas.Por ejemplo, para la cadena ’310110’, las posibles edades entre 1 y 10 son: 3, 10, 1, 10 y el promedio de ellas es 6Visto de esta manera consideremos la siguiente cadena y la restricción de edades de 1 a 10 ‘30101102020’ las edades validas son 3, 10, 1, 10, 2, 2 y el promedio de ellas es 4.67
#    Son muy comunes los problemas sobre las edades y el cálculo de promedios, de hecho es uno de los problemas clásicos cuando se enseña programación, este problema es algo parecido al clásico problema de leer edades y calcular el promedio de las edades, pero con una ligera variante, debes extraer las edades de una cadena de caracteres donde estan todas las edades juntas y de las cuales debes calcular el promedio, para facilitar tu análisis, cada edad es un numero entre 1 y 10 y tu tarea es ver la forma de extraer las edades de la cadena y calcular el promedio de ellas.
#    Por ejemplo, para la cadena ’310110’, las posibles edades entre 1 y 10 son: 3, 10, 1, 10 y el promedio de ellas es 6
#    Visto de esta manera consideremos la siguiente cadena y la restricción de edades de 1 a 10 ‘30101102020’ las edades validas son 3, 10, 1, 10, 2, 2 y el promedio de ellas es 4.67
#   Entrada
#    La entrada inicia primero con un número T, que es el número de casos de prueba, luego le siguen T líneas donde cada línea es un caso de prueba compuesta por una cadena de caracteres, cada cadena de caracteres tendrá al menos 1 caracter y a lo mas 20 caracteres.
#   Salida
#    Por cada caso de prueba, mostrar el promedio de las edades en la cadena leida, muestre el promedio con 2 decimales de precisión.
#   Ejemplo Entrada
#    711110310110101010155222222223
#   Ejemplo Salida
#    1.001.0010.006.007.755.002.11
#   Ayuda
#    Para la precisión con 2 decimales usar en python "{:.2f}".format(numero)

for _ in range(int(input())):
  V = [int(float(x)) for x in input().strip('\r')]
  s = 0
  a = 0
  for i in range(len(V)-1):
    if V[i] == 1 and V[i+1] == 0:
      V[i], V[i+1] = 10, 0
  for x in V:
    s=s+x
    if x!=0:
      a=a+1
  print("{:.2f}".format(s/a))