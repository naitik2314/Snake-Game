from turtle import Turtle


class Score(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        self.color("white")
        self.game_over = False

    def increase_score(self):
        self.score = self.score + 1
        self.write(f"Your Score: {self.score}", align='center', font=('Arial', 10))
    
    def final_score(self):
        self.goto(x=0, y=0)
        self.write(f"Game over", align='center', font=('Arial', 12))
