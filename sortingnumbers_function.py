def sortSecond(val):
	return val[1]

list1 = [(1, 2), (3, 3), (1, 1)]

list1.sort(key=sortSecond)
print(list1)

list1.sort(key=sortSecond, reverse=True)
print(list1)
