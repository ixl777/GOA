def manual_index(main_string, search_string):
    for i in range(len(main_string) - len(search_string) + 1):
        if main_string[i:i+len(search_string)] == search_string:
            return i
    return -1

main_string = "გამარჯობა, ეს არის ტესტი"
search_string = "ტესტი"
index = manual_index(main_string, search_string)
print(f"საძიებელი სტრინგი '{search_string}' ნაპოვნია ინდექსზე {index}")

