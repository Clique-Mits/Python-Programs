s=input("Enter the string").split(" ")
for i in range(0,len(s)):
    if (s[i]=="the"):
        s[i]="a"
print(" ".join(s))