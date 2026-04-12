# Solucion
# https://jv.umsa.bo/oj/problem.php?cid=2815&pid=0
#  Descomponer el tiempo
#  Enviar
#  Estado
#  Descripción
#    Tenemos una maquina que tiene una pequeña pantalla en el que indica cuantos segundos lleva funcionando. El problema radica en que para los humanos es muy dificil leer el tiempo solamente en segundos, es por eso que debes hacer un programa que descomponga este numero de segundos a un formato que sea mas facil de leer para los humanos.
#    Este formato consiste en descomponer ese numero de segundos en horas, minutos y segundos. Ademas no puede ser cualquier descomposición, debe ser una despcomposición valida, una descomposición es valida si no podemos tomar alguna cantidad de segundos de la descomposición y convertirla en un minutos, y no podemos tomar alguna cantidad de minutos de la descomposicion y convertirla en horas.
#   Entrada
#    La entrada consiste en un numero entero que representa la cantidad de segundos que indica la maquina.
#   Salida
#    Escriba en la salida la cantidad de horas, minutos y segundos separados por un espacio.
#   Ejemplo Entrada
#    3661
#   Ejemplo Salida
#    1 1 1
#   Ayuda
#    Ejemplos:
#    5 59 4 -> Formato valido5 61 4 -> Formato invalido, se pueden tomar 60 min. y convertirlo en 1 hora27 15 40 -> Formato valido3 5 123 -> Formato invalido, se pueden tomar 2 minutos(120 seg.) del contador de segundos.

S = int(input())
H = S//3600
S = S%3600
M = S//60
S = S%60
print(H,M,S)