from math import sin, radians
from time import sleep


def shivaliwave():
    for a in range(-180, 180):
        s = round(float("{:.02f}".format(sin(radians(a)) * 100))) // 2
        print(f"{a} degrees:", end="\t")
        print( (s + 50) * " ", end="*\n" )
        sleep(0.01)

# line 1 find sin of angle a, convert to integer = spaces, divide by two since it also involves negative numbers
# line 2 determines the angles of each line
# line 3 creates the wave (add and subtract based on positive and negative numbers)
#line 4 sleep = slows the wave down

while True:
    shivaliwave()

#while true loop makes it go on forever since there is no parameter that has be satisified for the while loop to be used.
