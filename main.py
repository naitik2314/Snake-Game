import time
from turtle import Screen
from food import Food
from score import Score
from snake import Snake

#Setup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake() #We created that object from this blueprint (Snake)
food = Food() #Create food from the food class we have on another file
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Moving the snake
while snake.game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move() #So now, whenver we want to call a method in the class, we just call it using the object that we created followed by the class name

    #Detect collision with food
    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.extend()
        food.refresh()

    #Detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.final_score()
screen.exitonclick()