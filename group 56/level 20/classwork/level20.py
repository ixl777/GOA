def get_integers(): 
    a = int(input("შეიყვანეთ პირველი მთელი რიცხვი: ")) 
    b = int(input("შეიყვანეთ მეორე მთელი რიცხვი: ")) 
    c = int(input("შეიყვანეთ მესამე მთელი რიცხვი: ")) 
    return a, b, c  
def main():  
    num1, num2, num3 = get_integers()  
    num_list = [num1, num2, num3] 
    print("რიცხვების სია:", num_list) 
if __name__ == "__main__": 
    main()