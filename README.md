# 📐 Visual Precalculus (Precálculo Animado con Manim)

Animaciones matemáticas rigurosas y didácticas desarrolladas con [Manim Community Edition](https://www.manim.community/), basadas en la colección de libros de texto de Precálculo (**Colección Yachay Tech / Editorial Amarun**, Dr. Juan Mayorga-Zambrano).

El objetivo de este repositorio es resolver y visualizar los **ejercicios pares** de cada capítulo, proporcionando explicaciones animadas con una duración prudente y un ritmo pedagógico equilibrado.

---

## ⏱️ Metodología de Animación y Ritmo (Pacing)

Cada animación está estructurada bajo la **regla de los 3 actos** para garantizar claridad y una duración óptima (~45 a 90 segundos):

1. **Acto 1: Enunciado y Asimilación (~10–14 s):**
   * Encabezado con capítulo, número de ejercicio par y tema.
   * Presentación del enunciado en $\LaTeX$ dentro de un marco destacado.
   * Pausa calculada proporcionalmente a la longitud del problema para lectura completa.
2. **Acto 2: Planteamiento Conceptual (~15–30 s):**
   * El enunciado se minimiza a la esquina superior.
   * Construcción de ejes, curvas, transformaciones o condiciones analíticas.
3. **Acto 3: Resolución Paso a Paso (~20–35 s):**
   * Desarrollo algebraico fluido con transiciones matemáticas.
   * Destacado de la respuesta final con recuadro verde y pausa final de contemplación antes del cierre.

---

## 📂 Estructura del Repositorio

```text
visual-precalculus/
├── common/                             # Módulos compartidos y estilos
│   ├── base_scene.py                  # Clase BaseExerciseScene con temporización estándar
│   └── styles.py                      # Paleta de colores consistente y tiempos base
├── libro2_precalculo/                 # Libro 2: Precálculo 2
│   ├── cap05_funciones_reales/        # Capítulo 5: Funciones reales
│   │   └── ej_05_02.py                # Ejercicio 5.2 (RMD y dominio)
│   ├── cap06_funciones_trigonometricas/
│   ├── cap07_numeros_complejos/
│   ├── cap08_polinomios_racionales/
│   └── cap09_sucesiones_reales/
├── TRACKING.md                         # Hoja de ruta y checklist de ejercicios pares
├── requirements.txt                   # Dependencias de Python
└── .gitignore                         # Exclusión de archivos pesados y renders locales
```

---

## 🚀 Instalación y Uso

### 1. Requisitos Previos

Se requiere Python 3.10+ y las dependencias multimedia del sistema para Manim:

```bash
# En Ubuntu / Debian / WSL:
sudo apt update
sudo apt install -y ffmpeg texlive-full
```

### 2. Instalar dependencias de Python

```bash
pip install -r requirements.txt
```

### 3. Renderizar una animación

* **Previsualización rápida (baja resolución, render en segundos):**
  ```bash
  manim -ql -p libro2_precalculo/cap05_funciones_reales/ej_05_02.py Ejercicio05_02
  ```

* **Render final en alta calidad (1080p 60fps):**
  ```bash
  manim -qh libro2_precalculo/cap05_funciones_reales/ej_05_02.py Ejercicio05_02
  ```

---

## 📋 Catálogo y Progreso de Ejercicios

Consulta [TRACKING.md](TRACKING.md) para ver la lista completa de ejercicios pares cubiertos, en desarrollo y planificados.
