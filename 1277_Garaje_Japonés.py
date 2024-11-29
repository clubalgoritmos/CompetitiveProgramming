# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=49
## https://jv.umsa.bo/oj/problem.php?id=1277
#    Copiado al portapapeles
#  Garaje Japonés
#  Enviar
#  Estado
#  Descripción
#    En las ciudades de Japón se puede ver garajes de todo tipo imaginable. Desafortunadamente, durante su visita a Japón, el autor de este problema era incapaz de comprender completamente cómo trabajan. Así que aquí vamos a utilizar dos modelos simplificados: Q-garajes y S-garajes.
#    Un Q-garaje almacena los coches en colas ( el "primero en entrar, primero en salir"). Sólo después de que todos los vehículos que entren hayan sido almacenados en las colas de un Q-garaje, los coches puede comenzar a salir de las colas. Un S-garaje es idéntico a un Q-garaje, salvo que usa pilas ("último en entrar, primero en salir") en lugar de colas.
#    Supongamos que n coches, numerados de 1,. . . , N, llegan a un garaje en el orden I1,... , In, y deben salir en el orden O1,. . . , On. ¿Cuál es el número mínimo de colas para un Q-garaje?, ¿Cuál es el número mínimo de pilas para un S-garaje?
#    Por ejemplo, suponga n = 8, que el orden de entrada es 6 8 5 2 1 7 3 4, y que el orden de salida debe ser 2 5 4 7 1 6 8 3. En este caso, un Q-garaje necesita 4 colas, mientras que un S-garaje, únicamente necesita 3 pilas. Estas son las posibles (no únicas) soluciones:
#    Versión original:https://www.jutge.org/problems/P33845_en
#    Versión original:
#    https://www.jutge.org/problems/P33845_en
#   Entrada
#    La entrada consiste de varios casos de prueba. donde cada caso de prueba comienza con 1<=n<=105 seguidos por la permutación I1,. . . , In, luego O1,. . . , On. La entrada termina con n=0.
#   Salida
#    Para cada caso de prueba escriba en la salida el minimo de colas Q y pilas tipo S que se requieren.
#   Ejemplo Entrada
#    81 2 3 4 5 6 7 84 3 8 6 5 1 2 7 11195 2 9 6 1 7 4 3 82 6 7 3 5 9 1 4 8101 2 3 4 5 6 7 8 9 1010 9 8 7 6 5 4 3 2 10
#   Ejemplo Salida
#    4 31 12 510 1
#   Ayuda

