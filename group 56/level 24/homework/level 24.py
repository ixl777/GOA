#ფუნქცია ხდის კოდს უფრო ადვილს დასაწერათ ფუნქცია არის კოდის ერთერთი ნაწილი ფუნქციები ქმნიან კოდის ორგანიზირებას
my_list = [10, 20, 30, 40, 50]
first_element = my_list[0]
print("პირელი ელემენტი", first_element)
my_list = [10, 20, 30, 40, 50]
last_element = my_list[-1]
print("ბოლო ელემენტი", last_element)
my_list = [10, 20, 30, 40, 50]
first_three_elements = my_list[:3]
print("პირველი სამი ელემენტი", first_three_elements)
my_string = "დანჩიკ"
last_five_chars = my_string[-5:]
print("ბოლო ხუთი ასო:", last_five_chars)
my_string = "ანდრია"
reversed_string = my_string[::-1]
print("შებრუნებული სტრინგი:", reversed_string)
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
every_third_element = my_list[::3]
print("ყოველი მესამე ელემენტი სიიდან:", every_third_element)
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
mid_index = len(my_list) // 2
first_half = my_list[:mid_index]
second_half = my_list[mid_index:]
print("პირველი ნახევარი:", first_half)
print("მეორე ნახევარი:", second_half)
import turtle
screen = turtle.Screen()
screen.setup(width=800, height=800)
def draw_square(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
squares = [
    (-300, 300, 200),    
    (100, 300, 200),     
    (-300, -100, 200),   
    (100, -100, 200)     
]
for x, y, size in squares:
    draw_square(x, y, size)
turtle.hideturtle()
turtle.done()


