# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=167
## https://jv.umsa.bo/oj/problem.php?id=1962
#    Copiado al portapapeles
#  Un nuevo nivel
#  Enviar
#  Estado
#  Descripción
#    Gustavo estuvo esperando la nueva actualización de Mario Maker 2 , ya que una novedad fue que Mario ya tieneel traje de rana (también los demás personajes) , ya descargo la actualización ahora Gustavo va a jugar como Mario , al jugar un nuevo nivel vio que ese nivel tiene algo bien distinto a todos los niveles que a jugado, el nivel será en una cadena y en todo ese nivel estará con el traje de rana , al empezar el nivel se queda a la izquierda de la cadena $s$: $s= s_{1},s_{2}, ... s_{n}$ que consta de $n$ caracteres (para ser más precisos: Mario inicialmente se queda en la celda 0).
#    Cada carácter de la cadena $s$ es $'L'$ o $'R'$. Significa que si Mario se queda en la celda $i$-ésima y el carácter $i$-ésimo es $'L'$, Mario puede saltar solo hacia la izquierda. Si Mario se queda en la celda $i$-ésima y el carácter $i$-ésimo es $'R'$, Mario puede saltar solo hacia la derecha. Mario puede saltar solo hacia la derecha desde la celda $0$.
#    NOTA:Hay que tener en cuenta que Mario puede saltar a la misma celda dos veces y puede realizar tantos saltos como sea necesario.
#    Para completar el nivel Mario tiene que alcanzar la celda $(n + 1)$ -ésima. Mario elige algún valor entero positivo $d$ antes del primer salto (y no puede cambiarlo más tarde) y salta no más de $d$ celdas a la vez. Es decir. si el carácter $i$-ésimo es $'L'$, entonces Mario puede saltar a cualquier celda en un rango $[max (0, i-d); i − 1]$, y si el carácter $i$-ésimo es $'R'$, entonces Mario puede saltar a cualquier celda en un rango $[i + 1;min (n + 1 ,i + d)]$.
#    Como aún no se acostumbra al traje rana, Gustavo no quiere que Mario salte lejos, por lo que tu tarea es encontrar el valor mínimo posible de $d$ de modo que Mario pueda alcanzar la celda $(n + 1)$-ésima desde la celda $0$ si no puede saltar más de $d$ celdas a la vez. Se garantiza que siempre es posible alcanzar $(n + 1)$ desde $0$.
#    Se tiene que responder $t$ casos de prueba independientes.
#   Entrada
#    La primera línea de la entrada contiene un número entero $t$ $(1 ≤ t ≤ (10^{4})$: el número de casos de prueba.
#    Las siguientes $t$-líneas describen casos de prueba. El caso de prueba $i$-ésimo se describe como una cadena que consiste en al menos $1$ carácter y como máximo $(2*10^{5})$ caracteres que solo consistirán en $'L'$ y $'R'$.
#   Salida
#    Para cada caso de prueba, imprima la respuesta que será el valor mínimo posible de $d$ de modo que Mario pueda alcanzar la celda $n + 1$ desde la celda 0 si salta no más de $d$ celdas.
#   Ejemplo Entrada
#    6LRLRRLLLLLRRRRRLLLLLLR
#   Ejemplo Salida
#    323171
#   Ayuda
#    La imagen hace referencia al primer caso de prueba
#    En el segundo caso de prueba del ejemplo, Mario solo puede saltar directamente de $0$ a $n + 1$.
#    En el tercer caso de prueba del ejemplo, Mario puede elegir $d = 3$, saltar a la celda $3$ desde la celda $0$ y luego a la celda $4$ desde la celda $3$.
#    En el cuarto caso de prueba del ejemplo, Mario puede elegir $d = 1$ y saltar $5$ veces hacia la derecha.
#    En el quinto caso de prueba del ejemplo, Mario solo puede saltar directamente de $0$ a $n + 1$.
#    En el sexto caso de prueba del ejemplo, Mario puede elegir $d = 1$ y saltar $2$ veces hacia la derecha.

