import turtle
import random

s = turtle.Screen()
s.title("Turtle Race Project")
s.bgcolor("gray")

player1 = turtle.Turtle()
player2 = turtle.Turtle()
start = turtle.Turtle()
dice = [1, 2, 3, 4, 5, 6]

start.hideturtle()
start.color("black", "black")
start.begin_fill()
start.penup()
start.goto(-270, 0)
start.pendown()
start.left(90)
start.forward(150)
start.right(90)
start.forward(55)
start.right(90)
start.forward(250)
start.right(90)
start.forward(55)
start.right(90)
start.forward(100)
start.end_fill()

player1.hideturtle()
player1.shape("turtle")
player1.color("red", "red")
player1.shapesize(2, 2, 2)
player1.pensize(3)

player2.hideturtle()
player2.shape("turtle")
player2.color("blue", "blue")
player2.shapesize(2, 2, 2)
player2.pensize(3)

player1.penup()
player1.goto(200, 95)
player1.pendown()
player1.circle(30)
player1.penup()
player1.goto(-250, 125)
player1.showturtle()

player2.penup()
player2.goto(200, -105)
player2.pendown()
player2.circle(30)
player2.penup()
player2.goto(-250, -75)
player2.showturtle()

redname = s.textinput("NOMBRE ROJA", "Ingrese el nombre de la tortuga ROJA")
bluename = s.textinput("NOMBRE AZUL", "Ingrese el nombre de la tortuga AZUL")

for i in range(20):
    if player1.pos() >= (160, 125):
        print("¡{} ha ganado!".format(redname))
        break
    elif player2.pos() >= (160, -75):
        print("¡{} ha ganado!".format(bluename))
        break
    else:
        turn1 = input("Presiona la tecla ENTER para avanzar la tortuga ROJA.")
        turn1 = random.choice(dice)
        print("Tu número es: {}\nAvanzas: {}".format(turn1, turn1 * 20))
        player1.pendown()
        player1.forward(turn1 * 20)

        turn2 = input("Presiona la tecla ENTER para avanzar la tortuga AZUL.")
        turn2 = random.choice(dice)
        print("Tu número es: {}\nAvanzas: {}".format(turn2, turn2 * 20))
        player2.pendown()
        player2.forward(turn2 * 20)

turtle.done()
