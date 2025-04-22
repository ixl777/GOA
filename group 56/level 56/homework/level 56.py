#1) codewars
def expression_matter(a, b, c):
    return max(a + b + c, a * b * c, (a + b) * c, a * (b + c))
print(expression_matter(1, 2, 3))

def how_much_i_love_you(nb_petals):
    phrases = [
        "I love you",
        "a little",
        "a lot",
        "passionately",
        "madly",
        "not at all"
    ]
    return phrases[(nb_petals - 1) % len(phrases)]
print(how_much_i_love_you(7)) 

def reverse_list(l):
    return l[::-1]
print(reverse_list([1, 2, 3, 4]))  

def odd_count(n):
    return n // 2
print(odd_count(10))  
print(odd_count(15)) 

def find_difference(a, b):
    return abs((a[0] * a[1] * a[2]) - (b[0] * b[1] * b[2]))
print(find_difference([2, 3, 4], [1, 2, 3])) 

def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"
print(people_with_age_drink(13))  
print(people_with_age_drink(17)) 
print(people_with_age_drink(20))  
print(people_with_age_drink(30))  

def two_sort(array):
    return "***".join(sorted(array)[0])

print(two_sort(["hello", "world", "python"])) 

la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals
print(total_goals) 

def solution(a, b):
    return a + b + a if len(a) < len(b) else b + a + b

print(solution("hello", "world"))  
print(solution("short", "longer"))  
print(solution("abc", ""))  

def find_multiples(integer, limit):
    return [num for num in range(integer, limit + 1, integer)]
print(find_multiples(3, 15))  
print(find_multiples(5, 25)) 

def create_array(n):
    res = []
    i = 1
    while i <= n:
        res.append(i)
        i += 1
    return res
def create_array(n):
    return list(range(1, n + 1))

# 2) Print your name
print("Andria")

# 3) Print a favorite quote
print('"The only way to do great work is to love what you do." - Steve Jobs')

# 4) Print multiple lines (short poem or message)
print("Roses are red,")
print("Violets are blue,")
print("Coding is fun, and so are you!")

# 5) Print a simple math result
print(2 + 3)

# 6) Print a shape with symbols (a simple triangle)
print("  *  ")
print(" *** ")
print("*****")

# 7) Convert string to integer
num_str = "42"
num_int = int(num_str)
print(num_int)

# 8) Add two floats
float1 = 3.5
float2 = 2.5
print(float1 + float2)

# 9) Concatenate two strings
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)

# 10) Create variables of different types and print their types
int_var = 10
str_var = "Hello"
float_var = 3.14

print(type(int_var))
print(type(str_var))
print(type(float_var))

# 11) User input and type conversion (age next year)
age = int(input("Enter your age: "))
print("Next year, you will be", age + 1)

# 12) Ask for your name
name = input("What is your name? ")
print("Hello, " + name + "!")

# 13) Ask for age and calculate next year's age
age = int(input("Enter your age: "))
print("Next year, you will be", age + 1)

# 14) Simple calculator: addition
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The sum is:", num1 + num2)

# 15) Favorite color
color = input("What is your favorite color? ")
print("Your favorite color is " + color + "!")

# 16) Check if the user is tall enough
height = int(input("Enter your height in cm: "))
if height > 150:
    print("You are tall enough!")
else:
    print("You are not tall enough.")

# 17) Print numbers from 1 to 5 using a loop
for i in range(1, 6):
    print(i)

# 18) Print each letter of a string
word = "Python"
for letter in word:
    print(letter)

# 19) Sum of numbers 1 to 10
sum_total = 0
for num in range(1, 11):
    sum_total += num
print("Sum from 1 to 10:", sum_total)

# 20) Print a multiplication table (1 to 5) for the number 2
for i in range(1, 6):
    print(f"2 x {i} =", 2 * i)

# 21) Print all even numbers between 2 and 20 (inclusive)
for num in range(2, 21, 2):
    print(num)

# 22) Print numbers from 1 to 5 using a while loop
i = 1
while i <= 5:
    print(i)
    i += 1

# 23) Sum of numbers 1 to 5 using a while loop
i = 1
sum_total = 0
while i <= 5:
    sum_total += i
    i += 1
