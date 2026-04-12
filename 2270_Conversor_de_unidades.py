# https://jv.umsa.bo/oj/problem.php?id=2270
#  Conversor de unidades
#  Enviar
#  Estado
#  Descripción
#    Escriba un programa que reciba una distancia en centímetros y que escriba esa distancia en kilómetros, metros y centímetros (escribiendo todas las unidades).
#    Escriba un programa que reciba una distancia en centímetros y que escriba esa distancia en kilómetros, metros y centímetros (escribiendo todas las unidades).
#    Escriba un programa que reciba una distancia en centímetros y que escriba esa distancia en kilómetros, metros y centímetros (escribiendo todas las unidades).
#    Escriba un programa que reciba una distancia en centímetros y que escriba esa distancia en kilómetros, metros y centímetros (escribiendo todas las unidades).
#    Escriba un programa que reciba una distancia en centímetros y que escriba esa distancia en kilómetros, metros y centímetros (escribiendo todas las unidades).
#   Entrada
#    Un número entero mayor a cero que representa la cantidad de centímetros a convertir
#    Un número entero mayor a cero que representa la cantidad de centímetros a convertir
#    Un número entero mayor a cero que representa la cantidad de centímetros a convertir
#    Un número entero mayor a cero que representa la cantidad de centímetros a convertir
#    Un número entero mayor a cero que representa la cantidad de centímetros a convertir
#   Salida
#    El equivalente expresado en kilómetros, metros y centímetros.
#    El equivalente expresado en kilómetros, metros y centímetros.
#    El equivalente expresado en kilómetros, metros y centímetros.
#    El equivalente expresado en kilómetros, metros y centímetros.
#    El equivalente expresado en kilómetros, metros y centímetros.
#   Ejemplo Entrada
#    43210
#   Ejemplo Salida
#    43210 centimetros son 0 km 432 m 10 cm
#   Ayuda

n = int(input())
km = n//100000
m = (n%100000)//100
cm = n%100
print(f"{n} centímetros son {km} km {m} m {cm} cm")