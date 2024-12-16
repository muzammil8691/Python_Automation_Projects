from turtle import *
import time

#Initial Settings
color("red")
begin_fill()
pensize(10)
speed(2)

#Left Side
left(50)
forward(133)
circle(50,200)

#Right Side
right(140)
circle(50,200)
forward(133)

end_fill()

# Write a message
penup()  
goto(0, -100)  # Move to a position below the heart
pendown()  

color("red")  
write("This Heart is for you", align="center", font=("Comic Sans MS", 20, "bold"))

done()