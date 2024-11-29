import turtle

# Screen
turtle.setup (800,1000)

#Base of house
turtle.penup()
turtle.goto(-350,-230)
turtle.width(3)
turtle.pendown()
turtle.forward(270)
turtle.left(90)
turtle.forward(290)
turtle.left(90)
turtle.forward(270)
turtle.left(90)
turtle.forward(290)

# Roof Seal
turtle.penup()
turtle.goto(-80,60)
turtle.left(90)
turtle.pendown()
turtle.forward(30)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(330)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(30)
turtle.penup()

# Roof
turtle.goto(-380,80)
turtle.left(45)
turtle.pendown()
turtle.forward(100)
turtle.right(45)
turtle.forward(190)
turtle.right(45)
turtle.forward(100)
turtle.penup()

# Chimney
turtle.goto(-185,153)
turtle.left(135)
turtle.pendown()
turtle.forward(32)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(32)
turtle.penup()

# Chimney Line
turtle.goto(-185,176)
turtle.left(90)
turtle.pendown()
turtle.forward(30)
turtle.penup()

# 2nd Story Room 1 (base)
turtle.goto(-305,127)
turtle.pendown()
turtle.forward(45)
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(45)
turtle.penup()

# 2nd Story Room 1 (roof)
turtle.goto(-306,172)
turtle.left(150)
turtle.pendown()
turtle.forward(50)
turtle.right(125)
turtle.forward(50)
turtle.penup()

# 2nd Story Room 2 (base)
turtle.goto(-250,130)
turtle.left(65)
turtle.pendown()
turtle.forward(45)
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(45)
turtle.penup()

# 2nd Story Room 2 (roof)
turtle.goto(-249,173)
turtle.left(150)
turtle.pendown()
turtle.forward(45)
turtle.right(120)
turtle.forward(45)
turtle.penup()

# 2nd Story Room (Lines)
turtle.goto(-297,170)  # 1st Room
turtle.right(30)
turtle.pendown()
turtle.forward(42)
turtle.penup()

turtle.goto(-270,171)  # 1st Room
turtle.pendown()
turtle.forward(42)
turtle.penup()

turtle.goto(-240,173)  # 2nd Room
turtle.pendown()
turtle.forward(42)
turtle.penup()

turtle.goto(-216,174)  # 2nd Room
turtle.pendown()
turtle.forward(42)
turtle.penup()

# Window 1
turtle.goto(-317,-39)
turtle.left(90)
turtle.pendown()
turtle.forward(45)
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(45)
turtle.penup()

# Window 2
turtle.goto(-241,-39)
turtle.left(90)
turtle.pendown()
turtle.forward(45)
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(45)
turtle.penup()

# Window 3
turtle.goto(-165,-39)
turtle.left(90)
turtle.pendown()
turtle.forward(45)
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(45)
turtle.penup()

# Window Crosses
turtle.goto(-295,4)  # 1st Window
turtle.pendown()
turtle.forward(45)
turtle.penup()

turtle.goto(-317,-15)
turtle.left(90)
turtle.pendown()
turtle.forward(45)
turtle.penup()

turtle.goto(-220,4)  # 2nd Window
turtle.right(90)
turtle.pendown()
turtle.forward(45)
turtle.penup()

turtle.goto(-241,-15)
turtle.left(90)
turtle.pendown()
turtle.forward(45)
turtle.penup()

turtle.goto(-143,4)  # 3rd Window
turtle.right(90)
turtle.pendown()
turtle.forward(45)
turtle.penup()

turtle.goto(-164,-15)
turtle.left(90)
turtle.pendown()
turtle.forward(45)
turtle.penup()

# Door
turtle.goto(-249,-230)
turtle.left(90)
turtle.pendown()
turtle.forward(60)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(60)
turtle.penup()


# Coordinates
def buttonclick(x, y):
    print("You clicked at this coordinate({0},{1})".format(x, y))

# onscreen function to send coordinate
turtle.onscreenclick(buttonclick, 1)
turtle.listen()  # listen to incoming connections
turtle.speed(10)  # set the speed

turtle.done()
