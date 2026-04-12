# https://jv.umsa.bo/oj/problem.php?id=1081
#  La décima plaga
#  Enviar
#  Estado
#  Descripción
#    Ya paso la pascua, época en la que los creyentes lo festejan recordando historias interesantes de eventos bíblicos, mientras los cristianos recuerdan la Pasión de Cristo, los judíos celebran la fiesta de los panes sin levadura en conmemoración de la liberación del pueblo judío de los látigos de Egipto. El libro Éxodo de antiguo testamento nos relata la historia de Moisés y su lucha instruida por Dios para liberar a su pueblo.
#    Ya paso la pascua, época en la que los creyentes lo festejan recordando historias interesantes de eventos bíblicos, mientras los cristianos recuerdan la Pasión de Cristo, los judíos celebran la fiesta de los panes sin levadura en conmemoración de la liberación del pueblo judío de los látigos de Egipto. El libro Éxodo de antiguo testamento nos relata la historia de Moisés y su lucha instruida por Dios para liberar a su pueblo.
#    Dios había enviado a Moisés para exigir al Faraón de Egipto que liberase a su pueblo, pero este tan solo se burlaba de Moisés. Dios enviaba plaga tras plaga para castigar al pueblo de Egipto mientras que Moisés advertía al Faraón del gran dolor que el Dios de Israel iba a provocar a Egipto, al mismo tiempo el corazón del Faraón se endurecía más y más. Finalmente la última plaga que Moisés anuncia termina convenciendo al Faraón.
#    Dios había enviado a Moisés para exigir al Faraón de Egipto que liberase a su pueblo, pero este tan solo se burlaba de Moisés. Dios enviaba plaga tras plaga para castigar al pueblo de Egipto mientras que Moisés advertía al Faraón del gran dolor que el Dios de Israel iba a provocar a Egipto, al mismo tiempo el corazón del Faraón se endurecía más y más. Finalmente la última plaga que Moisés anuncia termina convenciendo al Faraón.
#    Jehová ha dicho: A la media noche yo pasare por en medio de Egipto y morirá todo primogénito en la tierra de Egipto desde el primogénito del Faraón hasta el primogénito del empleado del molino.
#    Jehová ha dicho: A la media noche yo pasare por en medio de Egipto y morirá todo primogénito en la tierra de Egipto desde el primogénito del Faraón hasta el primogénito del empleado del molino.
#    La familia de números que se encontraban en Egipto, se asustaron al ver una niebla tenebrosa, que le denominaron “ángel de la muerte”; este ángel tenebroso aparecía en cualquier lugar y se expandía, matando al primer número de cada familia que se encontraba alrededor,
#    La familia de números que se encontraban en Egipto, se asustaron al ver una niebla tenebrosa, que le denominaron “ángel de la muerte”; este ángel tenebroso aparecía en cualquier lugar y se expandía, matando al primer número de cada familia que se encontraba alrededor,
#    Tomemos en cuenta la secuencia de números:
#    Tomemos en cuenta la secuencia de números:
#    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17
#    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17
#    Si el ángel de la muerte se posa en la posición del número 8 matara al número 7 para eso el ángel deberá avanzar 1 posición
#    Si el ángel de la muerte se posa en la posición del número 8 matara al número 7 para eso el ángel deberá avanzar 1 posición
#    Si el ángel de la muerte aparece en la posición del número 16, matara a 17 para eso avanzara una posición
#    Si el ángel de la muerte aparece en la posición del número 16, matara a 17 para eso avanzara una posición
#    Y finalmente si se posa en la posición del número 3 matara a 3 sin necesidad de avanzar posiciones
#    Y finalmente si se posa en la posición del número 3 matara a 3 sin necesidad de avanzar posiciones
#    En resumen si el ángel de la muerte se posa en una posición X, matara al primogénito más cercano ya sea que este a la izquierda o a la derecha.
#    En resumen si el ángel de la muerte se posa en una posición X, matara al primogénito más cercano ya sea que este a la izquierda o a la derecha.
#    Debes escribir un programa que: dada la posición X mostrar el número que representa las posiciones que la muerte debe recorrer para llegar al primogénito más cercano.
#    Debes escribir un programa que: dada la posición X mostrar el número que representa las posiciones que la muerte debe recorrer para llegar al primogénito más cercano.
#   Entrada
#    En la primera línea de entrada hay un número n (1<=n<=100000) que representa el número de casos de prueba, a continuación hay n líneas de entrada, cada línea tiene un entero x (1<x<100000) que representa la posición donde aparece el ángel de la muerte.
#    En la primera línea de entrada hay un número n (1<=n<=100000) que representa el número de casos de prueba, a continuación hay n líneas de entrada, cada línea tiene un entero x (1<x<100000) que representa la posición donde aparece el ángel de la muerte.
#   Salida
#    Por cada uno de los casos de entrada, deberá imprimir en una línea, la cantidad de posiciones que la muerte debe recorrer para llegar al primogénito más cercano.
#    Por cada uno de los casos de entrada, deberá imprimir en una línea, la cantidad de posiciones que la muerte debe recorrer para llegar al primogénito más cercano.
#   Ejemplo Entrada
#    78152221293463
#   Ejemplo Salida
#    1212032
#   Ayuda
#    No se consideran los números 0 y 1. Tenga cuidado con el tiempo de ejecución
#    No se consideran los números 0 y 1. Tenga cuidado con el tiempo de ejecución

for _ in range(int(input())):
  def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

  def primo_mas_cercano(n):
      c = 0
      while True:   
          if es_primo(n+c) or es_primo(n-c):
            break
          c+=1
      return c

  print(primo_mas_cercano(int(input())))