'''
Write a program that prints the numbers 
from 1 to 100 
and for multiples of ‘3’ print “Fizz”
instead of the number and for the multiples of ‘5’ print “Buzz”.
 
number divisible by 3 and 5 will
always be divisible by 15, print
'FizzBuzz' in place of the number
'''


for i in range(100):
    if i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    else:
        print(i)
