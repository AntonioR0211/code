#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl
import random as rndm

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:

  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.speed(5)
  ht.goto(-350, tloc)
  ht.setheading(0)

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.speed(5)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50
  
steps = 0
while steps < 30:
    for ht in horiz_turtles:
        for vt in vert_turtles:
            ht.forward(rndm.randrange(1,8))
            vt.forward(rndm.randrange(1,8))
            if (abs(ht.xcor() - vt.xcor()) < 20) and (abs(ht.ycor() - vt.ycor()) < 20):
                ht.backward(40)
                vt.backward(40)
                ht.fillcolor("blue")
                vt.fillcolor("blue")
    steps = steps + 1

for ht in horiz_turtles:
    for vt in vert_turtles:
        ht.fillcolor("red")
        vt.fillcolor("red")

wn = trtl.Screen()
wn.mainloop()
