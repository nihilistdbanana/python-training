# print sum of numbers from 1 to n, where you take n as input from user.

# Take input from the user
n=int(input("Enter any natural number :"))

#Creating an empty list 
l=[]

#Perform the Operations
for i in range(1,n+1):
    l.extend([i])
    
#Print
print()
print("Result of sum of numbers from 1, to the number provided by the user :", sum(l))



