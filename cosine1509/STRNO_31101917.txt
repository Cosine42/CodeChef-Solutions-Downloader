import math 
  
 
def pF(n): 
      
    c=0
    
    while n % 2 == 0:
        c+=1
        n = n / 2
     
          
     
    for i in range(3,int(math.sqrt(n))+1,2): 
          
         
        while n % i== 0: 
            c+=1 
            n = n / i 
              
    
    if n > 2: 
        c+=1
        
    return c

for _ in range(int(input())):

    x, k = list(map(int,input().split()))

    if pF(x)>=k:
        print(1)
    else:
        print(0)
