def check_parity(number):
    if number % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"
def power_calculation(number):
    if number >= 0:
        return number ** 2
    else:
        return number ** 3
    
def find_max(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
            
    return max_value
arr = [1, 2, 10, -20, 30, 100, 5]
print(find_max(arr)) 