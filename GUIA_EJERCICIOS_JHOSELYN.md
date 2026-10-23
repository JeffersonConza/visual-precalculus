# 📘 Guía de Ejercicios y Preparación para Jhoselyn
### *Nivelación / Precálculo — Colección Yachay Tech*
> **Objetivo:** Dominar el análisis algebraico y visual para asegurar **calificación 10/10 en el Quiz 4** y un rendimiento sobresaliente en el examen final.

---

## 🧭 Índice Rápido
1. [Bloque 1: Protocolo de Graficación y Análisis para el Quiz 4 (Prioridad Máxima)](#bloque-1-protocolo-de-graficación-y-análisis-para-el-quiz-4)
2. [Bloque 2: Inyectividad, Sobreyectividad y Función Inversa (Guía 2.6)](#bloque-2-inyectividad-sobreyectividad-y-función-inversa)
3. [Bloque 3: Transformaciones de Funciones y Forma Canónica (Guía 2.5)](#bloque-3-transformaciones-de-funciones-y-forma-canónica)
4. [⚠️ Las 5 Trampas de Examen donde se Suelen Perder Puntos](#-las-5-trampas-de-examen-donde-se-suelen-perder-puntos)
5. [🎥 Videos Animados Recomendados del Repositorio](#-videos-animados-recomendados-del-repositorio)

---

## BLOQUE 1: Protocolo de Graficación y Análisis para el Quiz 4

Para obtener **10/10 en el Quiz 4**, los profesores exigen seguir estrictamente el algoritmo de **7 pasos formales**. No te saltes ninguno en la hoja de examen:

```text
1. Dominio ──► 2. Cortes con Ejes ──► 3. Paridad ──► 4. Tabla de Signos ──► 5. Asíntotas ──► 6. Extremos/Monotonía ──► 7. Gráfica
```

---

### 📌 Ejercicio Clave 1 (Función Racional de 3 Ramas — Pregunta Típica de Examen)
**Enunciado:** Realizar el análisis completo y bosquejar la gráfica de:
$$f(x) = \frac{x^2 - 1}{x^2 - 4}$$

#### Paso 1: Dominio de Definición
El denominador no puede ser cero:
$$x^2 - 4 = 0 \iff (x - 2)(x + 2) = 0 \iff x = 2 \quad \lor \quad x = -2$$
$$\mathbf{\operatorname{Dom}(f) = \mathbb{R} \setminus \{-2, 2\} = ]-\infty, -2[ \cup ]-2, 2[ \cup ]2, +\infty[}$$

#### Paso 2: Intersecciones con los Ejes Coordenados
* **Corte con el eje $y$ (evaluar $x = 0$):**
  $$f(0) = \frac{0^2 - 1}{0^2 - 4} = \frac{-1}{-4} = \frac{1}{4} \implies \mathbf{P_y = \left(0, \frac{1}{4}\right)}$$
* **Cortes con el eje $x$ (hacer $f(x) = 0$):**
  $$\frac{x^2 - 1}{x^2 - 4} = 0 \iff x^2 - 1 = 0 \iff (x - 1)(x + 1) = 0 \implies \mathbf{x = 1, \; x = -1}$$
  $$\mathbf{P_{x_1} = (1, 0), \quad P_{x_2} = (-1, 0)}$$

#### Paso 3: Análisis de Paridad y Simetría
Evaluamos $f(-x)$:
$$f(-x) = \frac{(-x)^2 - 1}{(-x)^2 - 4} = \frac{x^2 - 1}{x^2 - 4} = f(x)$$
* **Conclusión formal:** Puesto que $f(-x) = f(x)$, la función es **PAR**.
* **Propiedad geométrica:** Presenta **simetría axial respecto al eje $y$** (la mitad derecha se refleja exactamente en la izquierda).

#### Paso 4: Factorización y Tabla de Signos por Factores
Factorizamos completamente numerador y denominador:
$$f(x) = \frac{(x - 1)(x + 1)}{(x - 2)(x + 2)}$$
Puntos críticos en orden: $-2, -1, 1, 2$.

| Factor | $]-\infty, -2[$ | $]-2, -1[$ | $]-1, 1[$ | $]1, 2[$ | $]2, +\infty[$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $x + 2$ | $-$ | $+$ | $+$ | $+$ | $+$ |
| $x + 1$ | $-$ | $-$ | $+$ | $+$ | $+$ |
| $x - 1$ | $-$ | $-$ | $-$ | $+$ | $+$ |
| $x - 2$ | $-$ | $-$ | $-$ | $-$ | $+$ |
| **Signo de $f(x)$** | **$+$** | **$-$** | **$+$** | **$-$** | **$+$** |
| **Comportamiento** | Arriba eje $x$ | Abajo eje $x$ | Arriba eje $x$ | Abajo eje $x$ | Arriba eje $x$ |

#### Paso 5: Cálculo de Asíntotas
1. **Asíntotas Verticales:** Ocurren en los ceros del denominador que no se simplifican:
   $$\mathbf{x = -2} \qquad \text{y} \qquad \mathbf{x = 2}$$
2. **Asíntota Horizontal:** Comparamos los grados del numerador ($n=2$) y denominador ($m=2$):
   $$\lim_{x \to \pm\infty} \frac{x^2 - 1}{x^2 - 4} = \lim_{x \to \pm\infty} \frac{1 - 1/x^2}{1 - 4/x^2} = \frac{1}{1} = 1 \implies \mathbf{y = 1}$$
3. **Asíntota Oblicua:** No existe, pues $\operatorname{grad}(P) = \operatorname{grad}(Q)$ (solo existe cuando $\operatorname{grad}(P) = \operatorname{grad}(Q) + 1$).

#### Paso 6: Extremos y Rango
* Como $f$ es par y diferenciable en $]-2, 2[$, el punto de corte con el eje $y$, $\left(0, \frac{1}{4}\right)$, actúa como **máximo local** de la rama central.
* Las ramas laterales van desde $y = 1$ hasta $+\infty$.
* **Rango:** $\mathbf{\operatorname{Rg}(f) = ]-\infty, 1/4] \cup ]1, +\infty[}$.

---

### 📌 Ejercicio Clave 2 (Función con Asíntota Oblicua)
**Enunciado:** Analizar las asíntotas y el comportamiento de:
$$f(x) = \frac{x^3 - 4x}{x^2 - 1}$$

#### Truco de Examen (División de Polinomios):
Dividimos el numerador $x^3 - 4x$ entre el denominador $x^2 - 1$:
$$x^3 - 4x = x(x^2 - 1) - 3x \implies \mathbf{f(x) = x - \frac{3x}{x^2 - 1}}$$
* **Asíntotas Verticales:** $x^2 - 1 = 0 \implies \mathbf{x = 1}$ y $\mathbf{x = -1}$.
* **Asíntota Horizontal:** No tiene ($\operatorname{grad}(P) > \operatorname{grad}(Q)$).
* **Asíntota Oblicua:** El cociente de la división polinomial es $y = mx + b$:
  $$\lim_{x \to \pm\infty} [f(x) - x] = \lim_{x \to \pm\infty} \left(-\frac{3x}{x^2 - 1}\right) = 0 \implies \mathbf{y = x \text{ (Asíntota Oblicua)}}$$

---

## BLOQUE 2: Inyectividad, Sobreyectividad y Función Inversa

### 📌 La Plantilla para Demostrar Inyectividad (10/10 en el Quiz)
Para demostrar que una función es inyectiva, **siempre** se escribe esta estructura de tres pasos:
1. *"Sean $x_1, x_2 \in \operatorname{Dom}(f)$ tales que $f(x_1) = f(x_2)$."*
2. *Desarrollo algebraico hasta cancelar términos.*
3. *Concluir: "Por tanto, $x_1 = x_2$, lo que demuestra que $f$ es inyectiva."*

#### Ejemplo Resuelto (Función Racional):
Sea $f: \mathbb{R} \setminus \{3\} \to \mathbb{R}$, $f(x) = \frac{2x + 1}{x - 3}$. Demostrar inyectividad:
$$f(x_1) = f(x_2) \implies \frac{2x_1 + 1}{x_1 - 3} = \frac{2x_2 + 1}{x_2 - 3}$$
Multiplicando en cruz:
$$(2x_1 + 1)(x_2 - 3) = (2x_2 + 1)(x_1 - 3)$$
$$2x_1 x_2 - 6x_1 + x_2 - 3 = 2x_1 x_2 - 6x_2 + x_1 - 3$$
Cancelamos $2x_1 x_2$ y $-3$:
$$-6x_1 + x_2 = -6x_2 + x_1 \iff 7x_2 = 7x_1 \iff \mathbf{x_1 = x_2 \quad \blacksquare}$$

---

### 📌 Cómo Demostrar que NO es Inyectiva (Contraejemplo)
Si la función tiene exponente par (ej. $f(x) = x^2 + 1$ en $\mathbb{R}$), **no uses álgebra**, usa un contraejemplo numérico directo:
> *"Tomamos $x_1 = -1$ y $x_2 = 1$. Notamos que $x_1 \neq x_2$, pero $f(-1) = (-1)^2 + 1 = 2$ y $f(1) = 1^2 + 1 = 2$. Como $f(-1) = f(1)$, la recta horizontal $y = 2$ corta la gráfica en dos puntos distintos. Por ende, $f$ NO es inyectiva en $\mathbb{R}$."*

---

### 📌 Restricción de Dominio y Cálculo de Inversa $f^{-1}$
**Ejercicio Típico:** Sea $f: [2, +\infty[ \to [-4, +\infty[$, con $f(x) = (x - 2)^2 - 4$.
1. **Inyectividad:** Como $x \ge 2$, la parábola solo toma la rama creciente; es inyectiva.
2. **Sobreyectividad:** Para todo $y \ge -4$, resolvemos $y = (x - 2)^2 - 4$:
   $$(x - 2)^2 = y + 4 \implies |x - 2| = \sqrt{y + 4}$$
   Como la hipótesis indica $x \ge 2 \implies x - 2 \ge 0$, se elimina el valor absoluto con signo positivo:
   $$x - 2 = +\sqrt{y + 4} \implies x = 2 + \sqrt{y + 4}$$
   Existe solución real pues $y \ge -4 \implies y + 4 \ge 0$. Por tanto, $f$ es sobreyectiva.
3. **Fórmula de la Función Inversa:**
   $$\mathbf{f^{-1}: [-4, +\infty[ \to [2, +\infty[, \qquad f^{-1}(x) = 2 + \sqrt{x + 4}}$$
4. **Propiedad gráfica clave:** Las curvas de $f(x)$ y $f^{-1}(x)$ son **simétricas respecto a la recta $y = x$**.

---

## BLOQUE 3: Transformaciones de Funciones y Forma Canónica

### 📌 La Fórmula Maestra
$$g(x) = a \cdot f(b(x - h)) + k$$

| Parámetro | Operación | Efecto en la Gráfica | Cuidado con el Signo |
| :---: | :---: | :--- | :--- |
| **$h$** | Horizontal | Desplaza a la **derecha** si $(x - h)$; a la **izquierda** si $(x + h)$ | ⚠️ El signo en la fórmula es opuesto al movimiento |
| **$k$** | Vertical | Desplaza hacia **arriba** si $+k$; hacia **abajo** si $-k$ | Sigue el signo directo |
| **$a$** | Vertical | $|a| > 1$: dilatación vertical; $|a| < 1$: compresión. Si $a < 0$: **reflexión respecto al eje $x$** | Invierte la curva verticalmente |
| **$b$** | Horizontal | $|b| > 1$: compresión horizontal; $|b| < 1$: dilatación. Si $b < 0$: **reflexión respecto al eje $y$** | Invierte la curva horizontalmente |

#### Ejercicio de Reconstrucción (Del Vértice y Punto de Paso):
Una transformación de $f(x) = |x|$ tiene vértice en $(-3, 4)$ y pasa por $(-1, 1)$, abriendo hacia abajo.
1. Forma con vértice $(h, k) = (-3, 4)$:
   $$g(x) = a|x - (-3)| + 4 = a|x + 3| + 4$$
2. Usamos el punto de paso $(-1, 1)$ reemplazando $x = -1, y = 1$:
   $$1 = a|-1 + 3| + 4 \implies 1 = 2a + 4 \implies 2a = -3 \implies a = -\frac{3}{2}$$
3. Ecuación final:
   $$\mathbf{g(x) = -\frac{3}{2}|x + 3| + 4}$$

---

## ⚠️ Las 5 Trampas de Examen donde se Suelen Perder Puntos

1. **Olvidar que $\sqrt{A^2} = |A|$:**
   Al despejar $x$ en funciones cuadráticas para hallar la inversa, nunca escribas directamente $x - h = \sqrt{\dots}$. Primero escribe $|x - h| = \sqrt{\dots}$ y luego justifica por qué el signo es $+$ o $-$ usando el dominio dado.
2. **Confundir Codominio con Rango:**
   Una función dada como $f: \mathbb{R} \to \mathbb{R}$ con $f(x) = x^2$ **no es sobreyectiva** porque su codominio es $\mathbb{R}$, pero su rango es $[0, +\infty[$. Para ser sobreyectiva se debe redefinir el codominio a $[0, +\infty[$.
3. **No evaluar el signo en la tabla de factores:**
   En el Quiz 4, poner solo los signos finales sin detallar la fila de cada factor individual resta puntos de justificación.
4. **Asíntotas horizontales en funciones con raíz:**
   En funciones como $f(x) = \frac{\sqrt{x^2 - 1}}{x - 2}$, cuando $x \to +\infty$ la asíntota es $y = 1$, pero cuando $x \to -\infty$, $\sqrt{x^2} = |x| = -x$, por lo que la asíntota horizontal izquierda es $y = -1$.
5. **Afirmar inyectividad solo con la gráfica:**
   La prueba de la recta horizontal sirve para sustentar o contradecir gráficamente, pero si el enunciado dice *"Demuestre"*, el profesor exige la deducción algebraica $f(x_1) = f(x_2) \implies x_1 = x_2$.

---

## 🎥 Videos Animados Recomendados del Repositorio

Todos estos videos ya están renderizados y listos en tu carpeta [`videos_compilados/capitulo_05/`](file:///mnt/c/Users/jconza/Documents/PreCalculus/videos_compilados/capitulo_05) para compartirle:

| Archivo de Video | Tema que Refuerza | Para qué Guía sirve |
| :--- | :--- | :---: |
| [`Ejercicio05_60.mp4`](file:///mnt/c/Users/jconza/Documents/PreCalculus/videos_compilados/capitulo_05/Ejercicio05_60.mp4) | Análisis completo de 4 funciones reales (dominio, rango, sobreyectividad, monotonía y gráfica) | **Quiz 4** |
| [`Ejercicio05_58.mp4`](file:///mnt/c/Users/jconza/Documents/PreCalculus/videos_compilados/capitulo_05/Ejercicio05_58.mp4) | Función racional homográfica, asíntotas e hipérbola equilátera | **Quiz 4** |
| [`Ejercicio05_70.mp4`](file:///mnt/c/Users/jconza/Documents/PreCalculus/videos_compilados/capitulo_05/Ejercicio05_70.mp4) | Dominio estricto, tabla de signos por factores y asíntotas verticales | **Quiz 4** |
| [`Ejercicio05_10.mp4`](file:///mnt/c/Users/jconza/Documents/PreCalculus/videos_compilados/capitulo_05/Ejercicio05_10.mp4) | Demostración formal de inyectividad y prueba de la recta horizontal | **Guía 2.6** |
| [`Ejercicio05_16.mp4`](file:///mnt/c/Users/jconza/Documents/PreCalculus/videos_compilados/capitulo_05/Ejercicio05_16.mp4) | Monotonía estricta como garantía analítica de inyectividad | **Guía 2.6** |
| [`Ejercicio05_54.mp4`](file:///mnt/c/Users/jconza/Documents/PreCalculus/videos_compilados/capitulo_05/Ejercicio05_54.mp4) | Redefinición biyectiva y cálculo paso a paso de la función inversa | **Guía 2.6** |
| [`Ejercicio05_62.mp4`](file:///mnt/c/Users/jconza/Documents/PreCalculus/videos_compilados/capitulo_05/Ejercicio05_62.mp4) | Inversa de función acotada y demostración de simetría respecto a $y = x$ | **Guía 2.6** |
| [`Ejercicio05_64.mp4`](file:///mnt/c/Users/jconza/Documents/PreCalculus/videos_compilados/capitulo_05/Ejercicio05_64.mp4) | Biyectividad e inversa en intervalo cerrado acotado $[3, 5]$ | **Guía 2.6** |
| [`Ejercicio05_50.mp4`](file:///mnt/c/Users/jconza/Documents/PreCalculus/videos_compilados/capitulo_05/Ejercicio05_50.mp4) | Paridad, imparidad y condiciones de simetría | **Guía 2.5 / Quiz 4** |

---

### 📅 Plan Sugerido de 3 Días para Salvar el Quiz 4
* **Día 1:** Repasar el *Ejercicio Clave 1* de esta guía y ver los videos `Ejercicio05_10.mp4` y `Ejercicio05_54.mp4`. Resolver 2 ejercicios de inyectividad de la Guía 2.6.
* **Día 2:** Repasar las transformaciones de la Guía 2.5 (reconstrucción de $g(x) = a|x-h|+k$) y ver `Ejercicio05_62.mp4`.
* **Día 3:** Hacer simulacro del Quiz 4 con la función racional $f(x) = \frac{x^2 - 1}{x^2 - 4}$ ejecutando los 7 pasos sin ver la respuesta. Contrastar con el video `Ejercicio05_60.mp4`.
