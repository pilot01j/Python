from turtle import Turtle
FONT = ("Courier", 14, "bold")
FONT_GAME_OVER = ("Courier", 40, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.t_score = 0
        self.penup()
        self.color("black")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.penup()
        self.goto(-235, 265)
        self.write(f"Score: {self.t_score}", align="center", font=FONT)

    def t_poit(self):
        self.clear()
        self.t_score += 1
        self.update_score()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.color("black")
        self.write("GAME OVER.", align="center", font=FONT_GAME_OVER)
