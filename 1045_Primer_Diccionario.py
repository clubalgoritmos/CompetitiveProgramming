# https://jv.umsa.bo/oj/problem.php?id=1045
#  Primer Diccionario
#  Enviar
#  Estado
#  Descripción
#    Andy, de 8 años, tiene un sueño - él quiere producir su propio diccionario. Esta no es una tarea fácil para él, ya que el número de palabras que él conoce, no son suficientes. En lugar de pensar en todas las palabras por sí mismo, tiene una idea brillante. De su estante de libros el escoge uno de sus libros de historia favoritos, del que copiará todas las palabras distintas. Tomando en cuenta el orden alfabético de las palabras, así lo realiza! Por supuesto, esto realmente le lleva mucho tiempo y aquí es donde un programa de computadora le sería útil.
#    Se le pide que escriba un programa que muestre todas las diferentes palabras del texto de entrada. En este problema, una palabra se define como una secuencia consecutiva de alfabetos, en mayúscula y/o minúscula. Las palabras con una sola 1 letra también deben ser consideradas. Por otra parte, el programa no debe diferenciar a las MaYúScUlAs de las MiNúScUlAs. Por ejemplo, las palabras como "Manzana", "manzana" o "MANZANA" se consideran iguales.
#    NOTA: En este problema se usara el alfabeto inglés para los casos de prueba.
#   Entrada
#    El archivo de entrada es un texto que no tiene más de 5000 líneas. Una línea de entrada tiene como máximo 200 caracteres. La entrada finaliza con el EOF (End Of File).
#   Salida
#    El resultado debe mostrar a todas las palabras diferentes que aparece en el texto de entrada, uno en cada línea. Las palabras deben estar en minúsculas, ordenadas en orden alfabético. Puede estar seguro de que el número de palabras distintas del texto, no superará a 5000.
#   Ejemplo Entrada
#    A man was pulled over for driving too fast, even though he thought he was driving just fine.Officer: You were speeding.Man: No, I was not.Officer: Yes, you were. I am giving you a ticket.Man: But I was not speeding.Officer: Tell that to the judge! (The officer gives man the ticket.)Man: Would I get another ticket if I called you a jerk?Officer: Yes, you would.Man: What if I just thought that you were?Officer: I can not give you a ticket for what you think.Man: Fine, I think you are a jerk!
#   Ejemplo Salida
#    aamanotherarebutcalledcandrivingevenfastfineforgetgivegivesgivingheiifjerkjudgejustmannonotofficeroverpulledspeedingtellthatthethinkthoughthoughttickettotoowaswerewhatwouldyesyou
#   Ayuda
#    Estructuras de Datos

import re
dics = set()
while True:
    try:
        S = input().split()
        for i in S:
            cleaned_word = re.sub(r'[^a-z]', '', i.lower())
            dics.add(cleaned_word)
    except EOFError:
        break
for a in sorted(dics):
    print(a)