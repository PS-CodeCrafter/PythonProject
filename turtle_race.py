import turtle
import random

WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_number_of_racers():
	while True:
		racers = input('Enter the number of racers (2 - 10): ')
		if racers.isdigit():
			racers = int(racers)
		else:
			print('Input is not numeric... Try Again!')
			continue

		if 2 <= racers <= 10:
			return racers
		else:
			print('Number not in range 2-10. Try Again!')

def init_turtle():
	screen = turtle.Screen()
	screen.setup(WIDTH, HEIGHT)

	screen.tracer(0)  # Turn off auto updates
	return screen

def create_turtles(colors):
	turtles = []
	spacingx = WIDTH // (len(colors) + 1)
	for i, color in enumerate(colors):
		racer = turtle.Turtle()
		racer.color(color)
		racer.shape('turtle')
		racer.left(90)
		racer.penup()
		racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
		racer.pendown()
		turtles.append(racer)
	return turtles

def race(colors):
	turtles = create_turtles(colors)
	while True:
		for racer in turtles:
			distance = random.randrange(1, 10)
			racer.forward(distance)

			if racer.ycor() >= HEIGHT//2 - 20:
				turtle.update()
				return racer.pencolor()
		turtle.update()

# --- RUN PROGRAM ---
racers = get_number_of_racers()
screen = init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color:", winner)
screen.mainloop()