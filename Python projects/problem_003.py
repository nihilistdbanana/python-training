#print the following pattern
n=6
for i in range(n):              # i for row reference
    for j in range(i+1):        # j for a column reference
        print("*",end="")
    print()                     #Print stars in a new line

#print the following pattern
n=6
for i in range(n):
    for j in range(n-i-1):      # J for a Space reference
        print(' ',end="")
    for j in range(2*i+1):
        print('*',end="")
    print()

#print the following pattern
n=6
for i in range(n):
    for j in range(n-i-1):
        print(' ',end="")
    for j in range(2*i+1):
        print('*',end="")
    print()
for i in range(n):
    for j in range(i):
        print(' ',end="")
    for j in range(2*(n-i)-1):
        print('*',end="")
    print()
