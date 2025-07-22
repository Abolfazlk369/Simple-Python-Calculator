#python calcucator 

operator = input("enter  your operator (+ , * , / - ): ")

num1 = float(input("Enter a number for num1 : "))

num2 = float(input("Enter a number for num2 : "))

if operator == "+":
    print(f"num1 + num2 = {round(num1 + num2, 2)}")
elif operator == "-":
    print(f"num1 - num2 = {round(num1 - num2, 2)}")
elif operator == "*":
    print(f"num1 * num2 = {round(num1 * num2, 2)}")
elif operator == "/":
    print(f"num1 / num2 = {round(num1 / num2, 2)}")
else:
    print(f"{operator} is valid operator")

