a=[]
n=int(input("Enter the limit :"))
print("Enter the numbers:")
for i in range(0,n):
    e=int(input())
    a.append(e)
def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x
for i in range(len(a)):
    for j in range(i+1,len(a)):
        hcf = compute_hcf(a[i],a[j])
        if hcf==1:
            print(a[i],a[j])

