# https://jv.umsa.bo/oj/problem.php?cid=2870&pid=35
## https://jv.umsa.bo/oj/problem.php?id=1186
#    Copiado al portapapeles
#  Monedas
#  Enviar
#  Estado
#  Descripción
#    Eres uno de los jugadores m ́as prominentes de Metal Slug y muchas personas quisieran jugarcontigo. Pero vamos, eres demasiado bueno y nadie esta a tu nivel, asi que mejor dejemos todoal azar. Ya que el arcade est ́a por cerrar, solo podr ́as pasarte el juego como m ́aximo 10 vecesm ́as. Entonces pides a los N jugadores que quieren jugar contigo que coloquen sus monedas enfila con el lado de la cara arriba, luego elijes 10 monedas al azar de las N monedas e iniciasun juego con las monedas. T ́u agarras M intervalos [a, b] (1 ≤ a ≤ b ≤ n) de monedas y lasvolteas. Despu ́es de hacer estos M volteos, buscas las 10 monedas que elegiste. Si la monedaesta mostrando el lado de cara, jugar ́as con ese jugador. Caso contrario, no jugar ́as con  ́el.
#   Entrada
#    Se te dar ́an 2 n ́umeros: N (10 ≤ N ≤ 10 5 ) el n ́umero de jugadores pasables y M (1 ≤ M ≤ 10 5 )el n ́umero de intervalos que seleccionar ́as. A continuaci ́on, te ser ́an dadas M l ́ıneas, compuestaspor dos n ́umeros a y b, que representan un intervalo de monedas que quieres voltear. Finalmentete ser ́an dados 10 enteros, los cuales representar ́an las posiciones de las 10 monedas de losjugadores pasables (1 ≤ vi ≤ N ).
#   Salida
#    Se te dar ́an 2 n ́umeros: N (10 ≤ N ≤ 10^ 5 ) el n ́umero de jugadores pasables y M (1 ≤ M ≤ 10^ 5 )el n ́umero de intervalos que seleccionar ́as. A continuaci ́on, te ser ́an dadas M l ́ıneas, compuestaspor dos n ́umeros a y b, que representan un intervalo de monedas que quieres voltear. Finalmentete ser ́an dados 10 enteros, los cuales representar ́an las posiciones de las 10 monedas de losjugadores pasables (1 ≤ vi ≤ N ).Explicaci ́on de la entrada: C= cara E=cruz Emotic ́on pacman Inicialmente las 10 monedasest ́an as ́ı CCCCCCCCCC Luego del primer update de rango [2, 8] quedan as ́ı CEEEEEEECC.En el segundo update [1, 7] quedan: ECCCCCCECC Y en el tercer update [3, 3] ECECCCCECCenotnces los unicos que no jugaran contigo ser ́an los jugadores 1,3 y 8.
#   Ejemplo Entrada
#    10 32 81 73 312345678910
#   Ejemplo Salida
#    NOSINOSISISISINOSISI
#   Ayuda

