# https://jv.umsa.bo/oj/problem.php?id=1265
#  Monedas Britanicas
#  Enviar
#  Estado
#  Descripción
#    Antes del año 1971, Gran Bretaña utilizó un sistema de monedas que se remonta a la época de Carlomagno. Las tres principales unidades de la moneda británica fueron el penique, el chelín, y la libra. Se tenían las siguientes equivalencias, existen 12 peniques en un chelín y 20 chelines en una libra. Dado una cantidad de monedas peniques se quiere convertir esta cantidad en libras, chelines y peniques para esto seprocede de la siguiente manera, la primera conversión sera de monedas de peniques a su equivalencia máxima en libras, y luego convertir la mayor cantidad de peniques restantes como sea posible hacia su equivalente en chelines y el restante se mantiene en peniques.Devuelve estos datos en un vector de enteros con tres elementos que contiene la equivalencia en monedas de libras, monedas de chelines, y el número de monedas de un penique, en ese orden.
#   Entrada
#    La entrada de datos consiste en un entero A que representa la cantidad de monedas disponible en peniques, el número está definido como se indica $0 \leq A \leq 10000$.
#    En la entrada hay un solo dato. Se muestran multiples datos como ejemplo
#   Salida
#    Escriba para cada caso de prueba tres números, los cuales son el equivalente en libras, chelín y peniques.
#   Ejemplo Entrada
#    53306409110000
#   Ejemplo Salida
#    (2, 4, 5)(0, 0, 0)(0, 0, 6)(17, 0, 11)(41, 13, 4)
#   Ayuda
#    Para resolver el problema debe colocar su solución dentro de;

import sys
for i in sys.stdin:
  i = int(i)
  l = i//(20*12)
  c = (i%(20*12))//12
  p = ((i%(20*12))%12)
  print((l,c,p))