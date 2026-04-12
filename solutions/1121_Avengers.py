# https://jv.umsa.bo/oj/problem.php?id=1121
## https://jv.umsa.bo/oj/problem.php?id=1121
#  Avengers
#  Enviar
#  Estado
#  Descripción
#    Todos conocemos a nuestros superheroes favoritos, los avengers, aunque despues de su ultima pelicula, han estado teniendo algunos problemas.
#    Todos conocemos a nuestros superheroes favoritos, los avengers, aunque despues de su ultima pelicula, han estado teniendo algunos problemas.
#    Todos conocemos a nuestros superheroes favoritos, los avengers, aunque despues de su ultima pelicula, han estado teniendo algunos problemas.
#    Se ha estado discutiendo quienes son los miembros mas valiosos, para entregarles unos certificados de reconocimiento, hay muchos criterios que se pueden usar al momento de decidir, algunos quisieran que sean medidos por su fuerza, agilidad, inteligencia, cantidad de misiones a las que participaron y muchos criterios mas.
#    Se ha estado discutiendo quienes son los miembros mas valiosos, para entregarles unos certificados de reconocimiento, hay muchos criterios que se pueden usar al momento de decidir, algunos quisieran que sean medidos por su fuerza, agilidad, inteligencia, cantidad de misiones a las que participaron y muchos criterios mas.
#    Se ha estado discutiendo quienes son los miembros mas valiosos, para entregarles unos certificados de reconocimiento, hay muchos criterios que se pueden usar al momento de decidir, algunos quisieran que sean medidos por su fuerza, agilidad, inteligencia, cantidad de misiones a las que participaron y muchos criterios mas.
#    La comision encargada de la decision, propuso que no existen miembros mas valiosos que otros, por lo que todos los avengers son igualmente valiosos y seran ordenados alfabeticamente, asi que preguntan a Nick Fury la cantidad de  premios que entregaran.
#    La comision encargada de la decision, propuso que no existen miembros mas valiosos que otros, por lo que todos los avengers son igualmente valiosos y seran ordenados alfabeticamente, asi que preguntan a Nick Fury la cantidad de  premios que entregaran.
#    La comision encargada de la decision, propuso que no existen miembros mas valiosos que otros, por lo que todos los avengers son igualmente valiosos y seran ordenados alfabeticamente, asi que preguntan a Nick Fury la cantidad de  premios que entregaran.
#    Nick Fury podria decidir que todos tengan un premio, pero ha estado teniendo problemas con el Avenger $A$, por lo que dara solamente premio a los avengers que tengan el nombre alfabeticamente menor al del avenger $A$.
#    Nick Fury podria decidir que todos tengan un premio, pero ha estado teniendo problemas con el Avenger $A$, por lo que dara solamente premio a los avengers que tengan el nombre alfabeticamente menor al del avenger $A$.
#    Nick Fury podria decidir que todos tengan un premio, pero ha estado teniendo problemas con el Avenger $A$, por lo que dara solamente premio a los avengers que tengan el nombre alfabeticamente menor al del avenger $A$.
#   Entrada
#    Existen varios casos de prueba, cada caso de prueba comienza con un entero ($1 \leq M \leq 100$) la cantidad de misiones que han existido, las siguientes $M$ lineas, comienzan con un número ($1 \leq N \leq 50$) que representa la cantidad de avengers que participaron en la mision, seguido por $N$ cadenas separadas por un espacio que tienen el nombre de un avenger, la ultima linea del caso de prueba, contiene el nombre del avenger $A$ que con el cual Nick ha tenido problemas.
#    Existen varios casos de prueba, cada caso de prueba comienza con un entero ($1 \leq M \leq 100$) la cantidad de misiones que han existido, las siguientes $M$ lineas, comienzan con un número ($1 \leq N \leq 50$) que representa la cantidad de avengers que participaron en la mision, seguido por $N$ cadenas separadas por un espacio que tienen el nombre de un avenger, la ultima linea del caso de prueba, contiene el nombre del avenger $A$ que con el cual Nick ha tenido problemas.
#    Existen varios casos de prueba, cada caso de prueba comienza con un entero ($1 \leq M \leq 100$) la cantidad de misiones que han existido, las siguientes $M$ lineas, comienzan con un número ($1 \leq N \leq 50$) que representa la cantidad de avengers que participaron en la mision, seguido por $N$ cadenas separadas por un espacio que tienen el nombre de un avenger, la ultima linea del caso de prueba, contiene el nombre del avenger $A$ que con el cual Nick ha tenido problemas.
#    Existen varios casos de prueba, cada caso de prueba comienza con un entero ($1 \leq M \leq 100$) la cantidad de misiones que han existido, las siguientes $M$ lineas, comienzan con un número ($1 \leq N \leq 50$) que representa la cantidad de avengers que participaron en la mision, seguido por $N$ cadenas separadas por un espacio que tienen el nombre de un avenger, la ultima linea del caso de prueba, contiene el nombre del avenger $A$ que con el cual Nick ha tenido problemas.
#   Salida
#    Por cada caso de prueba, mostrar la cantidad de certificados que se entregaran.
#    Por cada caso de prueba, mostrar la cantidad de certificados que se entregaran.
#    Por cada caso de prueba, mostrar la cantidad de certificados que se entregaran.
#    Por cada caso de prueba, mostrar la cantidad de certificados que se entregaran.
#   Ejemplo Entrada
#    53 hulk thor ironman3 spiderman thor hulk1 ironman2 spiderman hawkeye3 ironman spiderman thorspiderman21 spiderman1 ironmanironman
#   Ejemplo Salida
#    30
#   Ayuda
#    En el primer caso, el orden alfabetico de los avengers seria [hawkeye, hulk, ironman, spiderman, thor], como Nick esta enfadado con spiderman solo entregara certificados a los 3 primeros.
#    En el primer caso, el orden alfabetico de los avengers seria [hawkeye, hulk, ironman, spiderman, thor], como Nick esta enfadado con spiderman solo entregara certificados a los 3 primeros.
#    En el primer caso, el orden alfabetico de los avengers seria [hawkeye, hulk, ironman, spiderman, thor], como Nick esta enfadado con spiderman solo entregara certificados a los 3 primeros.
#    En el segundo caso, el orden alfabetico es [ironman, spiderman], como Nick esta enfadado con ironman, no dara certificados a ningun avenger.
#    En el segundo caso, el orden alfabetico es [ironman, spiderman], como Nick esta enfadado con ironman, no dara certificados a ningun avenger.
#    En el segundo caso, el orden alfabetico es [ironman, spiderman], como Nick esta enfadado con ironman, no dara certificados a ningun avenger.
#    Ordenar a los avenger por el nombre y todos los que esten antes de Avenger A tendran su premio.
#    Ordenar a los avenger por el nombre y todos los que esten antes de Avenger A tendran su premio.
#    Ordenar a los avenger por el nombre y todos los que esten antes de Avenger A tendran su premio.

while True:
    try:
        M = int(input())
        avengers = set()
        for _ in range(M):
            N, *av = input().split()
            avengers.update(av)
        A = input()
        print(sorted(avengers).index(A))
    except EOFError:
        break