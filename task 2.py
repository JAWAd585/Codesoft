def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1/num2

print("Welcome to calculator")
print("to exit enter first number blank")

while True:
    num1 = input("Enter first number: ")
    
    if num1 == "":
        break
    else:
        num1 = float(num1)
        
    operator = input("Enter Arethmetic operator: ")
    num2 = float(input("Enter second number: "))
    
    if operator == "+":
       print(f"{num1} {operator} {num2} = {add(num1, num2)}\n")
        
    elif operator == "-":
        print(f"{num1} {operator} {num2} = {subtract(num1, num2)}\n")
        
    elif operator == "*":
        print(f"{num1} {operator} {num2} = {multiply(num1, num2)}\n")
        
    elif operator == "/":
        print(f"{num1} {operator} {num2} = {divide(num1, num2)}\n")
