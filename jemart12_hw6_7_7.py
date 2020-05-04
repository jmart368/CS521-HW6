"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: March 1, 2020
Homework Problem # 7.7
Description: Test the LinearEquation class from LinearEquation.py
"""

from LinearEquation import LinearEquation

if __name__ == '__main__':
    # assign values to equation1
    equation1 = LinearEquation(9, 4, 3, -5, -6, -21)
    print('equation1: ')

    # checks if equation1 is solvable, displays x & y if it is
    if equation1.is_solvable():
        print('x is', equation1.get_x())
        print('y is', equation1.get_y())
    else:
        print('The equation has no solution')

    # prints blank line between outputs of the two equations
    print('')

    # assigns values to equation2
    equation2 = LinearEquation(1, 2, 2, 4, 4, 5)
    print('equation2: ')

    # checks if equation1 is solvable, displays x and y if it is
    if equation2.is_solvable():
        print('x is', equation2.get_x())
        print('y is', equation2.get_y())
    else:
        print('The equation has no solution')
