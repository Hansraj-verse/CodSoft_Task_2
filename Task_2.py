# ==========================================
# Task 2: Calculator
#
# Objective:
# Create a simple calculator that performs
# basic arithmetic operations.
#
# Program Description:
# This program takes two numbers from the user,
# allows the user to select an arithmetic
# operation, performs the calculation, and
# displays the result.
#
# Features:
# - Addition (+)
# - Subtraction (-)
# - Multiplication (*)
# - Division (/)
# - Basic error handling
#
# ==========================================

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display available operations
print("\nChoose an operation:")
print("+ : Addition")
print("- : Subtraction")
print("* : Multiplication")
print("/ : Division")

# User selects an operation
operation = input("Enter your choice (+, -, *, /): ")

# Perform calculation based on user's choice
if operation == "+":
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")

elif operation == "/":
    # Check for division by zero
    if num2 == 0:
        print("\nError: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")

else:
    print("\nInvalid operation selected. Please choose +, -, *, or /.")