import math
class Shape:
    id = 0
    def __init__(self):
        Shape.id +=1

    def print(self):
        print("Shape, perimeter: undefined, area: undefined")

    def perimeter(self):
        pass
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def perimeter(self):
        return math.pi * self.radius * 2
    def area(self):
        return math.pi * self.radius**2

    def print(self):
        print("Circle, perimeter:", format(self.perimeter(), ".5f"), "area:", format(self.area(), ".5f"))


class Ellipse(Shape):
    def __init__(self, semi_ma, semi_mi):
        super().__init__()
        self.semi_ma = semi_ma
        self.semi_mi = semi_mi


    def perimeter(self):
        pass

    def area(self):
        return math.pi * self.semi_ma * self.semi_mi

    def eccentricity(self):
        result = self.semi_ma ** 2 - self.semi_mi ** 2
        if result >= 0:
            result = math.sqrt(result)
        else:
            result = None
        return result

    def print(self):
        if self.eccentricity() is None:
            print("Ellipse, perimeter: undefined, area:", format(self.area(), ".5f"), "linear eccentricity: None")
        else:
            print("Ellipse, perimeter: undefined, area:", format(self.area(), ".5f"), "linear eccentricity:",
                  format(self.eccentricity(), ".5f"))

class Rhombus(Shape):
    def __init__(self, d1, d2):
        super().__init__()
        self.d1 = d1
        self.d2 = d2

    def perimeter(self):
        return 2 * math.sqrt(self.d1 ** 2 + self.d2 ** 2)

    def area(self):
        return (self.d1 * self.d2)/2

    def side(self):
        return math.sqrt(self.d1 ** 2 + self.d2 ** 2)/2

    def inradius(self):
        return (self.d1 * self.d2)/(2 * math.sqrt(self.d1 ** 2 + self.d2 ** 2))

    def print(self):
        print("Rhombus, perimeter:", format(self.perimeter(), ".5f"), "area:", format(self.area(), ".5f"), "in-radius:", format(self.inradius(), ".5f"))
