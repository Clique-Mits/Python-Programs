while(1):
    oper = int(input("1.Add 2.Subtract 3.Multipy 4.Divide 0.Exit : "))
    if(oper == 0):
        break
    arr = [int(x) for x in input("enter numbers : ").split()]
    if(oper == 1):
        sum = 0
        for i in arr:
            sum += i
        print(sum)
    elif(oper == 2):
        diff = arr[0]
        for i in range(1, len(arr)):
            diff -= arr[i]
        print(diff)
    elif(oper == 3):
        pro = 1
        for i in arr:
            pro *= i
        print(pro)
    elif(oper == 4):
        quo = arr[0]
        prt = True
        for i in range(1, len(arr)):
            if (arr[i] != 0):
                quo /= arr[i]
            else:
                prt = False
                print("Cannot divide by 0!!")
        if(prt == True):
            print(quo)
