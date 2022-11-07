#factorial
#Josue Cifuentes
#November 6, 2022
#Purpose is to Write a program that uses a for loop to compute the factorial of a user input value
import math
n = int(input('What is your number?'))
factorial=1
if n == 0:
    print('The factorial is 0')
else:
    for n in range (1,n+1):
        factorial = factorial *n
    print('the factorial of',n,'is',factorial)
