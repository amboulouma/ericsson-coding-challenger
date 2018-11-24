n = sorted(list(map(int, input().split())))
if len(n)%2 == 0:
    if ((n[len(n)//2 - 1] + n[len(n)//2])/2 // int ((n[len(n)//2 - 1] + n[len(n)//2])/2) == (n[len(n)//2 - 1] + n[len(n)//2])/2 ):
        print(int((n[len(n)//2 - 1] + n[len(n)//2])/2))
    else:
        print((n[len(n)//2 - 1] + n[len(n)//2])/2)
else:
    if( n[len(n)//2] // int(n[len(n)//2]) == n[len(n)//2]):
        print(int(n[len(n)//2]))
    else:
        print(n[len(n)//2])