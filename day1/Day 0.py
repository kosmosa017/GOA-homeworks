from turtle import*

#we want to paint house
goto(0, -100)
#step 1:  draw a square

width(7)
color("brown")
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
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 100)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("brown")
left(30)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
exitonclick()