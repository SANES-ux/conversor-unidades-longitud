"""
Pruebas unitarias para la lógica del conversor y la nueva funcionalidad de intercambio de unidades.
"""

import unittest
from app import convertir_longitud, intercambiar_unidades, ConversorLongitudApp


class TestConversorLogica(unittest.TestCase):
    """Pruebas de la lógica de conversión matemática."""

    def test_metros_a_centimetros(self):
        self.assertAlmostEqual(convertir_longitud(1.5, "Metros (m)", "Centímetros (cm)"), 150.0)

    def test_milimetros_a_metros(self):
        self.assertAlmostEqual(convertir_longitud(2500, "Milímetros (mm)", "Metros (m)"), 2.5)

    def test_centimetros_a_milimetros(self):
        self.assertAlmostEqual(convertir_longitud(12.5, "Centímetros (cm)", "Milímetros (mm)"), 125.0)

    def test_misma_unidad(self):
        self.assertAlmostEqual(convertir_longitud(10, "Metros (m)", "Metros (m)"), 10.0)


class TestMejoraIntercambiar(unittest.TestCase):
    """Criterios de aceptación del Issue #1: Intercambiar unidades."""

    def test_intercambiar_unidades_mm_a_m(self):
        origen, destino = "Milímetros (mm)", "Metros (m)"
        nuevo_origen, nuevo_destino = intercambiar_unidades(origen, destino)
        self.assertEqual(nuevo_origen, "Metros (m)")
        self.assertEqual(nuevo_destino, "Milímetros (mm)")

    def test_pulsar_dos_veces_restaura_unidades(self):
        origen, destino = "Milímetros (mm)", "Metros (m)"
        o1, d1 = intercambiar_unidades(origen, destino)
        o2, d2 = intercambiar_unidades(o1, d1)
        self.assertEqual(o2, origen)
        self.assertEqual(d2, destino)

    def test_comportamiento_app_intercambiar(self):
        """Verifica que en la app se conserve el valor y se reinicie el resultado a 'Resultado: —'."""
        app = ConversorLongitudApp()
        # Evitar mostrar la ventana física durante tests
        app.withdraw()

        try:
            # 1. Configurar estado inicial
            app.entry_valor.insert(0, "42.5")
            app.combo_de.set("Milímetros (mm)")
            app.combo_a.set("Metros (m)")
            app.label_resultado.configure(text="Resultado: 0.0425 m")

            # 2. Ejecutar intercambiar
            app.intercambiar()

            # Verificaciones
            self.assertEqual(app.combo_de.get(), "Metros (m)")
            self.assertEqual(app.combo_a.get(), "Milímetros (mm)")
            self.assertEqual(app.entry_valor.get(), "42.5", "El valor debe conservarse exactamente")
            self.assertEqual(app.label_resultado.cget("text"), "Resultado: —", "El resultado debe resetearse a — sin autoconvertir")

            # 3. Pulsar de nuevo (dos veces restaura unidades)
            app.intercambiar()
            self.assertEqual(app.combo_de.get(), "Milímetros (mm)")
            self.assertEqual(app.combo_a.get(), "Metros (m)")
            self.assertEqual(app.entry_valor.get(), "42.5")
        finally:
            app.destroy()


if __name__ == "__main__":
    unittest.main()
