#Count the occurrence of each vowel in a string without using any library functions
n=input("Enter the string :")
c=0
for j in range(len(n)):
    if n[j]=="a" or n[j]=="A" or n[j]=="i" or n[j]=="I" or n[j]=="o" or n[j]=="O"or n[j]=="u" or n[j]=="U" or n[j]=="e" or n[j]=="E":
        c=c+1
print(c)