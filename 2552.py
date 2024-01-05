A = [a for a in input().lower()]
for a in A:
  if not a in "aeiou":
    print(f".{a}", end='')