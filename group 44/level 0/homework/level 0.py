from turtle import *


#step
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#roof
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end roof


#first window

penup()
goto(200,175)
pendown()
right(60)
color("brown")
begin_fill()
forward(60)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#end first window

#second window
penup()
goto(1,175)
pendown()
right(90)
color("brown")
begin_fill()
forward(60)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

#end second window







exitonclick()