from art import logo


# define function for addition
def add(n1, n2):
    return n1 + n2


# define function for subtraction
def subtract(n1, n2):
    return n1 - n2


# define function for multiplication
def multiply(n1, n2):
    return n1 * n2


# define function for division
def divide(n1, n2):
    return n1 / n2


# dictionary with calculator operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# define recursive function for calculator
def calculator():
    print(logo)

    # get user input for first number
    num1 = float(input("What is the first number?: "))

    # define variable to keep track if user wants to continue making calculations
    should_continue = True

    # while loop to keep running if user wants to reuse numbers
    while should_continue:

        # print different operations for user
        for sign in operations:
            print(sign)

        # get user input for operation
        calculation = input("Pick an operation: ")

        # Get user inputs for next number
        num2 = float(input("What is the next number?: "))

        # perform calculation based on chosen operator and output calculation to user
        result = operations[calculation](num1, num2)
        print(f"{num1} {calculation} {num2} = {result}")

        new_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or type 's' to stop: ").lower()

        # replace first number with calculated answer if user wants to continue
        if new_calculation == 'y':
            num1 = result
        elif new_calculation == 'n':
            # stop loop and restart function
            should_continue = False
            calculator()
        else:
            # exit program
            break


# call calculator function
calculator()
