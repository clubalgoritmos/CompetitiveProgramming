# https://jv.umsa.bo/oj/problem.php?cid=2824&pid=4
## https://jv.umsa.bo/oj/problem.php?id=2073
#  Distanciamiento Social
#  Estado
#  Descripción
#    En tiempos de pandemia el distanciamiento social es clave para no propagar el virus.
#    Se te dara las de coordenadas de dos personas y tu tarea es verificar que la distancia entre ambas personas sea mayor igual a un 1 metro.
#   Entrada
#    La entrada consiste de $x_1, y_1, x_2, y_2$ $(-1000000 \le x_1, y_1, x_2, y_2 \le 1000000)$, donde $x_1$ y $y_1$ es la coordenada de la primera persona, $x_2$ y $y_2$ es la coordenada de la segunda persona.
#   Salida
#    Imprima "SI", si la distancia entre ambas personas es mayor igual a un metro, en otro caso imprima "NO". Luego en otro linea imprima la distacia total entra ambas personas en el siguiente formato Kilimetros, Metros y Centimetros, cada dato con una presicion de 2 decimales.
#   Ejemplo Entrada
#    1 1 2 2
#   Ejemplo Salida
#    NOkm: 0.00 m: 0.00 cm: 1.41
#   Ayuda

x1,y1,x2,y2 = map(int,input().split())
d = ((x2-x1)**2+(y2-y1)**2)**.5
if d>100:
    print("SI")
else:
    print("NO")
m = d//100
d = d%100
km = m//1000
m = m%1000
print(f"km: {km:.2f} m: {m:.2f} cm: {d:.2f}")