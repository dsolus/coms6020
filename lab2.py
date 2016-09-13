#!usr/bin/env python 3.5
#Daniel Solus
#Assignment LAB 2
"""You have three tries to hit the sheep with a hay bale. Choose an angle and velocity."""
import math

#The sheep is 300 meters away
def sheep_launcher(v, theta):
    g = 9.8
    sheep = 300

#Prompt the user for velocity and the angel of the launcher.
    v = input('Set the velocity of the launcher')
    theta = input('Set the angle of the launcher')

#convert theta to radians
    radians = math.radians(float(theta))

    print(v, radians)

#Input the data into the equation to find delta x.
    v = float(v)
    deltax = (2*v**2*math.sin(radians)*math.cos(radians))/g
    print(deltax)

#Check to see if the hay bale lands within 50 meters of the sheep.
#print the distance missed by the user if the sheep is not hit
    if deltax == 300:
        print('You hit the sheep!')
    elif deltax < 249:
        print('You missed by {}'.format(249 - deltax))
    elif deltax > 350:
        print('You missed by {}'.format(deltax - 350))
    else:
        print('You feed the sheep!')

for i in range(0, 3):
    sheep_launcher(v, theta)

