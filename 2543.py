mayus, minus = 0, 0
a = input()
for x in a:
  if x.isupper():
    mayus+=1
  else:
    minus+=1
if mayus>minus:
  a = a.upper()
else:
  a = a.lower()
print(a)