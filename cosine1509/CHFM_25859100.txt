values=[]
ans=[]
numTests = int(input())

for j in range (0,numTests):
     N = int(input())


     values = ( input().split(' ') )
     values = list(map(int,values))
     mean=sum(values)/len(values)
     x=0;
     for value in values:
          if int(value)==mean:
               ans.append(values.index(value)+1)
               x=1
               break;
               
     if x==0:
          ans.append('Impossible')
          
for an in ans:          
     print(an)