"""
Ejercicio 7 - Tutorías y Preparación Quiz 4 (Jhoselyn)
Tema: Análisis Completo y Gráfica de Funciones:
      Función con Radical y Tres Ramas: f(x) = sqrt((x^2 - 1) / (x^2 - 4)).
      Dominio con raíz cuadrada, paridad par, simetría axial bilateral eje Y,
      cortes coordenados, tabla de signos horizontal por factores (Guía Pág. 18),
      asíntotas verticales x = ±2, asíntota horizontal y = 1,
      monotonía y rango sin derivadas (100% Precálculo, máximo central en (0, 1/2)),
      cuadro de variación horizontal (Vista.webp) y trazado cartesiano de 3 ramas.

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica en 8 pasos con ecuaciones en LaTeX de gran legibilidad.
"""

from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

# Configuración de Plantilla LaTeX con Paleta Andina Editorial Amarun
AMARUN_TEX_TEMPLATE = TexTemplate()
AMARUN_TEX_TEMPLATE.add_to_preamble(r"""
\usepackage{xcolor}
\definecolor{amgold}{HTML}{F6B840}
\definecolor{amteal}{HTML}{5CE1E6}
\definecolor{amred}{HTML}{E53E3E}
\definecolor{amgreen}{HTML}{48BB78}
\definecolor{amorange}{HTML}{DB5A38}
""")
config.tex_template = AMARUN_TEX_TEMPLATE


