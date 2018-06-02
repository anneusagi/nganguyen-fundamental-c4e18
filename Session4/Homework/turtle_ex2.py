from turtle import *

speed(-1)
color("blue")

n = 10

for i in range(80):
    for j in range(4):
        forward(n)
        left(90)   
    left(360/60)
    n +=2

mainloop()