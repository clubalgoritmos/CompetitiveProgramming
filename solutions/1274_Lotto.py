# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=48
## https://jv.umsa.bo/oj/problem.php?id=1274
#    Copiado al portapapeles
#  Lotto
#  Enviar
#  Estado
#  Descripción
#    En la lotería denominada Lotto debe seleccionar 6 números del conjunto 1,2,...,49.Un estrategia popular pero que no asegura mejorarán sus probabilidad de ganar es escoger un sub conjunto S que contiene k (k>6) de estos 49 números. Luego juega muchas veces escogiendo solo números de S.Por ejemplo si k=8 y S = 1,2,3,5,8,13,21,34 hay 28 posibles juegos: [1,2,3,5,8,13], [1,2,3,5,8,21], [1,2,3,5,8,34], [1,2,3,5,13,21], ..., [3,5,8,13,21,34].Su tarea es escribir un programa que lea el numero k y el conjunto S luego imprima todos los posibles juegos escogiendo solo números de S.
#   Entrada
#    La entrada consiste de varios casos de prueba. Cada caso de prueba consiste del número k seguido por k números de la lotería. El numero k siempre estará entre (6 < k < 13).Termina cuando no hay más datos en la entrada.
#   Salida
#    Para cada caso de prueba escriba todos los posibles juegos. Cada una en una línea.
#   Ejemplo Entrada
#    7 1 2 3 4 5 6 78 1 2 3 5 8 13 21 34
#   Ejemplo Salida
#    1 2 3 4 5 61 2 3 4 5 71 2 3 4 6 71 2 3 5 6 71 2 4 5 6 71 3 4 5 6 72 3 4 5 6 71 2 3 5 8 131 2 3 5 8 211 2 3 5 8 341 2 3 5 13 211 2 3 5 13 341 2 3 5 21 341 2 3 8 13 211 2 3 8 13 341 2 3 8 21 341 2 3 13 21 341 2 5 8 13 211 2 5 8 13 341 2 5 8 21 341 2 5 13 21 341 2 8 13 21 341 3 5 8 13 211 3 5 8 13 341 3 5 8 21 341 3 5 13 21 341 3 8 13 21 341 5 8 13 21 342 3 5 8 13 212 3 5 8 13 342 3 5 8 21 342 3 5 13 21 342 3 8 13 21 342 5 8 13 21 343 5 8 13 21 34
#   Ayuda

