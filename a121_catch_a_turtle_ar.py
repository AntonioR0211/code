# a121_catch_a_turtle_ar.py
import turtle as tt
import random as rng

# Setups
tcolor = "White"
tshape = "circle"
tt.bgcolor("Red")
tfont = ("Roboto", 20, "normal")
tsize = 3
score = 0
timer = 30
count = 1000
timer_up = False

# Turtle Thing
circle = tt.Turtle()
circle.color(tcolor)
circle.shapesize(tsize)
circle.shape(tshape)
circle.pu()
tc = tt.Turtle()
tc.color("Lime")
tc.pu()
tc.goto(-190, 140)
tc.hideturtle()
score_display = tt.Turtle()
score_display.pu()
score_display.goto(190, 140)
score_display.color("Lime")
score_display.hideturtle()
# Game Itself

def update_score():
    global score
    score += 1
    score_display.clear()
    score_display.write("Clicks: " + str(score), font=tfont)

def countdown():
  global timer, timer_up
  tc.clear()
  if timer <= 0:
    tc.write("Time's Up", font=tfont)
    timer_up = True
  else:
    tc.write("Timer: " + str(timer), font=tfont)
    timer -= 1
    tc.getscreen().ontimer(countdown, count)

def when_clicked(i, j):
    global timer, tsize
    if (timer_up == False):
        circle.color("Red")
        circle.stamp()
        circle.color(tcolor)
        tsize -= .03
        circle.shapesize(tsize)
        update_score()
        change_position()
    else:
        circle.hideturtle()

def  change_position():
    new_xpos = rng.randint(-200, 200)
    new_ypos = rng.randint(-150, 150)
    circle.goto(new_xpos, new_ypos)

circle.onclick(when_clicked)
wn = tt.Screen()
wn.ontimer(countdown, count) 
wn.mainloop()
