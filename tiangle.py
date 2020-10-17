"""
Program for calculating areas of triangle.
"""

from math import sqrt

def area(line1, line2, line3):
    """
    Calculates how many triangle in area and calculating triangle .
    """

    s=(line1+line2+line3)/2
    result = sqrt(s*(s-line1)*(s-line2)*(s-line3))
    return result


def main():
    line1 = float(input("Enter the length of the first side: "))
    line2 = float(input("Enter the length of the second side: "))
    line3 = float(input("Enter the length of the third side: "))

    dx = area(line1, line2, line3)

    print("The triangle's area is {:.1f}".format(dx))


if __name__ == "__main__":
    main()