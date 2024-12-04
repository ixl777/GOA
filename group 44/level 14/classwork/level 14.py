elements = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]  
start_index = int(input("შეიყვანეთ დასაწყისის ინდექსი (0-9): ")) 
end_index = int(input("შეიყვანეთ დასასრულის ინდექსი (0-9): "))  
if 0 <= start_index < len(elements) and 0 <= end_index < len(elements): 
    print("ელემენტები დიაპაზონში:", elements[start_index:end_index+1]) 
else: 
    print("არასწორი ინდექსები!")

names = ["ანა", "ბორის", "ვერა", "გლებ", "დინა"]  
index = int(input("შეიყვანეთ ინდექსი (0-4): "))
if 0 <= index < len(names): 
    print("ელემენტი ინდექსზე", index, "არის:", names[index]) 
else: 
    print("ინდექსი არასწორია!")


user_name = input("შეიყვანეთ თქვენი სახელი: ")  
my_name = "კოპილოტი"  
result = user_name[:3] + my_name[-2:] 
print("შედეგი:", result)


my_list = [1, 2, 3, 4] 
print(my_list[2])

my_list = [1, 2, 3, 4, 5] 
print(my_list[1:4]) 


surname = input("შეიყვანეთ თქვენი გვარი: ") 
reversed_surname = surname[::-1]  
print("თქვენი გვარი:", surname) 
print("შებრუნებული გვარი:", reversed_surname)

