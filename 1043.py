for i in range(int(input())):
    pie,pal = map(int,input().split())
    pic = min(pie//3, pal//2)
    print(pic, pie+pal-pic*5)