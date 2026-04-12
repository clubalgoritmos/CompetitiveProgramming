# https://jv.umsa.bo/oj/problem.php?id=1520
#  Sucesion de Farey
#  Enviar
#  Estado
#  Descripción
#    LaSucesión de Fareyes una de esas curiosidades matemáticas a la vez llenas de belleza y fáciles de entender que casualmente descubrió un no-matemático, John Farey, en 1928.
#    La
#    La
#  Sucesión de Farey
#    Sucesión de Farey
#    Sucesión de Farey
#    es una de esas curiosidades matemáticas a la vez llenas de belleza y fáciles de entender que casualmente descubrió un no-matemático, John Farey, en 1928.
#    es una de esas curiosidades matemáticas a la vez llenas de belleza y fáciles de entender que casualmente descubrió un no-matemático, John Farey, en 1928.
#    La idea es tomar un número natural (ej. n =3 ) y empiezar a definir la serie $Farey(3)$ como una serie de fracciones que tienen como numerador y denominador los números entre $1$ y $n$. En el caso de $Farey(3)$ escribiendo todas estas fracciones serían
#    La idea es tomar un número natural (ej. n =3 ) y empiezar a definir la serie $Farey(3)$ como una serie de fracciones que tienen como numerador y denominador los números entre $1$ y $n$. En el caso de $Farey(3)$ escribiendo todas estas fracciones serían
#    La idea es tomar un número natural (ej. n =3 ) y empiezar a definir la serie $Farey(3)$ como una serie de fracciones que tienen como numerador y denominador los números entre $1$ y $n$. En el caso de $Farey(3)$ escribiendo todas estas fracciones serían
#    $\frac{1}{1},\frac{1}{2},\frac{1}{3},\frac{2}{1},\frac{2}{2},\frac{2}{3},\frac{3}{1},\frac{3}{2},\frac{3}{3}$
#    $\frac{1}{1},\frac{1}{2},\frac{1}{3},\frac{2}{1},\frac{2}{2},\frac{2}{3},\frac{3}{1},\frac{3}{2},\frac{3}{3}$
#    $\frac{1}{1},\frac{1}{2},\frac{1}{3},\frac{2}{1},\frac{2}{2},\frac{2}{3},\frac{3}{1},\frac{3}{2},\frac{3}{3}$
#    Esta serie tiene propiedades muy interesantes, pero antes de ello. ¿Podras mostrar la sucesion descrita arriba?
#    Esta serie tiene propiedades muy interesantes, pero antes de ello. ¿Podras mostrar la sucesion descrita arriba?
#    Esta serie tiene propiedades muy interesantes, pero antes de ello. ¿Podras mostrar la sucesion descrita arriba?
#   Entrada
#    La entrada consiste en un numero entero $1<=n<=100$ que representa el numero para el que quieres calcular $Farey(n)$
#    La entrada consiste en un numero entero $1<=n<=100$ que representa el numero para el que quieres calcular $Farey(n)$
#    La entrada consiste en un numero entero $1<=n<=100$ que representa el numero para el que quieres calcular $Farey(n)$
#   Salida
#    La salida consiste en la serie descrita anteriormente, la impresion sera de un termino por linea.
#    La salida consiste en la serie descrita anteriormente, la impresion sera de un termino por linea.
#    La salida consiste en la serie descrita anteriormente, la impresion sera de un termino por linea.
#   Ejemplo Entrada
#    3
#   Ejemplo Salida
#    1/11/21/32/12/22/33/13/23/3
#   Ayuda
#    $OK$

N = int(input())
for i in range(1,N+1):
    for j in range(1,N+1):
        print(f"{i}/{j}")