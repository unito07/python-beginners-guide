def greet(name):
    """
    A simple function that creates a personalized greeting
    """
    return f"Hello, {name}! Welcome to Python programming!"

def add_numbers(a, b):
    """
    Function to add two numbers
    """
    return a + b

def main():
    # Simple print statement
    print("Hello, World!")
    
    # Using our greeting function
    name = "Beginner"
    greeting = greet(name)
    print(greeting)
    
    # Demonstrating the add_numbers function
    num1 = 5
    num2 = 3
    sum_result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {sum_result}")

# This is a common Python idiom that runs the main() function
# only if this file is run directly (not imported as a module)
if __name__ == "__main__":
    main()