from turtle import *

#we want to paimt a house 

#step 1: draw a square
speed(10)
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
#emd of wquare

#drawimg a door

begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#drawing a window

color("brown")
penup()
goto(180, 170)
pendown()




right(150)
forward(10)
right(270)
forward(30)
right(270)
forward(50)
right(270)
forward(30)
right(270)
forward(40)
right(180)
forward(20)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(16)
right(90)
forward(50)




penup()
goto(10, 170)
pendown()




forward(40)
right(270)
forward(30)
right(270)
forward(50)
right(270)
forward(30)
right(270)
forward(30)
right(270)
forward(30)
right(270)
forward(30)
right(270)
forward(15)
right(270)
forward(50)








exitonclick()