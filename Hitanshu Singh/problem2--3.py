#print result of adding all even numbers and subtracting all odd numbers from 1 to n, where you take n as input from user

#Take n as input from user

n=int(input("Enter any positive integer :" ))
print()

#Initialize the inc_even(for addition of all even numbers)

inc_even=1

#Initialize the dec_odd(for subtraction of all odd numbers)

dec_odd=0

#Perform the operations

for i in range(1,n+1):
    if i%2==0:
        inc_even+=i
    else:
        if i==1:
            dec_odd=i-dec_odd
        else:
            dec_odd-=i

#Print

print("Result of addition of Even numbers from 1, to the number, provided by user :", inc_even)

print()

print("Result of subtraction of Odd numbers from 1, to the number, provided by user :", dec_odd)

