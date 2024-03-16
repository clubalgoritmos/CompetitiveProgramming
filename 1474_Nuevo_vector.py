# https://jv.umsa.bo/oj/problem.php?id=1474
#  Nuevo vector
#  Enviar
#  Estado
#  Descripción
#    Se te dará dos vectores de tamaño N y a continuación se te dará N instrucciones, estas instrucciones te ayudarán a crear un tercer vector estás son:
#    Se te dará dos vectores de tamaño N y a continuación se te dará N instrucciones, estas instrucciones te ayudarán a crear un tercer vector estás son:
#    Se te dará dos vectores de tamaño N y a continuación se te dará N instrucciones, estas instrucciones te ayudarán a crear un tercer vector estás son:
#    $+$ (sumar el i-esimo elemento del primer con el i'esimo elemento del segundo vector)
#    $+$ (sumar el i-esimo elemento del primer con el i'esimo elemento del segundo vector)
#    $*$ (multiplicar el i-esimo elemento del primer vector con el i-esimo elemento del segundo vector)
#    $*$ (multiplicar el i-esimo elemento del primer vector con el i-esimo elemento del segundo vector)
#    $>$ (elegir el mayor entre el i-esimo elemento del primer vector y el i-esimo elemento del segundo vector)
#    $>$ (elegir el mayor entre el i-esimo elemento del primer vector y el i-esimo elemento del segundo vector)
#    $<$ (elegir el menor entre el i-esimo elemento del primer vector y el i-esimo elemento del segundo vector)
#    $<$ (elegir el menor entre el i-esimo elemento del primer vector y el i-esimo elemento del segundo vector)
#   Entrada
#    Inicialmente se te dará un número $N$ ($1 \leq N \leq 10000$) el número de elementos del vector, el la segunda línea se te dará $N$ números los elementos del primer vector, en la tercera línea se te dará $N$ números los elementos del segundo vector, Y finalmente $N$ líneas las operaciones para crear el nuevo vector que siempre serán ( $+,* , >, <$ )
#    Inicialmente se te dará un número $N$ ($1 \leq N \leq 10000$) el número de elementos del vector, el la segunda línea se te dará $N$ números los elementos del primer vector, en la tercera línea se te dará $N$ números los elementos del segundo vector, Y finalmente $N$ líneas las operaciones para crear el nuevo vector que siempre serán ( $+,* , >, <$ )
#    Inicialmente se te dará un número $N$ ($1 \leq N \leq 10000$) el número de elementos del vector, el la segunda línea se te dará $N$ números los elementos del primer vector, en la tercera línea se te dará $N$ números los elementos del segundo vector, Y finalmente $N$ líneas las operaciones para crear el nuevo vector que siempre serán ( $+,* , >, <$ )
#   Salida
#    Imprimir los $N$ elementos del nuevo vector uno por línea.
#    Imprimir los $N$ elementos del nuevo vector uno por línea.
#    Imprimir los $N$ elementos del nuevo vector uno por línea.
#   Ejemplo Entrada
#    4 1 2 3 44 3 2 1+*><
#   Ejemplo Salida
#    5631
#   Ayuda
#    Para el lenguaje Java, se recomienda usar para la lectura de las operaciones:
#    Para el lenguaje Java, se recomienda usar para la lectura de las operaciones:
#    Para el lenguaje Java, se recomienda usar para la lectura de las operaciones:
#    Scanner cin=new Scanner(System.in);
#    Scanner cin=new Scanner(System.in);
#    Scanner cin=new Scanner(System.in);
#    String s=cin.next();
#    String s=cin.next();
#    String s=cin.next();
#    char c=s.charAt(0);
#    char c=s.charAt(0);
#    char c=s.charAt(0);
#    Ahora con c se puede hacer operaciones (comparaciones) como:
#    Ahora con c se puede hacer operaciones (comparaciones) como:
#    Ahora con c se puede hacer operaciones (comparaciones) como:
#    if(c== '+')
#    if(c== '+')
#    if(c== '+')
#    if(c=='*')
#    if(c=='*')
#    if(c=='*')

N = int(input())
A = [int(x) for x in input().rstrip().split(" ")]
B = [int(x) for x in input().rstrip().split(" ")]
for i in range(N):
  S = input()
  if S=="+":
    A[i]+=B[i]
  elif S=="*":
    A[i]*=B[i]
  elif S==">":
    A[i] = A[i] if A[i]>B[i] else B[i]
  else:
    A[i] = A[i] if A[i]<B[i] else B[i]
del B
for i in A:
  print(i)