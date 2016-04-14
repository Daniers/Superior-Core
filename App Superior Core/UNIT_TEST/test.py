# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../CLASSES/')
from credencial import Credencial

class TestStringMethods(unittest.TestCase):
    """
    def test_upper(self):
        self.assertEqual()
    """

    def test_obtener_permisos_vacio(self):
        """
            Caso de prueba a la función obtener_permisos de la clase Credencial,
            enviandole un parametro vacío.
        """
        credencial = Credencial()
        self.assertFalse(credencial.obtener_permisos("hola"))
        codigo = input("Ingrese Código: ")
        self.assertTrue(credencial.obtener_permisos(codigo))

    """
    def test_split(self):
        #s = 'hello world'
        s = 34
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    """
if __name__ == '__main__':
    unittest.main()