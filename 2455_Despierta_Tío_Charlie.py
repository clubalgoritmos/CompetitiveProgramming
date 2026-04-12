# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=213
## https://jv.umsa.bo/oj/problem.php?id=2455
#    Copiado al portapapeles
#  Despierta Tío Charlie
#  Enviar
#  Estado
#  Descripción
#    El Tío charlie ha pasado todo el día bailando en la entrada universitaria. Ahora tiene que dormir por lo menos "a" minutos para sentirse como nuevo.Tío Charlie solo puede despertarse al escuchar el sonido de su alarma de su Xiomi. Así que acaba de quedarse dormido y su primera alarma suena en “b” minutos.Cada vez que Tío Charlie se despierta, decide si quiere dormir un rato más o no. Si ha dormido menos de “a” minutos en total, configura la alarma para que suene en “c” minutos después de que se restablezca y tarda “d” minutos en volver a dormirse. De lo contrario, se levanta de la cama y continúa con el día. Si la alarma suena mientras Tío Charlie se está quedando dormido, entonces reinicia su alarma para que suene en otros “c” minutos e intenta volver a dormirse durante “d” minutos. Solo quiere saber cuándo se levantará de su cama o informar que nunca sucederá.Ejemplo
#    a = el tiempo que quiere dormir
#    b = el tiempo en sonar la primera alarma
#    c = el tiempo antes de que suene las siguientes alarmas
#    d = el tiempo que tarda en dormirse
#    a = 10; b =3; c = 6; d = 4;En el primer caso de prueba, Tío Charlie se despierta después de 3 minutos. Solo descansó 3 minutos de los 10 minutos que necesitaba. Entonces, después de eso, configura su alarma para que suene en 6 minutos y pasa 4 minutos durmiendo. Así, descansa 2 minutos más, totalizando 3+2=5 minutos de sueño. Luego repite el procedimiento tres veces más y termina con 11 minutos de sueño. Finalmente, se levanta de su cama. Pasó 3 minutos antes de la primera alarma y luego reinició su alarma cuatro veces. La respuesta es 3+4⋅6=27.
#   Entrada
#    La primera línea contiene un número entero $t$ ($1$ $\leq$ $t$ $\leq$ 1000 ) — el número de casos de prueba. La única línea de cada caso de prueba contiene cuatro números enteros a,b,c,d ($1$ $\leq$ $a$,$b$,$c$,$d$ $\leq$ $10^{9}$) — el tiempo que tiene que dormir Tío Charlie para sentirse renovado, el tiempo antes de que suene la primera alarma, el tiempo antes de que suene cada alarma sucesiva y el tiempo que dedica Policarpo a quedarse dormido.
#   Salida
#    Para cada caso de prueba, imprima un número entero. Si Tío Charlie nunca se levanta de su cama, imprima -1. De lo contrario, imprime el tiempo que tarda Tío Charlie en levantarse de la cama.
#   Ejemplo Entrada
#    710 3 6 411 3 6 45 9 4 106 5 2 31 1 1 13947465 47342 338129 123123234123843 13 361451236 361451000
#   Ejemplo Salida
#    27279-116471793358578060125049
#   Ayuda
#    El segundo ejemplo es casi como el primero, pero necesita 11 minutos de sueño en lugar de 10. Sin embargo, eso no cambia nada porque de todos modos obtiene 11 minutos con estos parámetros de alarma.En la tercera prueba, se despierta lo suficientemente descansado después de la primera alarma. Por lo tanto, la respuesta es b=9En el cuarto caso de prueba se despierta después de 5minutos. Desafortunadamente, sigue reiniciando su alarma infinitamente y no puede descansar ni un solo minuto :v

