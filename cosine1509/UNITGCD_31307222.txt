def LCM(a,b):
    if a>b:
        b,a=a,b

    for i in range(1,a+1):
        if (b*i)%a==0:
            return b*i
for _ in range(int(input())):
    n = int(input())
    l=list(range(1,n+1))
    
     
    
    if n<=3:
        print(1)
        print(n,end=" ")
        print(" ".join(list(map(str,l))))

    else:
        print(n//2)
        if n%2==0:
            for i in range(0,n-1,2):
                print(2,l[i],l[i+1])
        else:
            for i in range(0,n-4,2):
                print(2,l[i],l[i+1])
            print(3,l[-3],l[-2],l[-1])
