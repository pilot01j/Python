from turtle import Turtle
ALIGNMENT = "center"
FONT_SCORE = ("Courier", 18, "bold")
FONT_GAME_OVER = ("Courier", 40, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        file = open("data.txt", mode="r")
        self.high_points = int(file.read())
        file.close()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.points}  High Score: {self.high_points}", align=ALIGNMENT, font=FONT_SCORE)

    # def game_over(self):
    #     self.penup()
    #     self.goto(0, 0)
    #     self.color("white")
    #     self.write("GAME OVER.", align=ALIGNMENT, font=FONT_GAME_OVER)

    def reset (self):
        if self.points > self.high_points:
            self.high_points = self.points
            file = open("data.txt", mode="w")
            file.write(f"{self.high_points}")
            file.close()
        self.points = 0
        self.update_score()

    def increase_score(self):
        self.points += 1
        self.update_score()
