"""
Ejercicio 6 - Tutorías y Preparación Quiz 4 (Jhoselyn)
Tema: Análisis Completo y Gráfica de Funciones:
      Función Racional Par con Extremos Locales: f(x) = (x^2 - 9) / (x^2 - 1).
      Dominio, paridad par, simetría axial bilateral eje Y, cortes coordenados,
      tabla de signos horizontal por factores (Guía Pág. 16),
      asíntotas verticales x = ±1, asíntota horizontal y = 1,
      monotonía y rango sin derivadas (100% Precálculo, mínimo central en (0, 9)),
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


class EjercicioJh_06(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Jhoselyn",
            exercise="Ejercicio 6",
            topic="Función Racional y Extremos Locales",
            font_size=16.5
        )

        # 2. Enunciado institucional permanente con fórmula prominente (y = 2.65)
        self.setup_statement(
            desc_text="Analice y grafique la función racional par:",
            math_tex=r"{\color{amteal}f(x)} = \frac{{\color{amteal}x^2 - 9}}{{\color{amred}x^2 - 1}} \quad \text{\footnotesize (Mínimo central en $(0, 9)$)}",
            desc_font_size=18.0,
            math_font_size=25.0,
            box_pos=np.array([0.0, 2.65, 0.0]),
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (8 pasos detallados)
        self.setup_progress_bar([
            "1/8: Dominio y Ramas",
            "2/8: Paridad y Simetría Par",
            "3/8: Cortes Coordenados",
            "4/8: Tabla de Signos",
            "5/8: Asíntotas V. y H.",
            "6/8: Monotonía y Rango",
            "7/8: Cuadro de Variación",
            "8/8: Gráfica Cartesiana"
        ], dot_spacing=0.82, label_font_size=14.0)

        # ==========================================================
        # PASO 1: Dominio y Restricciones del Denominador
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Dominio y Restricciones:} \\[5pt]"
            r"&\text{Al ser una función racional, el denominador no se anula:} \\[4pt]"
            r"&x^2 - 1 \neq 0 \iff (x - 1)(x + 1) \neq 0 \implies x \neq \pm 1 \\[6pt]"
            r"&\mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R} \setminus \{-1, 1\}}} \\[5pt]"
            r"&\mathbf{\operatorname{Dom}(f) = {\color{amgreen}(-\infty, -1) \cup (-1, 1) \cup (1, +\infty)}} \\[6pt]"
            r"&\implies \text{El plano queda dividido en } \mathbf{3 \text{ ramas continuas}} \text{ disjuntas.}"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{1. Dominio y Restricciones:}\\[6pt]"
            r"$\bullet$ Toda fracción exige denominador no nulo:\\[3pt]"
            r"\hspace*{1.2em}$x^2 - 1 \neq 0 \implies x \neq -1 \quad \text{y} \quad x \neq 1$.\\[5pt]"
            r"$\bullet$ El dominio excluye ambos polos de discontinuidad:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgold}\operatorname{Dom}(f) = \mathbb{R} \setminus \{-1, 1\}}$.\\[5pt]"
            r"$\bullet$ La función se fragmenta en 3 ramas disjuntas:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgreen}(-\infty, -1)}, \quad {\color{amgreen}(-1, 1)} \quad \text{y} \quad {\color{amgreen}(1, +\infty)}$.\\[5pt]"
            r"$\bullet$ Base de delimitación para las asíntotas verticales."
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
            r"&f(-x) = \frac{(-x)^2 - 9}{(-x)^2 - 1} = \frac{x^2 - 9}{x^2 - 1} = f(x) \\[6pt]"
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
            r"$\bullet$ Al sustituir $-x$, todas las potencias son pares:\\[3pt]"
            r"\hspace*{1.2em}$(-x)^2 = x^2 \implies f(-x) = f(x)$.\\[5pt]"
            r"$\bullet$ Concluimos formalmente: ${\color{amteal}f \text{ es una función PAR}}$.\\[5pt]"
            r"$\bullet$ Presenta simetría axial bilateral respecto al eje $Y$.\\[5pt]"
            r"$\bullet$ La rama en $x < -1$ es el reflejo especular exacto de la rama en $x > 1$.\\[5pt]"
            r"$\bullet$ La rama central es simétrica respecto al eje $Y$."
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
            r"&\quad f(0) = \frac{0^2 - 9}{0^2 - 1} = \frac{-9}{-1} = 9 \implies \mathbf{{\color{amteal}P_y(0, 9)}} \\[6pt]"
            r"&\bullet \textbf{Interceptos con el eje } X \; (f(x) = 0): \\[3pt]"
            r"&\quad x^2 - 9 = 0 \iff (x - 3)(x + 3) = 0 \implies x = \pm 3 \\[5pt]"
            r"&\quad \text{Puntos: } {\color{amorange}P_{x_1}(-3, 0)} \quad \text{y} \quad {\color{amorange}P_{x_2}(3, 0)} \\[5pt]"
            r"&\implies P_y(0, 9) \text{ coincide con el vértice mínimo de la rama central.}"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{3. Cortes Coordenados:}\\[6pt]"
            r"$\bullet$ Corte con el eje vertical $Y$ ($x = 0$):\\[3pt]"
            r"\hspace*{1.2em}$f(0) = \frac{-9}{-1} = 9 \implies {\color{amteal}P_y(0, 9)}$.\\[5pt]"
            r"$\bullet$ Cortes con el eje horizontal $X$ ($f(x) = 0$):\\[3pt]"
            r"\hspace*{1.2em}Se anula cuando el numerador es cero: $x^2 - 9 = 0$.\\[5pt]"
            r"$\bullet$ Dos raíces simétricas en el plano:\\[3pt]"
            r"\hspace*{1.2em}${\color{amorange}x = -3} \quad \text{y} \quad {\color{amorange}x = 3}$.\\[5pt]"
            r"$\bullet$ Puntos: ${\color{amorange}P_{x_1}(-3, 0)}$ y ${\color{amorange}P_{x_2}(3, 0)}$."
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
            r"&{\color{amteal}f(x)} = \frac{(x + 3)(x - 3)}{(x + 1)(x - 1)} \\[4pt]"
            r"&\begin{array}{c|c|c|c|c|c}"
            r"\text{Factor} & (-\infty, -3) & (-3, -1) & (-1, 1) & (1, 3) & (3, +\infty) \\ \hline "
            r"x + 3 & - & + & + & + & + \\ \hline "
            r"x + 1 & - & - & + & + & + \\ \hline "
            r"x - 1 & - & - & - & + & + \\ \hline "
            r"x - 3 & - & - & - & - & + \\ \hline "
            r"f(x) & {\color{amgreen}+} & {\color{amred}-} & {\color{amgreen}+} & {\color{amred}-} & {\color{amgreen}+}"
            r"\end{array} \\[6pt]"
            r"&\bullet \text{Positiva en: } {\color{amgreen}(-\infty, -3) \cup (-1, 1) \cup (3, +\infty)} \quad (f(x) > 0). \\[3pt]"
            r"&\bullet \text{Negativa en: } {\color{amred}(-3, -1) \cup (1, 3)} \quad (f(x) < 0)."
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{4. Tabla de Signos (Guía Pág. 16):}\\[6pt]"
            r"$\bullet$ Tabla horizontal idéntica a la guía oficial de estudio.\\[5pt]"
            r"$\bullet$ 5 intervalos delimitados por 2 ceros ($\pm 3$) y 2 polos ($\pm 1$).\\[5pt]"
            r"$\bullet$ Regla de los signos por producto y cociente en cada columna.\\[5pt]"
            r"$\bullet$ Alternancia $(+, -, +, -, +)$ define las zonas arriba y abajo del eje $X$.\\[5pt]"
            r"$\bullet$ La rama central $(-1, 1)$ es estrictamente positiva ($f > 0$)."
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
            r"&\bullet \textbf{Asíntotas Verticales (A.V.): } \mathbf{{\color{amred}x = -1}} \quad \text{y} \quad \mathbf{{\color{amred}x = 1}} \\[3pt]"
            r"&\quad \lim_{x \to 1^-} f(x) = +\infty, \quad \lim_{x \to 1^+} f(x) = -\infty \\[3pt]"
            r"&\quad \lim_{x \to -1^+} f(x) = +\infty, \quad \lim_{x \to -1^-} f(x) = -\infty \\[5pt]"
            r"&\bullet \textbf{Asíntota Horizontal (A.H.): } \text{Grado}(N) = \text{Grado}(D) = 2 \\[3pt]"
            r"&\quad \lim_{x \to \pm\infty} \frac{x^2 - 9}{x^2 - 1} = \frac{1}{1} \implies \mathbf{{\color{amgold}y = 1}} \\[5pt]"
            r"&\bullet \textbf{Cruce con A.H.: } \frac{x^2 - 9}{x^2 - 1} = 1 \implies -9 = -1 \text{ (Falso, no corta)}."
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{5. Asíntotas del Sistema:}\\[6pt]"
            r"$\bullet$ Asíntotas Verticales en los polos irreducibles:\\[3pt]"
            r"\hspace*{1.2em}${\color{amred}x = -1} \quad \text{y} \quad {\color{amred}x = 1}$.\\[5pt]"
            r"$\bullet$ La rama central diverge a $+\infty$ por ambos lados.\\[5pt]"
            r"$\bullet$ Grados iguales en numerador y denominador:\\[3pt]"
            r"\hspace*{1.2em}Cociente de coeficientes principales: ${\color{amgold}y = 1}$.\\[5pt]"
            r"$\bullet$ La curva jamás cruza su asíntota horizontal $y = 1$."
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
            r"&\bullet \textbf{Mínimo de Rama Central: } \text{Vértice en } \mathbf{{\color{amteal}M(0, 9)}}. \\[4pt]"
            r"&\bullet \textbf{Comportamiento de Monotonía por Ramas:} \\[3pt]"
            r"&\quad \bullet \text{Decreciente en } {\color{amred}(-\infty, -1)} \quad (\text{desde } 1^- \text{ hacia } -\infty) \\[2pt]"
            r"&\quad \bullet \text{Decreciente en } {\color{amred}(-1, 0)} \quad (\text{desde } +\infty \text{ hasta } 9) \\[2pt]"
            r"&\quad \bullet \text{Creciente en } {\color{amgreen}(0, 1)} \quad (\text{desde } 9 \text{ hacia } +\infty) \\[2pt]"
            r"&\quad \bullet \text{Creciente en } {\color{amgreen}(1, +\infty)} \quad (\text{desde } -\infty \text{ hacia } 1^-) \\[4pt]"
            r"&\implies \text{Ramas exteriores toman } (-\infty, 1); \text{ rama central toma } [9, +\infty): \\[4pt]"
            r"&\implies \mathbf{\operatorname{Ran}(f) = {\color{amgold}(-\infty, 1) \cup [9, +\infty)}}."
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{6. Monotonía y Rango:}\\[6pt]"
            r"$\bullet$ Propiedad dada en el enunciado (Precálculo):\\[3pt]"
            r"\hspace*{1.2em}La rama central tiene su vértice mínimo en ${\color{amteal}M(0, 9)}$.\\[5pt]"
            r"$\bullet$ Por simetría par bilateral respecto al eje $Y$:\\[3pt]"
            r"\hspace*{1.2em}Decrece a la izquierda de $x=0$, crece a la derecha.\\[5pt]"
            r"$\bullet$ Las ramas exteriores cubren el intervalo $(-\infty, 1)$.\\[5pt]"
            r"$\bullet$ La rama central cubre $[9, +\infty)$. Franja vacía en $[1, 9)$:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgold}\operatorname{Ran}(f) = (-\infty, 1) \cup [9, +\infty)}$.\end{minipage}",
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
            r"x & (-\infty, -1) & (-1, 0) & (0, 1) & (1, +\infty) \\ \hline "
            r"\text{Tendencia} & {\color{amred}\text{Baja }(-)} & {\color{amred}\text{Baja }(-)} & {\color{amgreen}\text{Sube }(+)} & {\color{amgreen}\text{Sube }(+)} \\ \hline "
            r"f(x) & \searrow & \searrow & \nearrow & \nearrow"
            r"\end{array} \\[8pt]"
            r"&\bullet \mathbf{\text{Mínimo Central: }} \text{En } x = 0 \text{ pasa de baja a sube } \implies {\color{amteal}M(0, 9)}. \\[3pt]"
            r"&\bullet \mathbf{\text{Polos (A.V.): }} x = -1 \text{ y } x = 1 \text{ con asíntotas verticales}. \\[3pt]"
            r"&\bullet \mathbf{\text{Asíntota Horizontal: }} y = 1 \text{ como cota asintótica exterior}. \\[3pt]"
            r"&\bullet \mathbf{\text{Cortes } X: } P_{x_1}(-3, 0) \text{ y } P_{x_2}(3, 0) \text{ en las ramas laterales}."
            r"\end{aligned}",
            font_size=19.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{7. Síntesis Horizontal:}\\[6pt]"
            r"$\bullet$ Cuadro horizontal consolidado según el modelo de referencia.\\[5pt]"
            r"$\bullet$ El cambio de $\searrow$ a $\nearrow$ en $x = 0$ confirma el mínimo ${\color{amteal}M(0, 9)}$.\\[5pt]"
            r"$\bullet$ Describe el comportamiento asintótico hacia $x = \pm 1$ y $y = 1$.\\[5pt]"
            r"$\bullet$ Proporciona la guía exacta para el trazado de las 3 ramas en el plano cartesiano."
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
            r"&\bullet \mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R} \setminus \{-1, 1\}}} \\[4pt]"
            r"&\bullet \mathbf{\operatorname{Ran}(f) = {\color{amgold}(-\infty, 1) \cup [9, +\infty)}} \\[4pt]"
            r"&\bullet \mathbf{\text{Paridad: }} {\color{amteal}\text{Par }} (f(-x) = f(x)) \implies \text{Sim. Axial eje } Y \\[4pt]"
            r"&\bullet \mathbf{\text{Asíntotas V.: }} {\color{amred}x = -1}, \quad {\color{amred}x = 1} \\[4pt]"
            r"&\bullet \mathbf{\text{Asíntota Horizontal: }} {\color{amgold}y = 1} \quad (\text{no la corta}) \\[4pt]"
            r"&\bullet \mathbf{\text{Mínimo Local: }} {\color{amteal}M(0, 9)} \text{ (vértice central)} \\[4pt]"
            r"&\bullet \mathbf{\text{Cortes con Ejes: }} {\color{amorange}(-3, 0)}, \; {\color{amorange}(3, 0)}, \; {\color{amteal}(0, 9)} \\[4pt]"
            r"&\bullet \mathbf{\text{Monotonía: }} \text{Decrece en } (-\infty, 0) \setminus \{-1\}, \\[2pt]"
            r"&\quad \text{Crece en } (0, +\infty) \setminus \{1\} \quad {\color{amgreen}\blacksquare}"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        box8 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.18, corner_radius=0.1)

        # Gráfico cartesiano de la función racional con mínimo local
        axes = Axes(
            x_range=[-4.6, 4.6, 2],
            y_range=[-4.0, 13.0, 4],
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
            r"Gráfica de ${\color{amteal}f(x)} = \frac{{\color{amteal}x^2 - 9}}{{\color{amred}x^2 - 1}}$",
            font_size=21.5,
            color=WHITE
        ).move_to([3.25, 1.70, 0])

        # Asíntotas verticales discontinuas (x = -1 y x = 1)
        asymp_v1 = DashedLine(
            axes.c2p(-1.0, -3.8), axes.c2p(-1.0, 12.5),
            dash_length=0.08, color=THEME["poncho_red"], stroke_width=2.0
        )
        lbl_av1 = MathTex(r"x = -1", font_size=13.5, color=THEME["poncho_red"]).next_to(axes.c2p(-1.0, 11.5), LEFT, buff=0.08)

        asymp_v2 = DashedLine(
            axes.c2p(1.0, -3.8), axes.c2p(1.0, 12.5),
            dash_length=0.08, color=THEME["poncho_red"], stroke_width=2.0
        )
        lbl_av2 = MathTex(r"x = 1", font_size=13.5, color=THEME["poncho_red"]).next_to(axes.c2p(1.0, 11.5), RIGHT, buff=0.08)

        # Asíntota horizontal discontinua (y = 1)
        asymp_h = DashedLine(
            axes.c2p(-4.5, 1.0), axes.c2p(4.5, 1.0),
            dash_length=0.08, color=THEME["highlight"], stroke_width=1.8
        )
        lbl_ah = MathTex(r"y = 1", font_size=13.5, color=THEME["highlight"]).next_to(axes.c2p(-3.8, 1.0), UP, buff=0.08)

        # 3 Ramas continuas
        branch_left = axes.plot(
            lambda x: (x**2 - 9) / (x**2 - 1),
            x_range=[-4.5, -1.55],
            color=THEME["curve"],
            stroke_width=2.5
        )
        branch_center = axes.plot(
            lambda x: (x**2 - 9) / (x**2 - 1),
            x_range=[-0.52, 0.52],
            color=THEME["curve"],
            stroke_width=2.5
        )
        branch_right = axes.plot(
            lambda x: (x**2 - 9) / (x**2 - 1),
            x_range=[1.55, 4.5],
            color=THEME["curve"],
            stroke_width=2.5
        )
        curve_branches = VGroup(branch_left, branch_center, branch_right)
        curve_lbl = MathTex(r"y = f(x)", font_size=14.0, color=THEME["curve"]).move_to(axes.c2p(-2.8, 2.3))

        # Puntos notables: M(0, 9), P_x1(-3, 0), P_x2(3, 0)
        dot_m = Dot(axes.c2p(0.0, 9.0), radius=0.07, color=THEME["highlight"])
        lbl_m = MathTex(r"M(0, 9)", font_size=13.0, color=THEME["highlight"]).next_to(dot_m, DOWN + 0.6 * RIGHT, buff=0.10)

        dot_x1 = Dot(axes.c2p(-3.0, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_x1 = MathTex(r"(-3, 0)", font_size=13.0, color=THEME["statement_text"]).next_to(dot_x1, DOWN, buff=0.10)

        dot_x2 = Dot(axes.c2p(3.0, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_x2 = MathTex(r"(3, 0)", font_size=13.0, color=THEME["statement_text"]).next_to(dot_x2, DOWN, buff=0.10)

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
