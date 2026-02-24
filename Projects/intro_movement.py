import time, turtle, random
from utils import *
# Section 1: Setup
set_background("castle")
s1 = create_sprite("character1",0,-200)

# Section 2: define controls
def move_up():
    x = s1.xcor()
    y = s1.ycor() + 10
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 10
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 10
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 10
    y = s1.ycor() 
    s1.goto(x,y)

def draw ():
    s1.pendown ()

def stop_drawing ():
    s1.penup ()

def erase():
    s1.clear()

def red_pen ():
    s1.color("red")

def green_pen ():
    s1.color ("green")

def reset ():
    s1.goto(0,0)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")
window.onkeypress(draw, "z")
window.onkeypress(stop_drawing, "x")
window.onkeypress(erase, "c")
window.onkeypress(red_pen, "v")
window.onkeypress(green_pen, "b")
window.onkeypress(reset, "n")

# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")



s2 = create_sprite("character2",0,-200)

# Section 2: define controls
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

def draw2 ():
    s2.pendown ()

def stop_drawing2 ():
    s2.penup ()

def erase2():
    s2.clear()

def yellow_pen2 ():
    s2.color("yellow")

def pink_pen2 ():
    s2.color ("pink")

def reset2 (x,y):
    s2.goto(0,0)

window.onkeypress(move_up2, "Up")
window.onkeypress(move_down2, "Down")
window.onkeypress(move_left2, "Left")
window.onkeypress(move_right2, "Right")
window.onkeypress(draw2, "e")
window.onkeypress(stop_drawing2, "r")
window.onkeypress(erase2, "t")
window.onkeypress(yellow_pen2, "y")
window.onkeypress(pink_pen2, "u")
window.onscreenclick(reset2)

# Section 3: define other controls
def hide():
    s2.hideturtle()
def show():
    s2.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")

window.onkeypress(draw2, "e")
window.onkeyrelease(stop_drawing2, "e")


# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()