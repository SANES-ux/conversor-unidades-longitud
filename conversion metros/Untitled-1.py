"""
Aplicación de Escritorio para Conversión de Unidades de Longitud
(Milímetros, Centímetros y Metros) con CustomTkinter.
"""

import customtkinter as ctk
from tkinter import messagebox


# Configuración global del tema y estilo visual
ctk.set_appearance_mode("System")  # Detecta automáticamente modo Claro/Oscuro del sistema
ctk.set_default_color_theme("blue")  # Paleta de colores principal


class ConversorLongitudApp(ctk.CTk):
    """Clase principal de la interfaz gráfica del conversor de longitud."""

    # Factores de conversión estándar hacia metros (unidad base)
    FACTORES_A_METROS = {
        "Milímetros (mm)": 0.001,
        "Centímetros (cm)": 0.01,
        "Metros (m)": 1.0,
    }

    # Símbolos abreviados para mostrar en el resultado final
    SIMBOLOS = {
        "Milímetros (mm)": "mm",
        "Centímetros (cm)": "cm",
        "Metros (m)": "m",
    }

    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Conversor de Longitud")
        self.geometry("450x520")
        self.resizable(False, False)

        # Construcción y organización de widgets
        self._crear_widgets()

    def _crear_widgets(self):
        """Crea y posiciona todos los componentes visuales de la aplicación."""
        opciones_unidades = list(self.FACTORES_A_METROS.keys())

        # Contenedor central con tarjeta/card estilizada
        self.card = ctk.CTkFrame(self, corner_radius=15)
        self.card.pack(padx=25, pady=25, fill="both", expand=True)

        # Título principal
        self.label_titulo = ctk.CTkLabel(
            self.card,
            text="Conversor de Longitud",
            font=ctk.CTkFont(size=22, weight="bold"),
        )
        self.label_titulo.pack(pady=(20, 5))

        self.label_subtitulo = ctk.CTkLabel(
            self.card,
            text="Milímetros · Centímetros · Metros",
            font=ctk.CTkFont(size=12),
            text_color="gray",
        )
        self.label_subtitulo.pack(pady=(0, 20))

        # Entrada de valor
        self.label_valor = ctk.CTkLabel(
            self.card,
            text="Valor a convertir:",
            font=ctk.CTkFont(size=14, weight="bold"),
            anchor="w",
        )
        self.label_valor.pack(fill="x", padx=30, pady=(5, 3))

        self.entry_valor = ctk.CTkEntry(
            self.card,
            placeholder_text="Ej: 1.55",
            height=40,
            font=ctk.CTkFont(size=15),
        )
        self.entry_valor.pack(fill="x", padx=30, pady=(0, 15))
        # Permitir convertir pulsando la tecla Enter
        self.entry_valor.bind("<Return>", lambda event: self.convertir())

        # Selector: Unidad de origen ("De")
        self.label_de = ctk.CTkLabel(
            self.card,
            text="De (Unidad de origen):",
            font=ctk.CTkFont(size=14, weight="bold"),
            anchor="w",
        )
        self.label_de.pack(fill="x", padx=30, pady=(5, 3))

        self.combo_de = ctk.CTkOptionMenu(
            self.card,
            values=opciones_unidades,
            height=38,
            font=ctk.CTkFont(size=13),
        )
        self.combo_de.pack(fill="x", padx=30, pady=(0, 15))

        # Selector: Unidad de destino ("A")
        self.label_a = ctk.CTkLabel(
            self.card,
            text="A (Unidad de destino):",
            font=ctk.CTkFont(size=14, weight="bold"),
            anchor="w",
        )
        self.label_a.pack(fill="x", padx=30, pady=(5, 3))

        self.combo_a = ctk.CTkOptionMenu(
            self.card,
            values=opciones_unidades,
            height=38,
            font=ctk.CTkFont(size=13),
        )
        self.combo_a.pack(fill="x", padx=30, pady=(0, 20))

        # Marco para los botones de acción
        self.frame_botones = ctk.CTkFrame(self.card, fg_color="transparent")
        self.frame_botones.pack(fill="x", padx=30, pady=(0, 20))

        self.btn_convertir = ctk.CTkButton(
            self.frame_botones,
            text="Convertir",
            height=40,
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.convertir,
        )
        self.btn_convertir.pack(side="left", expand=True, fill="x", padx=(0, 8))

        self.btn_limpiar = ctk.CTkButton(
            self.frame_botones,
            text="Limpiar",
            height=40,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#6c757d",
            hover_color="#5a6268",
            command=self.limpiar,
        )
        self.btn_limpiar.pack(side="right", expand=True, fill="x", padx=(8, 0))

        # Área para mostrar el resultado
        self.label_resultado = ctk.CTkLabel(
            self.card,
            text="Resultado: —",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="#1f538d",
        )
        self.label_resultado.pack(pady=(10, 15))

        # Establecer valores iniciales predeterminados
        self.limpiar()

    def convertir(self):
        """Valida las entradas, realiza la conversión y muestra el resultado."""
        texto_ingresado = self.entry_valor.get().strip()

        # Validación 1: Verificar si el campo está vacío
        if not texto_ingresado:
            messagebox.showwarning(
                "Campo vacío",
                "Por favor, ingrese un valor numérico para convertir.",
            )
            self.entry_valor.focus_set()
            return

        # Validación 2: Intentar parsear el número (soporta '.' y ',' como separador decimal)
        texto_normalizado = texto_ingresado.replace(",", ".")
        try:
            valor = float(texto_normalizado)
        except ValueError:
            messagebox.showerror(
                "Valor inválido",
                "Ha ingresado caracteres no numéricos o un formato inválido.\n"
                "Ejemplos válidos: 10, 2.5, 0.75",
            )
            self.entry_valor.focus_set()
            return

        # Obtener unidades seleccionadas
        unidad_origen = self.combo_de.get()
        unidad_destino = self.combo_a.get()

        # Cálculo matemático pasando por la unidad base (metros)
        valor_en_metros = valor * self.FACTORES_A_METROS[unidad_origen]
        resultado = valor_en_metros / self.FACTORES_A_METROS[unidad_destino]

        # Formatear el resultado para evitar ceros innecesarios al final
        resultado_formateado = f"{resultado:.6f}".rstrip("0").rstrip(".")
        simbolo_destino = self.SIMBOLOS.get(unidad_destino, "")

        # Actualizar la interfaz con el resultado obtenido
        self.label_resultado.configure(
            text=f"Resultado: {resultado_formateado} {simbolo_destino}"
        )

    def limpiar(self):
        """Restaura los campos y selecciones a sus valores por defecto."""
        self.entry_valor.delete(0, "end")
        self.combo_de.set("Metros (m)")
        self.combo_a.set("Centímetros (cm)")
        self.label_resultado.configure(text="Resultado: —")
        self.entry_valor.focus_set()


if __name__ == "__main__":
    app = ConversorLongitudApp()
    app.mainloop()
