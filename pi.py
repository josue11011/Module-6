#pi
#Josue Cifuentes
#November 6, 2022
#Purpose is to Calculate an approximation for pi
import math
pi=0
denom=1
for i in range (0,1000):
    if i is i %2==0:
        pi=pi+4/denom
    else:
        pi=pi-4/denom

    denom=denom+2
print('PI=',pi)
print(math.pi)

