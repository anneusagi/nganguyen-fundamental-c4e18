from turtle import *

listcolors = ["red", "blue", "brown", "yellow", "gray"]

for i in range(3,8):
    color(listcolors[i-3])
    for j in range(i):
        forward(150)
        left(360/i)

mainloop()