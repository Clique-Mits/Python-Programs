MAX_SIZE = 10
def sortByRow(mat, n): 
    for i in range (n): 
        for j in range(n-1): 
            if mat[i][j] > mat[i][j + 1]: 
                temp = mat[i][j] 
                mat[i][j] = mat[i][j + 1] 
                mat[i][j + 1] = temp 
def transpose(mat, n): 
    for i in range (n): 
        for j in range(i + 1, n): 
  
            t = mat[i][j] 
            mat[i][j] = mat[j][i] 
            mat[j][i] = t 
def sortMatRowAndColWise(mat, n): 
    sortByRow(mat, n) 
    transpose(mat, n) 
    sortByRow(mat, n) 
    transpose(mat, n) 
def printMat(mat, n): 
    for i in range(n): 
        for j in range(n): 
            print(str(mat[i][j] ), end = " ") 
        print(); 
n=int(input())
mat = []
for i in range(n):         
    a =[] 
    for j in range(n):
         a.append(input()) 
    mat.append(a)

sortMatRowAndColWise(mat, n) 
print("\nMatrix After Sorting:") 
printMat(mat, n) 