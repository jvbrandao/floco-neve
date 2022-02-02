import turtle

lapis = turtle.Turtle()
turtle.Screen().bgcolor("black")
lapis.penup()
lapis.forward(90)
lapis.left(45)
lapis.pendown()
lapis.color("white")

def ramo():
  for i in range(3):
    for i in range(3):
      lapis.forward(30)
      lapis.backward(30)
      lapis.right(45)
    lapis.left(90)
    lapis.backward(30)
    lapis.left(45)
  lapis.right(90)
  lapis.forward(90)


for i in range(8):
  ramo()
  lapis.left(45)