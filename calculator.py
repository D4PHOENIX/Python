def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):        
    return x * y
def divide(x, y):    
    return x / y
def remainder(x, y):
    return x % y    
def power(x, y):
    return x ** y    
def average(x, y):
    return (x + y) / 2

inputNum1 = int(input("Enter first number: "))
inputNum2 = int(input("Enter second number: "))
inputOperator = input("Enter operator: ")

if inputOperator == "+":
    print(add(inputNum1, inputNum2))
elif inputOperator == "-":
    print(subtract(inputNum1, inputNum2))
elif inputOperator == "*":
    print(multiply(inputNum1, inputNum2))
elif inputOperator == "/":
    print(divide(inputNum1, inputNum2))
elif inputOperator == "%":
    print(remainder(inputNum1, inputNum2)) 
elif inputOperator == "**":
    print(power(inputNum1, inputNum2))
elif inputOperator == "avg":
    print(average(inputNum1, inputNum2))           