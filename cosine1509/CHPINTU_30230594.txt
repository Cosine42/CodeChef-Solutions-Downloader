t = int(input())
for _ in range(t):
    n, m = list(map(int,input().split()))
    f = list(map(int,input().split()))
    p = list(map(int,input().split()))
    dic = {}
    
     
 
    for i in range(n):
        dic.setdefault(f[i],0)
         
        dic[f[i]]+=p[i]
    
     
    l = list(dic.values())
    
    print ( min(l) )
     
