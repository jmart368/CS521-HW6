"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: March 1, 2020
Homework Problem # 7.1
Description: Create a class object to define a rectangle
"""


class Rectangle():
    """
    This class defines the parameters of a ractangle
    """

    def __init__(self, w=1, h=2):
        self.__width = w
        self.__height = h

    def get_width(self):
        """Returns the rectangle width"""
        return self.__width

    def get_height(self):
        """Returns rectangle height"""
        return self.__height

    def get_area(self):
        """Returns rectangle area using width and height values"""
        return self.__height * self.__width

    def get_perimeter(self):
        """Returns rectangle perimeter using width and height values"""
        return 2 * (self.__height + self.__width)
