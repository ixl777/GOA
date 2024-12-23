
#Slicing არის მეთოდი, რომელიც გამოიყენება მონაცემთა სტრუქტურების (მაგალითად, სიების, სტრინგების) ქვე-მონაცემთა სახით ამოღებისათვის. Python-ში სლაისინგი საშუალებას გვაძლევს, ავიღოთ ელემენტების ქვეჯგუფი მონაცემთა სტრუქტურიდან, გამოყენებით ინდექსების დიაპაზონის.
my_list = ["andria", "Danchik", "launch", "mate", "luka", "luka2x", "luka3x", "luka4x", "gio", "andria2x"]  
for element in my_list: 
    print(element)

my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

num1 = int(input("შეიყვანეთ პირველი რიცხვი (num1): "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი (num2): "))

list_length = len(my_list)

if num1 > num2:
    sliced_list = my_list[num2:num1]
    print("ახალი სია (num1 > num2):", sliced_list)
elif num2 > num1:
    sliced_list = my_list[num1:num2]
    print("ახალი სია (num2 > num1):", sliced_list)
else:
    print("ახალი სია:", [])

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

first_element = numbers[0]
third_element = numbers[2]
last_element = numbers[-1]

print("პირველი ელემენტი არის:", first_element)
print("მესამე ელემენტი არის:", third_element)
print("ბოლო ელემენტი არის:", last_element)

string_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

reversed_list = string_list[::-1]

print("უკუმიმართულებით სია:", reversed_list)


words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

every_second_word = words[::2]

print("თითოეული მეორე ელემენტი:", every_second_word)

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

numbers[3] = 100

print("შეცვლილი სია:", numbers)


