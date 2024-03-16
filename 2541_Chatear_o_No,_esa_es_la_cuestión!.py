# https://jv.umsa.bo/oj/problem.php?id=2541
#  Chatear o No, esa es la cuestión!
#  Enviar
#  Estado
#  Descripción
#    En esos días, muchos chicos usan fotos de chicas guapas como avatares en los foros. Por lo tanto, es bastante difícil saber el género de un usuario a primera vista. El año pasado, nuestro héroe Joaquín, fue a un foro y tuvo una agradable charla con una belleza (eso pensó). Después de eso hablaron muy a menudo y con el tiempo se convirtieron en pareja en la red.
#    ¡Pero ayer, quedaron en encontrarse en persona, y tenía todas las ganas de verla a "ella" en el mundo real, y descubrió que "ella" es en realidad un hombre muy fuerte! Nuestro héroe Joaquín, está muy triste y demasiado cansado para volver a amar ahora. Así que se le ocurrió una forma de reconocer los géneros de los usuarios por sus nombres de usuario.
#    Este es su método: si el número de caracteres distintos en el nombre de usuario es impar, entonces es un hombre, de lo contrario, es una mujer.
#    Se te proporciona la cadena que denota el nombre de usuario, y ahora ayuda a nuestro héroe a determinar el género de este usuario por su método.
#   Entrada
#    La primera línea contiene una cadena no vacía, que contiene solo letras minúsculas que corresponde al nombre de usuario. Esta cadena contiene como máximo 100 letras.
#   Salida
#    Si es una mujer según el método de nuestro héroe Joaquín, imprime "CHATEA CON ELLA!" (sin las comillas), de lo contrario, escribe "IGNORARLO!" (sin las comillas).
#   Ejemplo Entrada
#    wjmzbmr
#   Ejemplo Salida
#    CHATEA CON ELLA!
#   Ayuda

c = set(input())
if len(c)%2==0:
  print("CHATEA CON ELLA!")
else:
  print("IGNORARLO!")