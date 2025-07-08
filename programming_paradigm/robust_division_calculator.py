def safe_divide(numerator, denominator):
    try:
        return f"The result of the division is {numerator / denominator}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

# Handle ValueError during input
try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = safe_divide(numerator, denominator)
    print(result)
except ValueError:
    print("Error: Please enter numeric values only.")
