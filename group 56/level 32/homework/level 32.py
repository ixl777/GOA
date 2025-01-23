def welcome_message(name, age):
    return f"Welcome, {name}! You are {age} years old."
print(welcome_message("Andria", 14))
def format_name(first_name, last_name):
    capitalized_first_name = first_name.capitalize()
    capitalized_last_name = last_name.capitalize()
    return f"{capitalized_first_name} {capitalized_last_name}"

print(format_name("andria", "gobejishvili"))

def reverse_string_format(sentence):
    reversed_string = sentence[::-1]
    return f"The reversed string is: {reversed_string}"

print(reverse_string_format("privet vsem pupsiki"))


def insert_word(sentence, word, index):
    words = sentence.split()
    words.insert(index, word)
    return ' '.join(words)

print(insert_word("privet ia andrei", "andria", 3))


def sentence_to_words(sentence):
    words = sentence.split()
    return words

print(sentence_to_words("tipo ok "))

def csv_to_list(csv_string):
    items = csv_string.split(',')
    return [item.strip() for item in items]

print(csv_to_list("pp, cc, kk, aa"))


def csv_to_list(csv_string):
    items = csv_string.split(',')
    return [item.strip() for item in items]

print(csv_to_list("pp, cc, kk, aa"))

def split_into_sentences(paragraph):
    sentences = paragraph.split('. ')
    return [sentence.strip() for sentence in sentences if sentence]

print(split_into_sentences("agtgtgtgt. gtiithjihjyihjy. hjiyhjyijhiyjhyijhyi."))

def append_to_list(lst, item):
    lst.append(item)
    return lst

my_list = [1, 2, 3]
new_item = 4
print(append_to_list(my_list, new_item))

def append_items_to_list(lst, items):
    for item in items:
        lst.append(item)
    return lst

my_list = [1, 2, 3]
new_items = [4, 5, 6]
print(append_items_to_list(my_list, new_items))

def append_all_elements(list1, list2):
    list1.extend(list2)
    return list1

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(append_all_elements(list_a, list_b))


def insert_item_at_index(lst, index, item):
    lst.insert(index, item)
    return lst

my_list = [1, 2, 3, 5]
new_item = 4
index = 3
print(insert_item_at_index(my_list, index, new_item))

def insert_item_at_beginning(lst, item):
    lst.insert(0, item)
    return lst

my_list = [2, 3, 4, 5]
new_item = 1
print(insert_item_at_beginning(my_list, new_item))

def insert_item_at_end(lst, item):
    lst.insert(len(lst), item)
    return lst

my_list = [1, 2, 3, 4]
new_item = 5
print(insert_item_at_end(my_list, new_item))


