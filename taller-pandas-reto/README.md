# Taller Práctico: Manipulación y Limpieza de DataFrames con Pandas

Este repositorio contiene la solución al **Reto Práctico Integrador** del taller de Ciencia de Datos I.

## Descripción del Reto
El objetivo del reto es aplicar técnicas de normalización de cadenas, filtrado compuesto con máscaras booleanas y proyección tabular de datos sobre un dataset de librería.

### Criterios de Selección:
1. `categoria_limpia` sea exactamente `'Libreria'`.
2. `forma_pago_estandarizada` sea `'debito'`.
3. `cantidad_vendida` sea mayor o igual a `20` unidades.

## 🚀 Resultados y Auditoría

### DataFrame Resultante:
| | producto | precio | sucursal |
|---|---|---|---|
| **1** | lapicera | 1200 | Centro |
| **9** | Lapiz | 900 | Centro |

### Auditoría Tecnológica:
- **Tipo de Objeto:** `<class 'pandas.core.frame.DataFrame'>`
- **Dimensiones (`shape`):** `(2, 3)` (2 filas y 3 columnas)
