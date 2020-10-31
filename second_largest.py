list1 = []
n=int(input("Enter the limit :"))
for i in range(0,n):
    e=int(input("Enter the numbers:"))
    list1.append(e)

mx=max(list1[0],list1[1]) 
secondmax=min(list1[0],list1[1]) 
n =len(list1)
for i in range(2,n): 
	if list1[i]>mx: 
		secondmax=mx
		mx=list1[i] 
	elif list1[i]>secondmax and \
		mx != list1[i]: 
		secondmax=list1[i]

print("Second highest number is : ",\
	str(secondmax))
