# https://jv.umsa.bo/oj/problem.php?id=1717
#  El Juego de Reus
#  Enviar
#  Estado
#  Descripción
#    Reus es un chico muy curioso, a quien le gusta mucho la electrónica porque veía los proyectos en Protoboard de sus hermanos. Un día Reus se encontraba jugando con las cajas de sus hermanos y encontró una caja llena de pequeños dispositivos electrónicos hechos por ellos durante su vida Universitaria.
#    Reus es un chico muy curioso, a quien le gusta mucho la electrónica porque veía los proyectos en Protoboard de sus hermanos. Un día Reus se encontraba jugando con las cajas de sus hermanos y encontró una caja llena de pequeños dispositivos electrónicos hechos por ellos durante su vida Universitaria.
#    Reus es un chico muy curioso, a quien le gusta mucho la electrónica porque veía los proyectos en Protoboard de sus hermanos. Un día Reus se encontraba jugando con las cajas de sus hermanos y encontró una caja llena de pequeños dispositivos electrónicos hechos por ellos durante su vida Universitaria.
#    Dentro de esa caja había un curioso dispositivo nunca antes visto, el cual tenía una pantalla y dos botones. Inicialmente esta pantalla mostraba un número entero. Al pulsar los botones este va cambiando, despues de hacer varias pruebas Reus descubrió las funciones de cada uno de los botones. El primer botón agrega una unidad al número mostrado en la pantalla. El segundo botón invierte los dígitos del número mostrado en la pantalla, por ejemplo, invertir $123$ da como resultado $321$ e invertir $150$ da como resultado $51$ (teniendo en cuenta que se ignora los ceros a la izquierda).
#    Dentro de esa caja había un curioso dispositivo nunca antes visto, el cual tenía una pantalla y dos botones. Inicialmente esta pantalla mostraba un número entero. Al pulsar los botones este va cambiando, despues de hacer varias pruebas Reus descubrió las funciones de cada uno de los botones. El primer botón agrega una unidad al número mostrado en la pantalla. El segundo botón invierte los dígitos del número mostrado en la pantalla, por ejemplo, invertir $123$ da como resultado $321$ e invertir $150$ da como resultado $51$ (teniendo en cuenta que se ignora los ceros a la izquierda).
#    Dentro de esa caja había un curioso dispositivo nunca antes visto, el cual tenía una pantalla y dos botones. Inicialmente esta pantalla mostraba un número entero. Al pulsar los botones este va cambiando, despues de hacer varias pruebas Reus descubrió las funciones de cada uno de los botones. El primer botón agrega una unidad al número mostrado en la pantalla. El segundo botón invierte los dígitos del número mostrado en la pantalla, por ejemplo, invertir $123$ da como resultado $321$ e invertir $150$ da como resultado $51$ (teniendo en cuenta que se ignora los ceros a la izquierda).
#    Por lo cual sabiendo que tú eres bueno en programación, Reus pide de tu ayuda para calcular el mínimo número de pulsaciones de botones para que el número $A$ en pantalla cambie al número $B$.
#    Por lo cual sabiendo que tú eres bueno en programación, Reus pide de tu ayuda para calcular el mínimo número de pulsaciones de botones para que el número $A$ en pantalla cambie al número $B$.
#    Por lo cual sabiendo que tú eres bueno en programación, Reus pide de tu ayuda para calcular el mínimo número de pulsaciones de botones para que el número $A$ en pantalla cambie al número $B$.
#   Entrada
#    La entrada se inicia con un entero $T$ ($0 <  T \leq 500$), que indica el número de casos de prueba. Después de esto, la entrada consta de $T$ líneas, cada una de las cuales contiene dos unicos enteros $A$ y $B$, ($0 <  A  <  B  <10000$), $A$ es el numero inicial mostrado en pantalla y $B$ es el número final mostrado en la pantalla.
#    La entrada se inicia con un entero $T$ ($0 <  T \leq 500$), que indica el número de casos de prueba. Después de esto, la entrada consta de $T$ líneas, cada una de las cuales contiene dos unicos enteros $A$ y $B$, ($0 <  A  <  B  <10000$), $A$ es el numero inicial mostrado en pantalla y $B$ es el número final mostrado en la pantalla.
#    La entrada se inicia con un entero $T$ ($0 <  T \leq 500$), que indica el número de casos de prueba. Después de esto, la entrada consta de $T$ líneas, cada una de las cuales contiene dos unicos enteros $A$ y $B$, ($0 <  A  <  B  <10000$), $A$ es el numero inicial mostrado en pantalla y $B$ es el número final mostrado en la pantalla.
#   Salida
#    Para cada prueba, su programa debe mostrar un número entero $X$ que representa el mínimo numero de pulsaciones de botones.
#    Para cada prueba, su programa debe mostrar un número entero $X$ que representa el mínimo numero de pulsaciones de botones.
#    Para cada prueba, su programa debe mostrar un número entero $X$ que representa el mínimo numero de pulsaciones de botones.
#   Ejemplo Entrada
#    51 9100 301808 909133 2331 2
#   Ejemplo Salida
#    84331
#   Ayuda
#    Para el 5to Caso de prueba inicialmente la pantalla muestra un número $1$ (numero inicial $A$) pulsando el botón que agrega una unidad, como resultado la pantalla mostrara $2$ (el numero requerido $B$), solo se necesitó presionar una vez uno de los botones, entonces la respuesta es $1$.
#    Para el 5to Caso de prueba inicialmente la pantalla muestra un número $1$ (numero inicial $A$) pulsando el botón que agrega una unidad, como resultado la pantalla mostrara $2$ (el numero requerido $B$), solo se necesitó presionar una vez uno de los botones, entonces la respuesta es $1$.
#    Para el 5to Caso de prueba inicialmente la pantalla muestra un número $1$ (numero inicial $A$) pulsando el botón que agrega una unidad, como resultado la pantalla mostrara $2$ (el numero requerido $B$), solo se necesitó presionar una vez uno de los botones, entonces la respuesta es $1$.

#no funciona
for _ in range(int(input())):
    a,b = input().split()
    s=0
    for i, x in enumerate(zip(a,b)):
        ai,bi=map(int,x)
        u = abs(ai-bi)
        if u==0: u=1
        s+=u
    print(s)