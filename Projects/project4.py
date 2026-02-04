import turtle, time, random
from utils import *

# the game is where you spawn an amount of ducks to spawn another duck

# Section 1 - setup
# TODO - set a background using set_background()
set_background("ocean-.gif")
# TODO - create at least two variables and set their starting value. ex: cookies = 0
blue_duck=0
yellow_duck=0

# OPTIONAL: use this invisible alien to say a message
# message_sprite = create_sprite("alien", -200,200)
# message_sprite.hideturtle() 

# Section 2 - controls
# TODO - define an action. ex: def my_control()
def spawn_blue_duck () :
    global blue_duck
    blue_duck += 1
    x = random.randint (-200,200)
    y = random.randint (-200,200)
    create_sprite("blue_duck",x,y)
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
window.onkeypress(spawn_blue_duck, "space")
# TODO - make a second control
def spawn_yellow_duck () :
    global yellow_duck,blue_duck
    if blue_duck >= 10:
        blue_duck -= 10
        x = random.randint (-200, 200)
        y = random.randint (-200, 200)
        create_sprite("yellow_duck",x,y)
window.onkeypress(spawn_yellow_duck, "b")




# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    # message_sprite.clear()
    # message_sprite.write("Hello")

    time.sleep(0.1)
    window.update()