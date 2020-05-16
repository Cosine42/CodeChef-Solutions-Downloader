t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    elems = set(l)
    m = 0
    for e in elems:
        x = l.count(e)
        if x>m:
            m = x
    print(n-m)
    
