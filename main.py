# main.py
from calculator.calculator import Calculator

def main():
    while True:
        try:
            print("Select operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Divide")
            print("4. Exit")

            choice = input("Enter choice(1/2/3/4): ")

            if choice == '4':
                print("Exiting...")
                break

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = Calculator.add(num1, num2)
            elif choice == '2':
                result = Calculator.subtract(num1, num2)
            elif choice == '3':
                result = Calculator.divide(num1, num2)
            else:
                print("Invalid Input")
                continue

            print(f"The result is: {result}")

        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()