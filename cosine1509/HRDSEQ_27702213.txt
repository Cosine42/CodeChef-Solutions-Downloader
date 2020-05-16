t = int(input())

def rin(lis, item):
    for i in range(len(lis)-1, -1, -1):
        if item == lis[i]:
            return i


for _ in range(t):
    n = int(input())
    d=[0,]
    for i in range(1,n):
        s = d[:i-1]
        l = d[-1]
        if l not in s:
            d.append(0)
        else:
            r = rin(s,l)
            d.append(i-r-1)
            
    print(d.count(d[-1]))
  
