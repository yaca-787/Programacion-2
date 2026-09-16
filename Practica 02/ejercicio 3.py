import math

class Vector:
    def __init__(self, a1, a2, a3):
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
    def __add__(self, o):
        a1 = self.__a1 + o.__a1
        a2 = self.__a2 + o.__a2
        a3 = self.__a3 + o.__a3
        return Vector(a1, a2, a3)
    def __mul__(self, r):
        if isinstance(r, (int, float)):
            return Vector(
                r * self.__a1,
                r * self.__a2,
                r * self.__a3
            )
        return self.__a1 * r.__a1 + \
               self.__a2 * r.__a2 + \
               self.__a3 * r.__a3
    def __rmul__(self, r):
        return self * r
    def __abs__(self):
        return math.sqrt(
            self.__a1 ** 2 +
            self.__a2 ** 2 +
            self.__a3 ** 2
        )
    def normal(self):
        longitud = abs(self)
        if longitud == 0:
            raise ValueError(
                "No se puede calcular el normal de un vector cero"
            )
        return Vector(
            self.__a1 / longitud,
            self.__a2 / longitud,
            self.__a3 / longitud
        )
    def __matmul__(self, o):
        return self.__a1 * o.__a1 + \
               self.__a2 * o.__a2 + \
               self.__a3 * o.__a3
    def __xor__(self, o):
        a1 = self.__a2 * o.__a3 - self.__a3 * o.__a2
        a2 = self.__a3 * o.__a1 - self.__a1 * o.__a3
        a3 = self.__a1 * o.__a2 - self.__a2 * o.__a1
        return Vector(a1, a2, a3)
    def __str__(self):
        return "({}, {}, {})".format(
            self.__a1,
            self.__a2,
            self.__a3
        )
        
a = Vector(1, 2, 3)
b = Vector(4, 5, 6)
print("a =", a)
print("b =", b)
print("Suma =", a + b)
print("Multiplicacion por escalar =", 2 * a)
print("Longitud de a =", abs(a))
print("Normal de a =", a.normal())
print("Producto escalar =", a @ b)
print("Producto vectorial =", a ^ b)