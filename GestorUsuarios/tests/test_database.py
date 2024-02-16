import copy
import unittest
import Database as db
import Helpers


class TestDatabase (unittest.TestCase):
    
    def setUp(self):
        db.Clientes.lista = [db.Cliente("48271857", "Emerson", "Escalante"),
                             db.Cliente("58271857", 'Luis', 'Gonzalez'),
                             db.Cliente("68271857", 'Alexander', 'Gonzalez')]
        
    
    def test_buscar_Cliente(self):
        Cliente_existene = db.Clientes.BuscarCliente("48271857")
        Cliente_inexistene = db.Clientes.BuscarCliente("98271857")
        self.assertIsNotNone(Cliente_existene)
        self.assertIsNone(Cliente_inexistene)
        
    def test_crear_Cliente(self):
        nuevoCliente = db.Clientes.crearCliente("78271857", "Rebeca", "Romero")
        self.assertEqual(len(db.Clientes.lista),4)
        self.assertEqual(nuevoCliente.dui, "78271857")
        self.assertEqual(nuevoCliente.nombre, "Rebeca")
        self.assertEqual(nuevoCliente.apellido, "Romero")
        
    def test_modificar_cleinte(self):
        cliente_a_modificar = copy.copy(db.Clientes.BuscarCliente("68271857"))
        cliente_modificadp = db.Clientes.Modificar("68271857","William", "Gonzalez")
        self.assertEqual(cliente_a_modificar.nombre, "Alexander")
        self.assertEqual(cliente_modificadp.nombre, "William")
    
    def test_borara_cleinte(self):
        cliente_borrado = db.Clientes.Eliminar("58271857")
        cliente_buscado = db.Clientes.BuscarCliente("58271857")
        self.assertEqual(cliente_borrado.dui, "58271857")
        self.assertIsNone(cliente_buscado)
        
    def test_dui_valido(self):
        self.assertFalse(Helpers.validar_dui("1234567a", db.Clientes.lista))
        self.assertFalse(Helpers.validar_dui("1234567a89", db.Clientes.lista))