import turtle
import time
import snake #custom class
import food
import score
#Objects:
#/Screen
my_screen = turtle.Screen()
my_screen.setup(width= 600, height=600)
my_screen.bgcolor(0, 0, 0)
my_screen.title("K.Qari's Snake Game:")
my_screen.tracer(0)
turtle_movement_delay = 0.1 #(in sec)This come under sleep time of loop and is created by me however put unter turtle dection for easy under standing

#/Snake : It is an obj of custom class
my_snake = snake.Snake()
my_food = food.Food()
my_score = score.Score()

#screen listening:
my_screen.listen()
my_screen.onkey(my_snake.left, 'Left')
my_screen.onkey(my_snake.right, 'Right')
my_screen.onkey(my_snake.up, 'Up')
my_screen.onkey(my_snake.down, 'Down')


# Game Loop 
start = True
while start == True:
    time.sleep(turtle_movement_delay)                                           
    my_screen.update()
    my_snake.move()
        
    if my_food.distance(my_snake.tim[0].position()) < 15:
        my_food.random_food()
        
        my_score.score_inc()
        my_score.h_score_inc()
        my_snake.extend()
        

    if my_snake.tim[0].xcor() > 300 or my_snake.tim[0].xcor() < -300 or my_snake.tim[0].ycor() > 300 or my_snake.tim[0].ycor() < -300:
        # start = False
        my_snake.reset()
        my_score.game_over()


    for i in range(1, len(my_snake.tim)):
        if my_snake.tim[0].distance(my_snake.tim[i]) < 10:
            my_score.game_over()
            my_snake.reset()
            # start = False


#keep this in the end as this will be used to exit the screen
my_screen.exitonclick()

