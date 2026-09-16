import math

class MiPunto:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def distancia(self, punto_o_x, y=None):

        if isinstance(punto_o_x, MiPunto):
            x2 = punto_o_x.getX()
            y2 = punto_o_x.getY()

        else:
            x2 = punto_o_x
            y2 = y
        distancia = math.sqrt(
            (x2 - self.__x) ** 2 +
            (y2 - self.__y) ** 2
        )

        return distancia

p1 = MiPunto()
p2 = MiPunto(10, 30.5)

print("Punto 1: (", p1.getX(), ",", p1.getY(), ")")
print("Punto 2: (", p2.getX(), ",", p2.getY(), ")")

resultado = p1.distancia(p2)

print("Distancia entre los puntos:", resultado)


