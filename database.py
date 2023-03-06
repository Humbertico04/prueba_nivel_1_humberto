import csv

class Vehiculo():
    def __init__(self, id, color, ruedas):
        self.id = id
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)
    
class Coche(Vehiculo):
    def __init__(self, id, color, ruedas, velocidad, cilindrada):
        super().__init__(id, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)

class Bicicleta(Vehiculo):
    def __init__(self, id, color, ruedas, tipo):
        super().__init__(id, color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return Vehiculo.__str__(self) + ", de tipo {}".format(self.tipo)

class Formula1(Coche):
    def __init__(self, id, color, ruedas, numBastidor, velocidad, cilindrada, equipo):
        super().__init__(id, color, ruedas, numBastidor, velocidad, cilindrada)
        self.equipo = equipo
    def __str__(self):
        return Coche.__str__(self) + ", del equipo {}".format(self.equipo)
    
class Camioneta(Coche):
    def __init__(self, id, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(id, color, ruedas, velocidad, cilindrada)
        self.carga = carga
    def __str__(self):
        return Coche.__str__(self) + ", {} kg de carga".format(self.carga)
    
class Motocicleta(Bicicleta):
    def __init__(self, id, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(id, color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Bicicleta.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)

class Quad(Coche):
    def __init__(self, id, color, ruedas, velocidad, cilindrada, tipo, modelo, carga):
        super().__init__(id, color, ruedas, velocidad, cilindrada)
        self.tipo = tipo
        self.modelo = modelo
        self.carga = carga
    def __str__(self):
        return Coche.__str__(self) + ", de tipo {}, modelo {}, {} kg de carga".format(self.tipo, self.modelo, self.carga)

vehiculo = Vehiculo(123, "rojo", 4)
coche = Coche(123, "rojo", 4, 200, 1000)
motocicleta = Motocicleta(123, "rojo", 2, "deportiva", 200, 1000)
quad = Quad(123, "rojo", 4, "deportiva", 200, 1000, "modelo", 1000)

print(quad)

def catalogar(lista, ruedas=None):
    contador = 0
    for vehiculo in lista:
        if vehiculo.ruedas == ruedas:
            print("{}: {}".format(type(vehiculo).__name__, vehiculo))
            contador +=1
        elif ruedas == None:
            print("{}: {}".format(type(vehiculo).__name__, vehiculo))
    if vehiculo.ruedas == ruedas:
        print("Se han encontrado {} vehículos con {} ruedas".format(contador, ruedas))
    return contador

catalogar(lista=[vehiculo, coche, motocicleta, quad], ruedas=4)

# class Vehiculos:
#     lista = []
#     with open(config.db_path("bicis"), newline='\n') as fichero:
#         reader = csv.reader(fichero, delimiter=';')
#         for color, ruedas, tipo, velocidad, cilindrada in reader:
#             vehiculo = Vehiculo(color, ruedas, tipo, velocidad, cilindrada)
#             lista.append(vehiculo)

#     with open(config.db_path("coches"), newline='\n') as fichero:
#         reader = csv.reader(fichero, delimiter=';')
#         for color, ruedas, velocidad, cilindrada, carga in reader:
#             vehiculo = Vehiculo(color, ruedas, velocidad, cilindrada, carga)
#             lista.append(vehiculo)

    # @staticmethod
    # def buscar(dni):
    #     for cliente in Clientes.lista:
    #         if cliente.dni == dni:
    #             return cliente

    # @staticmethod
    # def crear(dni, nombre, apellido):
    #     cliente = Cliente(dni, nombre, apellido)
    #     Clientes.lista.append(cliente)
    #     Clientes.guardar()
    #     return cliente

    # @staticmethod
    # def modificar(dni, nombre, apellido):
    #     for indice, cliente in enumerate(Clientes.lista):
    #         if cliente.dni == dni:
    #             Clientes.lista[indice].nombre = nombre
    #             Clientes.lista[indice].apellido = apellido
    #             Clientes.guardar()
    #             return Clientes.lista[indice]

    # @staticmethod
    # def borrar(dni):
    #     for indice, cliente in enumerate(Clientes.lista):
    #         if cliente.dni == dni:
    #             cliente = Clientes.lista.pop(indice)
    #             Clientes.guardar()
    #             return cliente

    # @staticmethod
    # def guardar():
    #     with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
    #         writer = csv.writer(fichero, delimiter=';')
    #         for cliente in Clientes.lista:
    #             writer.writerow((cliente.dni, cliente.nombre, cliente.apellido))


