# https://jv.umsa.bo/oj/problem.php?id=1461
#  Números Felices
#  Enviar
#  Estado
#  Descripción
#    Tome un número, elevé sus digitos al cuadrado, halle la suma y repita este proceso con el valor de la suma hasta obtener un dígito $1$.
#    Tome un número, elevé sus digitos al cuadrado, halle la suma y repita este proceso con el valor de la suma hasta obtener un dígito $1$.
#    Tome un número, elevé sus digitos al cuadrado, halle la suma y repita este proceso con el valor de la suma hasta obtener un dígito $1$.
#    Veamos el ejemplo siguiente:$7^2=49$$4^2+9^2=97$$9^2+7^2=130$$1^2+3^2=10$$1^2+0^2=1$
#    Veamos el ejemplo siguiente:$7^2=49$$4^2+9^2=97$$9^2+7^2=130$$1^2+3^2=10$$1^2+0^2=1$
#    Veamos el ejemplo siguiente:$7^2=49$$4^2+9^2=97$$9^2+7^2=130$$1^2+3^2=10$$1^2+0^2=1$
#    Cuando después de este proceso se llega a $1$ entonces el número que tomo se denomina número $Feliz$. Si el resultado no llega a $1$ se denomina $No$ $Feliz$.
#    Cuando después de este proceso se llega a $1$ entonces el número que tomo se denomina número $Feliz$. Si el resultado no llega a $1$ se denomina $No$ $Feliz$.
#    Cuando después de este proceso se llega a $1$ entonces el número que tomo se denomina número $Feliz$. Si el resultado no llega a $1$ se denomina $No$ $Feliz$.
#    Tome en cuenta que el numero 4 es triste.
#    Tome en cuenta que el numero 4 es triste.
#    Tome en cuenta que el numero 4 es triste.
#   Entrada
#    La entrada consiste de múltiples casos de prueba. La primera línea contiene el numero de casos de prueba. Cada caso de prueba consiste en una linea con un número $1 \leq n \leq 10^{14}$.
#    La entrada consiste de múltiples casos de prueba. La primera línea contiene el numero de casos de prueba. Cada caso de prueba consiste en una linea con un número $1 \leq n \leq 10^{14}$.
#    La entrada consiste de múltiples casos de prueba. La primera línea contiene el numero de casos de prueba. Cada caso de prueba consiste en una linea con un número $1 \leq n \leq 10^{14}$.
#   Salida
#    En la salida escriba en una linea $Feliz$ si el número es $feliz$ y $Triste$ si $no$ $es$ $feliz$.
#    En la salida escriba en una linea $Feliz$ si el número es $feliz$ y $Triste$ si $no$ $es$ $feliz$.
#    En la salida escriba en una linea $Feliz$ si el número es $feliz$ y $Triste$ si $no$ $es$ $feliz$.
#   Ejemplo Entrada
#    47416338
#   Ejemplo Salida
#    FelizTristeTristeFeliz
#   Ayuda

for _ in range(int(input())):
    n = input()
    fuc = lambda n: int(n)**2
    while n!="1" and n!="4":
        n = str(sum(list(map(fuc,n))))
    if n!="1":
        print("Triste")
    else:
        print("Feliz")