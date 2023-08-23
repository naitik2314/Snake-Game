import time
from turtle import Turtle, Screen

from snake import Snake

#Setup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake() #We created that object from this blueprint (Snake)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

#Moving the snake
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move() #So now, whenver we want to call a method in the class, we just call it using the object that we created followed by the class name

screen.exitonclick()