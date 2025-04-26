# 2. User Input Number Division
def divide_numbers():
    """
    Asks the user for two numbers and divides them, handling potential errors.
    """
    try:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        num1 = float(num1)
        num2 = float(num2)
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = num1 / num2
        print(f"Result of division: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def access_list_index():
    """
    Creates a list and asks the user for an index, handling potential errors.
    """
    my_list = [10, 20, 30, 40, 50]
    print(f"The list is: {my_list}")
    try:
        index = int(input("Enter the index to access: "))
        if index < 0:
            raise IndexError("Index cannot be negative")
        value = my_list[index]
        print(f"Value at index {index}: {value}")
    except IndexError:
        print("Index is out of range.")
    except ValueError:
        print("Invalid input. Please enter an integer for the index.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def access_dictionary_key():
    """
    Creates a dictionary and tries to access a key, handling potential errors.
    """
    my_dict = {"a": 1, "b": 2, "c": 3}
    print(f"The dictionary is: {my_dict}")
    try:
        key = input("Enter the key to access: ")
        value = my_dict[key]
        print(f"Value for key '{key}': {value}")
    except KeyError:
        print(f"Key '{key}' not found in the dictionary.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def convert_string_to_integer():
    """
    Asks the user for a number and converts it to an integer, handling potential errors.
    """
    number_str = input("Enter a number: ")
    try:
        number_int = int(number_str)
        print(f"Integer value: {number_int}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Calls all the functions.
    """
    print("2. User Input Number Division")
    divide_numbers()
    print("\n3. List Index Access")
    access_list_index()
    print("\n4. Dictionary Key Access")
    access_dictionary_key()
    print("\n5. Convert String to Integer")
    convert_string_to_integer()
    
if __name__ == "__main__":
    main()

def greet(func):
    """
    Takes a function as an argument and calls it to print a greeting.

    Args:
        func: A function that prints a greeting.
    """
    func()

def say_hello():
    print("Hello!")

def say_welcome():
    print("Welcome!")

def multiplier(factor):
    """
    Returns a function that multiplies a number by a given factor.

    Args:
        factor: The factor to multiply by.

    Returns:
        A function that takes a number and returns the product of that number and the factor.
    """
    def multiply_by_factor(number):
        return number * factor
    return multiply_by_factor

def main():
    """
    Calls all the functions.
    """
    print("2. User Input Number Division")
    divide_numbers()
    print("\n3. List Index Access")
    access_list_index()
    print("\n4. Dictionary Key Access")
    access_dictionary_key()
    print("\n5. Convert String to Integer")
    convert_string_to_integer()
    print("\n6. Function as Argument – Greeting")
    greet(say_hello)  
    greet(say_welcome)
    print("\n7. Return a Function – Multiplier")
    multiply_by_5 = multiplier(5)  
    print(multiply_by_5(10))  
    multiply_by_3 = multiplier(3)
    print(multiply_by_3(7))

if __name__ == "__main__":
    main()
