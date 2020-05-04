"""
Name: Jose Martinez
Class: CS 521 - 2020 Spring 1
Date: March 1, 2020
Homework Problem # 7.1
Description: Test the rectangle from Rectangle.py
"""


from Rectangle import Rectangle


def test_rectangles(x):
    """
    Definition: Displays the results of the rectancle object.
    """
    # print table header with a spacing format
    print("{0:10} {1:10} {2:10} {3:10} {4:10}"
          .format('Rectangle', 'Width', 'Height', 'Area', 'Perimeter'))
    # print rectangle, width, height, area and perimeter
    # use enumarate to extract the table header from the above index list
    for x, rectangle in enumerate(x):
        print("{0:5}{1:11}{2:12}{3:11.2f}{4:12.2f}"
              .format(x + 1, rectangle.get_width(), rectangle.get_height(),
                      rectangle.get_area(), rectangle.get_perimeter()))


if __name__ == '__main__':
    """
    Display the two rectangles with width 4 and 3.5, and height 40 and 35.7
    """
    rectangle1 = Rectangle(4, 40)
    rectangle2 = Rectangle(3.5, 35.7)

    # display rectangle data from the test_rectangle
    test_rectangles([rectangle1, rectangle2])
