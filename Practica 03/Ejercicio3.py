class Sensor:
    tipo = "Generico"

    def __init__(self, id):
        self.id = id
        self.encendido = False

    def activar(self):
        self.encendido = True
        print(self.tipo, "activado")

    def desactivar(self):
        self.encendido = False
        print(self.tipo, "desactivado")

    def mostrar(self):
        print("Tipo:", self.tipo)
        print("ID:", self.id)
        print("Encendido:", self.encendido)

class Camara(Sensor):
    tipo = "Camara"

    def __init__(self, id, resolucion):
        super().__init__(id)
        self.resolucion = resolucion

    def mostrar(self):
        super().mostrar()
        print("Resolucion:", self.resolucion)

class SensorLuzLaser(Sensor):
    tipo = "Luz Laser"

    def __init__(self, id, alcance):
        super().__init__(id)
        self.alcance = alcance

    def mostrar(self):
        super().mostrar()
        print("Alcance:", self.alcance, "metros")

class VehiculoAutonomo(Camara, SensorLuzLaser):
    tipo = "Vehiculo Autonomo"

    def __init__(self, id, resolucion, alcance):
        Sensor.__init__(self, id)
        self.resolucion = resolucion
        self.alcance = alcance

    def mostrar(self):
        print("\n VEHICULO AUTONOMO ")
        print("Tipo:", self.tipo)
        print("ID:", self.id)
        print("Resolucion:", self.resolucion)
        print("Alcance:", self.alcance, "metros")
        print("Encendido:", self.encendido)

class Aplicacion:
    @staticmethod
    def main():
        sensor1 = Sensor("S001")
        camara1 = Camara("C001", "1920x1080")
        laser1 = SensorLuzLaser("L001", 100)
        vehiculo1 = VehiculoAutonomo(
            "VA001", "4K", 200
        )

        print(" SENSOR ")
        sensor1.mostrar()
        sensor1.activar()

        print("\n CAMARA ")
        camara1.mostrar()
        camara1.activar()

        print("\n SENSOR LUZ LASER ")
        laser1.mostrar()
        laser1.activar()

        print("\n VEHICULO AUTONOMO ")
        vehiculo1.mostrar()
        vehiculo1.activar()
        vehiculo1.desactivar()

if __name__ == "__main__":
    Aplicacion.main()
