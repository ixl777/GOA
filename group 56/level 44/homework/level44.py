def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.questions = [
            {"question": "What is the capital of France?", "choices": ["Paris", "London", "Rome", "Berlin"], "answer": "Paris"},
            {"question": "What is 2 + 2?", "choices": ["3", "4", "5", "6"], "answer": "4"},
            {"question": "What is 4 + 4", "choices": ["3", "4", "7", "8"], "answer": "8"},
        ]

number = int(input("შემოიტანეთ რიცხვი: "))

sum_of_numbers = 0
for i in range(0, number + 1):
    sum_of_numbers += i

print(f"0-დან {number}-მდე რიცხვების ჯამი არის: {sum_of_numbers}")



my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"] 
number = int(input("შეიყვანეთ რიცხვი: "))  
list_length = len(my_list)  
if 0 <= number < list_length: 
    print("ელემენტი ამ ინდექსზე არის:", my_list[number]) 
elif -list_length <= number < 0: 
    print("ელემენტი ამ ინდექსზე არის:", my_list[number]) 
else: print("მოცემული ინდექსი არასწორია.")

list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]  
for element in list1: 
    multiplied = element * 2 
    divided = element / 2 
    print(f"ელემენტი: {element}, გამრავლებული 2-ზე: {multiplied}, გაყოფილი 2-ზე: {divided}")    


def past(h, m, s):
    sum_of_seconds = 0

    sum_of_seconds += h * 3600
    
    sum_of_seconds += m * 60
    
    sum_of_seconds += s
    
    result = sum_of_seconds * 1000
    
    return result