class EjercicioJh_07(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Jhoselyn",
            exercise="Ejercicio 7",
            topic="Función con Raíz y Tres Ramas",
            font_size=16.5
        )

        # 2. Enunciado institucional permanente con fórmula prominente (y = 2.65)
        self.setup_statement(
            desc_text="Analice y grafique la función con radical:",
            math_tex=r"{\color{amteal}f(x)} = \sqrt{\frac{{\color{amteal}x^2 - 1}}{{\color{amred}x^2 - 4}}} \quad \text{\footnotesize (Máximo central en $\left(0, \frac{1}{2}\right)$)}",
            desc_font_size=18.0,
            math_font_size=23.5,
            box_pos=np.array([0.0, 2.65, 0.0]),
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (8 pasos detallados)
        self.setup_progress_bar([
            "1/8: Dominio y Restricciones",
            "2/8: Paridad y Simetría Par",
            "3/8: Cortes Coordenados",
            "4/8: Tabla de Signos",
            "5/8: Asíntotas V. y H.",
            "6/8: Monotonía y Rango",
            "7/8: Cuadro de Variación",
            "8/8: Gráfica Cartesiana"
        ], dot_spacing=0.82, label_font_size=14.0)

        # ==========================================================
        # PASO 1: Dominio y Restricciones del Radicando
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Dominio y Restricciones del Radicando:} \\[5pt]"
            r"&\text{Al tener raíz cuadrada, el radicando debe ser no negativo:} \\[4pt]"
            r"&\frac{x^2 - 1}{x^2 - 4} \ge 0 \iff \frac{(x - 1)(x + 1)}{(x - 2)(x + 2)} \ge 0, \quad x \neq \pm 2 \\[6pt]"
            r"&\mathbf{\operatorname{Dom}(f) = {\color{amgold}(-\infty, -2) \cup [-1, 1] \cup (2, +\infty)}} \\[5pt]"
            r"&\implies \text{El dominio queda fragmentado en } \mathbf{3 \text{ ramas continuas}} \\[4pt]"
            r"&\implies \text{No existe gráfica en los intervalos } (-2, -1) \text{ ni } (1, 2)."
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{1. Dominio y Restricciones:}\\[6pt]"
            r"$\bullet$ La raíz cuadrada exige radicando $\ge 0$:\\[3pt]"
            r"\hspace*{1.2em}$\frac{x^2 - 1}{x^2 - 4} \ge 0 \quad \text{con denominador } x \neq \pm 2$.\\[5pt]"
            r"$\bullet$ Ceros del numerador incluidos en el dominio: $[-1, 1]$.\\[5pt]"
            r"$\bullet$ Polos del denominador estrictamente excluidos: $x \neq \pm 2$.\\[5pt]"
            r"$\bullet$ Dominio formado por 3 ramas disjuntas:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgold}\operatorname{Dom}(f) = (-\infty, -2) \cup [-1, 1] \cup (2, +\infty)}$.\\[5pt]"
            r"$\bullet$ En $(-2, -1) \cup (1, 2)$ el radicando es negativo ($\nexists f$)."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=3.2)

        # ==========================================================
        # PASO 2: Paridad y Simetría Par (Axial Bilateral)
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Paridad y Simetría Par:} \\[5pt]"
            r"&\text{Evaluamos formalmente el valor de } f(-x): \\[4pt]"
            r"&f(-x) = \sqrt{\frac{(-x)^2 - 1}{(-x)^2 - 4}} = \sqrt{\frac{x^2 - 1}{x^2 - 4}} = f(x) \\[6pt]"
            r"&\implies \mathbf{{\color{amteal}f(-x) = f(x)}} \implies \mathbf{f \text{ es una Función PAR}} \\[6pt]"
            r"&\implies \mathbf{\text{Presenta Simetría Axial bilateral respecto al eje }} Y \\[5pt]"
            r"&\implies \text{Si } (x, y) \in f \implies (-x, y) \in f \text{ (reflejo especular bilateral)}."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{2. Paridad y Simetría:}\\[6pt]"
            r"$\bullet$ Al sustituir $-x$, todos los términos son cuadráticos:\\[3pt]"
            r"\hspace*{1.2em}$(-x)^2 = x^2 \implies f(-x) = f(x)$.\\[5pt]"
            r"$\bullet$ Concluimos formalmente: ${\color{amteal}f \text{ es una función PAR}}$.\\[5pt]"
            r"$\bullet$ Presenta simetría axial bilateral respecto al eje vertical $Y$.\\[5pt]"
            r"$\bullet$ La rama en $x > 2$ es el reflejo exacto de la rama en $x < -2$.\\[5pt]"
            r"$\bullet$ La rama central $[-1, 1]$ es simétrica respecto a $x = 0$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq2, just2, box_color=THEME["highlight"], advance_to_step=1, wait_time=3.2)

        # ==========================================================
        # PASO 3: Intersecciones con los Ejes Coordenados
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Intersecciones con los Ejes Coordenados:} \\[5pt]"
            r"&\bullet \textbf{Intercepto con el eje } Y \; (x = 0): \\[3pt]"
            r"&\quad f(0) = \sqrt{\frac{0^2 - 1}{0^2 - 4}} = \sqrt{\frac{-1}{-4}} = \sqrt{\frac{1}{4}} = \frac{1}{2} \implies \mathbf{{\color{amteal}P_y\left(0, \tfrac{1}{2}\right)}} \\[6pt]"
            r"&\bullet \textbf{Interceptos con el eje } X \; (f(x) = 0): \\[3pt]"
            r"&\quad \sqrt{\frac{x^2 - 1}{x^2 - 4}} = 0 \iff x^2 - 1 = 0 \implies x = \pm 1 \\[5pt]"
            r"&\quad \text{Puntos: } {\color{amorange}P_{x_1}(-1, 0)} \quad \text{y} \quad {\color{amorange}P_{x_2}(1, 0)} \\[5pt]"
            r"&\implies P_y\left(0, \tfrac{1}{2}\right) \text{ es el vértice superior máximo de la rama central.}"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{3. Cortes Coordenados:}\\[6pt]"
            r"$\bullet$ Corte con el eje vertical $Y$ ($x = 0$):\\[3pt]"
            r"\hspace*{1.2em}$f(0) = \sqrt{1/4} = 1/2 \implies {\color{amteal}P_y(0, 1/2)}$.\\[5pt]"
            r"$\bullet$ Cortes con el eje horizontal $X$ ($f(x) = 0$):\\[3pt]"
            r"\hspace*{1.2em}La raíz se anula cuando el numerador es cero: $x^2 - 1 = 0$.\\[5pt]"
            r"$\bullet$ Dos raíces simétricas en el plano:\\[3pt]"
            r"\hspace*{1.2em}${\color{amorange}x = -1} \quad \text{y} \quad {\color{amorange}x = 1}$.\\[5pt]"
            r"$\bullet$ Puntos: ${\color{amorange}P_{x_1}(-1, 0)}$ y ${\color{amorange}P_{x_2}(1, 0)}$ (extremos cerrados de rama central)."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=3.2)

        # ==========================================================
        # PASO 4: Factorización Canónica y Tabla Horizontal de Signos
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Tabla Horizontal de Signos por Factores:} \\[4pt]"
            r"&R(x) = \frac{(x + 1)(x - 1)}{(x + 2)(x - 2)} \ge 0, \quad f(x) = \sqrt{R(x)} \\[4pt]"
            r"&\begin{array}{c|c|c|c|c|c}"
            r"\text{Factor} & (-\infty, -2) & (-2, -1) & (-1, 1) & (1, 2) & (2, +\infty) \\ \hline "
            r"x + 2 & - & + & + & + & + \\ \hline "
            r"x + 1 & - & - & + & + & + \\ \hline "
            r"x - 1 & - & - & - & + & + \\ \hline "
            r"x - 2 & - & - & - & - & + \\ \hline "
            r"R(x) & {\color{amgreen}+} & {\color{amred}-} & {\color{amgreen}+} & {\color{amred}-} & {\color{amgreen}+} \\ \hline "
            r"f(x) & {\color{amgreen}> 0} & {\color{amred}\nexists} & {\color{amgreen}\ge 0} & {\color{amred}\nexists} & {\color{amgreen}> 0}"
            r"\end{array} \\[6pt]"
            r"&\bullet \text{Positiva en: } {\color{amgreen}(-\infty, -2) \cup (-1, 1) \cup (2, +\infty)} \quad (f(x) > 0). \\[3pt]"
            r"&\bullet \text{Se anula en: } x = \pm 1 \quad \bullet \text{No existe en: } {\color{amred}(-2, -1) \cup (1, 2)}."
            r"\end{aligned}",
            font_size=18.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{4. Tabla de Signos (Guía Pág. 18):}\\[6pt]"
            r"$\bullet$ Tabla horizontal idéntica a la guía oficial de estudio.\\[5pt]"
            r"$\bullet$ 5 intervalos delimitados por raíces ($\pm 1$) y polos ($\pm 2$).\\[5pt]"
            r"$\bullet$ Signo de $R(x)$ determina la existencia real de la raíz:\\[3pt]"
            r"\hspace*{1.2em}Donde $R(x) < 0$, la raíz cuadrada no es real ($\nexists f$).\\[5pt]"
            r"$\bullet$ La función es estrictamente no negativa ($f(x) \ge 0$ en todo su dominio).\\[5pt]"
            r"$\bullet$ Toda la gráfica se ubica sobre el semiplano superior $y \ge 0$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=3.2)

        # ==========================================================
        # PASO 5: Asíntotas Verticales y Asíntota Horizontal
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Asíntotas Verticales y Horizontal:} \\[4pt]"
            r"&\bullet \textbf{Asíntotas Verticales (A.V.): } \mathbf{{\color{amred}x = -2}} \quad \text{y} \quad \mathbf{{\color{amred}x = 2}} \\[3pt]"
            r"&\quad \lim_{x \to -2^-} f(x) = \sqrt{\tfrac{3}{0^+}} = +\infty, \quad \lim_{x \to 2^+} f(x) = \sqrt{\tfrac{3}{0^+}} = +\infty \\[3pt]"
            r"&\quad (\text{En } x \to -2^+ \text{ y } x \to 2^-, \; f(x) \nexists \text{ por radicando negativo}) \\[5pt]"
            r"&\bullet \textbf{Asíntota Horizontal (A.H.): } \text{Grado}(N) = \text{Grado}(D) = 2 \\[3pt]"
            r"&\quad \lim_{x \to \pm\infty} \sqrt{\frac{x^2 - 1}{x^2 - 4}} = \sqrt{1} = 1 \implies \mathbf{{\color{amgold}y = 1}} \\[5pt]"
            r"&\bullet \textbf{Cruce con A.H.: } \frac{x^2 - 1}{x^2 - 4} = 1 \implies -1 = -4 \text{ (Falso, no corta)}."
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{5. Asíntotas del Sistema:}\\[6pt]"
            r"$\bullet$ Asíntotas Verticales en los polos del radicando:\\[3pt]"
            r"\hspace*{1.2em}${\color{amred}x = -2} \quad \text{y} \quad {\color{amred}x = 2}$.\\[5pt]"
            r"$\bullet$ Las ramas exteriores divergen hacia $+\infty$ cerca de los polos.\\[5pt]"
            r"$\bullet$ Comportamiento en el infinito:\\[3pt]"
            r"\hspace*{1.2em}Cociente de coeficientes tiende a $1 \implies {\color{amgold}y = 1}$.\\[5pt]"
            r"$\bullet$ Como $x^2 - 1 > x^2 - 4$, las ramas exteriores van siempre por encima de la asíntota ($f(x) > 1$)."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=3.2)

        # ==========================================================
        # PASO 6: Monotonía, Extremo Local y Rango (100% Precálculo)
        # ==========================================================
        eq6 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Monotonía, Extremo Local y Rango:} \\[4pt]"
            r"&\text{Datos oficiales proporcionados en el enunciado de examen:} \\[4pt]"
            r"&\bullet \textbf{Máximo de Rama Central: } \text{Vértice en } \mathbf{{\color{amteal}M\left(0, \tfrac{1}{2}\right)}}. \\[4pt]"
            r"&\bullet \textbf{Comportamiento de Monotonía por Ramas:} \\[3pt]"
            r"&\quad \bullet \text{Creciente en } {\color{amgreen}(-\infty, -2)} \quad (\text{desde } 1^+ \text{ hacia } +\infty) \\[2pt]"
            r"&\quad \bullet \text{Creciente en } {\color{amgreen}[-1, 0]} \quad (\text{desde } 0 \text{ hasta } \tfrac{1}{2}) \\[2pt]"
            r"&\quad \bullet \text{Decreciente en } {\color{amred}[0, 1]} \quad (\text{desde } \tfrac{1}{2} \text{ hasta } 0) \\[2pt]"
            r"&\quad \bullet \text{Decreciente en } {\color{amred}(2, +\infty)} \quad (\text{desde } +\infty \text{ hacia } 1^+) \\[4pt]"
            r"&\implies \text{Rama central toma } \left[0, \tfrac{1}{2}\right]; \text{ ramas exteriores toman } (1, +\infty): \\[4pt]"
            r"&\implies \mathbf{\operatorname{Ran}(f) = {\color{amgold}\left[0, \tfrac{1}{2}\right] \cup (1, +\infty)}}."
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{6. Monotonía y Rango:}\\[6pt]"
            r"$\bullet$ Propiedad dada en el enunciado (Precálculo):\\[3pt]"
            r"\hspace*{1.2em}La rama central alcanza su máximo en ${\color{amteal}M(0, 1/2)}$.\\[5pt]"
            r"$\bullet$ Por simetría par bilateral respecto al eje $Y$:\\[3pt]"
            r"\hspace*{1.2em}Sube hasta $x=0$ y luego baja hacia $x=1$.\\[5pt]"
            r"$\bullet$ La rama central cubre el segmento $[0, 1/2]$.\\[5pt]"
            r"$\bullet$ Las ramas exteriores cubren $(1, +\infty)$. Franja vacía en $(1/2, 1]$:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgold}\operatorname{Ran}(f) = [0, 1/2] \cup (1, +\infty)}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq6, just6, box_color=THEME["highlight"], advance_to_step=5, wait_time=3.2)

        # ==========================================================
        # PASO 7: Cuadro Horizontal de Variación y Puntos Notables (Vista.webp)
        # ==========================================================
        eq7 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{7. Cuadro de Variación y Puntos Notables:} \\[6pt]"
            r"&\begin{array}{c|c|c|c|c}"
            r"x & (-\infty, -2) & [-1, 0] & [0, 1] & (2, +\infty) \\ \hline "
            r"\text{Tendencia} & {\color{amgreen}\text{Sube }(+)} & {\color{amgreen}\text{Sube }(+)} & {\color{amred}\text{Baja }(-)} & {\color{amred}\text{Baja }(-)} \\ \hline "
            r"f(x) & \nearrow & \nearrow & \searrow & \searrow"
            r"\end{array} \\[8pt]"
            r"&\bullet \mathbf{\text{Máximo Central: }} \text{En } x = 0 \text{ pasa de sube a baja } \implies {\color{amteal}M\left(0, \tfrac{1}{2}\right)}. \\[3pt]"
            r"&\bullet \mathbf{\text{Polos (A.V.): }} x = -2 \text{ y } x = 2 \text{ con divergencia a } +\infty. \\[3pt]"
            r"&\bullet \mathbf{\text{Asíntota Horizontal: }} y = 1 \text{ como cota inferior de ramas exteriores}. \\[3pt]"
            r"&\bullet \mathbf{\text{Cortes } X: } P_{x_1}(-1, 0) \text{ y } P_{x_2}(1, 0) \text{ como extremos de rama central}."
            r"\end{aligned}",
            font_size=18.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{7. Síntesis Horizontal:}\\[6pt]"
            r"$\bullet$ Cuadro horizontal consolidado según el modelo de referencia.\\[5pt]"
            r"$\bullet$ El cambio de $\nearrow$ a $\searrow$ en $x = 0$ confirma el máximo ${\color{amteal}M(0, 1/2)}$.\\[5pt]"
            r"$\bullet$ Describe el comportamiento asintótico hacia $x = \pm 2$ y $y = 1$.\\[5pt]"
            r"$\bullet$ Zonas vacías $(-2, -1)$ y $(1, 2)$ respetadas sin trazo de curva."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq7, just7, box_color=THEME["highlight"], advance_to_step=6, wait_time=3.6)

        # ==========================================================
        # PASO 8: Gráfica Cartesiana y Verificación Visual
        # ==========================================================
        left_summary = MathTex(
            r"\begin{aligned}"
            r"&\textbf{8. Resumen Formal de Resultados:} \\[4pt]"
            r"&\bullet \mathbf{\operatorname{Dom}(f) = {\color{amgold}(-\infty, -2) \cup [-1, 1] \cup (2, +\infty)}} \\[4pt]"
            r"&\bullet \mathbf{\operatorname{Ran}(f) = {\color{amgold}\left[0, \tfrac{1}{2}\right] \cup (1, +\infty)}} \\[4pt]"
            r"&\bullet \mathbf{\text{Paridad: }} {\color{amteal}\text{Par }} (f(-x) = f(x)) \implies \text{Sim. Axial eje } Y \\[4pt]"
            r"&\bullet \mathbf{\text{Asíntotas V.: }} {\color{amred}x = -2}, \quad {\color{amred}x = 2} \\[4pt]"
            r"&\bullet \mathbf{\text{Asíntota Horizontal: }} {\color{amgold}y = 1} \quad (\text{no la corta}) \\[4pt]"
            r"&\bullet \mathbf{\text{Máximo Local: }} {\color{amteal}M\left(0, \tfrac{1}{2}\right)} \text{ (vértice central)} \\[4pt]"
            r"&\bullet \mathbf{\text{Cortes con Ejes: }} {\color{amorange}(-1, 0)}, \; {\color{amorange}(1, 0)}, \; {\color{amteal}\left(0, \tfrac{1}{2}\right)} \\[4pt]"
            r"&\bullet \mathbf{\text{Monotonía: }} \text{Crece en } (-\infty, -2) \cup [-1, 0], \\[2pt]"
            r"&\quad \text{Decrece en } [0, 1] \cup (2, +\infty) \quad {\color{amgreen}\blacksquare}"
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        box8 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.18, corner_radius=0.1)

        # Gráfico cartesiano de la función con radical y 3 ramas
        axes = Axes(
            x_range=[-5.2, 5.2, 2],
            y_range=[-0.8, 4.6, 1],
            x_length=5.1,
            y_length=3.6,
            tips=True,
            axis_config={
                "color": THEME["axes"],
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 15,
                "tip_width": 0.12,
                "tip_height": 0.12,
            }
        ).move_to([3.25, -0.65, 0])
        axes_labels = axes.get_axis_labels(
            x_label=MathTex("x", font_size=18, color=THEME["statement_text"]),
            y_label=MathTex("y", font_size=18, color=THEME["statement_text"])
        )

        graph_title = Tex(
            r"Gráfica de ${\color{amteal}f(x)} = \sqrt{\frac{{\color{amteal}x^2 - 1}}{{\color{amred}x^2 - 4}}}$",
            font_size=21.0,
            color=WHITE
        ).move_to([3.25, 1.70, 0])

        # Asíntotas verticales discontinuas (x = -2 y x = 2)
        asymp_v1 = DashedLine(
            axes.c2p(-2.0, -0.6), axes.c2p(-2.0, 4.4),
            dash_length=0.08, color=THEME["poncho_red"], stroke_width=2.0
        )
        lbl_av1 = MathTex(r"x = -2", font_size=13.5, color=THEME["poncho_red"]).next_to(axes.c2p(-2.0, 4.1), LEFT, buff=0.08)

        asymp_v2 = DashedLine(
            axes.c2p(2.0, -0.6), axes.c2p(2.0, 4.4),
            dash_length=0.08, color=THEME["poncho_red"], stroke_width=2.0
        )
        lbl_av2 = MathTex(r"x = 2", font_size=13.5, color=THEME["poncho_red"]).next_to(axes.c2p(2.0, 4.1), RIGHT, buff=0.08)

        # Asíntota horizontal discontinua (y = 1)
        asymp_h = DashedLine(
            axes.c2p(-5.0, 1.0), axes.c2p(5.0, 1.0),
            dash_length=0.08, color=THEME["highlight"], stroke_width=1.8
        )
        lbl_ah = MathTex(r"y = 1", font_size=13.5, color=THEME["highlight"]).next_to(axes.c2p(4.0, 1.0), DOWN, buff=0.08)

        # 3 Ramas continuas
        branch_left = axes.plot(
            lambda x: np.sqrt((x**2 - 1) / (x**2 - 4)),
            x_range=[-5.0, -2.06],
            color=THEME["curve"],
            stroke_width=2.5
        )
        branch_center = axes.plot(
            lambda x: np.sqrt((x**2 - 1) / (x**2 - 4)),
            x_range=[-1.0, 1.0],
            color=THEME["curve"],
            stroke_width=2.5
        )
        branch_right = axes.plot(
            lambda x: np.sqrt((x**2 - 1) / (x**2 - 4)),
            x_range=[2.06, 5.0],
            color=THEME["curve"],
            stroke_width=2.5
        )
        curve_branches = VGroup(branch_left, branch_center, branch_right)
        curve_lbl = MathTex(r"y = f(x)", font_size=14.0, color=THEME["curve"]).move_to(axes.c2p(-3.6, 2.2))

        # Puntos notables: M(0, 1/2), P_x1(-1, 0), P_x2(1, 0)
        dot_m = Dot(axes.c2p(0.0, 0.5), radius=0.07, color=THEME["highlight"])
        lbl_m = MathTex(r"M\left(0, \tfrac{1}{2}\right)", font_size=12.5, color=THEME["highlight"]).next_to(dot_m, UP, buff=0.08)

        dot_x1 = Dot(axes.c2p(-1.0, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_x1 = MathTex(r"(-1, 0)", font_size=12.5, color=THEME["statement_text"]).next_to(dot_x1, DOWN, buff=0.08)

        dot_x2 = Dot(axes.c2p(1.0, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_x2 = MathTex(r"(1, 0)", font_size=12.5, color=THEME["statement_text"]).next_to(dot_x2, DOWN, buff=0.08)

        prog_anims = self.get_advance_progress_anims(7)

        self.play(
            FadeOut(self.active_math),
            FadeOut(self.active_just),
            FadeOut(self.active_box),
            FadeIn(left_summary),
            Create(box8),
            Create(axes),
            Write(axes_labels),
            Write(graph_title),
            *prog_anims,
            run_time=1.8
        )
        self.active_box = box8
        self.active_math = left_summary
        self.active_just = None

        self.play(
            Create(asymp_v1),
            Write(lbl_av1),
            Create(asymp_v2),
            Write(lbl_av2),
            Create(asymp_h),
            Write(lbl_ah),
            Create(curve_branches),
            Write(curve_lbl),
            FadeIn(dot_m),
            Write(lbl_m),
            FadeIn(dot_x1),
            Write(lbl_x1),
            FadeIn(dot_x2),
            Write(lbl_x2),
            run_time=2.4
        )
        self.wait(8.0)

        # Cierre institucional
        graph_group = VGroup(
            axes, axes_labels, graph_title,
            asymp_v1, lbl_av1, asymp_v2, lbl_av2,
            asymp_h, lbl_ah,
            curve_branches, curve_lbl,
            dot_m, lbl_m,
            dot_x1, lbl_x1,
            dot_x2, lbl_x2
        )
        self.play(
            FadeOut(graph_group),
            FadeOut(self.active_math),
            FadeOut(self.active_box),
            run_time=1.4
        )
        self.wait(1.0)
