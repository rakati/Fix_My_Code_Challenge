#!/usr/bin/python3


class square():
    """ A class represent Square"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initialize square parameters width and height"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Calculate the permiter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Return string representation of the square details"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Create a square and test our class"""
    s = square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
