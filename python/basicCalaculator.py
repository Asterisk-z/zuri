

from email.policy import default


try:
    firstNumber = int(input("Enter First Number:"))
    operation =  str(input("Enter Any Operator(*,+,-,/,%):"))
    secondNumber = int(input("Enter Second Number:"))

    if ((len(operation) != 1)):
        raise Exception('Error')

    def addition(first, second):
        print(first + second)


    def subtraction(first, second):
        print(first - second)


    def multiplication(first, second):
        print(first * second)


    def division(first, second):
        print(first / second)

    def modulus(first, second):
        print(first % second)


    match operation:
        case '+':
            addition(firstNumber, secondNumber)
        case '*':
            multiplication(firstNumber, secondNumber)
        case '-':
            subtraction(firstNumber, secondNumber)
        case '/':
            division(firstNumber, secondNumber)
        case '%':
            modulus(firstNumber, secondNumber)
        case _:
            raise Exception("Error")


except:
    print("An Error Occurred : Please Confirm Inputs")