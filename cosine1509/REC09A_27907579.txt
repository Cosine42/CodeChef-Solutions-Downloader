n, k = list(map(int,input().split()))

l = list(map(int,input().split()))
curr = sum(l)
l.sort()
x = (k-curr)

if (x>l[0] and x<l[-1] and (not x in(l))) or x==0:
    print("YES")
else:
    print("NO")
