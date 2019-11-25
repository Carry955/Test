class Vector3:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def __add__(self, anotherPoint):
        x = self.__x + anotherPoint.__x
        y = self.__y + anotherPoint.__y
        z = self.__z + anotherPoint.__z
        return Vector3(x, y, z)

    def __sub__(self, anotherPoint):
        x = self.__x - anotherPoint.__x
        y = self.__y - anotherPoint.__y
        z = self.__z - anotherPoint.__z
        return Vector3(x, y, z)

    def __mul__(self, n):
        x, y, z = self.__x * n, self.__y * n, self.__z * n
        return Vector3(x, y, z)

    def __truediv__(self, n):
        x, y, z = self.__x / n, self.__y / n, self.__z / n
        return Vector3(x, y, z)

    @property
    def length(self):
        return (self.__x ** 2 + self.__y ** 2 + self.__z ** 2) ** 0.5

    def __str__(self):
        return 'Vector3({},{},{})'.format(self.__x, self.__y, self.__z)


v1 = Vector3(3, 4, 5)
v2 = Vector3(5, 6, 7)
print(v1 + v2)
print(v1 - v2)
print(v1 * 3)
print(v2 / 2)
print(v2.length)