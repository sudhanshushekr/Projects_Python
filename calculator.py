# Creating Calculator 

def calculator():
    # methods for calculation operations 

    def add(n1, n2):
        # function to add two numbers
        return n1 + n2

    def subtract(n1, n2):
        # function to subtract second number from first number
        return n1 - n2

    def multiply(n1, n2):
        # function to multiply two numbers
        return n1 * n2

    def divide(n1, n2):
        # function to divide first number by second number
        return n1 / n2

    # dictionary to store operations and their corresponding functions
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    # prompt user to input the first number
    num1 = float(input("What is the first number?: "))

    # display the operator symbols to the user
    for symbol in operations:
        print(symbol)
    
    should_continue = True

    # user selects the operator symbol and the operation starts
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        # prompt user to input the next number
        num2 = float(input("What is the next number?: "))
        # retrieve the calculation function based on the selected operator
        calculation_function = operations[operation_symbol]
        # perform the calculation
        answer = calculation_function(num1, num2)
        # display the result of the calculation
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # prompt user to continue with the current result or start a new calculation
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            # restart the calculator for a new calculation
            calculator()
