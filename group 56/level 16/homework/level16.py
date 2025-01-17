def calculate_factorial(number):
    factorial = 1
    count = number
    while count > 0:
        factorial *= count
        count -= 1
    return factorial

number = int(input("Enter a number: "))
result = calculate_factorial(number)
print(f"The factorial of {number} is {result}.")

correct_username = "admin"
correct_password = "password123"

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username == correct_username and password == correct_password:
        print("Access granted!")
        break
    else:
        print("Incorrect username or password. Please try again.")

count = 10
while count > 0:
    print(count)
    count -= 1

print("Blast off!")

