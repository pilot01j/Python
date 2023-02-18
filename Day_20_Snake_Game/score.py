from turtle import Turtle
ALIGNMENT = "center"
FONT_SCORE = ("Courier", 18, "bold")
FONT_GAME_OVER = ("Courier", 40, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.points}", align=ALIGNMENT, font=FONT_SCORE)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.color("white")
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT_GAME_OVER)

    def increase_score(self):
        self.points += 1
        self.clear()
        self.update_score()
