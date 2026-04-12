# https://jv.umsa.bo/oj/problem.php?id=1637
#  Llave
#  Enviar
#  Estado
#  Descripción
#    Bienvenido a la Olimpiada Cientifica Estudiantil en Informatica, aca tenemos a Pipo, quien te recibe para que puedas poner a prueba tus habilidades en este primer concurso.
#    Bienvenido a la Olimpiada Cientifica Estudiantil en Informatica, aca tenemos a Pipo, quien te recibe para que puedas poner a prueba tus habilidades en este primer concurso.
#    Bienvenido a la Olimpiada Cientifica Estudiantil en Informatica, aca tenemos a Pipo, quien te recibe para que puedas poner a prueba tus habilidades en este primer concurso.
#    Puede que veamos a Pipo muy amenudo por aca, es mas acompañemoslo en su dia a dia en su preparacion para las olimpiadas.
#    Puede que veamos a Pipo muy amenudo por aca, es mas acompañemoslo en su dia a dia en su preparacion para las olimpiadas.
#    Puede que veamos a Pipo muy amenudo por aca, es mas acompañemoslo en su dia a dia en su preparacion para las olimpiadas.
#    Pipo esta de camino a casa despues del colegio y él sabe que siempre pierde mucho tiempo buscando la llave correcta para entrar a su casa, ya que recientemente cambio de cerradura, el recuerda que tiene la caja de la nueva cerradura en su mochila asi que la revisa y ve lo siguiente:
#    Pipo esta de camino a casa despues del colegio y él sabe que siempre pierde mucho tiempo buscando la llave correcta para entrar a su casa, ya que recientemente cambio de cerradura, el recuerda que tiene la caja de la nueva cerradura en su mochila asi que la revisa y ve lo siguiente:
#    Pipo esta de camino a casa despues del colegio y él sabe que siempre pierde mucho tiempo buscando la llave correcta para entrar a su casa, ya que recientemente cambio de cerradura, el recuerda que tiene la caja de la nueva cerradura en su mochila asi que la revisa y ve lo siguiente:
#    En la imagen observa que la cerradura completa tiene una altura de $5$ y que esta hecha para ser abierta con una llave de $3$ dientes.  En cada orificio donde va un diente de la llave esta marcado cuanto mide este, el tiene sus llaves y las mide la altura de cada diente, con estos datos quiere saber si esta llave es la que abrira su puerta.
#    En la imagen observa que la cerradura completa tiene una altura de $5$ y que esta hecha para ser abierta con una llave de $3$ dientes.  En cada orificio donde va un diente de la llave esta marcado cuanto mide este, el tiene sus llaves y las mide la altura de cada diente, con estos datos quiere saber si esta llave es la que abrira su puerta.
#    En la imagen observa que la cerradura completa tiene una altura de $5$ y que esta hecha para ser abierta con una llave de $3$ dientes.  En cada orificio donde va un diente de la llave esta marcado cuanto mide este, el tiene sus llaves y las mide la altura de cada diente, con estos datos quiere saber si esta llave es la que abrira su puerta.
#   Entrada
#    La entrada consiste de dos lineas, la primera linea tiene $3$ numeros enteros $a, b, c $ $(0 \leq a, b, c \leq 5)$ que representa las alturas anotadas en la caja de la cerradura. La segunda linea contiene $3$ numeros enteros $x, y, z$ $(0 \leq x, y, z \leq 5)$ la altura de cada diente de la llave a probar.
#    La entrada consiste de dos lineas, la primera linea tiene $3$ numeros enteros $a, b, c $ $(0 \leq a, b, c \leq 5)$ que representa las alturas anotadas en la caja de la cerradura. La segunda linea contiene $3$ numeros enteros $x, y, z$ $(0 \leq x, y, z \leq 5)$ la altura de cada diente de la llave a probar.
#    La entrada consiste de dos lineas, la primera linea tiene $3$ numeros enteros $a, b, c $ $(0 \leq a, b, c \leq 5)$ que representa las alturas anotadas en la caja de la cerradura. La segunda linea contiene $3$ numeros enteros $x, y, z$ $(0 \leq x, y, z \leq 5)$ la altura de cada diente de la llave a probar.
#   Salida
#    La salida consiste en una sola linea: "Esta es la llave" si es que esa es la llave que abrira su puerta e "Intenta con otra" si es que no lo hara.(Sin comillas)
#    La salida consiste en una sola linea: "Esta es la llave" si es que esa es la llave que abrira su puerta e "Intenta con otra" si es que no lo hara.(Sin comillas)
#    La salida consiste en una sola linea: "Esta es la llave" si es que esa es la llave que abrira su puerta e "Intenta con otra" si es que no lo hara.(Sin comillas)
#   Ejemplo Entrada
#    2 3 13 2 4
#   Ejemplo Salida
#    Esta es la llave
#   Ayuda

A = list(map(int,input().split()))
B = list(map(int,input().split()))
c = 5
if all([(a+b) == c for a,b in zip(A,B)]):
    print("Esta es la llave")
else:
    print("Intenta con otra")