sentence = "pupsik"
uppercase_sentence = sentence.upper()
print(uppercase_sentence)

user_name = input("თუ შეიძლება შეიყვანეთ თქვენი სახელი): ")
uppercase_name = user_name.upper()
print("თქვენი სახელი არის დიდი ასოებით):", uppercase_name)

def convert_to_uppercase(strings_list):
    uppercase_list = [string.upper() for string in strings_list]
    return uppercase_list
lowercase_strings = ["lanchik", "danchik", "sabaka"]
uppercase_strings = convert_to_uppercase(lowercase_strings)
print(uppercase_strings)

sentence = "REBATA ETO PRIMER TEXTA"
lowercase_sentence = sentence.lower()
print(lowercase_sentence)

email_address = input("vvedite svoi imel Chtob vso spizdit: ")

lowercase_email = email_address.lower()

print("თქვენი იმეილი არის ლოვერ ქეისში):", lowercase_email)



def to_lowercase(mixed_case_string):
    lowercase_string = mixed_case_string.lower()
    return lowercase_string
mixed_case_string = "HeLLo WoRLd!"
lowercase_string = to_lowercase(mixed_case_string)
print(lowercase_string)


sentence = input("შეიყვანეთ წინადადაება: ")
capitalized_sentence = sentence.capitalize()
print("კაპიტულაცია წინადადება:", capitalized_sentence)

def capitalize_first_letter(strings_list):
    capitalized_list = [string.capitalize() for string in strings_list]
    return capitalized_list

lowercase_strings = ["სისკი", "ხუი", "პიზდა"]
capitalized_strings = capitalize_first_letter(lowercase_strings)
print(capitalized_strings)

def capitalize_first_letter(input_string):
    capitalized_string = input_string.capitalize()
    return capitalized_string
example_string = "hello world"
capitalized_string = capitalize_first_letter(example_string)
print(capitalized_string)

def find_first_occurrence(sentence, word):
    position = sentence.find(word)
    return position
sentence = "python eto baza."
word = "Python"
position = find_first_occurrence(sentence, word)
print(f"The first occurrence of the word '{word}' is at position:", position)


def find_substring_position(sentence, substring):
    position = sentence.find(substring)
    return position
sentence = "კაროჩე ია ჩილოვი პარენ."
substring = input("Please enter the substring to search for: ")
position = find_substring_position(sentence, substring)
print(f"The starting index of the substring '{substring}' is:", position)


def find_char_index(input_string, char):
    index = input_string.find(char)
    return index
example_string = "Hello, world!"
char_to_find = 'o'
index = find_char_index(example_string, char_to_find)
print(f"index pupsoida'{char_to_find}' is:", index)


user_string = input("Please enter a string: ")
string_length = len(user_string)
print("The length of the provided string is:", string_length)

def get_string_lengths(strings_list):
    lengths_list = [len(string) for string in strings_list]
    return lengths_list
example_strings = ["sex", "shmeks", "keks"]
lengths = get_string_lengths(example_strings)
print(lengths)

def count_the_word(paragraph):
    words = paragraph.split()
    count = words.count("the")   
    return count
paragraph = "ia sevodno Shol domoi i nechaino obosralsa."
count = count_the_word(paragraph)
print(f"The word 'xui' appears {count} times in the paragraph.")

def count_character_occurrences(input_string, char):
    count = input_string.count(char)
    return count
input_string = "Hello, world!"
char_to_count = input("Please enter a character to count its occurrences: ")
count = count_character_occurrences(input_string, char_to_count)
print(f"The character '{char_to_count}' appears {count} times in the string.")


def count_word_occurrences(text, word):
    words = text.split()
    count = words.count(word)
    return count
text = "fox fox fox fox govno"
word_to_count = "fox"
count = count_word_occurrences(text, word_to_count)
print(f"The word '{word_to_count}' appears {count} times in the text.")


def find_hello_index(input_string):
    index = input_string.find("hello")
    return index
example_string = "Hello chmo kak ti"
index = find_hello_index(example_string)
print(f"The first occurrence of the word 'hello' is at index:", index)

def find_char_index(input_string, char):
    index = input_string.find(char)
    return index
input_string = "prevet pupsik mi teba lubim!"
char_to_find = input("Please enter a character to find its index: ")
index = find_char_index(input_string, char_to_find)
print(f"The index of the character '{char_to_find}' is:", index)

def check_all_lowercase(input_string):
    all_lowercase = input_string.islower()
    return all_lowercase

input_string = "hello world"
result = check_all_lowercase(input_string)
print(f"All characters in the string are lowercase: {result}")

def is_all_lowercase(input_string):
    all_lowercase = input_string.islower()
    return all_lowercase
example_string = "hello world"
result = is_all_lowercase(example_string)
print(f"Is the string '{example_string}' all lowercase? {result}")

def verify_lowercase():
    user_string = input("Please enter a string: ")
    
    is_lowercase = user_string.islower()
    
    if is_lowercase:
        print("The string contains only lowercase letters.")
    else:
        print("The string does not contain only lowercase letters.")

verify_lowercase()

def verify_uppercase():
    user_string = input("Please enter a string: ")
    
    is_uppercase = user_string.isupper()
    
    if is_uppercase:
        print("All characters in the string are uppercase.")
    else:
        print("Not all characters in the string are uppercase.")
        
verify_uppercase()

def is_all_uppercase(input_string):
    all_uppercase = input_string.isupper()
    return all_uppercase
example_string = "HELLO WORLD"
result = is_all_uppercase(example_string)
print(f"Is the string '{example_string}' all uppercase? {result}")

def check_uppercase():
    user_string = input("Please enter a string: ")
    is_uppercase = user_string.isupper()
    if is_uppercase:
        print("The string is in uppercase.")
    else:
        print("The string is not in uppercase.")
check_uppercase()

def replace_dog_with_cat(sentence):
    modified_sentence = sentence.replace("dog", "cat")
    return modified_sentence

sentence = "The quick brown dog jumps over the lazy dog."
modified_sentence = replace_dog_with_cat(sentence)
print(modified_sentence)

def replace_spaces_with_underscores(input_string):

    modified_string = input_string.replace(" ", "_")
    return modified_string


example_string = "Hello world this is a test"
modified_string = replace_spaces_with_underscores(example_string)
print(modified_string)

def swap_case(input_string):
    swapped_string = input_string.swapcase()
    return swapped_string
example_string = "Hello World!"
swapped_string = swap_case(example_string)
print(swapped_string)

def swap_case(sentence):
    swapped_sentence = sentence.swapcase()
    return swapped_sentence

sentence = "Hello World! This is a Test."
swapped_sentence = swap_case(sentence)
print(swapped_sentence)





