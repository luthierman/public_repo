import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")
	dave = turtle.Turtle()
	dave.shape("turtle")
	dave.color("green")
	dave.speed(2)
	dave.forward(100)
	dave.right(90)
	dave.forward(100)
	dave.right(90)
	dave.forward(100)
	dave.right(90)
	dave.forward(100)
	dave.right(90)

	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")
	angie.circle("100")

	window.exitonclick()

draw_square()
