def binary_search(arr, low, high, x): 
	if high >= low: 
		mid = (high + low) // 2 
		if arr[mid] == x: 
			print(mid) 
		elif arr[mid] > x: 
			return binary_search(arr, low, mid - 1, x) 
		else: 
			return binary_search(arr, mid + 1, high, x) 
	else: 
		print("-1")

arr=[int(x) for x in input().split()]
x=int(input())
res = binary_search(arr, 0, len(arr)-1, x) 
