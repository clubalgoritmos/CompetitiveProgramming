# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=75
## https://jv.umsa.bo/oj/problem.php?id=1392
#    Copiado al portapapeles
#  Ositos Barrigones Intergalácticos
#  Enviar
#  Estado
#  Descripción
#    Los Ositos Barrigones Intergalácticos (OBI) crearon una red comercial construyendo una ruta, bi-direccional, entre todos los pares de planetas de la galaxia. Todos eran felices realizando sus negocios hasta que los Insectos Corrupto-Planetario-Comerciantes (ICPC) llegaron a corromper las rutas comerciales. Se dice que una ruta es corrupta si los ICPC se apropiaron de esta.Los ICPC sólo pueden recorrer rutas corruptas y los OBI por rutas no corruptas.Se dice que un subconjunto de planetas es seguro comercialmente si existe una ruta comercial no corrupta entre cada par de estos planetas. Un subconjunto de un solo planeta es siempre seguro comercialmente y se lo debe tomar encuenta.
#    Tu trabajo es reponder a las preguntas de los ositos en la configuración actual de la red comercial. Se realizan operaciones de tipo pregunta y actualización en la red comercial.a: Pregunta. ¿Cuántos distintos subconjuntos de planetas no vacíos son seguros comercialmente en este momento?b: Actualización. Los ICPC Corrompen una ruta de la red comercial que conecta el planeta U con el V.
#    Se garantiza que los ICPC corrompen rutas sólo si esta les permite un nuevo camino entre dos planetas entre los cuales antes no podían moverse. En otras palabras, jamás corremperán la ruta de U hacia V si ya existía un camino de rutas corruptas entre estos planetas.
#   Entrada
#    La primer línea de entrada T contiene el número de casos a considerar.A continuación se tiene un entero N y Q que representa el número de planetas y el número de operaciones respectivamente.Le siguen Q líneas. Una línea es del tipo a si el primer carácter de la línea es una letra a y además le siguen dos enteros U y V representando que en ese momento la arista que los unía ha sido corrompida. Una línea del tipo b significa que se le pregunta cuántos subconjuntos de planetas distintos que existen tal que son seguros comercialmente.
#    1<=T<=101<=U,V<=N1<=N<=10001<=Q<=2000
#   Salida
#    Por cada línea del tipo b imprimir la cantidad de distintos subconjuntos de planetas no vacíos que son seguros comercialmente en ese momento módulo 1000000007.
#   Ejemplo Entrada
#    23 4ba 1 2a 1 3b10 10ba 4 7a 5 8a 5 9a 5 10ba 2 4a 2 5a 1 3b
#   Ejemplo Salida
#    741023431257
#   Ayuda

