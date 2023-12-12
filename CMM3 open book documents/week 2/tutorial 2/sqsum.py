# Function that returns the sum of 
# square of first n natural numbers 
def squaresum(n) : 
    # Initialise the sum to 0
    sm = 0
    # Iterate i from 1  
    # to n finding  
    # the square of i and 
    # add to sum. 
    for i in range(1, n+1) : 
        sm = sm + (i * i) 
    return sm 
  
# Main Program 
# Specify n
n = 20
# Call the function squaresum
sum_numbers = squaresum(n)
# Print result on screen
print(sum_numbers) 
