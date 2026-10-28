# Reglas Institucionales del Proyecto · Precálculo Universitario
### Editorial Amarun / Yachay Tech

---

## 🚫 REGLA FUNDAMENTAL: PROHIBICIÓN ESTRICTA DE DERIVADAS

**Este repositorio corresponde exclusivamente al curso de Precálculo Universitario.**  
Bajo ninguna circunstancia se deben emplear herramientas de Cálculo Diferencial en la resolución de ejercicios, guías, documentación o animaciones Manim.

### 1. Elementos Prohibidos
- ❌ **No usar la notación de derivadas:** Prohibido $f'(x)$, $y'$, $\frac{df}{dx}$, $\frac{d}{dx}$, etc.
- ❌ **No usar reglas de derivación:** Ni regla de la cadena, cociente, producto o potencias.
- ❌ **No usar criterios de derivadas:** Ni criterio de la primera derivada para monotonía/extremos ni criterio de la segunda derivada para concavidad.
- ❌ **No usar límites para derivadas:** No usar definición por cociente de Newton como sustituto encubierto.

---

## 📐 METODOLOGÍA OFICIAL DE PRECÁLCULO (HERRAMIENTAS PERMITIDAS)

Toda demostración analítica, justificación de monotonía, búsqueda de extremos y deducción de rango debe realizarse utilizando únicamente herramientas algebraicas y geométricas de **Precálculo**:

### 1. Monotonía (Crecimiento y Decrecimiento)
- **Definición Formal por Desigualdades:**
  - **Estrictamente Creciente:** Demostrar que $\forall x_1 < x_2 \implies f(x_1) < f(x_2)$.
  - **Estrictamente Decreciente:** Demostrar que $\forall x_1 < x_2 \implies f(x_1) > f(x_2)$.
- **Funciones Lineales / Afines ($f(x) = mx + b$):**
  - Justificar mediante el signo de la pendiente $m$:
    - $m > 0 \implies$ Función estrictamente creciente.
    - $m < 0 \implies$ Función estrictamente decreciente.
  - Demostración directa por desigualdades: $x_1 < x_2 \iff mx_1 > mx_2$ (cuando $m < 0$).
- **Funciones Racionales Homográficas ($f(x) = \frac{ax+b}{cx+d}$):**
  - Descomponer en forma canónica canónica: $f(x) = q + \frac{k}{cx+d}$.
  - Justificar el comportamiento aplicando las propiedades de orden del recíproco sobre intervalos de signo constante:
    $$0 < u < v \implies \frac{1}{u} > \frac{1}{v}$$
- **Funciones Cuadráticas ($f(x) = ax^2 + bx + c$):**
  - Identificar el eje de simetría $x = h = -\frac{b}{2a}$.
  - Analizar la monotonía a la izquierda ($x \le h$) y a la derecha ($x \ge h$) mediante la forma canónica $a(x-h)^2 + k$.

### 2. Extremos (Máximos y Mínimos)
- **En Intervalos Compactos con Monotonía:**
  - Si la función es monótona continua en $[a, b]$, los extremos globales ocurren únicamente en los extremos de frontera:
    - Decreciente: $M = f(a)$ (máximo) y $m = f(b)$ (mínimo).
    - Creciente: $m = f(a)$ (mínimo) y $M = f(b)$ (máximo).
- **Vértice de Parábolas:**
  - Completación canónica de cuadrados: $f(x) = a(x - h)^2 + k$.
  - Si $a > 0$, el mínimo absoluto es $k = f(h)$ en el vértice $V(h, k)$.
  - Si $a < 0$, el máximo absoluto es $k = f(h)$ en el vértice $V(h, k)$.
- **Funciones con Valor Absoluto y Raíces Cuadradas:**
  - Propiedad de no negatividad: $|u| \ge 0$ y $\sqrt{u} \ge 0$.
  - El vértice o mínimo natural ocurre donde el argumento se anula ($u = 0$), condicionado a si pertenece al dominio.

### 3. Deducción Rigurosa del Rango
- **Método de Construcción de Desigualdades:**
  - Partir de la doble desigualdad del dominio: $a \le x \le b$.
  - Aplicar operaciones que preservan o invierten el orden algebraico de manera justificada hasta obtener la expresión de $f(x)$.
- **Método de la Variable Dependiente (Despeje de $x$):**
  - Plantear $y = f(x)$, despejar $x = g(y)$ y analizar las restricciones de existencia real de $x$ en el dominio dado.

---

## 🎨 ESTÁNDARES EDITORIALES Y DE ANIMACIÓN MANIM

1. **Estructura Pedagógica:** Animaciones en 8 pasos con Metamorfosis 3B1B (`AmarunExerciseScene`).
2. **Duración:** Estrictamente calibrada en el rango $[55.0, 65.0]\text{ segundos}$.
3. **Escala Tipográfica HD:**
   - Enunciado institucional: $\ge 20.0\text{ pt}$ (descripción), $\ge 24.0\text{ pt}$ (fórmulas), `arrange_direction=DOWN`.
   - Fórmulas de pasos: $\ge 19.5 - 21.0\text{ pt}$.
   - Justificaciones: $\ge 18.5\text{ pt}$ en `\begin{minipage}{7.6cm}\raggedright`.
4. **Paleta Andina Institucional:** Usar constantes de `THEME` (`amgold`, `amteal`, `amred`, `amgreen`, `amorange`).
5. **Control de Versiones:** **NUNCA modificar `TRACKING.md`**. Enlaces en markdown siempre con formato `file://`.
