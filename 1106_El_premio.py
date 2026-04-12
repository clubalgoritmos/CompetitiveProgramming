# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=12
## https://jv.umsa.bo/oj/problem.php?id=1106
#    Copiado al portapapeles
#  El premio
#  Enviar
#  Estado
#  Descripción
#    Las máquinas tragaperras fueron las primeras máquinas de apuestas automáticas. El jugador introduce en ellas una determinada cantidad de dinero, que apuesta esperando conseguir alguna combinación ganadora en los rodillos. La máquina proporciona un pequeño tiempo de juego y eventualmente un premio en efectivo.
#    Aunque hoy en día la mayoría son digitales, las antiguas máquinas tragaperras eran mecánicas, tras el rotundo éxito del invento los casinos se afanaron por regular la cantidad de premios que las máquinas debían proporcionar. Desde entonces se fuerza así a una cantidad mínima de reembolsos; el secreto mejor guardado es naturalmente cuando los darán. A veces, ni siquiera el fabricante lo sabe, ya que actualmente generan las respuestas al azar. Sin embargo algunos modelos mecánicos antiguos generaban premios cíclicamente. Esos ciclos se guardaban celosamente: un jugador que conociera el ciclo de una máquina sabría cuál era el mejor momento para empezar a echar monedas y cuando parar.
#   Entrada
#    La entrada está compuesta por múltiples casos de prueba. Cada uno comienza con la longitud del ciclo 1<=L<=10⁶, seguido de su descripción.
#    El ciclo está compuesto por una secuencia de L números, indicando el beneficio neto del jugador en cada partida. Así un valor de -1 indica que el jugador echa una moneda y la pierde, al no conseguir premio. Un valor de 1<=P<10⁵ indica que el jugador echa una moneda y a cambio la máquina le premia con P+1 monedas. La entrada termina con un 0.
#   Salida
#    Para cada caso de prueba se escribirá la mayor cantidad de monedas que se pueden conseguir con la máquina de una sola vez, teniendo en cuenta que se pueden jugar tantas partidas consecutivas como se desee. Se puede elegir a partir de qué momento empezar a echar monedas y en qué momento parar, pero no está permitido “saltarse” jugadas una vez que se ha empezado a jugar.
#    Ten en cuenta que tras lelgar al final, la máquina repite el ciclo. Se garantiza que la máquina siempre da al menos un premio, pero, al mismo tiempo, siempre gana dinero a largo plazo. Es decir si una persona juega  el ciclo completo de la máquina, saldrá perdiendo.
#   Ejemplo Entrada
#    9-1 -1 2 -1 3 -1 -1 -1 -19-1 3 -1 -1 -1 -1 -1 -1 29-1 -1 2 -1 -1 -1 3 -1 -10
#   Ejemplo Salida
#    443
#   Ayuda
#    El problema pide allar una subsequencia del vector tal que la suma sea maxima, podemos ir acumulando la sumas de mientras sea mayor a 0, si la suma se vuelve negativa entonces no nos conviene tomar esa subsecuencia

