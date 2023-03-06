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
        print("[5] Borrar un vehículo   ")
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
            print("{}: {}".format(type(vehiculo).__name__, vehiculo)) if vehiculo else print("Vehículo no encontrado.")

        elif opcion == '3':
            print("=======================")
            print(" Selección de Vehículo  ")
            print("=======================")
            print("[1] Coche")
            print("[2] Bicicleta   ")
            print("[3] Formula 1   ")
            print("[4] Camioneta")
            print("[5] Motocicleta   ")
            print("[6] Quad    ")
            print("=======================")

            opcion = input("> ")
            helpers.limpiar_pantalla()
            print("Añadiendo un vehiculo...\n")
            id = None
            while True:
                id = helpers.leer_texto(3, 3, "ID (2 int y 1 char)").upper()
                if helpers.id_valido(id, db.Vehiculos.lista):
                    break

            color = helpers.leer_texto(2, 30, "Color (de 2 a 30 chars)").capitalize()
            ruedas = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 chars)").capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente añadido correctamente.")

        elif opcion == '5':
            print("Borrando un vehículo...\n")
            dni = helpers.leer_texto(3, 3, "ID (2 int y 1 char)").upper()
            print("Vehículo borrado correctamente.") if db.Vehiculos.borrar(
                dni) else print("Vehículo no encontrado.")

        elif opcion == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")
