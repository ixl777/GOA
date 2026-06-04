age=int(input("enter your age"))
if age >= 18:
    print("you can vote")
else:
    print("you cant vote")


student_score = 67
if student_score >= 90:
    print("A - ფრიადი")
elif 80 <= student_score <= 89:
    print("B - ძალიან კარგი") 
elif student_score < 40:
    print("F - ძალიან ცუდი შედეგი")
else:
    print("შედეგი საშუალოა (C/D)")


temp = 25  
if temp >= 30:
    print("ძალიან ცხელა, ფრთხილად იყავით")
elif 20 <= temp <= 29:
    print("კარგი ამინდია")
elif 10 <= temp <= 19:
    print("ცივა, თბილად ჩაიცვი")
else:
    print("ძალიან ცივა, სახლში დარჩი")