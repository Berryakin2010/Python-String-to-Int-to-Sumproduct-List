#!/usr/bin/env python3
import numpy

def find_sum_of_digits(numbers):
    sum_of_digits= 0
    num1= str(numbers)
    num2= list(num1)
    num3= map(int, num2)
    num4= list(num3)
    sum_of_digits= numpy.product(num4)
    return sum_of_digits
    
sum_of_digits= find_sum_of_digits(123)
print(sum_of_digits)
