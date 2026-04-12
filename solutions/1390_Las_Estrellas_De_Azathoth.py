# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=73
## https://jv.umsa.bo/oj/problem.php?id=1390
#    Copiado al portapapeles
#  Las Estrellas De Azathoth
#  Enviar
#  Estado
#  Descripción
#    Azathoth, el primer motor del caos, la antítesis de la creación, el necio sultán de los demonios, el que roe, gime y babea en el centro del vacío final o más conocido como el centro del universo; es una fanático de los grafos.Es por esto que encomendó a Nyarlathotep (Dios Heraldo de Azathot), una importante misión: Crear un grafo no direccionado con estrellas de una galaxia. Nyarlathotep debe crear una arista espectral entre cada una de las estrellas de esa galaxia exceptuando una lista de aristas prohibidas. Una tarea de tal magnitud requiere mucho esfuerzo, incluso para un Dios. Se sabe que el esfuerzo de crear una arista entre dos estrellas es igual al cuadrado de la distancia euclideana (en años luz) entre el centro de masa de cada una de estas. Se requiere saber cual es el esfuerzo total para crear el grafo.
#   Entrada
#    Entrada:La primera linea contiene dos enteros N y M, el número de estrellas a considerar y el número de aristas prohibidas. Las siguientes N líneas contienen las coordenadas enteras en años luz Xi, Yi, Zi, 1<=i<=N, del centro de masa de la estrella iésima, Ei. Las siguientes M líneas contienen dos enteros Uj y Vj que representan a una de las aristas prohibidas por Azathoth, es decir que no debe haber una arista de la estrella número Uj y la estrella número Vj.1<=N<=1000000<=M<=100000-1000<=Xi,Yi,Zi<=10001<=Uj<Vj<=N
#   Salida
#    Imprimir el esfuerzo total para crear el grafo descrito en el enunciado.
#   Ejemplo Entrada
#    3 10 0 01 1 12 2 21 3
#   Ejemplo Salida
#    6
#   Ayuda

