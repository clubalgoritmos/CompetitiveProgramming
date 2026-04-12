# https://jv.umsa.bo/oj/problem.php?id=1043
#  Crafting in Minecraft
#  Enviar
#  Estado
#  Descripción
#    Minecraft es un juego desarrollado por Notch en Java utilizando OpenGL. Cuando juegas Minecraft, estás en un mundo hecho de cubitos, y los puedes tomar y guardar en tu inventario. Con los cubitos de tu inventario, puedes construir cosas colocando los cubitos en donde quieras (cosas como casas, estatuas, monumentos, hay quienes, incluso construyen réplicas de ciudades!). Pero también puedes hacer items con los cubitos de tu inventario (puedes hacer espadas, picotas, hachas, palas, mesas, camas, hechizos, estufas, armaduras, etc...), como se muestra en la figura.Lo más divertido de Minecraft es que puedes entrar a cuevas, y buscar oro, hierro y diamantes (que son muy difíciles de encontrar), pero para recolectar todo este mineral (y también para romper la piedra que lo cubre) necesitas muchas picotas, porque si usas mucho una picota, se te rompe! y tienes que usar una nueva para continuar minando.Para construir una picota, necesitas 2 palitos y 3 piedras (como en la imagen).
#    Estás por entrar a una cueva, y necesitas saber cuántas picotas puedes construir para planificar correctamente tu aventura. Si tienes x palitos y y piedras...¿Cuántas picotas puedes construir?¿Te sobra material?¿Cuánto material te sobra?
#   Entrada
#    Primero, se te dará un número $ 0 \leq n \leq 20$, indicando la cantidad de casos de entrada.Se te darán dos números enteros: $0 \leq r \leq 10^6$ y $0 \leq p \leq 10^6$, indicando: la cantidad de cubos de piedra que tienes, y la cantidad de palitos que tienes, respectivamente.
#   Salida
#    Debes imprimir dos números enteros en una sola línea: $a$ y $b$, indicando: la cantidad de picotas que puedes construir y la cantidad de material que te sobra.
#   Ejemplo Entrada
#    310 109 61 1
#   Ejemplo Salida
#    3 53 00 2
#   Ayuda
#    Considerar la cantidad de piedras necesarias es mayor a los palitos necesarios para hacer una picota

for i in range(int(input())):
    pie,pal = map(int,input().split())
    pic = min(pie//3, pal//2)
    print(pic, pie+pal-pic*5)