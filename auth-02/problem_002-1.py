# print sum of numbers from 1 to n, where you take n as input from user

# Take input from the user
n = int(input("Enter a positive integer n: "))

# Initialize the sum
sum_of_numbers = 0

# Calculate sum
for i in range(1, n + 1):
    sum_of_numbers += i

# Print 
print("The sum of numbers from 1 to", n, "is:", sum_of_numbers)
