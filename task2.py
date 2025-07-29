a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("Choose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

operation = input("Enter operation symbol (+, -, *, /): ")

if operation == '+':
    result = a + b
    print("Result:", result)
elif operation == '-':
    result = a - b
    print("Result:", result)
elif operation == '*':
    result = a * b
    print("Result:", result)
elif operation == '/':
    if b != 0:
        result = a / b
        print("Result:", result)
    else:
        print("infinity")
else:
    print("Please select again")
