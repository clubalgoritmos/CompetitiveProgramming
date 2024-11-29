# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=32
## https://jv.umsa.bo/oj/problem.php?id=1182
#    Copiado al portapapeles
#  WiFi
#  Enviar
#  Estado
#  Descripción
#    Tu victoria en la liga coreana, es algo poco creíble y es posible que aún no lo hayas hecho. Asíque cambiemos de juego pero no de desarrollador. Decides jugar a World of Warcraft, despuésde horas de gritar en Dalaran (ciudad ficticia dentro del juego), consigues una banda parapoder combatir contra Kil’Jaeden (Jefe en Meseta de la Fuente del Sol, mazmorra del juego)y estas listo para ser invocado frente al poderoso jefe. Pero... Mensaje salvaje aparece....Labatería esta apunto de agotarse. Por favor conecte su cargador. Así que decides correr a través de tu casa, hasta el enchufe más cercano pero muchos de tusenchufes tienen conectados routers. Los routers tienen una potencia determinada y esta vadecreciendo a medida que te alejas de él. Al jugar online el ping (Tiempo de respuesta con elservidor) es un factor muy importante, el ping ideal es 100ms que es el que tienes al estar sobrela posición de un router. Por ejemplo si estas parado en un router de potencia 2, si te alejas un cuadro de él, tu ping incrementara a 200ms y si te alejas otro mas sufriras una desconeccion. No se puede caminar sobre espacios que no sean tocados por algún router.
#    Así que tu tarea se complica debes llegar al enchufe libre mas cercano y evitar que tu ping subade x ms (como asumimos que no eres un robot, te puedes mover en las 8 direcciones).
#    Puede que nunca hayas tenido el ping deseado por lo que ya no te queda hacer nada.
#   Entrada
#    La entrada consiste en T (1 ≤ T ≤ 5) casos de prueba, cada caso comienza con cinco enteros n(1 ≤ n ≤ 100), m (1 ≤ m ≤ 100), x (100 ≤ x ≤ 10000), a (1 ≤ a ≤ n) y b (1 ≤ b ≤ m), donde ny m son las dimensiones de la matriz que representa tu casa, x la cantidad máxima de ping que quieres tener en todo el recorrido por tu casa y a , b que son tu posicióninicial. Seguidamentese te darán n lineas, cada una con m caracteres que podr ́an ser . si es una posición libre de lacasa o una E si en este lugar hay un enchufe. Después se te dará un entero r (1 ≤ r ≤ 100) que es la cantidad de routers que tienes en tu casa, seguidos por r lineas con la información delos router, cada linea tendrá tres enteros i (1 ≤ i ≤ n), j (1 ≤ j ≤ m), y k (1 ≤ k ≤ 50), queson la posición del router y su potencia. Se garantiza que los routers siempre estar ́an sobre unenchufe y que a lo sumo habrá un router por enchufe.
#   Salida
#    La salida consta de una sola linea. SI si existe un camino desde tu posición hasta el enchufelibre mas cercano cumpliendo que en todo momento por el camino tu ping no suba de x ms.NO si no existe tal camino.
#   Ejemplo Entrada
#    212 14 600 2 6............................................................................E.............................................................................E....E........26 7 612 6 612 14 300 2 6............................................................................E.............................................................................E....E........26 7 612 6 6
#   Ejemplo Salida
#    SINO
#   Ayuda

