from turtle import Turtle, Screen

from score import Score
starting_position = [(0, 0), (-20, 0), (-40, 0)] #The starting position is going to be constant for every snake we make
MOVE_DISTANCE = 20 #We are keeping the moving distance to be the same
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Score):
    def __init__(self):
        super().__init__()
        self.segments = [] #For every snake we create, we will have a new segments array
        self.create_snake() #We are just calling the function
        self.head = self.segments[0]
        self.game_is_on = True

    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)            
        self.segments.append(new_segment) #In this, the object we create using this class will have a unique segments array. To tap into that unique segment array of each object that we create, we use #! self.

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            if new_x > 280 or new_x < -280 or new_y > 280 or new_y < -280:
                self.game_is_on = False
                self.final_score()
            self.segments[seg_num].goto(new_x, new_y)
            
    
        self.segments[0].forward(MOVE_DISTANCE) 

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

