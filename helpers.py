import os
import platform

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto    

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
