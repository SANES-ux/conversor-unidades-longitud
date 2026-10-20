# Especificación del Conversor de Unidades de Longitud (SPEC.md)

## 1. Descripción General
Aplicación de escritorio interactiva desarrollada en Python con `CustomTkinter` para la conversión precisa entre unidades de longitud del sistema métrico:
- Milímetros (`mm`)
- Centímetros (`cm`)
- Metros (`m`)

---

## 2. Componentes de la Interfaz Gráfica (GUI)
- **Tarjeta central (Card)**: Diseño moderno centrado con esquinas redondeadas.
- **Título y Subtítulo**: Identificación clara de la aplicación.
- **Campo de Valor (`entry_valor`)**:
  - Entrada de texto con placeholder de ejemplo.
  - Soporte de tecla <kbd>Enter</kbd> para conversión rápida.
  - Acepta enteros y decimales (usando punto o coma decimal).
- **Selector Origen (`combo_de`)**: Menú desplegable con las unidades origen disponibles.
- **Botón Intercambiar (`btn_intercambiar`)**: Botón central con ícono `⇅ Intercambiar unidades`.
- **Selector Destino (`combo_a`)**: Menú desplegable con las unidades destino disponibles.
- **Acciones principales**:
  - **Convertir (`btn_convertir`)**: Realiza el cálculo matemático y formatea el resultado.
  - **Limpiar (`btn_limpiar`)**: Restablece los selectores a valores por defecto, limpia el campo de texto y el resultado.
- **Área de Resultado (`label_resultado`)**: Etiqueta destacada en tamaño y color visible mostrando el valor final con su símbolo.

---

## 3. Especificación de la Mejora: Intercambiar Unidades (Issue #1)

### 3.1 Comportamiento
Al presionar el botón **Intercambiar unidades** (`btn_intercambiar`):
1. Intercambia la unidad de origen (`combo_de`) con la de destino (`combo_a`).
2. Conserva íntegramente el texto que el usuario haya escrito en el campo de entrada (`entry_valor`).
3. Restablece el texto del resultado a `Resultado: —` (borra el cálculo previo).
4. **No** realiza la conversión de forma automática.
5. El botón **Convertir** sigue funcionando exactamente igual.

### 3.2 Criterios de Aceptación
- Si el origen es `Milímetros (mm)` y destino `Metros (m)`, pasa a origen `Metros (m)` y destino `Milímetros (mm)`.
- El campo `entry_valor` no se modifica ni se limpia.
- `label_resultado` vuelve al estado neutro `Resultado: —`.
- Presionar el botón dos veces seguidas restablece las unidades a su estado inicial.
- Toda la lógica existente de validación y cálculo permanece intacta y funcional.

---

## 4. Validaciones y Manejo de Errores
1. **Campo vacío**: Alerta visual advirtiendo al usuario que debe introducir un valor numérico.
2. **Entrada no numérica**: Alerta de error si se ingresan letras o caracteres no válidos.
3. **Normalización decimal**: Convierte automáticamente comas `,` a puntos `.` antes del cálculo.

---

## 5. Pruebas Automatizadas
Ubicadas en `tests/test_mejora.py`:
- `TestConversorLogica`: Pruebas de conversión entre mm, cm y m.
- `TestMejoraIntercambiar`: Verificación de todos los criterios de aceptación del intercambio de unidades.
