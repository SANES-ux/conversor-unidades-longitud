# Conversor de Unidades de Longitud 📏

Aplicación de escritorio interactiva desarrollada en Python con **CustomTkinter** para realizar conversiones entre Milímetros (mm), Centímetros (cm) y Metros (m).

## 🚀 Características

- **Interfaz moderna y adaptable**: Construida con CustomTkinter con soporte para modo claro/oscuro del sistema.
- **Conversión bidireccional precisa**: Soporta conversiones entre:
  - Milímetros (mm)
  - Centímetros (cm)
  - Metros (m)
- **Soporte numérico**: Permite enteros y decimales (usando punto `.` o coma `,`).
- **Validaciones en tiempo real**: Alertas intuitivas en caso de campos vacíos o entradas no numéricas.
- **Acciones rápidas**:
  - Botón **Convertir** y ejecución rápida con la tecla `Enter`.
  - Botón **⇅ Intercambiar unidades** para alternar origen y destino al instante sin perder el valor.
  - Botón **Limpiar** para reiniciar la interfaz a su estado por defecto.

## 📦 Requisitos e Instalación

1. Asegúrate de tener Python 3.8 o superior instalado.
2. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

## 💻 Ejecución

Para iniciar la aplicación, ejecuta el siguiente comando en la terminal:

```bash
python app.py
```
*(En Windows también puedes usar `py app.py`)*

## 🧪 Pruebas Unitarias

Para ejecutar la suite de pruebas unitarias:

```bash
python -m unittest discover tests
```

## 📂 Estructura del Proyecto

```text
├── app.py              # Código fuente principal de la aplicación GUI
├── SPEC.md             # Especificación técnica y requerimientos
├── requirements.txt    # Dependencias del proyecto
├── .gitignore          # Exclusiones de Git
├── README.md           # Documentación del proyecto
└── tests/              # Suite de pruebas automatizadas
    └── test_mejora.py  # Tests unitarios de conversión e intercambio
```
