from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)

user_input = screen.textinput(title="Place your bet", prompt="Which turtle will win? Enter a color")

color = ["red", "orange", "yellow", "green", "blue", "purple"]

ycor = [25, -25, 75, -75, 125, -125]

turtles_in_game = []

game_on = False

for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(color[i])
    new_turtle.goto(-230, ycor[i])
    turtles_in_game.append(new_turtle)

if user_input:
    game_on = True

while game_on:

    for turtle in turtles_in_game:
        if turtle.xcor() > 230:
            game_on = False
            winning_color = turtle.pencolor()
            if user_input == winning_color:
                print(f"You won the bet! {winning_color} turtle won the race")
            else:
                print(f"You lost the bet! {winning_color} turtle won the race")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
