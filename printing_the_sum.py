
print("This is the sum of the current number and the previous number")

# Iterate through the first 10 numbers
for i in range(1, 11):

# Calculate the sum of the current and previous number
    current_number = i
    previous_number = i - 1
    sum_result = current_number + previous_number

# Print the sum for each iteration
    print(f"Current Number {current_number} + Previous Number: {previous_number} = Sum: {sum_result}")