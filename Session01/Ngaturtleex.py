# A SQUARE
from turtle import *

color("green")
fillcolor("yellow")

begin_fill()
for i in range(4):
    forward(100)
    left(90)

end_fill()
mainloop()

# AN EQUILATERAL TRIANGLE
from turtle import *

color("green")
fillcolor("yellow")

begin_fill()

for i in range(3):
    forward(100)
    left(120)

end_fill()
mainloop()

#A CIRCLE
from turtle import *

color("green")
fillcolor("yellow")

begin_fill()
circle(50)

end_fill()
mainloop()

#MULTI-CIRCLES
from turtle import *

color("green")
for i in range(6):
    circle(50)
    left(60)

mainloop()

#MULTI-CIRCLES (Even better)
from turtle import *
speed(-1)
color("green")
for i in range(36):
    circle(50)
    left(10)

mainloop()