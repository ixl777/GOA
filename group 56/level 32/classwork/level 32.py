def generate_big_sentence(name, surname, age):
    print("My name is {} {} and I am {} years old.".format(name, surname, age))

name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")

generate_big_sentence(name, surname, age)

def generate_big_sentence(name, surname, age):
    print(f"My name is {name} {surname} and I am {age} years old.")

name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
generate_big_sentence(name, surname, age)

def my_split(main_string, string_to_split):
    split_list = main_string.split(string_to_split)
    print(split_list)

main_string = input("Enter the main string: ")
string_to_split = input("Enter the string to split by: ")

my_split(main_string, string_to_split)


def manual_append(main_list, item_to_insert):
    main_list.insert(len(main_list), item_to_insert)
main_list = [1, 2, 3]
item_to_insert = 4

manual_append(main_list, item_to_insert)
print(main_list)





