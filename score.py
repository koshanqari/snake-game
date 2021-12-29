import turtle 

class Score:
    def __init__(self):
        self.num = 0
        self.h_num = 0
        with open("Score.txt") as file:
            self.h_num= int(file.read())
        self.tim = turtle.Turtle()
        self.tim.pencolor("red")
        self.tim.hideturtle()
        self.display_score()
    

    def display_score(self):
        self.tim.clear()
        self.tim.penup()
        self.tim.goto(100,270)
        self.tim.write("Score: " + str(self.num), align='center', font=('Arial', 18, 'normal'))
        self.tim.goto(-100,270)
        self.tim.write("High Score: " + str(self.h_num), align='center', font=('Arial', 18, 'normal'))


    def score_inc(self):
        self.num +=1
        self.display_score()
    

    def game_over(self):
        # self.tim.goto(0,0)
        # self.tim.write("Game Over", align='center', font=('Arial', 18, 'normal'))
        # self.tim.goto(0,-30)
        # self.tim.write("Thanks for Playing K.Qari's Snake Game", align='center', font=('Arial', 18, 'normal'))
        self.num = 0
        self.display_score()



    def h_score_inc(self):
        if self.h_num < self.num:
            self.h_num = self.num
            self.display_score()
            with open("Score.txt", mode= 'w') as file:
                file.write(str(self.h_num))
            with open("Score.txt", mode= 'r') as file:
                print(file.read())
                








