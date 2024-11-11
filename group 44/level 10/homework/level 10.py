number1 =int(input("შეიყვანეთ რიცხვი: "))
for digit in range(number1):
    print(digit)


number2 =int(input("შეიყვანეთ რიცხვი: "))
for digit in range(number2,-1,-1):
    print(digit)


number3 =int(input("შეიყვანეთ რიცხვი: "))
i=1
while i<=number3:
    print(i) 
    i+=2



number4 =int(input("შეიყვანეთ რიცხვი: "))
for i in range(0,number4+1,2):
    print(i)
    

# იტერაცია(ერთიდაიგივე მოქმედების ბევრჯერ გამეორება
#for ციკლი მუშაობს ისე რომ ის იხურება იმის მიხრდვით თუ რა მნიშვნელობა აქვს ცვლადს
#while ციკლი მუშაობს ისე რომ მანამდე სანამ რაიმე პირობა ჭეშმარიტია ციკლი იმუსავებს
