"""
Homework Problem # 7.5
Description: Test the RegularPolygon class from RegularPolygon.py
"""


from RegularPolygon import RegularPolygon

if __name__ == '__main__':
    """
    Test program that creates 3 RegularPolygons displaying the perimeter and
    area for each polygon"""

    # Polygon 1 output
    polygon_1 = RegularPolygon()
    print('The perimeter and area for Polygon 1 is: \nPerimeter: {}\
\nArea: {:.4f}' .format(polygon_1.get_perimeter(), polygon_1.get_area()))

    # Polygon 2 output
    polygon_2 = RegularPolygon(6, 4)
    print('\nThe perimeter and area for Polygon 2 is: \nPerimeter:\
{}\nArea: {:.4f}' .format(polygon_2.get_perimeter(), polygon_2.get_area()))

    # Polygon 3 output
    polygon_3 = RegularPolygon(10, 4, 5.6, 7.8)
    print('\nThe perimeter and area for Polygon 3 is: \nPerimeter:\
{}\nArea: {:.4f}' .format(polygon_3.get_perimeter(), polygon_3.get_area()))
