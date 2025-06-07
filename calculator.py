Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def add(x, y):
...     return x + y
... 
... def subtract(x, y):
...     return x - y
... 
... def multiply(x, y):
...     return x * y
... 
... def divide(x, y):
...     if y == 0:
...         return "Error! Division by zero."
...     return x / y
... 
... print("Select operation:")
... print("1. Add")
... print("2. Subtract")
... print("3. Multiply")
... print("4. Divide")
... 
... while True:
...     choice = input("Enter choice (1/2/3/4): ")
... 
...     if choice in ('1', '2', '3', '4'):
...         num1 = float(input("Enter first number: "))
...         num2 = float(input("Enter second number: "))
... 
...         if choice == '1':
...             print(f"Result: {num1} + {num2} = {add(num1, num2)}")
...         elif choice == '2':
...             print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
...         elif choice == '3':
...             print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
...         elif choice == '4':
...             print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
...         
...         next_calculation = input("Do you want to perform another calculation? (yes/no): ")
...         if next_calculation.lower() != 'yes':
...             break
...     else:
