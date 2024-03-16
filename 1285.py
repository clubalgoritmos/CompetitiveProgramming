while True:
    try:
        if sum([a*(-1)**i for i,a in enumerate(map(int,input()))]) == 0:
            print("SI")
            continue
        print("NO")
    except EOFError:
        break