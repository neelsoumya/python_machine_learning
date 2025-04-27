# script to show how functions work

# Define a simple function that takes no arguments
def greet():
    print("Hello, welcome to learning Python Functions!")

# Define a function that takes arguments
def add_numbers(a, b):
    return a + b

# Define a function that returns a value
def square(number):
    return number * number

# Main function that calls other functions
#def main():
#    # Call the greet function
#    greet()

#    # Call the add_numbers function with arguments
#    result = add_numbers(5, 7)
#    print(f"The sum of 5 and 7 is: {result}")

#    # Call the square function and store the result
#    squared_value = square(4)
#    print(f"The square of 4 is: {squared_value}")

# Run the main function
if __name__ == "__main__":
    #main()
    greet()
    result = add_numbers(5,7)
    print(result) 
