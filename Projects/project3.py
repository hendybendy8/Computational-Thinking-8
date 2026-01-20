import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 =-20
y1 =200
x2 =-20
y2 =100
x3 =-20
y3 =0
x4 =-20
y4 =-100
# where 

# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("bath.gif")
t1 = create_sprite("yellowduck.gif",x1,y1)
t2 = create_sprite("pinkduck.gif",x2,y2)
t3 = create_sprite("blueduck.gif",x3,y3)
t4 = create_sprite("orangeduck.gif",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(30):
    x1 +=10
    x2 +=25
    x3 +=40
    x4 +=5
# the 3rd duck in the row of ducks is the fastest because its speed number is the highest 
    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("the blue duck wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("the blue duck wins!")
elif x3 >= x2 and x3 >= x1 and x3 >= x4:
    print("the blue duck wins!")
elif x4 >= x1 and x4 >= x3 and x4 >= x2:
    print("the blue duck wins!")

turtle.exitonclick()