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

        print("Record:", self.record, "vidas restantes")

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("Vidas restantes:", self.numeroDeVidas)

        return self.numeroDeVidas > 0

# CLASE JUEGOADIVINANUMERO
class JuegoAdivinaNumero(Juego):

    def __init__(self, vidas):
        super().__init__(vidas)
        self.numeroAAdivinar = 0

    def validaNumero(self, numero):
        return 0 <= numero <= 10

    def generaNumero(self):
        return random.randint(0, 10)

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = self.generaNumero()

        print("\n JUEGO ADIVINA NUMERO ")
        print("Adivina un numero entre 0 y 10")
        print("Tienes", self.numeroDeVidas, "vidas.")

        while self.numeroDeVidas > 0:
            try:
                numero = int(input("Introduce un numero: "))
            except ValueError:
                print("Error: introduce un numero entero.")
                continue

            if not self.validaNumero(numero):
                print("Error: el numero debe estar entre 0 y 10.")
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

# CLASE JUEGOADIVINAPAR
class JuegoAdivinaPar(JuegoAdivinaNumero):

    def validaNumero(self, numero):
        if not 0 <= numero <= 10:
            print("Error: el numero debe estar entre 0 y 10.")
            return False

        if numero % 2 != 0:
            print("Error: debes introducir un numero par.")
            return False

        return True

    def generaNumero(self):
        return random.choice([0, 2, 4, 6, 8, 10])


# CLASE JUEGOADIVINAIMPAR
class JuegoAdivinaImpar(JuegoAdivinaNumero):

    def validaNumero(self, numero):
        if not 0 <= numero <= 10:
            print("Error: el numero debe estar entre 0 y 10.")
            return False

        if numero % 2 == 0:
            print("Error: debes introducir un numero impar.")
            return False

        return True

    def generaNumero(self):
        return random.choice([1, 3, 5, 7, 9])

class Aplicacion:

    @staticmethod
    def main():
        print("\n PRIMER JUEGO ")
        print("ADIVINA NUMERO")
        juego1 = JuegoAdivinaNumero(3)
        juego1.juega()

        print("\n SEGUNDO JUEGO ")
        print("ADIVINA NUMERO PAR")
        juego2 = JuegoAdivinaPar(3)
        juego2.juega()

        print("\n TERCER JUEGO ")
        print("ADIVINA NUMERO IMPAR")
        juego3 = JuegoAdivinaImpar(3)
        juego3.juega()

if __name__ == "__main__":
    Aplicacion.main()


# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    Aplicacion.main()
