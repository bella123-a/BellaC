import turtle

t = turtle.Turtle()
t3 = turtle.Turtle()
t3.hideturtle()
screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor("navy blue")
t.write("My presentation by Bella", font=("Arial", 24, "bold"), align="center")
turtle.addshape("sunset.gif")
t3.penup()
t3.goto(0,100)
t3.shape("intro.gif")
a= t3.stamp()
t3.goto(0,0)
t.penup()
t.goto(50,-200)
t.pendown()
t.fillcolor("light pink")
t.begin_fill()
t.circle(25)
t.end_fill()
t.penup()
t.goto(-100,100)


enter = input("Press enter to begin")
t.clear()
t3.clearstamps()
screen.bgcolor("orange")
t.penup()
t.goto(-100,-100)
t.pendown()
t.fillcolor("pink")
t.begin_fill()
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.forward(25)
t.left(90)
t.penup()
t.goto(-100,175)
t.pendown()
t.write("My Favorite Foods", font=("Arial", 24, "bold"), align="center")
turtle.addshape("icr.gif")
t3.shape("icr.gif")
b = t3.stamp()
t3.goto(150,75)
turtle.addshape("steak.gif")
t3.shape("steak.gif")
c = t3.stamp()
t3.goto(80,80)
turtle.addshape("pizza.gif")
t3.shape("pizza.gif")
d = t3.stamp()
t.end_fill()

enter = input("Press enter to begin")
t.clear()
t3.clearstamps()
screen.bgcolor("purple")
t.write("My Hobbies", font=("Arial", 24, "bold"), align="center")
turtle.addshape("softball.gif")
t3.shape("softball.gif")
e = t3.stamp()
t3.goto(-60,50)
turtle.addshape("videogame.gif")
t3.shape("videogame.gif")
f = t3.stamp()
t3.goto(-175,75)
turtle.addshape("sleeping.gif")
t3.shape("sleeping.gif")
g = t3.stamp()
t3.goto(135,20)
turtle.addshape("basketball.gif")
t3.shape("basketball.gif")
h = t3.stamp()
t.penup()
t.goto(-150,-150)
t.pendown()
t.fillcolor("Blue")
t.begin_fill()
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.end_fill()

enter = input("Press enter to begin")
t.clear()
t3.clearstamps()
screen.bgcolor("White")
t.penup()
t.goto(-100,175)
t.pendown()
t.write("Favorite Movie", font=("Arial", 24, "bold"), align="center")
t.penup()
turtle.addshape("Spiderman.gif")
t3.shape("Spiderman.gif")
i = t3.stamp()
t.goto(-25,15)
t.pendown()
t.fillcolor("Purple")
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(25)
t.left(90)
t.forward(50)
t.left(90)
t.forward(25)
t.left(90)
t.end_fill()

enter = input("Press enter to begin")
t.clear()
t3.clearstamps()
screen.bgcolor("Navy Blue")
t3.goto(180,-65)
t.penup()
t.goto(-100,175)
t.pendown()
t.write("Favorite Sport", font=("Arial", 24, "bold"), align="center")
t3.goto(180,-65)
turtle.addshape("softball.gif")
t3.shape("softball.gif")
i = t3.stamp()
t.penup()
t.goto(-15,75)
t.pendown()
t.fillcolor("neaon green")
t.begin_fill()
t.setheading(45)
t.forward(50)
t.setheading(135)
t.forward(50)
t.setheading(270)
t.forward(75)
t.end_fill()

turtle.done()


