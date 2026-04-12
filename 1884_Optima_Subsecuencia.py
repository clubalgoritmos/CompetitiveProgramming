# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=157
## https://jv.umsa.bo/oj/problem.php?id=1884
#    Copiado al portapapeles
#  Optima Subsecuencia
#  Enviar
#  Estado
#  Descripción
#    Te dan una secuencia de enteros $A = [a_1, a_2, …, a_n]$ de longitud n. Una subsecuencia es obtenida eliminando cero o mas elementos de la subsecuencia.
#    Por ejemplo de la secuencia $A = [11, 20, 11, 33, 11, 20, 11]$ entonces $[11, 20, 11, 33, 11, 20, 11], [1, 20, 11, 33, 11, 20], [11, 11, 11, 11], [20], [33, 20]$ son subsecuencias de A y $[40], [33, 33], [33, 20, 20], [20, 20, 11, 11]$ no son subsecuencias de A.
#    Te dan un K $(1 \leq k \leq n)$.
#    La subsecuencia es llamada optima si tienen una longitud k y la suma de los elementos es lo maximo posible de todas las subsecuencias de de tamaño k, si existen varias subsecuencias maximas hallar el minimo lexicograficamente.
#    Dado una secuencia A, k y M imprimir el m'esimo elemento de la subsecuencia con suma maxima y menor lexicograficamente con tamaño k.
#   Entrada
#    La primera linea contiene un entero n $(1 \leq n \leq 100)$ la longitud de la secuencia A.
#    La segunda linea contiene n elementos de la secuencia A: $a_1, a_2, …, a_n (1 \leq a_i \leq 10^9)$.
#    La tercera linea contiene un entero q $(1 \leq q \leq 100)$ el numero de preguntas.
#    La siguiente m lineas contienen pares de enteros k y m $(1 \leq k \leq n, 1 \leq m \leq k)$.
#   Salida
#    Imprimir q enteros $r_1,r_2, …, r_m (1 \leq r_j \leq 10^9) $ una por linea que sera el m'esimo elemento de la subsecuencia con suma maxima (si existe varias la menor subsecuencia lexicograficamente) y con longitud k.
#   Ejemplo Entrada
#    310 20 1061 12 12 23 13 23 3
#   Ejemplo Salida
#    201020102010
#   Ayuda

