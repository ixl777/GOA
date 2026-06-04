numbers = [1, 15, 8, 22, 5, 30]
result = [x for x in numbers if x > 10]
print(result) 

cities = ["tbilisi", "qutaisi", "batumi"]
for city in cities:
    print(f"me vcxovrob: {city}-shi")


numbers = [10, 20, 30, 40, 50]
sum_first_last = numbers[0] + numbers[-1]
print(sum_first_last) 

numbers = [1, 2, 3, 4, 5]
print(numbers[::-1]) 

numbers = [10, -5, 3, -1, -8, 0, 7]
negative_count = len([x for x in numbers if x < 0])
print(negative_count)

names = ["andria", "amiko", "luka", "danieli"]
user_input = input("enter your name: ")

if user_input in names:
    print(names.index(user_input))
else:
    print("-1")