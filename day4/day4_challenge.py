#!/usr/bin/env python3

def add(x, y):
    print(x + y)

def subtract(x, y):
    print(x - y)

def divide(x, y):
    if y != 0:
        print(x / y)
    else:
        print("You can't divide by zero!")

def multiply(x, y):
    print(x * y)

def main():
    while True:
        try:
            x = float(input("Enter in a number: "))
            y= float(input("Enter ANOTHER number: "))
            break
        except:
            print("Invalid input, try again.")

    operation = ""

    while(operation not in ['add', 'subtract','divide','multiply']):
        operation = input("What operation would like to perform? OPTIONS: 'add', 'subtract','divide','multiply': ").lower()

    calculator_dict = {
        "add": add,
        "subtract": subtract,
        "divide": divide,
        "multiply": multiply
    }

    calculator_dict[operation](x,y)

if __name__ == "__main__":
    main()
