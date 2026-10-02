# Repaso de Python para Data Science

Práctica del **Módulo 0 – Unidad 1** del curso *Data Science II: Machine Learning para la Ciencia de Datos* (Coderhouse).

El objetivo es consolidar el manejo de datos básicos en Python antes de pasar a librerías como Pandas o Scikit-Learn.

## Contenido

| Archivo | Descripción |
|---|---|
| `analisis_basico.py` | Script con las 4 tareas de la práctica |

## Tareas resueltas

1. **Variables:** nombre (`str`), precio (`float`), stock (`int`) y descuento (`bool`) de un producto, resumidos con f-strings.
2. **Bucle + condicional:** la lista `precios` se recorre y cada valor se clasifica como *Caro* (> 100) o *Económico* (≤ 100).
3. **Diccionario:** `almacen` guarda producto → stock; se agrega un producto nuevo y se consulta uno específico.
4. **Función:** `resumen_estadistico(numeros)` recibe una lista y devuelve un diccionario con `suma`, `promedio` y `cantidad`.

## Cómo ejecutarlo

```bash
python analisis_basico.py
```

No requiere librerías externas (Python 3.8+).

## Salida esperada (extracto)

```
Resumen estadístico: {'suma': 60, 'promedio': 20.0, 'cantidad': 3}
```

---
Autor: Matías Rodríguez
