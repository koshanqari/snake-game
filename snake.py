import turtle
class Snake:
    def __init__(self):

        self.tim = []
        self.create()

    def create(self):
        for i in range(3):
            self.tim.append(turtle.Turtle())
            self.tim[i].shape('square')
            if i == 0:
                self.tim[i].color('grey')
            else:
                self.tim[i].color('white')
            self.tim[i].penup()
            self.tim[i].goto(-(2*i)*10, 0)

    def left(self):
        if self.tim[0].heading() != 0:
            self.tim[0].setheading(180)
    def right(self):
        if self.tim[0].heading() != 180:
            self.tim[0].setheading(0)
    def up(self):
        if self.tim[0].heading() != 270:
            self.tim[0].setheading(90)
    def down(self):
        if self.tim[0].heading() != 90:
            self.tim[0].setheading(270)

    def extend(self):
        self.tim.append(turtle.Turtle())
        self.tim[-1].penup()
        self.tim[-1].shape('square')
        self.tim[-1].color('white')
        self.tim[-1].goto(self.pos[-1])
        
    def move(self):
        self.pos=[]
        self.pos.append(self.tim[0].pos())
        #Direct the SNAKE HEAD(tim[0]) between these lines👇:    
        self.tim[0].fd(20)
        #Snake head 👆

        for i in range(1, len(self.tim)):
            self.pos.append(self.tim[i].pos())
            self.tim[i].goto(self.pos[i-1])

    def reset(self):
        for i in range(len(self.tim)):
            self.tim[i].reset()
        
        self.tim = []
        self.create()
        self.tim[0].goto(0, 0)



