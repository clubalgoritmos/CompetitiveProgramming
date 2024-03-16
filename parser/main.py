import lib

par = lib.Parser(path="C:\\Users\\Andres\\Proyectos\\PyCompetitiveProgramming")
if input("is a problem?").lower()=="yes":
    while True:
        try:
            print(par.create_Problem(input()))
        except EOFError:
            break
else:
    print(par.get_from_table(input()))
#print(lib.Parser(path="C:\\Users\\Andres\\Proyectos\\Practicas-competencias\\parser\\ejercicios").get_from_table("https://jv.umsa.bo/oj/contest.php?cid=2567&pid=7"))#.create_Problem(input()))
#print(par.list_contest())