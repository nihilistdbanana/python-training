# print sum of numbers from 1 to n, where you take n as input from user


# print sum of squares of numbers from 1 to n, where you take n as input from user
# n = int(input("Enter a number"))

# if(n <= 0):
#     print("Please enter a positive number ")
#     quit()

# ans = 0
# for i in range(1,n+1):
#     ans += i**2

# print("The sum of squares of numbers from 1 to ", n, " is ", ans)

# print result of adding all even numbers and subtracting all odd numbers from 1 to n, where you take n as input from user


# (Optional) now try to solve all problems above without using a loop

#problem 2

# the sum of squares of numbers from 1 to n is equal to n(n+1)(2n+1)/6
n = int(input("Enter a number"))

if(n <= 0):
    print("Please enter a positive number ")
    quit()

ans = int(n*(n+1)*(2*n+1)/6)
print("The sum of squares of numbers from 1 to ", n, " is ", ans)
