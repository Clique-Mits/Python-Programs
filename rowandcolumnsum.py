    
def row_sum(arr,m,n) : 
    sum = 0
    print("\nFinding Sum of each row:\n") 
    for i in range(m) : 
        for j in range(n) : 
            sum += arr[i][j] 
        print("Sum of the row",i,"=",sum) 
        sum = 0

def column_sum(arr,m,n) : 
    sum = 0
    print("\nFinding Sum of each column:\n") 
    for i in range(n) : 
        for j in range(m) : 
            sum += arr[j][i] 
        print("Sum of the column",i,"=",sum) 
        sum = 0
  
m = int(input("Enter number of rows"))
n=int(input("Enter number of columns"))
arr=[]
x = 1
for i in range(m) :
    a=[] 
    for j in range(n) : 
        a.append(int(input()))
    arr.append(a)
row_sum(arr,m,n) 
column_sum(arr,m,n) 
row_sum(arr,m,n) 
column_sum(arr,m,n) 