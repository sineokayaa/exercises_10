class Circle:
    '''
    This is a class describing a circle.

    Attributes of class
    -----------
    - all_circles: a list collecting all instances of the class.
    - pi: an attribute of the class containing the value of the number pi.

    Attributes
    -----------
    - r: an attribute that stores the radius of a circle.

    Methods
    --------
    - area(): Returns the area of the circle.
    - total_area(): Returns the total area of all instances of the Circle class.
    '''
    all_circles = []
    pi = 3.1415

    def __init__(self, r=None):
        if r is None:
            self.r = 1
        else:
            self.r = r
        Circle.all_circles.append(self)

    def __str__(self):
        return f'{self.r}'

    def __repr__(self):
        return self.__str__()

    def area(self):
        '''
        Calculate and return the area of the circle.
        '''
        area = Circle.pi * self.r ** 2
        return area

    @staticmethod
    def total_area():
        '''
        Calculate and return the total area of all instances of the Circle class.
        '''
        summ = 0
        for area in Circle.all_circles:
            summ += area.r ** 2 * Circle.pi
        return summ


c1 = Circle()
c2 = Circle(7)
c3 = Circle(5)
print(c2.area())
print(c3)
print(Circle.pi)
print(Circle.all_circles)
print(Circle.total_area())
print(len(c3.__class__.all_circles))
