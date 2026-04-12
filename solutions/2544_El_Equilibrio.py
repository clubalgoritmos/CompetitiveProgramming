# https://jv.umsa.bo/oj/problem.php?id=2544
#  El Equilibrio
#  Enviar
#  Estado
#  Descripción
#    Jimmy es estudiante en la universidad y es además un fanático del fútbol.
#    Un domingo, Jimmy se la paso viendo los partidos de futbol de España, de Italia, de Inglaterra y finalmente de los que se juegan en Bolivia, pero se olvidó de hacer sus tareas.
#    Al día siguiente, su querido profesor se enojó mucho y decidió darle una lección a Jimmy. Le dio una tarea aparentemente fácil: se le da un cuerpo inactivo en el espacio y las fuerzas que lo afectan. El cuerpo puede ser considerado como un punto material con coordenadas (x=0; y=0; z=0). Y Jimmy debe responder si el cuerpo está en equilibrio. "Pan comido" — pensó Jimmy, ya que solo necesitamos verificar si la suma de todos los vectores es igual a 0.
#    Ayuda a Jimy escribiendo un programa que determine si un cuerpo está inactivo o se mueve según los vectores de fuerzas dados.
#   Entrada
#    La primera línea contiene un número entero positivo n (1≤n≤100), luego siguen n líneas que contienen tres números enteros cada una: la coordenada xi, la coordenada yi y la coordenada zi del vector de fuerza, aplicado al cuerpo (-100≤xi,yi,zi≤100).
#   Salida
#    Escriba la palabra "SI" si el cuerpo está en equilibrio, o la palabra "NO" si no lo está.
#   Ejemplo Entrada
#    33 -1 7-5 2 -42 -1 -3
#   Ejemplo Salida
#    SI
#   Ayuda

x,y,z = 0,0,0
for _ in range(int(input())):
  a,b,c = (int(i) for i in input().split(' '))
  x,y,z = x+a,y+b,z+c
if x+y+z == 0:
  print('SI')
else:
  print('NO')