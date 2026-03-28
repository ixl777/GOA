age = 27
if age < 18:
    print("შენ ჯერ არასრულწლოვანი ხარ")
elif 18 <= age <= 65:
    print("შენ სრულწლოვანი ხარ")
else:
    print("შენ პენსიონერი ხარ")

username = input("შეიყვანეთ სახელი: ")
password = input("შეიყვანეთ პაროლი: ")
if username == "admin":
    if password == "12345":
        print("მოგესალმებით, მიხარია რომ დაბრუნდით!")
    else:
        print("პაროლი არასწორია!")
else:
    print("მომხმარებელი ვერ მოიძებნა!")


#