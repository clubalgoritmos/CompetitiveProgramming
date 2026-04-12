# https://jv.umsa.bo/oj/problem.php?id=1269
#  Fracciones
#  Enviar
#  Estado
#  Descripción
#    Se dice que dos fracciones son iguales si el numerador y el denominador de las dos fracciones son iguales, por ejemplo $33/15$ es igual a $11/5$ ya que simplifícando $33/15$ tenemos $11/5$ que es igual a la segunda fracción.Dado dos fracciones determinar si estos son iguales.
#    Se dice que dos fracciones son iguales si el numerador y el denominador de las dos fracciones son iguales, por ejemplo $33/15$ es igual a $11/5$ ya que simplifícando $33/15$ tenemos $11/5$ que es igual a la segunda fracción.Dado dos fracciones determinar si estos son iguales.
#    Se dice que dos fracciones son iguales si el numerador y el denominador de las dos fracciones son iguales, por ejemplo $33/15$ es igual a $11/5$ ya que simplifícando $33/15$ tenemos $11/5$ que es igual a la segunda fracción.Dado dos fracciones determinar si estos son iguales.
#   Entrada
#    La entrada viene dada por varios casos en una misma entrada. Cada linea de la entrada representa un caso.
#    La entrada viene dada por varios casos en una misma entrada. Cada linea de la entrada representa un caso.
#    La entrada viene dada por varios casos en una misma entrada. Cada linea de la entrada representa un caso.
#    Cada caso consiste en cuatro números enteros los dos primeros $n_1$ y $d_1$ son los valores de la primera fracción siendo $n_1$ el numerador y $d_1$ el denominador, siguen $n_2$ y $d_2$ siendo los valores de la segunda fracción donde $n_2$ es el numerador y $d_2$ el denominador ($1 <= n_1, n_2, d_1, d_2 <= 1000$) la entrada termina cuando $n_1 = d_1 = n_2 = d_2 = 0$. Es decir, los ultimo 4 numeros de la entrada seran 0's y este caso representa el fin de los datos de entrada y no debe ser procesado.
#    Cada caso consiste en cuatro números enteros los dos primeros $n_1$ y $d_1$ son los valores de la primera fracción siendo $n_1$ el numerador y $d_1$ el denominador, siguen $n_2$ y $d_2$ siendo los valores de la segunda fracción donde $n_2$ es el numerador y $d_2$ el denominador ($1 <= n_1, n_2, d_1, d_2 <= 1000$) la entrada termina cuando $n_1 = d_1 = n_2 = d_2 = 0$. Es decir, los ultimo 4 numeros de la entrada seran 0's y este caso representa el fin de los datos de entrada y no debe ser procesado.
#    Cada caso consiste en cuatro números enteros los dos primeros $n_1$ y $d_1$ son los valores de la primera fracción siendo $n_1$ el numerador y $d_1$ el denominador, siguen $n_2$ y $d_2$ siendo los valores de la segunda fracción donde $n_2$ es el numerador y $d_2$ el denominador ($1 <= n_1, n_2, d_1, d_2 <= 1000$) la entrada termina cuando $n_1 = d_1 = n_2 = d_2 = 0$. Es decir, los ultimo 4 numeros de la entrada seran 0's y este caso representa el fin de los datos de entrada y no debe ser procesado.
#   Salida
#    Imprimir '=' si las fracciones son iguales caso contrario imprimir '!=', sin incluir las comillas.
#    Imprimir '=' si las fracciones son iguales caso contrario imprimir '!=', sin incluir las comillas.
#    Imprimir '=' si las fracciones son iguales caso contrario imprimir '!=', sin incluir las comillas.
#   Ejemplo Entrada
#    33 15 11 57 8 11 20 0 0 0
#   Ejemplo Salida
#    =!=
#   Ayuda

while True:
        a,b,c,d = map(int,input().split())
        if (a==0 and b==0 and c==0 and d==0):
            break
        if (a/b==c/d):
            print("=")
            continue
        print("!=")