s = input().strip().lower()

if s == ''.join(sorted(s)) or s == ''.join(sorted(s, reverse=True)):
    print("yes")
else:
    print("no")