# https://jv.umsa.bo/oj/problem.php?id=2536
#  Palabras demasiado largas
#  Enviar
#  Estado
#  Descripción
#    A veces, algunas palabras como "localización" o "internacionalización" son tan largas que escribirlas muchas veces en un mismo texto es bastante tedioso.
#    Consideremos a una palabra como demasiado larga, si su longitud es estrictamente superior a 10 caracteres. Todas las palabras demasiado largas deben reemplazarse con una abreviatura especial.
#    Esta abreviatura se la arma así: escribimos la primera y la última letra de una palabra y entre ellas escribimos el número de letras entre la primera y la última letra. Ese número está en sistema decimal y no contiene ceros a la izquierda.
#    Por lo tanto, "localización" se escribirá como "l10n", e "internacionalización» se escribirá como "i18n".
#    Se le pide realizar un programa para automatizar el proceso de cambiar las palabras por sus abreviaturas. En ese caso, todas las palabras demasiado largas deben ser reemplazadas por la abreviatura y las palabras que no son demasiado largas no deben sufrir ningún cambio.
#   Entrada
#    La primera línea contiene un número entero T (1≤T≤100). Cada una de las siguientes T líneas contiene una palabra. Todas las palabras consisten en letras latinas minúsculas y poseen longitudes de 1 a 100 caracteres.
#   Salida
#    Imprimir T líneas. Cada línea contiene el resultado de reemplazar las palabras de acuerdo a lo explicado.
#    Imprimir T líneas. Cada línea contiene el resultado de reemplazar las palabras de acuerdo a lo explicado.
#   Ejemplo Entrada
#    4umsalocalizaremosinternacionalizaremosesternocleidomastoideo
#   Ejemplo Salida
#    umsal11si19se20o
#   Ayuda

t = int(input())
for i in range(t):
 a = input()
 if len(a)>10:
  V=[x for x in a]
  a=f"{V[0]}{len(V)-2}{V[-1]}"
 print(a)