class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self):
        return self._length * self._width * 25 * 5


r = Road(100, 50)
print(r.calculate_mass())
