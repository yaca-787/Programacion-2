import random

# CLASE JUEGO
class Juego:

    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.vidasIniciales = numeroDeVidas
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales

    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas

        print("Record:", self.record)

    def quitaVida(self):
        self.numeroDeVidas -= 1

        print("Vidas restantes:", self.numeroDeVidas)

        return self.numeroDeVidas > 0

# CLASE JUEGOADIVINANUMERO
class JuegoAdivinaNumero(Juego):

    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()

        self.numeroAAdivinar = random.randint(0, 10)

        print("\n JUEGO ADIVINA NUMERO ")
        print("Adivina un numero entre 0 y 10")

        while self.numeroDeVidas > 0:

            try:
                numero = int(input("Introduce un numero: "))
            except ValueError:
                print("Introduce un numero entero.")
                continue

            if numero < 0 or numero > 10:
                print("El numero debe estar entre 0 y 10.")
                continue

            if numero == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                return

            quedanVidas = self.quitaVida()

            if quedanVidas:
                if self.numeroAAdivinar > numero:
                    print("El numero a adivinar es mayor.")
                else:
                    print("El numero a adivinar es menor.")

                print("Intenta de nuevo.")

            else:
                print("Perdiste!!")
                print("El numero era:", self.numeroAAdivinar)
                return

class Aplicacion:

    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()

if __name__ == "__main__":
    Aplicacion.main()
