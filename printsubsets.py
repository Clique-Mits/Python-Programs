n=int(input("Enter the limit of the array:"))
a=[]
s=0
print("Enter the elements of the array:")
for i in range(0,n):
    c=int(input())
    a.append(c)
k=int(input("Enter the number:"))
for i in range(0,n):
    for j in range(i+1,n):
        s=a[i]+a[j]
        if s==k:
            print(a[i],a[j])