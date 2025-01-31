number = int(input("Enter a number: "))
if number % 2 == 0:
    print("even")
else:
    print("odd")
numbers = [1, 15, 9, 12, 18, 7, 25, 4, 11]
for number in numbers:
    if number > 10:
        print(number)
numbers = [1, 15, 9, 12, 18, 7, 25, 4, 11]
for number in numbers:
    if number > 10:
        print(number)
numbers = [3, 8, 2, 9, 6, 7, 5, 4, 11, 10]
first_element = numbers[0]
last_element = numbers[-1]

difference = first_element - last_element
sum_result = first_element + last_element
product = first_element * last_element

print(f"Difference: {difference}")
print(f"Sum: {sum_result}")
print(f"Product: {product}")
index = int(input("Enter a number: "))
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

if 0 <= index < len(names):
    print(f"Element at index {index}: {names[index]}")
else:
    print("Index out of range")
