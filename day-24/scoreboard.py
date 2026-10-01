from turtle import Turtle

ALIGNMENT = 'center'
SCORE_FONT = ('Courier New', 12, 'bold')
GAME_OVER_FONT = ('Courier New', 24, 'bold italic')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.speed('fastest')
        self.goto(x=0, y=280)
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=SCORE_FONT)

    # def game_over(self):
    #     self.home()
    #     self.write(arg="Game Over", align=ALIGNMENT, font=GAME_OVER_FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score()
