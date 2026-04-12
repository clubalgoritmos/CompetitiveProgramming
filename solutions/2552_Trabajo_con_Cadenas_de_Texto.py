# https://jv.umsa.bo/oj/problem.php?id=2552
#  Trabajo con Cadenas de Texto
#  Enviar
#  Estado
#  Descripción
#    Dianita empezó a asistir a clases de programación. En la primera lección, su tarea consistía en escribir un programa sencillo. El programa debe hacer lo siguiente: lee una cadena de texto, formada por letras mayúsculas y minúsculas.
#    El programa debe realizar las siguientes modificaciones:
#    1. Elimina todas las vocales,
#    2. Inserta un carácter "." antes de cada consonante,
#    3. Sustituye todas las consonantes mayúsculas por las correspondientes minúsculas.
#    4. Las vocales son: "A", "E", "I", "O", "U", y el resto son consonantes.
#    La entrada del programa es exactamente una cadena, debe devolver como resultado una sola cadena, resultante después de que el programa procese la cadena inicial.
#    Ayuda a Dianita a enfrentarse a esta sencilla tarea.
#   Entrada
#    La primera línea representa la cadena de entrada del programa de Dianita. Esta cadena sólo consta de letras mayúsculas y minúsculas y su longitud va de 1 a 100 caracteres.
#   Salida
#    Imprime la cadena resultante.
#   Ejemplo Entrada
#    aBAcAba
#   Ejemplo Salida
#    .b.c.b
#   Ayuda

A = [a for a in input().lower()]
for a in A:
  if not a in "aeiou":
    print(f".{a}", end='')