# https://jv.umsa.bo/oj/problem.php?id=1374
#  Intervalos
#  Enviar
#  Estado
#  Descripción
#    Escriba un programa talque dados dos intervalos, calcule el intervalo que corresponde a su intersección o indica si esta vacío.
#    Escriba un programa talque dados dos intervalos, calcule el intervalo que corresponde a su intersección o indica si esta vacío.
#    Escriba un programa talque dados dos intervalos, calcule el intervalo que corresponde a su intersección o indica si esta vacío.
#   Entrada
#    La entrada consiste de cuatro enteros $a_{1},b_{1},a_{2},b_{2}$ que representan los intervalos $[a_{1} , b_{1}]$ y $[a_{2} , b_{2}]$ . Asuma que $a_{1} \leq b_{1}$ y $a_{2} \leq b_{2}$.
#    La entrada consiste de cuatro enteros $a_{1},b_{1},a_{2},b_{2}$ que representan los intervalos $[a_{1} , b_{1}]$ y $[a_{2} , b_{2}]$ . Asuma que $a_{1} \leq b_{1}$ y $a_{2} \leq b_{2}$.
#    La entrada consiste de cuatro enteros $a_{1},b_{1},a_{2},b_{2}$ que representan los intervalos $[a_{1} , b_{1}]$ y $[a_{2} , b_{2}]$ . Asuma que $a_{1} \leq b_{1}$ y $a_{2} \leq b_{2}$.
#   Salida
#    Imprima $[]$ si la intersección es vacía o $[x, y]$ si la intersección no esta vacía.
#    Imprima $[]$ si la intersección es vacía o $[x, y]$ si la intersección no esta vacía.
#    Imprima $[]$ si la intersección es vacía o $[x, y]$ si la intersección no esta vacía.
#   Ejemplo Entrada
#    20 30 10 40
#   Ejemplo Salida
#    [20,30]
#   Ayuda

a1,b1,a2,b2 = map(int, input().split())
print(f"[{max(a1,a2)},{min(b1,b2)}]" if max(a1,a2) <= min(b1,b2) else "[]")