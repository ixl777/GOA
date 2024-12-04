# კვირის დღეების სია
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# პირველი და ბოლო დღის ამოღება და დაბეჭდვა
print("პირველი დღე:", days[0])
print("ბოლო დღე:", days[-1])

# მესამე ელემენტის შეცვლა ახალ მნიშვნელობაზე
days[2] = "Midweek"
print("განახლებული სია:", days)

animals = []
for i in range(5):
    animal = input("შეიყვანეთ საყვარელი ცხოველის სახელი: ")
    animals.append(animal)


print("პირველი ცხოველი:", animals[0])
print("ბოლო ცხოველი:", animals[-1])

# მეორე ცხოველის სახელის შეცვლა
new_animal = input("შეიყვანეთ ახალი სახელი მეორე ცხოველისთვის: ")
animals[1] = new_animal
print("განახლებული სია:", animals)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

third_elements = numbers[2::3]
print("ყოველი მესამე ელემენტი:", third_elements)

reversed_list = numbers[::-1]
print("უკუღმა სია:", reversed_list)

middle_six = numbers[3:9]
print("შუა 6 ელემენტი:", middle_six)


numbers = list(range(1000, 10001, 500))

first_five = numbers[:5]
print("პირველი ხუთი რიცხვი:", first_five)

every_third = numbers[::3]
print("ყოველი მესამე რიცხვი:", every_third)

count_elements = len(numbers)
print("სულ ელემენტები სიაში:", count_elements)

numbers_input = input("შეიყვანეთ 10 რიცხვი მძიმით გამოყოფილად: ")
numbers_list = [int(x) for x in numbers_input.split(",")]

first_three = numbers_list[:3]
print("პირველი სამი რიცხვი:", first_three)

middle_four = numbers_list[3:7]
print("შუა ოთხი რიცხვი:", middle_four)

if numbers_list[-1] == 10:
    print("ბოლო ელემენტი არის 10.")
else:
    print("ბოლო ელემენტი არ არის 10.")