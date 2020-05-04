"""
Homework Problem # 12.1
Description: Create a Triangle class
"""


from GeometricObject import GeometricObject
import math


class Triangle(GeometricObject):
    """Initializesthe triangle values"""

    def __init__(self, side1=1.0, side2=1.0, side3=1.0):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def get_side1(self):
        return self.__side1

    def get_side2(self):
        return self.__side2

    def get_side3(self):
        return self.__side3

    def get_area(self):
        """Returns the area of the triangle"""
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        area = math.sqrt(
            s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3)
        )
        return area

    def get_perimeter(self):
        """Returns the perimeter of the triangle"""
        return self.__side1 + self.__side2 + self.__side3

    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side 2 = " + \
            str(self.__side2) + " side3 = " + str(self.__side3)
