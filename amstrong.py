n=int(input())
p=n
s=0
while n>0:
    d=int(n%10)
    s=s+pow(d,3)
    #print(d,s)
    n=int(n/10)
    #print(n)
if s==p:
    print("amstrong number")
else:
    print("not amstrong number")