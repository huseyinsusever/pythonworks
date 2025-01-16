# try:
#     number = int(input("Enter a number: "))
#     print(f"Enter your number: {number}")
# except ValueError:
#     print("invalid entry! please enter a number")    

try:
    number1 = int(input("First number give: "))
    number2 = int(input("Second number enter: "))
    result = number1/number2
    print(f"Result:{result}")
except ValueError:
    print("invalid pass! please give a number. ")
except ZeroDivisionError:
    print("Division by zero error!")        