# -*- coding: utf-8 -*-
'''
# @Time     :   2020/1/13 8:18 PM
# @Author   :   bin li
# @File     :   fizzbuzz.py
# @Input    :
# @Output   :
# @Function : 
'''

def process(number):
    if number % 3 ==0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 ==0:
        return 'Buzz'
    return number

if __name__ == '__main__':
    for i in range(1,101):
        print(process(i))
