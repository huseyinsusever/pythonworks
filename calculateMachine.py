
    
def calculate_machine():
    try:
    
        number1 = float(input("First number enter: "))
        number2 = float(input("Second number enter: "))
        process = input("Enter the transaction (+,-,*,/): ")

        match process:
            case '+':
                print(f"Result: {number1 + number2}")
            case '-':
                print(f"Result: {number1 - number2}")
            case '*':
                print(f"Result: {number1 * number2}")
            case '/':
                if number2 == 0:
                    print(f"Result: {number1 / number2}")
            case _:
                print("Invalid transaction")
    except ValueError:
        print("Invalid entry! Please enter a number.")
                                
while True:
    calculate_machine()
    continue_input = input("Do you want to perform another calculation?(yes/no): ").strip().lower()
    if continue_input != 'yes':
        print("Exiting the calculator.Goodbye!")
        break