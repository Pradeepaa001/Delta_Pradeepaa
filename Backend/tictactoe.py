n=int(input("Enter the number of rows: "))
for i in range(n-1):
    for j in range(n):
        if j!=n-1:
            print("_|",end='')
        else:
            print("_",end='')
    print(" ")
for i in range(1):
    for j in range(2*n-1):
        if j%2==0:
            print(" ",end='')
        else:
            print("|",end='')
    print(" ")