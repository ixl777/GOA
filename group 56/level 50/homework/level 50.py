try:
    user_input = input("Please enter a number: ")

    number = float(user_input)
    print(f"You entered the number: {number}")

except ValueError:
    print("Error: That is not a valid number!")



try:
    my_list = [1, 2, 3]

    print(my_list[5])

except IndexError:
    print("Error: The index you tried to access does not exist in the list.")
try:
    result = 5 + "hello"

except TypeError as e:
    print(f"TypeError occurred: {e}")


