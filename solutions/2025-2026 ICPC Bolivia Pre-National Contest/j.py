S = input()

les = {"I", "l", "0", "O", "8", "B"}

if any(c in les for c in S):
    print("SI")
else:
    print("NO")
