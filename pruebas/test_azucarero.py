import unittest

from azucarero import Azucarero


class PruebasAzucarero(unittest.TestCase):
    def setUp(self):
        self.azucarero = Azucarero(10)

    def test_debe_decir_verdadero_si_hay_azucar(self):
        self.assertTrue(self.azucarero.hay_azucar(5))
        self.assertTrue(self.azucarero.hay_azucar(10))

    def test_debe_decir_falso_si_no_hay_azucar(self):
        self.assertFalse(self.azucarero.hay_azucar(15))

    def test_debe_restar_azucar(self):
        self.azucarero.dar_azucar(5)
        self.assertEqual(5, self.azucarero.obtener_cantidad_azucar())

        self.azucarero.dar_azucar(2)
        self.assertEqual(3, self.azucarero.obtener_cantidad_azucar())


if __name__ == "__main__":
    unittest.main()
