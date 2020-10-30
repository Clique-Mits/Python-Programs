def recsearch( arr, l, r, x): 
	if r < l: 
		return -1
	if arr[l] == x: 
		return l
	if arr[r] == x: 
		return r 
	return recsearch(arr, l+1, r-1, x) 

arr = [int(x) for x in input().split()] 
n = len(arr) 
x = int(input())
index = recsearch(arr, 0, n-1, x) 
print(index)
