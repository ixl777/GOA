def say_hello():
    print("Hello, World!")


def print_sum(num1, num2):
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is: {sum}")
print_sum(5, 3)

def multiply_by_ten(num):
    return num * 10
result = multiply_by_ten(5)
print(result)  

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Andria")  
greet()        

def outer_function():
    def inner_function():
        print("Hello from the inner function!")
    
    print("Hello from the outer function!")
    inner_function()

outer_function()
def check_even_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")


numbers_list = [1, 2, 3, 4, 5, 6]
check_even_odd(numbers_list)

def find_maximum(numbers):
    if not numbers:  
        return None  
    
    max_num = numbers[0]  
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

numbers_list = [3, 5, 2, 8, 1, 4]
max_number = find_maximum(numbers_list)
print(f"The maximum number in the list is: {max_number}")

def filter_positive_numbers(numbers):
    positive_numbers = []
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)
    return positive_numbers

numbers_list = [-2, 3, -5, 8, -1, 4, 0]
positive_numbers = filter_positive_numbers(numbers_list)
print(f"The list of positive numbers is: {positive_numbers}")

def sum_divisible_by_3(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        if num % 3 == 0:
            total_sum += num
    return total_sum

result = sum_divisible_by_3(1, 100)
print(f"The total sum of numbers divisible by 3 from 1 to 100 is: {result}")

