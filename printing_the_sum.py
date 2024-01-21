# Iterate through the first 10 numbers
for i in range(1, 11):

# Calculate the sum of the current and previous number
    current_number = i
    previous_number = i - 1
    sum_result = current_number + previous_number

# Print the sum for each iteration
    print(f"iteration {i}: {current_number} + {previous_number} = {sum_result}")