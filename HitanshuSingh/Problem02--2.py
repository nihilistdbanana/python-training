# print sum of squares of numbers from 1 to n, where you take n as input from user.

#Take input from the user
n=int(input("Enter any positive integer :"))

#Create an empty tuple
t=()

#Performing Operations
for i in range(1,n+1):
    t=t+(i**2,)

#Print
print()
print("The sum of squares of numbers from 1, to the number provided by the user :", sum(t))
