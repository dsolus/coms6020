#!usr/bin/env python 3.5
#Daniel Solus
#Assignment LAB 2
"""You have three trys to hit the sheep with a hay bale. Choose an angle and velocity. 
This program calls the function sheep_laucher three times. The function allows you to choose
an intial velocity and angle for the launcher. If the hay falls within 50 meters of the sheep
you win the game"""
import math

#The sheep is 300 meters away
def sheep_launcher(*args):
    g = 9.8
    sheep = 300

#Prompt the user for velocity and the angel of the launcher.
    v = input('Set the velocity of the launcher (m/s) ')
    theta = input('Set the angle of the launcher (degrees) ')

#convert theta to radians
    radians = math.radians(float(theta))

#Input the data into the equation to find delta x.
    v = float(v)
    deltax = (2*v**2*math.sin(radians)*math.cos(radians))/g
    print('deltax: {} meters'.format(deltax))

#Check to see if the hay bale lands within 50 meters of the sheep.
#print the distance missed by the user if the sheep is not hit
    if deltax == 300:
        print('You hit the sheep!')
    elif deltax < 249:
        print('You missed! The hay was short by {} meters.'.format(249 - deltax))
    elif deltax > 350:
        print('You missed! The hay was long by {} meters.'.format(deltax - 350))
    else:
        print('You fed the sheep!')
    return

#Calling the sheep_laucher fucntion for 3 trys.
print("You have three trys to hit the sheep. Good Luck!")
for i in range(0, 3):
    sheep_launcher()

