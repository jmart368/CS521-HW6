"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: March 1, 2020
Homework Problem # 7.7
Description: Create a LinearEquation class
"""


class LinearEquation():

    def __init__(self, a, b, c, d, e, f):
        """
        Gets the inputs from a coefficient for a,b,c,d,e,f
        """
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_d(self):
        return self.__d

    def get_e(self):
        return self.__e

    def get_f(self):
        return self.__f

    def is_solvable(self):
        """Returns solvable solution of a quadractic equation"""
        if (self.__a * self.__d) - (self.__b * self.__c) != 0:
            return True
        else:
            return False

    def get_x(self):
        """Returns no solution for x else no solutions if x is not solvable"""
        if self.is_solvable() is True:
            x = ((self.__e * self.__d) - (self.__b * self.__f)) / \
                ((self.__a * self.__d) - (self.__b * self.__c))
            return x
        else:
            print('The equation has no solution')

    def get_y(self):
        """Returns no solution for y else no solution if y is not solvable"""
        if self.is_solvable() is True:
            y = ((self.__a * self.__f) - (self.__e * self.__c)) / \
                ((self.__a * self.__d) - (self.__b * self.__c))
            return y
        else:
            print('The equation has no solution')
