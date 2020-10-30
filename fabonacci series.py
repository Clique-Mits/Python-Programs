n=int(input("ENTER THE NO. UPTO WHICH YOU WANT TO KNOW FABONACCI SERIES: "))
a,b,sum=0,1,0
for i in range(n):
    if(i==0):
        print (a,end=" ")
        continue
    if(i==1):
        print(b,end=" ")
        continue
    sum=a+b
    print(sum,end=" ")
    a=b
    b=sum
    
    
    
    
