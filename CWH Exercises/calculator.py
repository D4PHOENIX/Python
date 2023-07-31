add = lambda x, y: x + y
subtract = lambda  x, y: x - y
multiply = lambda  x, y: x * y
divide = lambda  x, y: x / y
remainder = lambda  x, y: x % y    
power = lambda x, y: x ** y    
average = lambda x, y: (x + y) / 2

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