import math

class AlgebraVectorial:
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getZ(self):
        return self.__z
    def suma(self, b):
        return AlgebraVectorial(
            self.__x + b.__x,
            self.__y + b.__y,
            self.__z + b.__z
        )
    def resta(self, b):
        return AlgebraVectorial(
            self.__x - b.__x,
            self.__y - b.__y,
            self.__z - b.__z
        )
    def longitud(self):
        return math.sqrt(
            self.__x ** 2 +
            self.__y ** 2 +
            self.__z ** 2
        )
    def productoEscalar(self, b):
        return (
            self.__x * b.__x +
            self.__y * b.__y +
            self.__z * b.__z
        )
    def perpendicular(self, b):
        return math.isclose(
            self.suma(b).longitud(),
            self.resta(b).longitud()
        )
    def perpendicular3(self, b):
        return math.isclose(
            self.productoEscalar(b), 0
        )
    def perpendicular4(self, b):
        return math.isclose(
            self.suma(b).longitud() ** 2,
            self.longitud() ** 2 +
            b.longitud() ** 2
        )
    def paralela(self, b, r):
        return (
            math.isclose(self.__x, r * b.__x) and
            math.isclose(self.__y, r * b.__y) and
            math.isclose(self.__z, r * b.__z)
        )
    def paralela2(self, b):
        x = self.__y * b.__z - self.__z * b.__y
        y = self.__z * b.__x - self.__x * b.__z
        z = self.__x * b.__y - self.__y * b.__x
        return (
            math.isclose(x, 0) and
            math.isclose(y, 0) and
            math.isclose(z, 0)
        )
    def proyeccion(self, b):
        producto = self.productoEscalar(b)
        longitud2 = b.longitud() ** 2
        if longitud2 == 0:
            raise ValueError("Vector cero")
        factor = producto / longitud2
        return AlgebraVectorial(
            factor * b.__x,
            factor * b.__y,
            factor * b.__z
        )
    def componente(self, b):
        longitud = b.longitud()
        if longitud == 0:
            raise ValueError("Vector cero")
        return self.productoEscalar(b) / longitud
    def __str__(self):
        return f"({self.__x}, {self.__y}, {self.__z})"
a = AlgebraVectorial(3, 4, 0)
b = AlgebraVectorial(4, -3, 0)
c = AlgebraVectorial(6, 8, 0)

print("a =", a)
print("b =", b)
print("c =", c)
print("\nPERPENDICULAR")
print(" |a+b| = |a-b|:", a.perpendicular(b))
print("  a · b = 0:", a.perpendicular3(b))
print(" |a+b|² = |a|² + |b|²:", a.perpendicular4(b))
print("\nPARALELA")
print(" a = r b:", c.paralela(a, 2))
print(" a * b = 0:", c.paralela2(a))
print("\nPROYECCION")
print(" Proyección de a sobre b:", a.proyeccion(b))
print("\nCOMPONENTE")
print(" Componente de a en b:", a.componente(b))
