mv = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for _ in range(int(input())):
  d, m, y = map(int,input().split(" "))
  try:
    if d>=0 and (d<=mv[m] or (d<=29 and m==2 and (y/4)%100==0)):
      print("Fecha correcta")
    else:
      raise 
  except:
    print("Fecha incorrecta")
