s=input("Enter the string")
upp=0
low=0
digit=0
for i in s:
    if i.isalpha():
        if (ord(i) >= 97 and ord(i) <= 122):
            low+=1
        elif (ord(i) >= 65 and ord(i) <= 90):
            upp+=1
    if i.isdigit():
        digit+=1
print("No. of Uppercases: ",upp)
print("No. of LowerCases: ",low)
print("No. of digits: ",digit)
