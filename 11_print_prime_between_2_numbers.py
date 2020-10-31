# Print prime numbers in an interval
#number should be greater than 1
start = float(input('Enter the starting number: '))
end = float(input('Enter the ending number: '))
 
for i in range(start,end):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)
