def transpose(mat, row, col):
	tr = [[0 for i in range(row)] for i in range(col)]
	for i in range(row):
		for j in range(col):
			tr[j][i] = mat[i][j]
	return tr

def RowWiseSort(B):
	for i in range(len(B)):
		B[i] = sorted(B[i])
	return B

def sortCol(mat, N, M):
	B = transpose(mat, N, M)
	B = RowWiseSort(B)
	mat = transpose(B, M, N)
	for i in range(N):
		for j in range(M):
			print(mat[i][j], end = " ")
		print()


if __name__ == '__main__':
  
	mat =[ [1, 6, 10 ],
			[ 8, 5, 9 ],
			[ 9, 4, 15 ],
			[ 7, 3, 60 ] ]

	N = len(mat)
	M = len(mat[0])

	sortCol(mat, N, M)
