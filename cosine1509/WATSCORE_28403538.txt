t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    r = []
    for i in range(n):
        p, s = list(map(int, input().split()))
        if p<9:
            if not p in(l):
                l.append(p)
                r.append(s)
            else:
                x = l.index(p)
                if ( s > r[x] ):
                    r[x] = s
    print(sum(r))
                
            
