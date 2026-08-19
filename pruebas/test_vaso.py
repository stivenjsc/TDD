import unittest

from vaso import Vaso


class PruebasVaso(unittest.TestCase):
    def test_debe_decir_verdadero_si_hay_vasos(self):
        vasos_pequenos = Vaso(2, 10)
        self.assertTrue(vasos_pequenos.hay_vasos(1))

    def test_debe_decir_falso_si_no_hay_vasos(self):
        vasos_pequenos = Vaso(1, 10)
        self.assertFalse(vasos_pequenos.hay_vasos(2))

    def test_debe_restar_la_cantidad_de_vasos(self):
        vasos_pequenos = Vaso(5, 10)
        vasos_pequenos.dar_vasos(1)
        self.assertEqual(4, vasos_pequenos.obtener_cantidad_vasos())


if __name__ == "__main__":
    unittest.main()
