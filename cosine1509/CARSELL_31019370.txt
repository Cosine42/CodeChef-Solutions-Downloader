M = 1000000007
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l=sorted(l,reverse=True)
   
    for i in range(n):
        if i<l[i]:
            l[i]-=i
        else:
            l[i]=0
     
    print(sum(l)%(M))
