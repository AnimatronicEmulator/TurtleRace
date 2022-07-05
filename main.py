from turtle import Turtle, Screen
import random


def turtle_maker(list_of_colors):
    list_of_turtles = []
    for value in list_of_colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(value)
        new_turtle.speed(0)
        list_of_turtles.append(new_turtle)
    return list_of_turtles


def race_generator(list_of_turtle_objects):
    random.shuffle(list_of_turtle_objects)
    for race_turtle in list_of_turtle_objects:
        race_turtle.setheading(0)
        race_turtle.forward(random.randint(0, 10))


def did_you_win(winner, bet_placed):
    user_won = False
    if winner.color() == bet_placed:
        print(f"The {winner.color()[0]} turtle won! You did it!")
    else:
        print(f"Sorry, the {winner.color()[0]} turtle won. Try again.")
    return user_won



def turtle_placer(list_of_turtle_objects, screen_width):
    x_coord = int(-((screen_width / 2) + 10))

    turt = 0
    for race_turtle in list_of_turtle_objects:
        if len(list_of_turtle_objects) % 2 == 0:
            y_above_axis = 15
            if list_of_turtle_objects.index(race_turtle) % 2 == 0:
                y_coord = y_above_axis + (30 * turt)
            else:
                y_coord = -(y_above_axis + (30 * turt))
                turt += 1
            race_turtle.penup()
            race_turtle.setpos(x_coord, y_coord)
        else:
            y_above_axis = 30
            if list_of_turtle_objects.index(race_turtle) == 0:
                y_coord = 0
            elif list_of_turtle_objects.index(race_turtle) % 2 == 0:
                y_coord = -(y_above_axis + (30 * turt))
                turt += 1
            else:
                y_coord = y_above_axis + (30 * turt)
            race_turtle.penup()
            race_turtle.setpos(x_coord, y_coord)


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = turtle_maker(colors)

screen = Screen()
screen.setup(width=500, height=400)

turtles_racing_string = ", ".join(colors)
turtle_placer(turtles, screen.canvwidth)
user_bet = screen.textinput(f"Turtle Race Betting", "Who will win the race? The turtles racing today are:\n"
                                                    f"{turtles_racing_string}.\n"
                                                    f"Enter a color: ")

turtle_has_won = False
winner = 0
while not turtle_has_won:
    race_generator(turtles)
    for race_turtle in turtles:
        if race_turtle.xcor() > ((screen.canvwidth / 2) - 10):
            turtle_has_won = True
            winner = race_turtle

did_you_win(winner, user_bet)

screen.exitonclick()
