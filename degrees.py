#degrees
#Josue Cifuentes
#November 6, 2022
#Purpose is to convert radians to degrees
import math
pi=math.pi
radian = int(input('What is the radian value?'))
degrees=2*pi*radian
print('This is',degrees,'degrees')

#compare your result with the value obtained from math.degrees
print("The value from degree function is {}".format(math.degrees(radian))
