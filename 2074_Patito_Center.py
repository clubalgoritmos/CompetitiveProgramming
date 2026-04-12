# https://jv.umsa.bo/oj/problem.php?cid=2824&pid=5
## https://jv.umsa.bo/oj/problem.php?id=2074
#  Patito Center
#  Estado
#  Descripción
#    PatitoCenter es un nuevo centro de comercio en la ciudad, por seguridad se registrar la hora de entrada y salida de cada persona. Si una persona estuvo en el establecimiento más de 3 horas se la sancionara.
#    Tu tarea es hacer un programa que calcule el tiempo que estubo una persona y verificar si se la sancionara ó no.
#    Las horas viene dadas desde las 0 horas hasta las 24 horas. Esto es despues de las 12 del medio dia vienen las 13.
#   Entrada
#    La entrada consiste de multiples casos de prueba, cada caso de prueba contiene dos lineas, en la primera linea se te dara la hora de ingreso y en la segunda linea  la hora de salida de cada persona en el siguiente formato $HH:MM:SS$.
#   Salida
#    Por cada caso de prueba imprima "Si", si la persona sera sancionada, en otro caso imprima "No".
#   Ejemplo Entrada
#    02:05:0905:05:0002:05:0905:05:10
#   Ejemplo Salida
#    NoSi
#   Ayuda

while True:
    try:
        a,b,c = map(int,input().split(":"))
        x,y,z = map(int,input().split(":"))
        if a>x:
            x+=24
        if b>y:
            y+=60
            x-=1
        if c>z:
            z+=60
            y-=1
        if (x-a)*3600+(y-b)*60+z-c>10800:
            print("Si")
        else:
            print("No")
    except EOFError:
        break
