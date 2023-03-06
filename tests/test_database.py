import csv
import config
import helpers
import unittest
import database as db


class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Vehiculos.lista = [
            db.Coche("11A", "rojo", "4", "200", "2000"),
            db.Motocicleta("55E", "rosa", "2", "urbana", "200", "2000"),
            db.Quad("66F", "negro", "4", "200", "2000", "urbana", "modelo", "1000")
        ]

    def test_buscar_vehiculo(self):
        vehiculo_existente = db.Vehiculos.buscar('11A')
        vehiculo_inexistente = db.Vehiculos.buscar('77G')
        self.assertIsNotNone(vehiculo_existente)
        self.assertIsNone(vehiculo_inexistente)

    def test_crear_vehiculo(self):
        nuevo_vehiculo = db.Vehiculos.crear('2', '22B', 'azul', '2', 'urbana')
        self.assertEqual(len(db.Vehiculos.lista), 4)
        self.assertEqual(nuevo_vehiculo.id, '22B')
        self.assertEqual(nuevo_vehiculo.color, 'azul')
        self.assertEqual(nuevo_vehiculo.ruedas, '2')
        self.assertEqual(nuevo_vehiculo.tipo, 'urbana')

    def test_borrar_vehiculo(self):
        vehiculo_borrado = db.Vehiculos.borrar('11A')
        vehiculo_rebuscado = db.Vehiculos.buscar('11A')
        self.assertEqual(vehiculo_borrado.id, '11A')
        self.assertIsNone(vehiculo_rebuscado)

    def test_id_valido(self):
        self.assertTrue(helpers.id_valido('00A', db.Vehiculos.lista))
        self.assertFalse(helpers.id_valido('232323S', db.Vehiculos.lista))
        self.assertFalse(helpers.id_valido('F35', db.Vehiculos.lista))
        self.assertFalse(helpers.id_valido('11A', db.Vehiculos.lista))

    def test_escritura_csv(self):
        db.Vehiculos.borrar('11A')
        db.Vehiculos.borrar('55E')

        vehiculo, id, color, ruedas, velocidad, cilindrada, tipo, modelo, carga = None, None, None, None, None, None, None, None, None
        with open(config.DATABASE_PATH, newline='\n') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            vehiculo, id, color, ruedas, velocidad, cilindrada, tipo, modelo, carga= next(reader)

        self.assertEqual(vehiculo, 'Quad')
        self.assertEqual(id, '66F')
        self.assertEqual(color, 'negro')
        self.assertEqual(ruedas, '4')
        self.assertEqual(velocidad, '200')
        self.assertEqual(cilindrada, '2000')
        self.assertEqual(tipo, 'urbana')
        self.assertEqual(modelo, 'modelo')
        self.assertEqual(carga, '1000')