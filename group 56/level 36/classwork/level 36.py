def multiply(a, b):
    return a * b


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def number_to_string(num):
    return str(num)

def solution(string):
    return string[::-1]

def make_negative( number ):
    return -abs(number)
def opposite(number):
    return number * -1


def bool_to_word(boolean):
    return "Yes" if boolean else "No"

def positive_sum(arr):
    return sum(x for x in arr if x > 0)

def repeat_str(repeat, string):
    return string * repeat

def remove_char(s):
    return s[1:-1]

def square_sum(numbers):
    return sum(x**2 for x in numbers)

numbers = [1, 2, 3, 4]
print(square_sum(numbers))  

