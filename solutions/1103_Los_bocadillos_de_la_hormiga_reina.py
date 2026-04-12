# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=10
## https://jv.umsa.bo/oj/problem.php?id=1103
#    Copiado al portapapeles
#  Los bocadillos de la hormiga reina
#  Enviar
#  Estado
#  Descripción
#    Ser hormiga reina no es fácil. No vamos a enumerar aquí todos y cada uno de los problemas que tiene que solucionar a lo largo del día; baste con uno de ellos a modo de ejemplo.
#    Cuando llega la hora de la merienda tiene que ponerse a hacer bocadillos para toda su prole. Migas de pan y de corteza no le faltan, pero cada uno de los trozos de corteza tiene un tamaño distinto, así que conseguir dos trozos iguales para poder poner en la base del bocadillo y en la tapa es una tarea complicada. Afortunadamente sus hijas son bastante inocentes y si la tapa inferior del bocadillo está formada por distintos trozos de corteza no se darán cuenta, siempre y cuanto la corteza superior cubra exactamente todos los trozos de corteza de la capa inferior.
#    Como no tiene tiempo que perder ha decidido simplificar las cosas. Ha puesto en fila todos los trozos de corteza que hay en el hormiguero (¡son muchos!). Para hacer el primer bocadillo simplemente busca desde la izquierda de la hilera hacia el final un cacho de corteza que sirva de tapa de todos los trocitos que quedan a la derecha. ¿Podrá hacer un bocadillo? ¿Con qué tapa?
#   Entrada
#    La entrada está compuesta por distintos casos de prueba, cada uno de ellos ocupando dos líneas. La primera línea indica el número de cortezas que hay en el hormiguero (como mucho 100000); la segunda línea contiene los tamaños de cada uno de los trocitos, según han quedado dispuestos para hacer los bocadillos. Todos los tamaños serán números positivos y la suma de todos ellos no será superior a 10⁹.
#    .
#    La entrada termina con un caso de prueba sin cortezas, que no debe procesarse.
#   Salida
#    Para cada caso de prueba se indicará si se podrá hacer un bocadillo utilizando el mecanismo simplificado de la reina explicado más arriba que tenga una tapa con la misma longitud que la base. En caso negativo se indicaráNO. En caso afirmativo se escribiráSIseguido de la posición que ocupa en la hilera original la tapa superior del bocadillo (empezando a contar desde el 1).
#    Si hay varios posibles bocadillos, se montará el más grande posible; después de todo las hormigas son pequeñas, pero están hambrientas.
#   Ejemplo Entrada
#    103 5 8 25 12 15 5 7 1 276 2 3 1 1 8 1289 45 5 20 10 1 6 30
#   Ejemplo Salida
#    SI 6NOSI 2
#   Ayuda
#    Acumular un vector B de derecha a izquierda la suma del vector V, luego pregunta si V[i] >= B[i + 1]

