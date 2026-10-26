# 📐 Visual Precalculus (Precálculo Animado con Manim)

Animaciones matemáticas rigurosas y didácticas desarrolladas con [Manim Community Edition](https://www.manim.community/), basadas en la colección de libros de texto de Precálculo (**Colección Yachay Tech / Editorial Amarun**, Dr. Juan Mayorga-Zambrano).

El objetivo de este repositorio es resolver y visualizar los **ejercicios pares** de cada capítulo, proporcionando explicaciones animadas con una duración prudente, ritmo pedagógico equilibrado e identidad gráfica andina.

---

## 🎨 Principios de Diseño e Identidad Visual

Las animaciones siguen un estándar pedagógico y estético unificado mediante la clase base [`AmarunExerciseScene`](common/base_scene.py):

* **Enunciado Permanente y Legibilidad en Dos Líneas (`arrange_direction=DOWN`):** Fijado en la parte superior en un recuadro institucional rojo poncho (`#a32f30`), visible durante todo el video. Cuando el enunciado es extenso, la arquitectura lo distribuye automáticamente en dos líneas verticales (descripción arriba y expresión matemática abajo), garantizando que las fuentes nunca se compriman ni se reduzcan indebidamente.
* **Estándar Tipográfico de Alta Visibilidad:**
  * **Texto descriptivo de enunciado:** $\ge 20.0\text{ pt}$ (o $28.0\text{ pt}$ en enunciados directos).
  * **Expresiones matemáticas de enunciado:** $25.0 - 30.0\text{ pt}$.
  * **Panel izquierdo (mutación algebraica):** $\ge 24.5 - 25.0\text{ pt}$.
  * **Panel derecho (justificaciones teóricas con `minipage`):** $\ge 22.5\text{ pt}$.
  * **Gráfica cartesiana:** Números de ejes a $15.0\text{ pt}$, nombres de ejes a $21.0\text{ pt}$ y etiquetas de curvas a $\ge 18.0\text{ pt}$.
* **Metamorfosis Algebraica (Estilo 3Blue1Brown):** En el panel izquierdo, las expresiones matemáticas mutan directamente en su lugar (`ReplacementTransform`), mientras el panel derecho actualiza la justificación teórica paso a paso.
* **Tachado Explícito:** Al simplificar factores fraccionarios, se trazan líneas diagonales en rojo poncho sobre los términos cancelados, con pausas de asimilación antes de la reducción.
* **Estructura Pedagógica (Preferencia de ~6 a 8 Pasos):** Desglose estructurado de etapas progresivas bien delimitadas, adaptándose con flexibilidad según la naturaleza del problema sin forzar pasos artificiales ni omitir justificaciones deductivas.
* **Barra de Progreso Interactiva:** En la parte inferior ($y = -3.55$), una línea con nodos dinámicos indica la etapa activa (amarillo inca), las etapas superadas (verde andino) y el rótulo de la fase actual.
* **Interpretación Gráfica Cartesiana:** Cada ejercicio concluye con la visualización de la curva en el plano cartesiano, destacando puntos abiertos (discontinuidades evitables), asíntotas, vértices y cortes con los ejes.
* **Paleta Andina Institucional ([common/styles.py](common/styles.py)):**
  * Fondo: Carbón noche andino (`#151212`)
  * Enunciado / Títulos: Blanco alpaca (`#fdfbf7`) y Turquesa Amarun (`#8ec3c0`)
  * Énfasis algebraico: Oro Inca (`#f6b840`) y Terracota (`#db5a38`)
  * Conclusiones: Verde esmeralda andino (`#48bb78`)
  * Exclusiones / Tachado: Rojo Poncho Yachay (`#a32f30`)

---

## 🎬 Niveles de Calidad y Resolución de Renderizado

Manim permite compilar cualquier ejercicio en 5 niveles de resolución y tasa de cuadros mediante la bandera `-q` (`--quality`):

| Bandera | Perfil | Resolución | Tasa de Cuadros | Carpeta de Salida | Propósito Recomendado |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **`-ql`** | *Low* (Baja) | **854 × 480** (480p) | 15 fps | `media/.../480p15/` | **Desarrollo y pruebas rápidas** (renderiza en ~15–20 s) |
| **`-qm`** | *Medium* (Media) | **1280 × 720** (720p HD) | 30 fps | `media/.../720p30/` | Revisiones intermedias y dispositivos móviles |
| **`-qh`** | *High* (Alta) | **1920 × 1080** (1080p FHD) | 60 fps | `media/.../1080p60/` | **Estándar para YouTube, clases virtuales y proyectores** |
| **`-qp`** | *Production* (2K) | **2560 × 1440** (1440p QHD) | 60 fps | `media/.../1440p60/` | Monitores de alta densidad y edición de video |
| **`-qk`** | *FourK* (Ultra Alta) | **3840 × 2160** (4K UHD) | 60 fps | `media/.../2160p60/` | **Máxima calidad cinematográfica / Máster de archivo** |

### ⚡ Automatización con `render.py` (Recomendado)

El repositorio incluye un script CLI inteligente (`render.py`) que detecta automáticamente todos los ejercicios del repositorio (Capítulos 5 y 6, y la serie personalizada de Jhoselyn), compila con Manim en la resolución deseada y genera de forma inmediata la vista previa GIF optimizada:

```bash
# 1. Previsualización rápida (480p15 + GIF automático):
python render.py 5.2
python render.py 6.2
python render.py jh.1

# 2. Renderizado en Alta Calidad (Full HD 1080p a 60 fps):
python render.py 5.2 --high
python render.py 6.4 --high
python render.py jh.9 --high

# 3. Renderizado en Máxima Calidad (4K Ultra HD a 60 fps):
python render.py 5.4 --4k

# 4. Listar los 51 ejercicios disponibles y su estado de render/GIF:
python render.py --list

# 5. Renderizar todos los ejercicios en bloque (batch):
python render.py all --low
```

### 📁 Organización y Exportación de Videos (`organizar_videos.py`)

Para mantener el directorio limpio y estructurado sin depender de los directorios internos de Manim (`media/`), el script `organizar_videos.py` escanea y sincroniza automáticamente las versiones en mayor resolución hacia la carpeta raíz `videos/`:

```bash
python organizar_videos.py
```
Estructura resultante de distribución:
* `videos/capitulo_05/`: 39 videos Full HD 1080p60 / 4K.
* `videos/capitulo_06/`: 3 videos Full HD 1080p60.
* `videos/jhoselyn/`: 9 videos Full HD 1080p60.

### Comandos Manuales de Manim

Si prefieres invocar directamente las herramientas del sistema:

* **Desarrollo rápido (480p15):**
  ```bash
  manim -ql libro2_precalculo/cap05_funciones_reales/ej_05_02.py Ejercicio05_02
  ```
* **Calidad alta (1080p60):**
  ```bash
  manim -qh libro2_precalculo/cap05_funciones_reales/ej_05_02.py Ejercicio05_02
  ```
* **Máxima resolución (4K UHD 60fps):**
  ```bash
  manim -qk libro2_precalculo/cap05_funciones_reales/ej_05_02.py Ejercicio05_02
  ```
* **Generar GIF optimizado manualmente:**
  ```bash
  ffmpeg -y -i media/videos/ej_05_02/480p15/Ejercicio05_02.mp4 \
         -vf "fps=10,scale=480:-1:flags=lanczos" \
         docs/previews/ej_05_02.gif
  ```

---

## 📂 Estructura del Repositorio

```text
visual-precalculus/
├── common/                             # Módulos compartidos y arquitectura
│   ├── base_scene.py                  # AmarunExerciseScene (clase base reutilizable)
│   ├── styles.py                      # Paleta de colores andina e identitaria
│   └── __init__.py
├── docs/                               # Previews y material de documentación
│   └── previews/                      # GIFs optimizados para README (51 previews)
├── ejercicios_jhoselyn/                 # Serie de tutoría universitaria personalizada (Ejercicios 01 al 09)
│   ├── ej_jh_01.py                    # Ejercicio Jh 01 (Parábola cuadrática completa)
│   ├── ej_jh_02.py                    # Ejercicio Jh 02 (Polinomio cúbico impar)
│   ├── ...
│   └── ej_jh_09.py                    # Ejercicio Jh 09 (Transformaciones canónicas)
├── videos/                             # Videos finales compilados en alta resolución (1080p60)
│   ├── capitulo_05/                   # 39 videos finales del Capítulo 5
│   ├── capitulo_06/                   # 3 videos finales del Capítulo 6
│   └── jhoselyn/                      # 9 videos finales de la serie Jhoselyn
├── EJERCICIOS_DOCS_JHOSELYN.md         # Compendio formal de ejercicios resueltos y de examen
├── GUIA_EJERCICIOS_JHOSELYN.md         # Protocolo de examen, trampas frecuentes y plan de estudio
├── images/                             # Activos gráficos institucionales
│   ├── Fondo_Poncho.jpg               # Muestra textil del poncho Yachay Tech
│   └── logo_Amarun.jpg                # Isotipo oficial de Editorial Amarun
├── libro2_precalculo/                 # Libro 2: Precálculo 2
│   ├── cap05_funciones_reales/        # Capítulo 5: Funciones reales (39 ejercicios)
│   │   ├── ej_05_02.py                # Ejercicio 5.2 (RMD, dominio y gráfico)
│   │   ├── ...
│   │   ├── ej_05_44.py                # Ejercicio 5.44 (RMD en racionales y radicales)
│   │   ├── ej_05_46.py                # Ejercicio 5.46 (Composición de funciones reales)
│   │   ├── ...
│   │   └── ej_05_78.py                # Ejercicio 5.78 (Ecuaciones logarítmicas y raíces extrañas)
│   ├── cap06_funciones_trigonometricas/ # Capítulo 6: Funciones trigonométricas
│   │   ├── ej_06_02.py                # Ejercicio 6.2 (Paridad de la función coseno)
│   │   ├── ej_06_04.py                # Ejercicio 6.4 (Coseno del ángulo doble)
│   │   └── ej_06_06.py                # Ejercicio 6.6 (Identidades del seno y ángulo doble)
│   ├── cap07_numeros_complejos/
│   ├── cap08_polinomios_racionales/
│   └── cap09_sucesiones_reales/
├── TRACKING.md                         # Hoja de ruta y checklist de ejercicios pares
├── requirements.txt                   # Dependencias de Python
├── render.py                          # CLI inteligente de automatización de renders
├── organizar_videos.py                # Sincronizador de videos a la carpeta videos/
└── .gitignore                         # Exclusión de renders pesados locales
```

---

## 🚀 Instalación y Requisitos

### 1. Dependencias del Sistema

Se requiere Python 3.10+ junto con FFmpeg y LaTeX para la rasterización de fórmulas:

```bash
# En Ubuntu / Debian / WSL:
sudo apt update
sudo apt install -y libcairo2-dev libpango1.0-dev pkg-config \
                    ffmpeg texlive-latex-base texlive-latex-extra \
                    texlive-fonts-recommended dvisvgm
```

### 2. Dependencias de Python

```bash
pip install -r requirements.txt
```

---

## 📋 Catálogo y Progreso de Ejercicios

Consulta [TRACKING.md](TRACKING.md) para ver la lista completa de ejercicios pares cubiertos, en desarrollo y planificados.

| Módulo / Colección | Ejercicios Implementados | Estado de Videos (1080p60) | Vistas Previas GIF | Cobertura |
| :--- | :---: | :---: | :---: | :---: |
| **Capítulo 5: Funciones Reales** | **39** (Ej. 5.2 al 5.78) | ✅ 39/39 en `videos/capitulo_05/` | ✅ 39/39 en `docs/previews/` | **100%** |
| **Capítulo 6: Funciones Trigonométricas** | **3** (Ej. 6.2, 6.4, 6.6) | ✅ 3/3 en `videos/capitulo_06/` | ✅ 3/3 en `docs/previews/` | **100%** |
| **Serie Tutoría Jhoselyn (Quiz 4 / Nivelación)** | **9** (Jh 01 al Jh 09) | ✅ 9/9 en `videos/jhoselyn/` | ✅ 9/9 en `docs/previews/` | **100%** |
| **TOTAL GENERAL** | **51 Ejercicios** | **✅ 51 Videos Full HD** | **✅ 51 GIFs Optimizados** | **100%** |

### Muestra 1: Capítulo 5 · Ejercicio 5.2
> **Tema:** Regla del Máximo Dominio (RMD)  
> **Problema:** Encontrar el dominio de $h(x) = \ln\left(\frac{x^3+1}{x+1}\right)$  
> **Resultado:** $\operatorname{Dom}(h) = \mathbb{R} \setminus \{-1\}$  
> **Comportamiento Gráfico:** Curva $y = \ln(x^2 - x + 1)$ con discontinuidad evitable (punto abierto) en $(-1, \ln 3)$.

![Ejercicio 5.2](docs/previews/ej_05_02.gif)

### Muestra 2: Capítulo 5 · Ejercicio 5.4
> **Tema:** Paridad de Funciones (Teorema 5.4)  
> **Problema:** Demostrar paridad para $f \cdot g$, $f/g$, $f_1 + f_2$ y $g_1 + g_2$.  
> **Resultado:** $f \cdot g$ y $f/g$ son impares; $f_1 + f_2$ es par; $g_1 + g_2$ es impar.  
> **Comportamiento Gráfico:** Simetría axial (eje Y) vs. simetría central (origen).

![Ejercicio 5.4](docs/previews/ej_05_04.gif)

### Muestra 3: Capítulo 5 · Ejercicio 5.6
> **Tema:** Propiedades del Valor Absoluto (Teorema 5.6)  
> **Problema:** Demostrar $|a \cdot b| = |a| \cdot |b|$ para todo $a, b \in \mathbb{R}$ usando la definición $|x| = \sqrt{x^2}$.  
> **Resultado:** Radicando $(ab)^2 = a^2 b^2 \implies \sqrt{a^2}\sqrt{b^2} = |a||b|$. Corolario: $|a/b| = |a|/|b|$ si $b \neq 0$.  
> **Comportamiento Gráfico:** Dilatación y contracción métrica en la familia de curvas $f_k(x) = |k \cdot x| = |k||x|$.

![Ejercicio 5.6](docs/previews/ej_05_06.gif)

### Muestra 4: Capítulo 5 · Ejercicio 5.8
> **Tema:** Desigualdad Triangular (Corolario 5.11)  
> **Problema:** Demostrar $||x| - |y|| \le |x - y|$ y $|x - y| \le |x - a| + |a - y|$ para todo $x, y, a \in \mathbb{R}$.  
> **Resultado:** Acotamiento doble $-|x - y| \le |x| - |y| \le |x - y| \implies ||x| - |y|| \le |x - y|$. Descomposición con punto intermedio.  
> **Comportamiento Gráfico:** Función cuenca $g(a) = |x - a| + |a - y|$ con piso mínimo en $|x - y| = 3$ e intervalo de igualdad $a \in [-1, 2]$.

![Ejercicio 5.8](docs/previews/ej_05_08.gif)

### Muestra 5: Capítulo 5 · Ejercicio 5.10
> **Tema:** Inyectividad de Funciones (Sección 5.5)  
> **Problema:** Probar que $g: \mathbb{R} \to \mathbb{R}$ con $g(x) = 2x^3 - 1$ es inyectiva y graficar en el plano cartesiano.  
> **Resultado:** $(x_1 - x_2)(x_1^2 + x_1 x_2 + x_2^2) = 0 \implies x_1 = x_2$ pues $(x_1 + x_2/2)^2 + \frac{3}{4}x_2^2 > 0$ si $(x_1, x_2) \neq (0, 0)$.  
> **Comportamiento Gráfico:** Curva cúbica $g(x) = 2x^3 - 1$ con corte en $(0, -1)$, verificando el test de la recta horizontal con preimagen única en $(1, 1)$.

![Ejercicio 5.10](docs/previews/ej_05_10.gif)

### Muestra 6: Capítulo 5 · Ejercicio 5.12
> **Tema:** Paridad de la Función Inversa (Teorema 5.15)  
> **Problema:** Probar que si $f: \mathbb{R} \to \mathbb{R}$ es biyectiva e impar, entonces $f^{-1}$ es también impar.  
> **Resultado:** $-y = -f(x) = f(-x) \implies f^{-1}(-y) = -x = -f^{-1}(y)$ para todo $y \in \mathbb{R}$.  
> **Comportamiento Gráfico:** Simetría axial respecto a la diagonal $y = x$ y simetría central respecto al origen $(0, 0)$ en las curvas $f(x) = x^3$ y $f^{-1}(x) = \sqrt[3]{x}$.

![Ejercicio 5.12](docs/previews/ej_05_12.gif)

### Muestra 7: Capítulo 5 · Ejercicio 5.14
> **Tema:** Monotonía de la Suma de Funciones (Teorema 5.18)  
> **Problema:** Probar que la suma de crecientes es creciente, y que creciente más estrictamente creciente es estrictamente creciente.  
> **Resultado:** $f(x_1) \le f(x_2) \land g(x_1) < g(x_2) \implies (f+g)(x_1) < (f+g)(x_2)$. Aditividad de la tasa de variación $\alpha_{f+g} = \alpha_f + \alpha_g > 0$.  
> **Comportamiento Gráfico:** Superposición cartesiana de $f(x) = x$ y $g(x) = x^3$ generando la curva más inclinada $(f+g)(x) = x + x^3$, evaluada en $x = 1$.

![Ejercicio 5.14](docs/previews/ej_05_14.gif)

### Muestra 8: Capítulo 6 · Ejercicio 6.2
> **Tema:** Paridad de la Función Coseno (Teorema 6.3)  
> **Problema:** Demostración axiomática a partir de los postulados P1–P4: $\forall x \in \mathbb{R}: \cos(-x) = \cos(x)$.  
> **Resultado:** Simetría axial respecto al eje $y$ con visualización trigonométrica rigurosa.  
> **Comportamiento Gráfico:** Curva cosenoidal simétrica con corte en $(0, 1)$ y raíces en $\pm\frac{\pi}{2}$.

![Ejercicio 6.2](docs/previews/ej_06_02.gif)

### Muestra 9: Capítulo 6 · Ejercicio 6.4
> **Tema:** Coseno del Ángulo Doble (Corolario 6.9)  
> **Problema:** Demostrar $\forall x \in \mathbb{R}: \cos(2x) = \cos^2(x) - \operatorname{sen}^2(x)$ a partir de la identidad del coseno de la suma.  
> **Resultado:** Deducción deductiva mediante sustitución simétrica $y = x$.  
> **Comportamiento Gráfico:** Curva resultante con duplicación de frecuencia y periodo $T = \pi$.

![Ejercicio 6.4](docs/previews/ej_06_04.gif)

---

## 🎓 Serie Especial: Tutoría Universitaria para Jhoselyn (Nivelación Yachay Tech)

Serie de animaciones matemáticas en alta definición (**1080p60**) con duración pedagógica calibrada ($55-65\text{ s}$), tipografía legible garantizada ($\ge 20.0\text{ pt}$ en enunciado multilínea, $\ge 21.0 - 25.0\text{ pt}$ en fórmulas y $\ge 22.5\text{ pt}$ en justificaciones) y maquetación estructurada, basada en sus guías de estudio (`Grafica de funciones.pdf`, `2.6.pdf` y `2.5.pdf`):

| Ejercicio | Guía / Tema | Función de Estudio | Código Manim | Video 1080p60 | Vista Previa |
| :---: | :---: | :--- | :---: | :---: | :---: |
| **Jh 01** | Quiz 4 | $f(x) = -\frac{1}{2}x^2 + \frac{3}{2}x + \frac{27}{8}$ | [`ej_jh_01.py`](ejercicios_jhoselyn/ej_jh_01.py) | [`EjercicioJh_01.mp4`](videos/jhoselyn/EjercicioJh_01.mp4) | [GIF](docs/previews/ej_jh_01.gif) |
| **Jh 02** | Quiz 4 | $f(x) = \frac{1}{2}x^3 - \frac{3}{2}x$ | [`ej_jh_02.py`](ejercicios_jhoselyn/ej_jh_02.py) | [`EjercicioJh_02.mp4`](videos/jhoselyn/EjercicioJh_02.mp4) | [GIF](docs/previews/ej_jh_02.gif) |
| **Jh 03** | Quiz 4 | $f(x) = \frac{1}{4}x^4 - \frac{3}{2}x^2 + \frac{5}{4}$ | [`ej_jh_03.py`](ejercicios_jhoselyn/ej_jh_03.py) | [`EjercicioJh_03.mp4`](videos/jhoselyn/EjercicioJh_03.mp4) | [GIF](docs/previews/ej_jh_03.gif) |
| **Jh 04** | Quiz 4 | $f(x) = \frac{x^2 - 1}{x^2 - 4}$ | [`ej_jh_04.py`](ejercicios_jhoselyn/ej_jh_04.py) | [`EjercicioJh_04.mp4`](videos/jhoselyn/EjercicioJh_04.mp4) | [GIF](docs/previews/ej_jh_04.gif) |
| **Jh 05** | Quiz 4 | $f(x) = \frac{x^3 - 4x}{x^2 - 1}$ | [`ej_jh_05.py`](ejercicios_jhoselyn/ej_jh_05.py) | [`EjercicioJh_05.mp4`](videos/jhoselyn/EjercicioJh_05.mp4) | [GIF](docs/previews/ej_jh_05.gif) |
| **Jh 06** | Quiz 4 | $f(x) = \frac{x^2 - 9}{x^2 - 1}$ | [`ej_jh_06.py`](ejercicios_jhoselyn/ej_jh_06.py) | [`EjercicioJh_06.mp4`](videos/jhoselyn/EjercicioJh_06.mp4) | [GIF](docs/previews/ej_jh_06.gif) |
| **Jh 07** | Quiz 4 | $f(x) = \sqrt{\frac{x^2 - 1}{x^2 - 4}}$ | [`ej_jh_07.py`](ejercicios_jhoselyn/ej_jh_07.py) | [`EjercicioJh_07.mp4`](videos/jhoselyn/EjercicioJh_07.mp4) | [GIF](docs/previews/ej_jh_07.gif) |
| **Jh 08** | Guía 2.6 | $f: [0, \infty) \to [1, \infty), \; f(x) = x^2 + 1$ | [`ej_jh_08.py`](ejercicios_jhoselyn/ej_jh_08.py) | [`EjercicioJh_08.mp4`](videos/jhoselyn/EjercicioJh_08.mp4) | [GIF](docs/previews/ej_jh_08.gif) |
| **Jh 09** | Guía 2.5 | $g(x) = -\frac{3}{2}(2x + 4)^2 + 5$ | [`ej_jh_09.py`](ejercicios_jhoselyn/ej_jh_09.py) | [`EjercicioJh_09.mp4`](videos/jhoselyn/EjercicioJh_09.mp4) | [GIF](docs/previews/ej_jh_09.gif) |
| **Jh 10** | Guía 2.5 | $g(x) = -2f(x - 3) + 4$ vs $h(x) = f(-2(x - 3)) + 4$ | [`ej_jh_10.py`](ejercicios_jhoselyn/ej_jh_10.py) | [`EjercicioJh_10.mp4`](videos/jhoselyn/EjercicioJh_10.mp4) | [GIF](docs/previews/ej_jh_10.gif) |

### Muestra Destacada: Transformaciones Cuadráticas Canónicas (Ejercicio Jh 09)
> **Tema:** Factorización de argumento $2(x+2)$, forma canónica $g(x) = -6(x+2)^2 + 5$, vértice $V(-2, 5)$ y gráfica cartesiana dual.

![Ejercicio Jh 09](docs/previews/ej_jh_09.gif)
