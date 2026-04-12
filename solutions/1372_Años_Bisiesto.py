# https://jv.umsa.bo/oj/problem.php?id=1372
#  Años Bisiesto
#  Enviar
#  Estado
#  Descripción
#    Los años bisiestos tienen $366$ dias y son aquellos que son multiplos de $4$ y no terminan con dos ceros o aquellos que despues de quitar los dos ceros del final son divisibles por $4$ (divisibles por $400$). Por ejemplo $1800$, y $1900$ no son años bisiestos, sin embargo el año $2000$ si lo fue.
#    Los años bisiestos tienen $366$ dias y son aquellos que son multiplos de $4$ y no terminan con dos ceros o aquellos que despues de quitar los dos ceros del final son divisibles por $4$ (divisibles por $400$). Por ejemplo $1800$, y $1900$ no son años bisiestos, sin embargo el año $2000$ si lo fue.
#    Los años bisiestos tienen $366$ dias y son aquellos que son multiplos de $4$ y no terminan con dos ceros o aquellos que despues de quitar los dos ceros del final son divisibles por $4$ (divisibles por $400$). Por ejemplo $1800$, y $1900$ no son años bisiestos, sin embargo el año $2000$ si lo fue.
#   Entrada
#    La entrada consiste de numeros naturales en el rango de $1800$ y $9999$.
#    La entrada consiste de numeros naturales en el rango de $1800$ y $9999$.
#    La entrada consiste de numeros naturales en el rango de $1800$ y $9999$.
#   Salida
#    En la salida escriba una palabra que diga "$si$" si fue biciesto y "$no$" si no fue bisiesto, sin comillas.
#    En la salida escriba una palabra que diga "$si$" si fue biciesto y "$no$" si no fue bisiesto, sin comillas.
#    En la salida escriba una palabra que diga "$si$" si fue biciesto y "$no$" si no fue bisiesto, sin comillas.
#   Ejemplo Entrada
#    1800
#   Ejemplo Salida
#    no
#   Ayuda
#    Ejemplo de entrada 11800Ejemplo de salida 1noEjemplo de entrada 22000Ejemplo de salida 2si
#    Ejemplo de entrada 11800Ejemplo de salida 1noEjemplo de entrada 22000Ejemplo de salida 2si
#    Ejemplo de entrada 11800Ejemplo de salida 1noEjemplo de entrada 22000Ejemplo de salida 2si

N = int(input())
#ver si N es un año bisiesto
if N%4==0 and (N%100!=0 or N%400==0):
    print("si")
else:
    print("no")