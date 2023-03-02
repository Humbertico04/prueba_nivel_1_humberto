class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas )
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)
    
# c = Coche("azul", 4, 150, 1200)
# print(c)
# Color azul, 4 km/h, 150 ruedas, 1200 cc

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return Vehiculo.__str__(self) + ", de tipo {}".format(self.tipo)
    
class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga
    def __str__(self):
        return Coche.__str__(self) + ", {} kg de carga".format(self.carga)
    
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        Bicicleta.__init__(self, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Bicicleta.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)

camioneta = Camioneta("negro", 4, 120, 2000, 1000)
motocicleta = Motocicleta("azul", 2, "deportiva", 180, 1000)
coche = Coche("rosa", 4, 210, 2500)
bicicleta = Bicicleta("marron", 2, "urbana")
lista = (camioneta, motocicleta, coche, bicicleta)


def catalogar(lista):
    for vehiculo in lista:
        print("{}: {}".format(type(vehiculo).__name__, vehiculo))
    return lista

catalogar(lista)

