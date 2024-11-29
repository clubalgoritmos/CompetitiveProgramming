# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=85
## https://jv.umsa.bo/oj/problem.php?id=1419
#    Copiado al portapapeles
#  No hay agua!
#  Enviar
#  Estado
#  Descripción
#    Se acabó el agua en La Paz, por lo que cuando llueve hay que sacar los baldes y tratar de recolectar un poco de agua. Gauss tuvo una brillante idea, creó un sistema de reconocimiento de gotitas de lluvia y un robot flash que recolecta agua con un balde. El sistema puede detectar una gota de agua en el aire y el robot, gracias a la "speed force", se puede mover muy rápidamente de forma casi instantanea (sin embargo no lo suficiente como para estar en dos lugares al mismo tiempo ni crear o romper líneas de tiempo) a la locación para recolectar esa gotita en su balde. Bien, el único problema que le queda a Gauss es saber de que ancho tiene que ser el balde de tal forma que sea capaz de recoger todas las gotas de agua. Gauss está muy ocupado, tiene muchos examenes y expocisiones por lo que debe estar jugando Overthrow. Tu misión es leer los datos de las gotitas y verificar cuál es el menor ancho, mayor igual uno, que necesita tener el balde para poder recolectar todas las gotas de agua.
#    El sistema está en beta, así que sólo reconoce un plano en 2D, por lo que por cada gota de agua se te dará un punto (x,y,t), que significa que el sitema detectó la gota con coordenadas (x,y) en el tiempo t en segundos. Las gotas caen perfectamente en forma vertical, un centrimetro cada segundo, es decir que la gota que estaba en (x,y) en un tiempo t estará en (x,y-1) en el tiempo t+1. El suelo está bajo la recta y=0, y la altura a la que está el balde es 0. Considere que las gotas de agua son infinitamente pequeñas de tal forma que cualquier gota que esté en el punto (x,0) y cumpla a<=x<=b, siendo a el extremo izquierdo del balde y b el extremo derecho, será recibida sin problemas por el balde. Gauss pensó en todo, así que no debes preocuparte por que el balde llega a desbordarse.
#   Entrada
#    La primera línea de entrada contiene un número natural n, 1<=n<=100000 que representa la cantidad de gotas de que caerán. Las siguiente n líneas tienen tres números enteros cada una, x, y, t, 1<=x,y,t<=100000 que representan la información de una gota (x,y,t).
#   Salida
#    Imprimir el mínimo ancho del balde mayor igual a uno tal que, si se lo equipa al robot, sea capaz de recibir todas las gotas de agua.
#   Ejemplo Entrada
#    41 1 25 2 12 1 13 1 1
#   Ejemplo Salida
#    4
#   Ayuda

