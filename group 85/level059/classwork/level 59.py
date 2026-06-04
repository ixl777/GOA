numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = [True if n % 2 != 0 else False for n in numbers]
print(results)
fruits = ["ვაშლი", "მსხალი", "ატამი"]
print(f"მე მიყვარს {fruits[2]}")
numbers = [10, 20, 30, 40]
total = 0
for n in numbers:
    total += n
print(total)
numbers = [5, 12, 8, 25, 3]
min_num = numbers[0]
for n in numbers:
    if n < min_num:
        min_num = n
print(min_num)