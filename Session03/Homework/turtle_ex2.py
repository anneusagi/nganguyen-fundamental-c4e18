from turtle import *

listcolors = ["red", "blue", "brown", "yellow", "gray"]

for i in range(5):
    begin_fill()
    fillcolor(listcolors[i])
    color(listcolors[i])
    for j in range(2): 
        forward(50)
        left(90)
        forward(100)
        left(90)
        
    forward(50)
    end_fill()
 

mainloop()