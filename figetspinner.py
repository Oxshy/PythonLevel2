from turtle import *
turn=0
def spinner():
    clear()
    angle=turn/10
    right(angle)
    forward(100)
    dot(120,"red")
    back(100)
    right(120)
    forward(100)
    dot(120,"green")
    back(100)
    right(120)
    forward(100)
    dot(120,"blue")
    back(100)
    right(120)
    update()
def animate():
    global turn
    if turn>0:
        turn-=1
    spinner()
    ontimer(animate,20)
def flick():
    global turn
    turn=turn+10
setup(400,400,None,None)
width(20)
tracer(False)
speed(0)
onkey(flick,"Down")
listen()
animate()
#spinner()
done()
