# https://jv.umsa.bo/oj/problem.php?id=1428
#  Distancia entre dos puntos
#  Enviar
#  Estado
#  Descripción
#    Dadas las cordenados de dos puntos $P1=(x1,y1)$ y $P2=(x2,y2)$ hallar la distancia entre dos puntos.La formula para la distancia de dos puntos es \[ distancia= \sqrt((x1-x2)^2+(y1-y2)^2) \]
#   Entrada
#    La entrada consiste de cuatro números con decimales, que representan las coordenadas de los dos puntos $x1,y1,x2,y2$ respectivamente.
#   Salida
#    Escriba una línea con la distancia de los dos puntos con dos decimales.
#   Ejemplo Entrada
#    1.1 2.3 -2.2 3.33
#   Ejemplo Salida
#    3.46
#   Ayuda

x1, y1, x2, y2 = map(float,input().split())
print("{:.2f}".format(((x1-x2)**2+(y1-y2)**2)**0.5))