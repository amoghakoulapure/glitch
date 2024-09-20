def multiply_numbers():
    # Ask for the number of inputs
    n = int(input("Enter the number of inputs you want to multiply: "))
    
    # Initialize the result to 1 (multiplicative identity)
    result = 1
    
    # Loop to get the numbers from the user
    for i in range(n):
        number = float(input(f"Enter number {i + 1}: "))  # You can change float to int if you want integers
        result *= number  # Multiply the current number to the result
    
    print(f"The result of multiplication is: {result}")

# Call the function
multiply_numbers()
