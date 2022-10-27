from exceptions import NotComplexNumber


class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):
        return f"{self.x} + {self.y}i"


    def __add__(self, other):
        try:
            self.validate_numbers(other)
        except NotComplexNumber as err:
            print(err)
        else:
            return Complex(self.x + other.x, self.y + other.y)


    def __mul__(self, other):
        try:
            self.validate_numbers(other)
        except NotComplexNumber as err:
            print(err)
        else:
            first_part = self.x * other.x
            im_part = self.x * other.y + self.y * other.x
            last_part = -(self.y * other.y)
            return Complex(first_part + last_part, im_part)


    def validate_numbers(self, other):
        if not isinstance(other, Complex):
            raise NotComplexNumber


first = Complex(-7, 8)
second = Complex(0, 3)
x = first + 23
print(first * second)

