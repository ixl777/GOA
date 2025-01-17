
name = input("შეიყვანეთ თქვენი სახელი: ")

choice = input("შეიყვანეთ არჩევანი ('u' ან 'l'): ")

if choice == 'u':
    print(name.upper())
elif choice == 'l':
    print(name.lower())
else:
    print("wrong information")


def manual_find(main_string, str_to_find):
    for i in range(len(main_string) - len(str_to_find) + 1):
        if main_string[i:i+len(str_to_find)] == str_to_find:
            return i
    return -1
print(manual_find("hello world", "world")) 
print(manual_find("hello world", "python")) 


main_str = input("შეიყვანეთ მთავარი სთრინგი: ")
str_to_count = input("შეიყვანეთ დასათვლელი სთრინგი: ")
count = main_str.count(str_to_count)
print(f"{str_to_count} შეგხვდება {count} ჯერ მთავარ სთრინგში.")


def manual_swapcase(s):
    new_string = ""
    for char in s:
        if char.isupper():
            new_string += char.lower()
        elif char.islower():
            new_string += char.upper()
        else:
            new_string += char
    return new_string
print(manual_swapcase("Hello World!")) 
print(manual_swapcase("Python123")) 
