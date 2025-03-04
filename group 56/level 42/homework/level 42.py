my_dict = {
    "a": 1,
    "b": 2,
    "g": 3,
    "e": 4,
    "v": 5
}

keys = my_dict.keys()
print(keys)


my_dict = {
    "ab": 1,
    "gd": 2,
    "ev": 3,
    "zt": 4,
    "ik": 5
}


values = my_dict.values()
print(values)

my_dict = {
    "ada": 1,
    "daa": 2,
    "d": 3,
    "ddd": 4,
    "aaa": 5
}

items = my_dict.items()
print(items)


my_dict = {
    "ada": 1,
    "daa": 2,
    "d": 3,
    "ddd": 4,
    "aaa": 5
}

for key, value in my_dict.items():
    print(f"{key}: {value}")


my_dict = {
    "zz": 1,
    "ssss": 2,
    "dddd": 3,
    "dddaaaa": 4,
    "ooo": 5
}

for key, value in my_dict.items():
    print(f"{key}: {value}")


my_dict = {
    "zz": 1,
    "ssss": 2,
    "dddd": 3,
    "dddaaaaee": 4,
    "ooo": 5
}

key_to_check = "zz"
if key_to_check in my_dict:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")

my_dict = {
    "apple": 1,
    "zz": 1,
    "ssss": 2,
    "dddd": 3,
    "dddaaaaee": 4,
    "ooo": 5
}

key_to_retrieve = "zz"
value = my_dict.get(key_to_retrieve, "Key not found")
print(f"The value for '{key_to_retrieve}' is: {value}")

key_to_retrieve = "xyi"
value = my_dict.get(key_to_retrieve, "Key not found")
print(f"The value for '{key_to_retrieve}' is: {value}")


my_dict = {
    "apple": 1,
    "zz": 2,
    "ssss": 3,
    "dddd": 4,
    "dddaaaaee": 5,
    "ooo": 6
}

my_dict["xyi"] = 7
print(my_dict)


my_dict = {
    "apple": 1,
    "zz": 2,
    "ssss": 3,
    "dddd": 4,
    "dddaaaaee": 5,
    "ooo": 6
}

my_dict.pop("zz")
print(my_dict)


my_dict = {
    "apple": 1,
    "zz": 2,
    "ssss": 3,
    "dddd": 4,
    "dddaaaaee": 5,
}
additional_dict = {
    "xui": 6,
    "govno": 7,
    "nado": 8  
}
my_dict.update(additional_dict)
print(my_dict)

my_dict = {
     "apple": 1,
    "zz": 2,
    "ssss": 3,
    "dddd": 4,
    "dddaaaaee": 5,
}
dictionary_length = len(my_dict)
print(dictionary_length)



def sum_of_values(my_dict):
    total = 0
    for value in my_dict.values():
        if isinstance(value, (int, float)):
            total += value
    return total
my_dict = {
    "apple": 1,
    "zz": 2,
    "ssss": 3,
    "dddd": 4,
    "dddaaaaee": 5,
    "ooo": 6.5
}
result = sum_of_values(my_dict)
print(result)

my_dict = {
    "apple": 1,
    "zz": 2,
    "ssss": 3,
    "dddd": 4,
    "dddaaaaee": 5,
    "ooo": 6
}
my_dict.clear()
print(my_dict)

