from math import sqrt

class Vector:
    def __init__(self, init_tuple):
        self._entries = init_tuple

    def __getitem__(self, index):
        return self._entries[index]

    def __add__(self, vector):
        return Vector(tuple(entry + vector[i] for i, entry in enumerate(self._entries)))

    def __mul__(self, scalar):
        return Vector(tuple(scalar * entry for entry in self._entries))

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __str__(self):
        return "Vector{}".format(str(self._entries))

    @property
    def length(self):
        return sqrt(sum(entry ** 2 for entry in self._entries))

class Vector2D(Vector):
    def __init__(self, x, y):
        super().__init__((x, y))

    def rotate(self, angle):




v1 = Vector((1, 2, 3))
v2 = Vector((3, 2, 1))

print(v1 + 2 * v2)
print(v2.length)
