from turtle import *

speed(-1)
color("blue")


for i in range(22):
    for j in range(4):
        forward(100)
        left(90)
    left(360/22)

mainloop()