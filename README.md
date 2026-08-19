# Práctica TDD: Máquina de Café

Implementación de una máquina dispensadora de café utilizando **Test-Driven Development (TDD)** en Python con `unittest`.

---

## 🎯 Requerimientos

1. **Tamaños de vaso:**
   - Pequeño: 3 Oz
   - Mediano: 5 Oz
   - Grande: 7 Oz
2. **Azúcar:** Selección de cucharadas de azúcar.
3. **Validación de disponibilidad:**
   - Sin vasos suficientes: `"No hay Vasos"`
   - Sin café suficiente: `"No hay Cafe"`
   - Sin azúcar suficiente: `"No hay Azucar"`
4. **Despacho:**
   - Descuenta los insumos utilizados.
   - Retorna: `"Felicitaciones"`

---

## 📁 Estructura del Proyecto

- `vaso.py`: Manejo y control de vasos.
- `cafetera.py`: Manejo del café disponible.
- `azucarero.py`: Manejo del azúcar disponible.
- `maquina_de_cafe.py`: Orquestador principal de la máquina.
- `main.py`: Programa interactivo por consola.
- `pruebas/`: Suite completa de pruebas unitarias (`unittest`).

---

## 🧪 Ejecutar Pruebas

Para ejecutar todas las pruebas unitarias:

```bash
python -m unittest discover -s pruebas -v
```

---

## ☕ Ejecutar la Aplicación

Para interactuar con la máquina desde la terminal:

```bash
python main.py
```
