age1, ammount1 = map(int, input().split())
age2, ammount2 = map(int, input().split())
age3 = int(input())

if (age3 - age1) * ammount1 >= (age3 - age2) * ammount2:
    print("1")
    exit()

print("2")
