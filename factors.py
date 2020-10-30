n = int(input("Enter the number : "))
k = [i for i in range(1, int(n/2)+1) if(n % i == 0)]
k.append(n)
print("Factors of ", n, " ", k)
