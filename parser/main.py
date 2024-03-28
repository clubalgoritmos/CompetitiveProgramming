import lib

par = lib.Parser(path="C:\\Users\\Andres\\Proyectos\\PyCompetitiveProgramming")
#print(par.create_problem("https://jv.umsa.bo/oj/problem.php?id="+input()))
print(par.get_contest("https://jv.umsa.bo/oj/contest.php?cid=2819"))
#if input("is a problem?").lower()=="yes":
#    while True:
#        try:
#            print(par.create_Problem(f"https://jv.umsa.bo/oj/problem.php?id={input('https://jv.umsa.bo/oj/problem.php?id=')}"))
#        except EOFError:
#            break
#elif input("search contest?").lower()=="yes":
#    for i in range(int(input()),int(input())):
#        print(par.search_contest(f"https://jv.umsa.bo/oj/contest.php?cid={i}"))
#else:
#    print(par.get_from_table(input()))
#print(lib.Parser(path="C:\\Users\\Andres\\Proyectos\\Practicas-competencias\\parser\\ejercicios").get_from_table("https://jv.umsa.bo/oj/contest.php?cid=2567&pid=7"))#.create_Problem(input()))
#print(par.list_contest())

# par = lib.Parser(path="C:\\Users\\Andres\\Proyectos\\Practicas-competencias\\parser\\ejercicios")
#print(par._get_from_table("https://estadistica.umsa.bo/plan-de-estudios2021"))