def addition(number1, number2):  # addition function
    return f"The result of addition two numbers is: {number1 + number2}"


def subtraction(number1, number2):  # subtraction function
    return f"The result of subtraction two numbers is: {number1 + number2}"


def multiplication(number1, number2):  # multiplication function
    return f"The result of multiplication two numbers is: {number1 * number2}"


def division(number1, number2):  # division function
    try:
        result = number1 / number2
        return f"The result of division two numbers is: {result}"
    except ZeroDivisionError:
        return "Second number can't be zero!"


if __name__ == "__main__":

    try:
        number_1 = int(input("Please enter the first number: \n"))
        number_2 = int(input("Please enter the second number: \n"))
    except ValueError:
        print("Wrong input!")
        exit()
    print("""
    Please select an operation:

    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division

    """)

    operand = input("Enter your choice (1-4): ")


    # dictionary of functuions
    operation = {"1": addition(number_1, number_2),
                "2": subtraction(number_1, number_2),
                "3": multiplication(number_1, number_2),
                "4": division(number_1, number_2)}

    # verification of the correctness of the operation input
    if operand in operation:
        print(operation[operand])
    else:
        print("Wrong choice!")
