# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=104
## https://jv.umsa.bo/oj/problem.php?id=1556
#    Copiado al portapapeles
#  Recaudando Fondos
#  Enviar
#  Estado
#  Descripción
#    En un pequeño pueblo todas las casas se han construido en círculo alrededor de una plaza.Le han asignado la tarea de recaudar donativos para la restauración.Cada residente del pueblo, ubicado al contorno de la plaza, está deseoso de donar una cierta cantidad de dinero. Sin embargo nadie está de acuerdo en contribuir a un fondo en el cual sus vecinos que se encuentra en la puerta contigua, hayan contribuido. Los vecinos que viven en la puerta contigua siempre se listan consecutivamente. La última casa también es vecina de la primera.Halle el máximo dinero que puede ser recaudado.Por ejemplo, dada la secuencia de donativos $10, 3, 2, 5, 7, 8$, el valor máximo se obtiene con $10+2+7$. Es mejor $10+5+8$, sin embargo el $8$ y $10$ corresponden a vecinos. El valor máximo que se puede recaudar es 19.
#   Entrada
#    La entrada consiste de varios casos de prueba. La primera línea contiene un número ($2 \leq N \leq 40$) que representa el número de personas. Luego siguen ($0 \leq d_i \leq 1000$) valores separados por espacio representando el valor que cada vecino puede donar. Los casos de prueba terminan cuando no hay más datos.
#   Salida
#    Por cada caso de prueba escriba en una línea la máxima donación que puede obtener.
#   Ejemplo Entrada
#    610 3 2 5 7 8211 1577 7 7 7 7 7 7101 2 3 4 5 1 2 3 4 5 4094 40 49 65 21 21 106 80 92 81 6794 61 6 237 12 72 74 29 95 265 35 47 1 61 397 52 72 37 51 1 81 45 435 7 36 57 86 81 72
#   Ejemplo Salida
#    191521162926
#   Ayuda

