import turtle

def draw_heart():
  turtle.color("red")

  turtle.penup()
  turtle.goto(-100, 0)
  turtle.pendown()

  turtle.left(45)
  turtle.forward(60)
  turtle.right(90)
  turtle.forward(60)
  turtle.right(90)
  turtle.forward(60)
  turtle.right(90)
  turtle.forward(60)
  turtle.right(45)

  turtle.left(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)

  turtle.penup()
  turtle.goto(-100, 0)
  turtle.pendown()
  turtle.right(135)
  turtle.forward(141.42)

draw_heart()
turtle.done()