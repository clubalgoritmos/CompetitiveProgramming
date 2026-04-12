# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=14
## https://jv.umsa.bo/oj/problem.php?id=1109
#    Copiado al portapapeles
#  ATENCION MÉDICA
#  Enviar
#  Estado
#  Descripción
#    Su gobierno finalmente ha resuelto el problema de la atención sanitaria universal! Ahora todo el mundo, ricos o pobres, finalmente tendrán acceso al mismo nivel de atención médica. ¡Hurra!
#    Hay una complicación menor. Todos los hospitales del país se han condensado hacia abajo en un solo lugar, por lo que sólo puede hacerse cargo de una sola persona a la vez. Pero no te preocupes! También hay un plan en marcha para un sistema computarizado justo, eficiente para determinar quiénes serán admitidos. Usted está a cargo de la programación de este sistema.
#    A todos los ciudadanos de la nación se le asignará un número único, de 1 a P (donde P es la población actual). Ellos se pondrán en una cola, con 1 frente a 2, 2 frente a 3, y así sucesivamente. El hospital atenderá a los pacientes, uno por uno, en orden de esta cola. Una vez que un ciudadano ha sido admitido, se trasladarán inmediatamente desde el principio de la cola a la parte posterior.
#    Por supuesto, a veces surgen situaciones de emergencia; si acabas de ser atropellado por una arrolladora, no se puede esperar a que la mitad del país se realice un chequeo de rutina antes de que pueda ser tratado! Por lo tanto, para estas ocasiones (esperemos raras), un comando expedita se puede dar a mover una persona a la parte frontal de la cola. Orden relativo de todos los demás se mantendrá sin cambios.
#    Dada la secuencia de comandos de procesamiento y agilización, salida de la orden en el que los ciudadanos van a ser admitidos en el hospital.
#   Entrada
#    La entrada consiste de a lo sumo diez casos de prueba. Cada caso de prueba comienza con una línea que contiene P, la población de su país (1 ≤ P ≤ 1000000000), y C, el número de comandos de proceso (1 ≤ C ≤ 1,000).
#    Los próximos C líneas cada uno contienen un comando de la forma "N", indicando que el próximo ciudadano ha de ser admitido, o "E x", lo que indica que los ciudadanos x debe ser acelerada a la parte delantera de la cola.
#    El último caso de prueba es seguido por una línea que contiene dos ceros.
#   Salida
#    Para cada caso de prueba imprimir la serie de atención. Esto es seguido por una línea de salida para cada comando "N", lo que indica que los ciudadanos deben ser atendidos.
#   Ejemplo Entrada
#    3 6NNE 1NNN10 2NN00
#   Ejemplo Salida
#    Case 1:12132Case 2:12
#   Ayuda
#    Dado un vector en la posicion "i" actualizas la posicion en la cola de la persona "i".

