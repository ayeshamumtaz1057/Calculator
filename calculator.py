"""
Simple command-line calculator.
Supports +, -, *, /, and repeated calculations until the user quits.
"""


def calculate(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError(f"Unknown operator: {op}")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_operator():
    while True:
        op = input("Operator (+, -, *, /): ").strip()
        if op in ("+", "-", "*", "/"):
            return op
        print("Please enter one of: + - * /")


def main():
    print("=== Simple Calculator ===")
    print("Type 'q' at any prompt to quit.\n")

    while True:
        first = input("First number (or 'q' to quit): ").strip()
        if first.lower() == "q":
            break
        try:
            a = float(first)
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        op = get_operator()
        b = get_number("Second number: ")

        try:
            result = calculate(a, op, b)
            print(f"= {result}\n")
        except ZeroDivisionError as e:
            print(f"Error: {e}\n")

    print("Goodbye!")


if __name__ == "__main__":
    main()
