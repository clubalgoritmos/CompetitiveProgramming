# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=183
## https://jv.umsa.bo/oj/problem.php?id=2196
#    Copiado al portapapeles
#  Cuaderno infinito
#  Enviar
#  Estado
#  Descripción
#    Un día cuando ibas caminando por la calle y encontraste un cuaderno muy raro, ya que tenia un numero infinito de paginas. Cuando lo revisaste notaste que tiene una regla escrita, el cual dice: “Tienes que escribir nombres en este cuaderno durante n días consecutivos, durante el i-ésimo día tienes que escribir exactamente ai nombres”. Tú muy confundido simplemente decidiste seguir esta regla (aún no sabes el por qué).
#    Impresionado por ello decidiste buscar una estrategia para escribir los nombres en el cuaderno. Calculaste que solo puedes escribir m nombres como máximo en cada pagina. Escribirás nombres en la pagina actual siempre que no excedas el límite del número de nombres en esta página, cuando alcances el limite de nombres, solo pasas la página. Ten en cuenta que siempre pasas la página cuando terminas, no importa si es el último día o no. Si después de algún día la página actual todavía puede contener al menos un nombre, durante el día siguiente continuará escribiendo los nombres de la página actual. Sigues buscando datos para tu estrategia, así que ahora te hiciste una pregunta ¿cuántas veces daré vuelta a la página durante cada día?. Estás interesado en el número de páginas que pasarás cada día de 1 a n.
#   Entrada
#    La primera línea de entrada contiene dos números enteros n y m(1≤n≤2⋅105 , 1≤m≤109); el número de dias que escribiras nombres en el cuaderno y el número máximo de nombres que se pueden escribir en cada página del cuaderno.
#    La segunda línea de entrada contiene n enteros separados por un espacio a1, a2, a3, ... , an (1≤ai≤109), donde cada ai significa el número de nombres que escribiras en el cuaderno durante el i-esimo día.
#   Salida
#    Imprime en una sola línea exactamente n enteros t1, t2, t3, ... tn, separados por un espacio, donde ti es el número de veces que pasarás la página durante el i-esimo día.
#   Ejemplo Entrada
#    3 53 7 9
#   Ejemplo Salida
#    0 2 1
#   Ayuda
#    EJEMPLO ENTRADA 2                 EJEMPLO SALIDA 2
#    4 20                             0 0 1 1
#    10 9 19 2
#    Nota:
#    La salida debe tener un espacio al final, vease los ejemplos.

