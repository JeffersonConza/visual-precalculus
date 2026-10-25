"""
Ejercicio 4 - Tutorías y Preparación Quiz 4 (Jhoselyn)
Tema: Análisis Completo y Gráfica de Funciones:
      Función Racional de 3 Ramas: f(x) = (x^2 - 1) / (x^2 - 4).
      Dominio, paridad par, simetría axial, cortes coordenados, tabla de signos,
      asíntotas verticales y horizontal, monotonía, máximo local en M(0, 1/4),
      rango (-∞, 1/4] U (1, +∞), cuadro resumen de puntos notables y trazado cartesiano.

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


class EjercicioJh_04(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Jhoselyn",
            exercise="Ejercicio 4",
            topic="Función Racional de 3 Ramas",
            font_size=16.5
        )

        # 2. Enunciado institucional permanente con fórmula prominente (y = 2.65)
        self.setup_statement(
            desc_text="Analice completamente y grafique la función racional de 3 ramas:",
            math_tex=r"{\color{amteal}f(x)} = \frac{{\color{amteal}x^2 - 1}}{{\color{amred}x^2 - 4}}",
            desc_font_size=18.5,
            math_font_size=30.0,
            box_pos=np.array([0.0, 2.65, 0.0]),
            read_time=3.5
        )

        # 3. Barra de Progreso Interactiva (8 pasos detallados)
        self.setup_progress_bar([
            "1/8: Dominio y Restricciones",
            "2/8: Paridad y Simetría",
            "3/8: Cortes con los Ejes",
            "4/8: Tabla de Signos",
            "5/8: Asíntotas V. y H.",
            "6/8: Monotonía y Extremos",
            "7/8: Cuadro de Puntos Notables",
            "8/8: Gráfica Cartesiana y Verificación"
        ], dot_spacing=0.82, label_font_size=14.0)

        # ==========================================================
        # PASO 1 (C2): Dominio y Restricciones del Denominador
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Dominio y Restricciones:} \\[5pt]"
            r"&\text{Al ser una función racional, el denominador no se anula:} \\[4pt]"
            r"&x^2 - 4 \neq 0 \iff (x - 2)(x + 2) \neq 0 \implies x \neq \pm 2 \\[6pt]"
            r"&\mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R} \setminus \{-2, 2\}}} \\[5pt]"
            r"&\mathbf{\operatorname{Dom}(f) = {\color{amgreen}(-\infty, -2) \cup (-2, 2) \cup (2, +\infty)}} \\[6pt]"
            r"&\implies \text{El plano queda dividido en } \mathbf{3 \text{ ramas continuas}}."
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{1. Dominio y Restricciones:}\\[6pt]"
            r"$\bullet$ Toda fracción exige denominador no nulo:\\[3pt]"
            r"\hspace*{1.2em}$x^2 - 4 \neq 0 \implies x \neq -2 \quad \text{y} \quad x \neq 2$.\\[5pt]"
            r"$\bullet$ El dominio excluye ambos puntos:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgold}\operatorname{Dom}(f) = \mathbb{R} \setminus \{-2, 2\}}$.\\[5pt]"
            r"$\bullet$ Genera tres ramas continuas en la curva:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgreen}(-\infty, -2)}, \quad {\color{amgreen}(-2, 2)} \quad \text{y} \quad {\color{amgreen}(2, +\infty)}$.\\[2pt]"
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=3.3)

        # ==========================================================
        # PASO 2: Paridad y Simetría Axial
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Paridad y Simetría:} \\[5pt]"
            r"&\text{Evaluación formal de paridad } f(-x): \\[4pt]"
            r"&f(-x) = \frac{(-x)^2 - 1}{(-x)^2 - 4} = \frac{x^2 - 1}{x^2 - 4} = f(x) \\[6pt]"
            r"&\implies {\color{amteal}f(-x) = f(x)} \implies \mathbf{\text{Función PAR}} \\[6pt]"
            r"&\implies \text{Presenta } \mathbf{\text{Simetría Axial respecto al eje vertical } y} \\[5pt]"
            r"&\implies \text{La rama izquierda } (x < -2) \text{ es reflejo de la derecha } (x > 2)."
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{2. Paridad y Simetría:}\\[6pt]"
            r"$\bullet$ Evaluamos $f(-x)$ sustituyendo $-x$ en el cociente:\\[3pt]"
            r"\hspace*{1.2em}$f(-x) = \frac{(-x)^2 - 1}{(-x)^2 - 4} = \frac{x^2 - 1}{x^2 - 4} = f(x)$.\\[5pt]"
            r"$\bullet$ Concluimos formalmente: ${\color{amteal}f \text{ es PAR}}$.\\[5pt]"
            r"$\bullet$ La gráfica presenta simetría axial respecto al eje ${\color{amteal}y}$.\\[5pt]"
            r"$\bullet$ Las ramas laterales son imágenes especulares mutuas."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq2, just2, box_color=THEME["highlight"], advance_to_step=1, wait_time=3.3)

        # ==========================================================
        # PASO 3: Intersecciones con los Ejes Coordenados
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Intersecciones con los Ejes Coordenados:} \\[5pt]"
            r"&\bullet \textbf{Intercepto vertical } (x = 0): \\[3pt]"
            r"&\quad f(0) = \frac{0^2 - 1}{0^2 - 4} = \frac{-1}{-4} = \frac{1}{4} \implies \mathbf{{\color{amteal}P_y = \left(0, \frac{1}{4}\right)}} \\[6pt]"
            r"&\bullet \textbf{Interceptos horizontales } (f(x) = 0): \\[3pt]"
            r"&\quad \frac{x^2 - 1}{x^2 - 4} = 0 \iff x^2 - 1 = 0 \implies x = \pm 1 \\[5pt]"
            r"&\quad \mathbf{{\color{amorange}x_1 = -1}}, \quad \mathbf{{\color{amorange}x_2 = 1}} \\[4pt]"
            r"&\quad \text{Puntos: } {\color{amorange}P_{x_1}(-1, 0)}, \quad {\color{amorange}P_{x_2}(1, 0)}."
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{3. Cortes Coordenados:}\\[6pt]"
            r"$\bullet$ Corte con el eje $y$ ($x = 0$):\\[3pt]"
            r"\hspace*{1.2em}$f(0) = \frac{-1}{-4} = {\color{amteal}\frac{1}{4} \implies P_y(0, 0.25)}$.\\[5pt]"
            r"$\bullet$ Cortes con el eje $x$ ($f(x) = 0$):\\[3pt]"
            r"\hspace*{1.2em}Se anula cuando el numerador es cero: $x^2 - 1 = 0$.\\[5pt]"
            r"$\bullet$ Ceros reales: ${\color{amorange}x = -1}$ y ${\color{amorange}x = 1}$.\\[5pt]"
            r"$\bullet$ Intersecciones: ${\color{amorange}P_{x_1}(-1, 0)}$ y ${\color{amorange}P_{x_2}(1, 0)}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=3.3)

        # ==========================================================
        # PASO 4: Factorización y Tabla de Signos
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Factorización y Tabla de Signos:} \\[4pt]"
            r"&{\color{amteal}f(x)} = \frac{(x + 1)(x - 1)}{(x + 2)(x - 2)}, \quad \text{Ceros: } \{{\color{amorange}-2, -1, 1, 2}\} \\[5pt]"
            r"&\bullet (-\infty, -2): \; \frac{(+)}{(+)} = {\color{amgreen}\mathbf{(+)}} > 0 \quad \bullet (-2, -1): \; \frac{(+)}{(-)} = {\color{amred}\mathbf{(-)}} < 0 \\[4pt]"
            r"&\bullet (-1, 1): \; \frac{(-)}{(-)} = {\color{amgreen}\mathbf{(+)}} > 0 \quad \bullet (1, 2): \; \frac{(+)}{(-)} = {\color{amred}\mathbf{(-)}} < 0 \\[4pt]"
            r"&\bullet (2, +\infty): \; \frac{(+)}{(+)} = {\color{amgreen}\mathbf{(+)}} > 0 \\[5pt]"
            r"&\mathbf{\text{Positiva: } {\color{amgreen}(-\infty, -2) \cup (-1, 1) \cup (2, +\infty)}} \\[4pt]"
            r"&\mathbf{\text{Negativa: } {\color{amred}(-2, -1) \cup (1, 2)}}."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{4. Intervalos de Signo:}\\[6pt]"
            r"$\bullet$ Ceros del numerador y denominador dividen en 5 tramos.\\[4pt]"
            r"$\bullet$ $(-\infty, -2)$: $(+)/(+) = {\color{amgreen}(+)} \implies {\color{amgreen}f(x) > 0}$.\\[4pt]"
            r"$\bullet$ $(-2, -1)$: $(+)/(-) = {\color{amred}(-)} \implies {\color{amred}f(x) < 0}$.\\[4pt]"
            r"$\bullet$ $(-1, 1)$: $(-)/(-) = {\color{amgreen}(+)} \implies {\color{amgreen}f(x) > 0}$.\\[4pt]"
            r"$\bullet$ $(1, 2)$: $(+)/(-) = {\color{amred}(-)} \implies {\color{amred}f(x) < 0}$.\\[4pt]"
            r"$\bullet$ $(2, +\infty)$: $(+)/(+) = {\color{amgreen}(+)} \implies {\color{amgreen}f(x) > 0}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=3.3)

        # ==========================================================
        # PASO 5: Asíntotas Verticales y Horizontal
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Asíntotas Verticales y Horizontal:} \\[4pt]"
            r"&\bullet \textbf{Asíntotas Verticales (A.V.):} \\[3pt]"
            r"&\quad \text{Ceros del denominador irreducibles:} \\[3pt]"
            r"&\quad \mathbf{{\color{amred}x = -2}} \quad \text{y} \quad \mathbf{{\color{amred}x = 2}} \\[4pt]"
            r"&\quad \lim_{x \to 2^+} f(x) = +\infty, \quad \lim_{x \to 2^-} f(x) = -\infty \\[5pt]"
            r"&\bullet \textbf{Asíntota Horizontal (A.H.):} \\[3pt]"
            r"&\quad \lim_{x \to \pm\infty} \frac{x^2 - 1}{x^2 - 4} = \mathbf{{\color{amgold}1}} \implies \mathbf{{\color{amgold}y = 1}} \\[4pt]"
            r"&\bullet \textbf{Corte con A.H.: } \frac{x^2 - 1}{x^2 - 4} = 1 \implies -1 = -4 \; (\text{No corta})."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{5. Asíntotas del Sistema:}\\[6pt]"
            r"$\bullet$ Asíntotas Verticales en ceros del denominador:\\[3pt]"
            r"\hspace*{1.2em}${\color{amred}x = -2} \quad \text{y} \quad {\color{amred}x = 2}$.\\[5pt]"
            r"$\bullet$ Límites laterales confirman divergencia al infinito:\\[3pt]"
            r"\hspace*{1.2em}hacia $+\infty$ por fuera, hacia $-\infty$ por dentro.\\[5pt]"
            r"$\bullet$ Grados iguales ($2=2$) $\implies$ Asíntota horizontal:\\[3pt]"
            r"\hspace*{1.2em}$y = \frac{1}{1} = {\color{amgold}1 \implies y = 1}$.\\[5pt]"
            r"$\bullet$ La curva nunca corta su asíntota horizontal."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=3.3)

        # ==========================================================
        # PASO 6: Monotonía, Extremos Locales y Rango
        # ==========================================================
        eq6 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Monotonía, Extremos Locales y Rango:} \\[4pt]"
            r"&\bullet \textbf{Primera derivada formal } f'(x): \\[3pt]"
            r"&\quad f'(x) = \frac{2x(x^2 - 4) - (x^2 - 1)(2x)}{(x^2 - 4)^2} = \mathbf{\frac{-6x}{(x^2 - 4)^2}} \\[5pt]"
            r"&\bullet \textbf{Punto Crítico } (f'(x) = 0): -6x = 0 \implies \mathbf{{\color{amteal}x = 0}} \\[4pt]"
            r"&\quad \bullet x < 0 \; (x \neq -2): {\color{amgreen}f'(x) > 0} \implies \text{Estrictamente Creciente} \\[3pt]"
            r"&\quad \bullet x > 0 \; (x \neq 2): {\color{amred}f'(x) < 0} \implies \text{Estrictamente Decreciente} \\[4pt]"
            r"&\implies \mathbf{\text{Máximo Local en } {\color{amgold}M\left(0, \frac{1}{4}\right)}} \text{ (vértice central)} \\[5pt]"
            r"&\implies \mathbf{\operatorname{Ran}(f) = {\color{amgold}\left(-\infty, \frac{1}{4}\right] \cup (1, +\infty)}}."
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{6. Monotonía y Rango:}\\[6pt]"
            r"$\bullet$ Derivada del cociente:\\[3pt]"
            r"\hspace*{1.2em}$f'(x) = \frac{-6x}{(x^2 - 4)^2}$.\\[5pt]"
            r"$\bullet$ El denominador al cuadrado es positivo; el signo de $f'$ es opuesto a $x$.\\[5pt]"
            r"$\bullet$ En $x = 0$, $f'$ cambia de $+$ a $-$:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgold}M\left(0, \frac{1}{4}\right)}$ es un ${\color{amgold}\textbf{Máximo Local}}$.\\[5pt]"
            r"$\bullet$ Rango con franja vacía en $\left(\frac{1}{4}, 1\right]$:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgold}\operatorname{Ran}(f) = (-\infty, 1/4] \cup (1, +\infty)}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq6, just6, box_color=THEME["highlight"], advance_to_step=5, wait_time=3.3)

        # ==========================================================
        # PASO 7: Cuadro Horizontal de Variación y Puntos Notables
        # ==========================================================
        eq7 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{7. Cuadro de Variación y Puntos Notables:} \\[6pt]"
            r"&\begin{array}{c|c|c|c|c}"
            r"x & (-\infty, -2) & (-2, 0) & (0, 2) & (2, +\infty) \\ \hline "
            r"-6x & + & + & - & - \\ \hline "
            r"(x^2 - 4)^2 & + & + & + & + \\ \hline "
            r"f'(x) & {\color{amgreen}\mathbf{+}} & {\color{amgreen}\mathbf{+}} & {\color{amred}\mathbf{-}} & {\color{amred}\mathbf{-}} \\ \hline "
            r"f(x) & \nearrow & \nearrow & \searrow & \searrow"
            r"\end{array} \\[8pt]"
            r"&\bullet \mathbf{\text{Punto Crítico: }} x = 0 \implies {\color{amgold}M(0, 1/4)} \text{ (Máximo Local)}. \\[3pt]"
            r"&\bullet \mathbf{\text{Polos (A.V.): }} x = -2 \text{ y } x = 2 \text{ con divergencia } \pm\infty. \\[3pt]"
            r"&\bullet \mathbf{\text{Cortes } X: } P_{x_1}(-1, 0) \text{ y } P_{x_2}(1, 0) \text{ en la rama central}."
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{7. Síntesis Horizontal:}\\[6pt]"
            r"$\bullet$ La tabla horizontal resume el signo de $f'(x)$ por factores.\\[5pt]"
            r"$\bullet$ Flechas confirman el crecimiento ($\nearrow$) hacia ${\color{amgold}M(0, 1/4)}$ y decrecimiento ($\searrow$).\\[5pt]"
            r"$\bullet$ Muestra los polos de discontinuidad en $x = \pm 2$ (Asíntotas Verticales).\\[5pt]"
            r"$\bullet$ Puntos de anclaje para el trazado cartesiano continuo."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq7, just7, box_color=THEME["highlight"], advance_to_step=6, wait_time=3.7)

        # ==========================================================
        # PASO 8: Gráfica Cartesiana y Verificación Visual
        # ==========================================================
        left_summary = MathTex(
            r"\begin{aligned}"
            r"&\textbf{8. Resumen Formal de Resultados:} \\[4pt]"
            r"&\bullet \mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R} \setminus \{-2, 2\}}} \\[4pt]"
            r"&\bullet \mathbf{\operatorname{Ran}(f) = {\color{amgold}\left(-\infty, \frac{1}{4}\right] \cup (1, +\infty)}} \\[4pt]"
            r"&\bullet \mathbf{\text{Paridad: }} {\color{amteal}\text{Par }} (f(-x) = f(x)) \\[4pt]"
            r"&\bullet \mathbf{\text{Asíntotas V.: }} {\color{amred}x = -2}, \quad {\color{amred}x = 2} \\[4pt]"
            r"&\bullet \mathbf{\text{Asíntota H.: }} {\color{amgold}y = 1} \quad (\text{sin intersección}) \\[4pt]"
            r"&\bullet \mathbf{\text{Máx. Local: }} {\color{amgold}M\left(0, \frac{1}{4}\right)}, \quad \mathbf{\text{Cortes: }} {\color{amorange}(\pm 1, 0)} \\[4pt]"
            r"&\bullet \mathbf{\text{Positiva: }} {\color{amgreen}(-\infty, -2) \cup (-1, 1) \cup (2, +\infty)} \quad {\color{amgreen}\blacksquare}"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        box8 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.18, corner_radius=0.1)

        # Gráfico cartesiano de la función racional de 3 ramas
        axes, axes_labels = self.setup_axes(
            x_range=[-4.5, 4.5, 1],
            y_range=[-3.2, 3.5, 1],
            x_length=4.8,
            y_length=3.4,
            center=[3.25, -0.65, 0],
            include_numbers=True,
            numbers_font_size=16,
            labels_font_size=19
        )
        graph_title = Tex(
            r"Gráfica de ${\color{amteal}f(x)} = \frac{{\color{amteal}x^2 - 1}}{{\color{amred}x^2 - 4}}$",
            font_size=21.5,
            color=WHITE
        ).move_to([3.25, 1.70, 0])

        # Asíntotas verticales discontinuas (x = -2 y x = 2)
        asymp_v1 = DashedLine(
            axes.c2p(-2.0, -3.1), axes.c2p(-2.0, 3.3),
            dash_length=0.08, color=THEME["poncho_red"], stroke_width=2.0
        )
        lbl_av1 = MathTex(r"x = -2", font_size=14.0, color=THEME["poncho_red"]).next_to(axes.c2p(-2.0, -2.5), LEFT, buff=0.06)

        asymp_v2 = DashedLine(
            axes.c2p(2.0, -3.1), axes.c2p(2.0, 3.3),
            dash_length=0.08, color=THEME["poncho_red"], stroke_width=2.0
        )
        lbl_av2 = MathTex(r"x = 2", font_size=14.0, color=THEME["poncho_red"]).next_to(axes.c2p(2.0, -2.5), RIGHT, buff=0.06)

        # Asíntota horizontal discontinua (y = 1)
        asymp_h = DashedLine(
            axes.c2p(-4.3, 1.0), axes.c2p(4.3, 1.0),
            dash_length=0.08, color=THEME["highlight"], stroke_width=1.8
        )
        lbl_ah = MathTex(r"y = 1", font_size=14.0, color=THEME["highlight"]).next_to(axes.c2p(-4.1, 1.0), DOWN, buff=0.06)

        # 3 Ramas continuas de la curva
        branch_left = axes.plot(
            lambda x: (x**2 - 1) / (x**2 - 4),
            x_range=[-4.2, -2.285],
            color=THEME["curve"],
            stroke_width=2.5
        )
        branch_center = axes.plot(
            lambda x: (x**2 - 1) / (x**2 - 4),
            x_range=[-1.82, 1.82],
            color=THEME["curve"],
            stroke_width=2.5
        )
        branch_right = axes.plot(
            lambda x: (x**2 - 1) / (x**2 - 4),
            x_range=[2.285, 4.2],
            color=THEME["curve"],
            stroke_width=2.5
        )
        curve_branches = VGroup(branch_left, branch_center, branch_right)
        curve_lbl = MathTex(r"y = f(x)", font_size=14.5, color=THEME["curve"]).move_to(axes.c2p(3.2, 2.2))

        # Puntos notables: M(0, 1/4), P_x1(-1, 0), P_x2(1, 0)
        dot_max = Dot(axes.c2p(0.0, 0.25), radius=0.07, color=THEME["highlight"])
        lbl_max = MathTex(r"M\left(0, \frac{1}{4}\right)", font_size=13.5, color=THEME["highlight"]).next_to(dot_max, DOWN, buff=0.08)

        dot_x1 = Dot(axes.c2p(-1.0, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_x1 = MathTex(r"(-1, 0)", font_size=13.0, color=THEME["statement_text"]).next_to(dot_x1, UP + LEFT, buff=0.08)

        dot_x2 = Dot(axes.c2p(1.0, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_x2 = MathTex(r"(1, 0)", font_size=13.0, color=THEME["statement_text"]).next_to(dot_x2, UP + RIGHT, buff=0.08)

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
            FadeIn(dot_max),
            Write(lbl_max),
            FadeIn(dot_x1),
            Write(lbl_x1),
            FadeIn(dot_x2),
            Write(lbl_x2),
            run_time=2.4
        )
        self.wait(8.5)

        # Cierre institucional
        graph_group = VGroup(
            axes, axes_labels, graph_title,
            asymp_v1, lbl_av1, asymp_v2, lbl_av2,
            asymp_h, lbl_ah,
            curve_branches, curve_lbl,
            dot_max, lbl_max,
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
