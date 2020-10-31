m=int(input("Enter number of rows: "))
n=int(input("Enter number of columns: "))
A=[]
for i in range(m):
    aa=[]
    for j in range(n):
        aa.append(int(input()))
    A.append(aa)

rez = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))] 
print("\n Transponse is: \n") 
for row in rez: 
    print(row) 