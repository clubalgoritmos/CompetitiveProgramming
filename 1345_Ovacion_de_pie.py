# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=59
## https://jv.umsa.bo/oj/problem.php?id=1345
#    Copiado al portapapeles
#  Ovacion de pie
#  Enviar
#  Estado
#  Descripción
#    Se abre la noche en la ópera, y tu amiga es la prima donna (la cantante femenina más famosa). Desafortunadamente  no estarás en la audiencia, pero querrás asegurarte de que ella reciba una ovación de pie - que cada miembro de la audiencia se ponga de pie y aplauda.Inicialmente, todo el público está sentado. Todo el público tiene un nivel de timidez. Un miembro del público con el nivel de timidez Si va a esperar hasta q al menos Si otros miembros de la audiencia ya se ha puesto de pie a aplaudir, y si es así, el o ella inmediatamente se pondrá de pie y aplaudirá. Si  Si = 0, entonces el miembro de la audiencia siempre se pondrá de pie y aplaudirá inmediatamente, independientemente de lo que hagan los demás. Por ejemplo, un miembro del público con Si = 2 se sentará en el comienzo, pero se pondrá de pie para aplaudir más tarde después de que el o ella ve al menos otras dos personas de pie y aplaudiendo.Usted sabe que el nivel de la timidez de todos los miembros de la audiencia, y tu estas preparado para invitar amigos adicionales de la prima donna para estar en la audiencia para asegurarse de que todos en la multitud se pongan de pie y aplauden al final. Cada uno de estos amigos puede tener cualquier valor timidez que desee, no necesariamente el mismo. ¿Cuál es el número mínimo de amigos que usted necesita para invitar a garantizar una ovación de pie?
#    Se abre la noche en la ópera, y tu amiga es la prima donna (la cantante femenina más famosa). Desafortunadamente  no estarás en la audiencia, pero querrás asegurarte de que ella reciba una ovación de pie - que cada miembro de la audiencia se ponga de pie y aplauda.
#    Inicialmente, todo el público está sentado. Todo el público tiene un nivel de timidez. Un miembro del público con el nivel de timidez Si va a esperar hasta q al menos Si otros miembros de la audiencia ya se ha puesto de pie a aplaudir, y si es así, el o ella inmediatamente se pondrá de pie y aplaudirá. Si  Si = 0, entonces el miembro de la audiencia siempre se pondrá de pie y aplaudirá inmediatamente, independientemente de lo que hagan los demás. Por ejemplo, un miembro del público con Si = 2 se sentará en el comienzo, pero se pondrá de pie para aplaudir más tarde después de que el o ella ve al menos otras dos personas de pie y aplaudiendo.
#    Inicialmente, todo el público está sentado. Todo el público tiene un nivel de timidez. Un miembro del público con el nivel de timidez
#    S
#    i
#    va a esperar hasta q al menos
#    otros miembros de la audiencia ya se ha puesto de pie a aplaudir, y si es así, el o ella inmediatamente se pondrá de pie y aplaudirá. Si
#    = 0, entonces el miembro de la audiencia siempre se pondrá de pie y aplaudirá inmediatamente, independientemente de lo que hagan los demás. Por ejemplo, un miembro del público con
#    = 2 se sentará en el comienzo, pero se pondrá de pie para aplaudir más tarde después de que el o ella ve al menos otras dos personas de pie y aplaudiendo.
#    Usted sabe que el nivel de la timidez de todos los miembros de la audiencia, y tu estas preparado para invitar amigos adicionales de la prima donna para estar en la audiencia para asegurarse de que todos en la multitud se pongan de pie y aplauden al final. Cada uno de estos amigos puede tener cualquier valor timidez que desee, no necesariamente el mismo. ¿Cuál es el número mínimo de amigos que usted necesita para invitar a garantizar una ovación de pie?
#   Entrada
#    La primera línea de la entrada da el número de casos de prueba, casos de prueba T<=200. T líneas  siguen. Cada uno consta de una línea con Smax, el nivel máximo de la timidez de la persona más tímida en la audiencia, seguido de una cadena de Smax + 1 dígito. El dígito de orden k de esta cadena (contando a partir de 0) representa el número de personas en la audiencia tienen nivel de timidez k. Por ejemplo, la cadena "409" significaría que había cuatro miembros de la audiencia con Si = 0 y nueve miembros de la audiencia con Si = 2 (y ninguno con Si = 1 o cualquier otro valor). Tenga en cuenta que inicialmente será siempre entre 0 y 9 personas con cada nivel de timidez.La cadena nunca va a terminar en un 0. Nótese que esto implica que siempre habrá al menos una persona en la audiencia.
#    La primera línea de la entrada da el número de casos de prueba, casos de prueba T<=200. T líneas  siguen. Cada uno consta de una línea con Smax, el nivel máximo de la timidez de la persona más tímida en la audiencia, seguido de una cadena de Smax + 1 dígito. El dígito de orden k de esta cadena (contando a partir de 0) representa el número de personas en la audiencia tienen nivel de timidez k. Por ejemplo, la cadena "409" significaría que había cuatro miembros de la audiencia con Si = 0 y nueve miembros de la audiencia con Si = 2 (y ninguno con Si = 1 o cualquier otro valor). Tenga en cuenta que inicialmente será siempre entre 0 y 9 personas con cada nivel de timidez.
#    La cadena nunca va a terminar en un 0. Nótese que esto implica que siempre habrá al menos una persona en la audiencia.
#   Salida
#    Para cada caso de prueba, imprima un numero Y que es el número mínimo de amigos a los debe invitar.
#   Ejemplo Entrada
#    44 111111 095 1100110 1
#   Ejemplo Salida
#    0120
#   Ayuda
#    en el primer caso la audiencia automaticamente sin la necesidad de agregar a nadie,el primer miembro de la audiencia con Si=0 se parara , luego al audiencia con Si=1 se parara tambien y asi sucecivamente.En el caso 2 se necesita invitar a un amigo para que toda la audiencia se ponga de pie.En el caso 3  una optima solucion es invitar a dos personas mas con Si=2
#    en el primer caso la audiencia automaticamente sin la necesidad de agregar a nadie,el primer miembro de la audiencia con Si=0 se parara , luego al audiencia con Si=1 se parara tambien y asi sucecivamente.
#    En el caso 2 se necesita invitar a un amigo para que toda la audiencia se ponga de pie.
#    En el caso 3  una optima solucion es invitar a dos personas mas con Si=2

