import os
import platform

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

def tipo_clase(objeto):
    return type(objeto).__name__

def catalogar(lista, ruedas=None):
    contador = 0
    for vehiculo in lista:
        if vehiculo.ruedas == ruedas:
            print("{}: {}".format(type(vehiculo).__name__, vehiculo))
            contador +=1
            print("Se han encontrado {} vehículos con {} ruedas".format(contador, ruedas))
        elif ruedas == None:
            print("{}: {}".format(type(vehiculo).__name__, vehiculo))
    return contador
