n = int(input("enter number of lines: "))

# represents number of lines
for i in range(0, n):
    st = ""
    # represents no.of stars in each line.
    for j in range(0, n):
        if(j < i):
            st += "  "
        else:
            st += "* "
    print(st)
