n, w = map(int, input().split())
h = list(map(int, input().split()))
h.sort(reverse=True)
for i in range(w, n):
    if h[i] >= h[i - w]:
        print("no")
        break
else:
    print("yes")