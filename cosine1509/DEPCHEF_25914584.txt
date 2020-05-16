numTests = int(input())

ans= []
for i in range(0,numTests):
    n = input()
    a = list(map( int,input().split() ) )
    d = list(map( int,input().split() ) )
    l = len(a)
    survive=[]
    for i in range(0,l):
        if i==l-1:
            attack = a[i-1]+a[0]
        elif i==0:
            attack = a[-1]+a[i+1]
        else:
            attack = a[i-1]+a[i+1]
            
        defence = d[i]
        
        if defence>attack:
            survive.append(defence)
    survive.sort()
    if len(survive)==0:
        ans.append(-1)
    else:    
        ans.append(survive[-1])
for an in ans:
    print(int(an))
