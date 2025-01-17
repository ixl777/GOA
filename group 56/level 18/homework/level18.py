def check_even_odd(number):
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

number = int(input("Enter a number: "))
result = check_even_odd(number)
print(result)

def check_positive_negative(number):
    if number > 0:
        return "The number is positive."
    elif number < 0:
        return "The number is negative."
    else:
        return "The number is zero."
number = float(input("Enter a number: "))
result = check_positive_negative(number)
print(result)

def is_divisible_by_5(number):
    if number % 5 == 0:
        return "The number is divisible by 5."
    else:
        return "The number is not divisible by 5."
number = int(input("Enter a number: "))
result = is_divisible_by_5(number)
print(result)

def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
count = 0
while count < 5:
    number = int(input("Enter a number: "))
    result = check_even_odd(number)
    print(f"The number {number} is {result}.")
    count += 1

correct_password = "Goa best"
attempts = 0

while True:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted!")
        break
    else:
        attempts += 1
        print("Incorrect password. Try again.")

print(f"Number of incorrect attempts: {attempts}")

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero is not allowed."
    else:
        return "Invalid operator."

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

result = calculate(num1, num2, operator)
print(f"The result is: {result}")



