while True:
    try:
        n = input()
        s = sum(list(map(int,n)))
        print(f"La suma de los digitos de {n} es {s}")
    except EOFError:
        break