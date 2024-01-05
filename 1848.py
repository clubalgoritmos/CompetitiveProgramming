for _ in range(int(input())):
  a = input().upper()
  p = list(set(a))
  c = 0
  for x in p:
    if a.count(x) > c:
      c = a.count(x)
  abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
  r = ""
  r = r + abc[c-1]
  for x in a:
    r = r + abc[abc.find(x)+c]
  print(r)