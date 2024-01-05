for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[0], end=" ")
    print(arr[1], end=" ")
    a=2
    sw=False
    while a<len(arr) and sw==False:
        for i in range(a):
            for j in range(i+1,a):
                if not arr[i]+arr[j]==arr[a]:
                    print(arr[a])
                    sw=True
                    break
            if sw:
               break
        a+=1