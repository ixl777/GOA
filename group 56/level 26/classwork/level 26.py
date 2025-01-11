def greet(andria):
    print(f"გამარჯობა, {andria}")
greet("თქვენი სახელი")



def manual_range(start,end,step):
   for number in range(start,end,step):
    if number % 2==0:
        print(number)


manual_range(0, 10, 1)  
manual_range(5, 25, 2)  
manual_range(10, 0, -1)  
manual_range(1, 10, 3)  
manual_range(2, 20, 4)  


def manual_len(my_list):
    count = 0
    for item in my_list:
        count += 1
    return count


test_list = [1, 2, 3, 4, 5]
length = manual_len(test_list)
print("სიის სიგრძე არის:", length)
