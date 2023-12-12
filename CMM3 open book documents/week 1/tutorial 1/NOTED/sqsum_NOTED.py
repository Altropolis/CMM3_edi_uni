# Function to calculate the sum of the squares of the first n natural numbers
def squaresum(n):
  
    # Initialize the sum variable
    sm = 0
    
    # Iterate from 1 to n, calculating the square of each number and adding to the sum
    for i in range(1, n + 1):
        sm = sm + (i * i)
      
    # Return the final sum
    return sm
  
# Main Program 

# Set the value of n
n = 20

# Call the squaresum function with n as an argument and store the result in sum_numbers
sum_numbers = squaresum(n)

# Print the result
print(sum_numbers)
