"""
Homework Problem # 12.1
Description: Tests both GeometricObject.py and Triangle.py with user input
"""

from Triangle import Triangle

if __name__ == '__main__':
    """
    Prompts user for the number of sides, color, whether triangle is filled
    """
    while True:
        try:
            side_list = [float(side) for side in input(
                'Enter the length of each side of a triangle'
                ' separated by spaces: ').split()]

            color = input("Enter the triangle's color: ")
            filled = bool(int(input("Is the triangle filled? 1=Yes, 0=No: ")))

            # prompts user again if three sides are not entered
            if len(side_list) != 3:
                print('Incorrect amount of inputs. Try again.')
                continue
            else:
                break

        except ValueError:
            print('Could not convert input. Try again.')

    # new triangle object initiated with user input
    triangle1 = Triangle(side_list[0], side_list[1], side_list[2])

    # sets triangle1 color to user-selected color
    triangle1.set_color(color)

    # sets triangle1 filled value to user's input
    triangle1.set_filled(filled)

    # prints string value, the area, perimeter,color, and whether it is filled
    print('\n' + triangle1.__str__())
    print('Area:', triangle1.get_area())
    print('Perimeter:', triangle1.get_perimeter())
    print('Color:', triangle1.get_color())
    print('Filled:', triangle1.is_filled())
