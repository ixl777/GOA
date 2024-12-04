elements = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = int(input("შეიყვანეთ ინდექსი (0-9): ")) 
if 0 <= index < len(elements): 
    print("ელემენტი ინდექსზე", index, "არის:", elements[index])
else: 
    print("ინდექსი არასწორია!")


mutable_list = [1, 2, 3]
mutable_list[0] = 10  
print(mutable_list) 
[10, 2, 3]  
immutable_str = "hello" 
immutable_str = "H"  
new_str = immutable_str.replace("h", "H") 
print(new_str) 