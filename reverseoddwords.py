s=input("Enter the string: ").split(" ")
for i in range(0,len(s)):
    if(i%2==0):
        print(s[i][::-1],end=" ")
    else :
        print(s[i],end=" ")

