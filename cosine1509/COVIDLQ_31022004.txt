for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    f=0
    if n<6 and sum(a)>1:
        print("NO")
    else:
        for i in range(0,n-5):
            if sum(a[i:i+6])>1:
                f=1
                print("NO")
                break;
        if f==0:
            print("YES")
    
