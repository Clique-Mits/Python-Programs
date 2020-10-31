n=int(input("Enter the number of string:"))
a=[]
print("Enter the strings:")
for i in range(0,n):
    c=input()
    a.append(c)
a.sort(key=len) 
print("Sorted string:")
for i in a:
    print(i)