print("Sum from 1 to 5:", sum_total)

# 24) Count down from 10 to 1 using a while loop
i = 10
while i >= 1:
    print(i)
    i -= 1

# 25) Print all odd numbers between 1 and 10 using a while loop
i = 1
while i <= 10:
    print(i)
    i += 2

# 26) Ask for user input until they enter "exit"
while True:
    user_input = input("Enter something (type 'exit' to stop): ")
    if user_input.lower() == "exit":
        break
    print("You entered:", user_input)

# 27) Print all elements of a list
items = ["apple", "banana", "cherry"]
for item in items:
    print(item)

# 28) Find the length of a list
my_list = [10, 20, 30, 40, 50]
print("Length of the list:", len(my_list))

# 29) Access a specific element from the list
numbers = [5, 10, 15, 20]
print("Second element:", numbers[1])

# 30) Add an element to the list
my_list = ["dog", "cat", "rabbit"]
my_list.append("hamster")
print("Updated list:", my_list)

# 31) Remove an element from the list
animals = ["lion", "tiger", "bear"]
animals.remove("tiger")
print("List after removal:", animals)

# 32) Create a list of squares
squares = [x**2 for x in range(1, 6)]
print("List of squares:", squares)

# 33) Create a list of even numbers
evens = [x for x in range(2, 11, 2)]
print("List of even numbers:", evens)

# 34) Filter odd numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odds = [x for x in numbers if x % 2 != 0]
print("List of odd numbers:", odds)

# 35) Convert a list of strings to uppercase
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print("Uppercase list:", uppercase_words)

# 36) Create a list of numbers squared if they are divisible by 2
numbers = [1, 2, 3, 4, 5, 6]
squared_evens = [num**2 for num in numbers if num % 2 == 0]
print("Squares of even numbers:", squared_evens)

# 37) Function to greet a user
def greet(name):
    print(f"Hello, {name}!")

greet("Andria")

# 38) Function to add two numbers
def add_numbers(a, b):
    return a + b

print("Sum:", add_numbers(5, 7))

# 39) Function to check if a number is even or odd
def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

print("Number type:", check_even_odd(10))

# 40) Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

print("Rectangle area:", rectangle_area(5, 3))

# 41) Function to reverse a string
def reverse_string(s):
    return s[::-1]

print("Reversed string:", reverse_string("Python"))

# 42) Create and print a tuple
my_tuple = (42, "hello", 3.14)
print("Tuple:", my_tuple)

# 43) Access an element in a tuple
my_tuple = ("apple", "banana", "cherry", "date")
print("Second element:", my_tuple[1])

# 44) Find the length of a tuple
tuple_example = (10, 20, 30, 40, 50)
print("Length of the tuple:", len(tuple_example))

# 45) Concatenate two tuples
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
combined_tuple = tuple1 + tuple2
print("Concatenated tuple:", combined_tuple)

# 46) Check if an item exists in a tuple
my_tuple = ("red", "blue", "green", "yellow")
search_item = "blue"

if search_item in my_tuple:
    print("Found")
else:
    print("Not found")

# 47) Create and print a set
my_set = {1, "hello", 3.14}
print("Set:", my_set)

# 48) Check if an element is in a set
my_set = {"red", "blue", "green"}
if "blue" in my_set:
    print("Yes")
else:
    print("No")

# 49) Add an element to a set
my_set = {10, 20, 30}
my_set.add(40)
print("Updated set:", my_set)

# 50) Remove an element from a set
my_set = {"apple", "banana", "cherry"}
my_set.remove("banana")
print("Set after removal:", my_set)

# 51) Find the union of two sets
set1 = {1, 2, 3}
set2 = {"a", "b", "c"}
union_set = set1 | set2
print("Union of sets:", union_set)

# 52) Create and print a dictionary
my_dict = {"name": "Andria", "age": 25}
print("Dictionary:", my_dict)

# 53) Access a value by key
print("Name:", my_dict["name"])

# 54) Add a new key-value pair to a dictionary
my_dict["city"] = "Tbilisi"
print("Updated dictionary:", my_dict)

#55) codewars
a = "code"
b = "wa.rs"
name = a + b
print(name)  

#56) codewars
def get_char(c):
    return chr(c)

print(get_char(65))  