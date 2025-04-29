from turtle import Screen
from Movement import Snake_script
from Food_script import food
from Score_board import Scoreboard
import time

def create_play():
    global screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

def play_start():
    global food_count, snake, snake_food, score, game_is_on

    food_count=0

    snake = Snake_script()
    snake_food=food()
    score=Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        score.score_update()
        snake.move()
        
        #detect food
        if snake.head.distance(snake_food)<15:
            snake_food.refresh()
            score.addPoint()
            snake.extend()
            
           
            
                

        #detect collision
        if snake.head.xcor()>290 or snake.head.xcor()< -290 or snake.head.ycor()>270 or snake.head.ycor()< -290 :
            score.game_pause()
            game_is_on=False
            

        # Detect tail collision
        for seg in snake.segments:
            if seg == snake.head:
                pass
            elif snake.head.distance(seg)<1:
                score.game_pause()
                game_is_on=False

    screen.onkey(restart_game, "space")
    screen.listen() 
    
def restart_game():
    screen.clear()
    create_play()
    # score.resetscr() 
    # snake.resetpos()  
    play_start()


create_play()
play_start()
restart_game()

screen.exitonclick()
