print("Welcome the calculator!")

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
operator = input("Choose operator (x, /, -, +): ")

if operator == "x":
    print(f"Multiplication of these two numbers: {num1 * num2}")
elif operator == "/":
    print(f"Quotient of these two numbers: {num1 / num2}")
elif operator == "-":
    print(f"Subtraction of these two numbers: {num1 - num2}")
elif operator == "+":
    print(f"The sum of these two numbers: {num1 + num2}")
else:
    print("Please choose a correct operator!")












