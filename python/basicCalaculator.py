
firstNumber = 4
operation = 'multiplication'
secondNumber = 2

def addition(first, second):
    print(first + second)


def subtraction(first, second):
    print(first - second)


def multiplication(first, second):
    print(first * second)


def division(first, second):
    print(first / second)


match operation:
    case 'addition':
         addition(firstNumber, secondNumber)
    case 'multiplication':
         multiplication(firstNumber, secondNumber)
    case 'subtraction':
         subtraction(firstNumber, secondNumber)
    case 'division':
         division(firstNumber, secondNumber)
