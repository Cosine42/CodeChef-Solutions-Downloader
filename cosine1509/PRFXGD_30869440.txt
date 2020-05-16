for _ in range(int(input())):
    s = input()
    n=len(s)
    k, x = list(map(int,input().split()))
    dic = {}
    t=set(s)
    for e in t:
        dic[e]=0;
        w=""
     
    for i in range(n):
        t=s[i]
        if dic[t]>=x:
            if k==0:
                break
            else: 
                k-=1
               
                dic[t]+=1
        else:
            w+=t
            dic[t]+=1
    print(len(w))
    
