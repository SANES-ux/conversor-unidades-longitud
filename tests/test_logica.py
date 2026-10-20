"""
Pruebas de la lógica base de conversión.
"""

import unittest
from app import convertir_longitud


class TestLogicaConversor(unittest.TestCase):
    """Pruebas base del conversor."""

    def test_metros_a_centimetros(self):
        self.assertAlmostEqual(convertir_longitud(1.0, "Metros (m)", "Centímetros (cm)"), 100.0)

    def test_centimetros_a_milimetros(self):
        self.assertAlmostEqual(convertir_longitud(10.0, "Centímetros (cm)", "Milímetros (mm)"), 100.0)

    def test_milimetros_a_metros(self):
        self.assertAlmostEqual(convertir_longitud(1000.0, "Milímetros (mm)", "Metros (m)"), 1.0)


if __name__ == "__main__":
    unittest.main()

