import turtle, math, time, random
from utils import *

# Section 1: Setup
# TODO - create your player character and any other sprites
s1 = create_sprite("luigi.gif",200,0)
s2 = create_sprite("mario.gif",-200,0)

message_sprite = create_sprite("alien", -200,200)
message_sprite.hideturtle()
# TODO - set your background
set_background("rb.gif")
# TODO - set the starting value for your variables
# sprite_list = []
mario_score=0
luigi_score=0
who_is_it="mario"
# Section 2: Controls
# TODO - define your controls
def move_up1():
    x = s1.xcor()
    y = s1.ycor() + 10
    s1.goto(x,y)
        
def move_down1():
    x = s1.xcor()
    y = s1.ycor() - 10
    s1.goto(x,y)
    
def move_left1():
    x = s1.xcor() - 10
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right1(): 
    x = s1.xcor() + 10
    y = s1.ycor() 
    s1.goto(x,y)

def move_up2():
    x = s2.xcor()
    y = s2.ycor() + 10
    s2.goto(x,y)
        
def move_down2():
    x = s2.xcor()
    y = s2.ycor() - 10
    s2.goto(x,y)
    
def move_left2():
    x = s2.xcor() - 10
    y = s2.ycor() 
    s2.goto(x,y)
    
def move_right2(): 
    x = s2.xcor() + 10
    y = s2.ycor() 
    s2.goto(x,y)
# TODO - pick keys for each control
window.onkeypress(move_up1, "Up")
window.onkeypress(move_down1, "Down")
window.onkeypress(move_left1, "Left")
window.onkeypress(move_right1, "Right")

window.onkeypress(move_up2, "w")
window.onkeypress(move_down2, "s")
window.onkeypress(move_left2, "a")
window.onkeypress(move_right2, "d")
# Section 3: Game Loop
window.listen()


for i in range(10000000000):
    message_sprite.clear()
    message_sprite.write(f"mario points:{mario_score}\nluigi points:{luigi_score}",font=("Arial",30,"normal"))  
    if get_distance(s1,s2)<100:
        if who_is_it == "mario":
            mario_score+=1
            who_is_it = "luigi"
            s1.goto(250,0)
            s2.goto(-250,0)
        elif who_is_it =="luigi":
            luigi_score+=1
            who_is_it = "mario"
            s1.goto(250,0)
            s2.goto(-250,0)
    if i >=30*100:
        break
        
    time.sleep(0.01)
    window.update()
	

if i >= 30*100:
    if mario_score>=luigi_score:
        print ("mario won")
    if luigi_score>=mario_score:
        print ("luigi won")

print ("game over")