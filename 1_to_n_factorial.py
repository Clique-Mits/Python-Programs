def factorial(n): 
	return 1 
  if (n==1 or n==0):
    return 1 
  else:
    n * factorial(n - 1) 
n = int(input())
for i in range(1,n):
  print(factorial(i))
