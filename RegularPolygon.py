"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: March 1, 2020
Homework Problem # 7.5
Description: Create a RegularPolygon class
"""

import math


class RegularPolygon():
    """
    Establish polygon parameters where n = 3, side = 1, x = 0, and y = 0
    """

    def __init__(self, n=3, side=1, x=0.0, y=0.0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    def get_n(self):
        """returns number of sides"""
        return self.__n

    def set_n(self, new_n):
        """sets number of sides"""
        self.__n = new_n

    def get_side(self):
        """returns side length"""
        return self.__side

    def set_side(self, new_side):
        """sets side length"""
        self.__side = new_side

    def get_x(self):
        """returns x value"""
        return self.__x

    def set_x(self, new_x):
        """sets x value"""
        self.__x = new_x

    def get_y(self):
        """returns y value"""
        return self.__y

    def set_y(self, new_y):
        """sets y value"""
        self.__y = new_y

    def get_perimeter(self):
        """returns polygon perimeter using side length and n"""
        perimeter = self.__side * self.__n
        return perimeter

    def get_area(self):
        """returns polygon area using side length and n"""
        area = (self.__n * (self.__side**2)) /\
               (4 * math.tan(math.pi / self.__n))
        return area
