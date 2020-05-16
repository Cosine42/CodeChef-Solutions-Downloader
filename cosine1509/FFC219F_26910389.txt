t = int(input())
for _ in range(t):
    n, p = list(map(int,input().split()))
    a = list(map(int, input().split()))
    a.sort()
    c = 0
    for i in a:
        if i<=p:
            c += 1
            p -= i
            
        else:
            break
    print(c)
        
