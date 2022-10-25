#print the following pattern
for i in range(1,7):             # i for row reference
    for j in range(1,i+1):       # j for a column reference
        print("*",end="")
    print("\n")                 #Print stars in a new line

# print the following pattern

for i in range(1,7):
    for k in range(1,7-i):     # K for a Space reference
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end="")
    print("\n")

# print the following pattern

for i in range(1,7):
    for k in range(1,7-i):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end="")
    print("\n")
for i in range(5,0,-1):
    for k in range(1,5-i):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end="")
    print("\n")



