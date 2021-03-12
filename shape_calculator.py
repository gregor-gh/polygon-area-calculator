import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (((self.width ** 2) + (self.height ** 2)) ** 0.5)

    def get_picture(self):
        # check if height or width over 50, retyrn error if so
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        pic = ""
        # loop through height and width
        h = self.height
        while h > 0:
            w = self.width
            while w > 0:
                pic += "*"
                w -= 1
            pic += "\n"
            h -= 1

        return pic

    def get_amount_inside(self, rect):
        w = self.width / rect.width
        h = self.height / rect.height

        return math.floor(w)*math.floor(h)
        


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return "Square(side="+str(self.width)+")"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side


rect = Rectangle(3, 6)
print(rect.get_diagonal())
