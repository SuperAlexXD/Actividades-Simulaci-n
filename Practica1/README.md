# Simulación de Lluvia

Proyecto académico de la asignatura **Simulación** — Unidad 1.

Modelo matemático: **I = 0.5H + 0.3N + 0.2Tr**

## Patrones aplicados
- **MVC**: `modelos/`, `vistas/`, `controladores/`
- **Strategy**: `IndiceBase` vs `IndiceAjustado` en `servicios/simulador.py`

## Reglas de clasificación
| Índice I        | Estado           |
|-----------------|------------------|
| I < 0.40        | Sin lluvia       |
| 0.40 ≤ I < 0.60 | Baja posibilidad |
| 0.60 ≤ I < 0.75 | Lluvia probable  |
| I ≥ 0.75        | Lluvia           |

## Ejecución

pip install -r requirements.txt
python main.py
Autor
Nombre: Tu nombre

Docente: José O. Guamán Q.

---

## ✅ Orden recomendado para programar

1. `modelos/clima.py`
2. `modelos/__init__.py`
3. `servicios/simulador.py`
4. `servicios/__init__.py`
5. `controladores/controlador.py`
6. `controladores/__init__.py`
7. `vistas/vista.py`
8. `vistas/__init__.py`
9. `main.py`
10. `requirements.txt`, `.gitignore`, `README.md`

---

## 🚀 Probar

pip install -r requirements.txt
python main.py
Deberías ver dos tablas en consola y una ventana con la gráfica comparativa.