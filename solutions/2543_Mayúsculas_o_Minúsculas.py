# https://jv.umsa.bo/oj/problem.php?id=2543
#  Mayúsculas o Minúsculas
#  Enviar
#  Estado
#  Descripción
#    Marquito está muy molesto porque muchas personas en la Red mezclan letras mayúsculas y minúsculas en una sola palabra. Por eso decidió inventar una extensión para su navegador favorito, que cambiaría el registro de las letras de cada palabra para que solo fueran minúsculas o solo mayúsculas.
#    Por tanto, se debe cambiar las letras en cada palabra. Si hay más letras en mayúsculas, todas las letras pasan a mayúsculas. Si hay más letras en minúsculas, entonces todas las letras pasan a minúsculas.
#    Por ejemplo, si la palabra fuera Casa, el resultado del reemplado sería la palabra casa y para la palabra PaZ el resultado sería PAZ.
#    Si una palabra contiene la misma cantidad de letras mayúsculas y minúsculas, debe reemplazar todas las letras por minúsculas.
#    Por ejemplo, maTRIz debería ser reemplazado por matriz. Su tarea es usar el método dado en una palabra dada.
#   Entrada
#    La primera línea contiene una palabra S que consta de letras latinas mayúsculas y minúsculas y tiene una longitud entre 1 a 100 letras.
#   Salida
#    Imprime la palabra corregida que contemple los cambios solicitados. Si la palabra dada S tiene estrictamente más letras mayúsculas, escriba la palabra en el registro de mayúsculas, de lo contrario, en minúsculas.
#   Ejemplo Entrada
#    uniVERsiTaRiO
#   Ejemplo Salida
#    universitario
#   Ayuda

mayus, minus = 0, 0
a = input()
for x in a:
  if x.isupper():
    mayus+=1
  else:
    minus+=1
if mayus>minus:
  a = a.upper()
else:
  a = a.lower()
print(a)