import helpers
import database as db



def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("========================")
        print("  Bienvenido al Gestor  ")
        print("========================")
        print("[1] Listar los vehículos ")
        print("[2] Buscar un vehículo   ")
        print("[3] Añadir un cliente   ")
        print("[4] Modificar un cliente")
        print("[5] Borrar un cliente   ")
        print("[6] Cerrar el Gestor    ")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Listando los vehiculos...\n")
            for vehiculo in db.Vehiculos.lista:
                print("{}: {}".format(type(vehiculo).__name__, vehiculo))
        
        elif opcion == '2':
            print("Buscando un vehiculo...\n")
            id = helpers.leer_texto(3, 3, "ID (2 int y 1 char)").upper()
            vehiculo = db.Vehiculos.buscar(id)
            print(vehiculo) if vehiculo else print("Vehículo no encontrado.")

        elif opcion == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")
