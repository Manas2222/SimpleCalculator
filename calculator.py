def add(a, b):
    return a + b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a * b

def divide(a,b):
    return a/b

def showMenu():
    try:
        choice = int(input("Choose an operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\nEnter your choice: "))
        if choice == 1:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {add(a, b)}")
        elif choice == 2:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {subtract(a, b)}")
        elif choice == 3:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {multiply(a, b)}")
        elif choice == 4:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if b != 0:
                print(f"Result: {divide(a, b)}")
            else:
                print("Error! Division by zero.")
        elif choice == 5:
            print("Exiting the calculator. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def main():
    while (True):
        showMenu()


if __name__ == "__main__":
    main()


