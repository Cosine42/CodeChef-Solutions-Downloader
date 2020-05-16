numTests = int(input())
ans=[]
for i in range (0,numTests):
        c=0
        cars=[]
        N = int(input())
        cars = list(map(int,input().split()))
        copy = cars[:]

        
        for j in range(1,len(cars)):
                
                if copy[j]>copy[j-1]:
                        copy[j]=copy[j-1]

        for k in range(0,len(cars)):
                if cars[k]==copy[k]:
                        c+=1
                        
        print(c)
