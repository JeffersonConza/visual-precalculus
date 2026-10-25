"""
Ejercicio 4 - Tutorías y Preparación Quiz 4 (Jhoselyn)
Tema: Análisis Completo y Gráfica de Funciones:
      Función Racional de 3 Ramas: f(x) = (x^2 - 1) / (x^2 - 4).
      Dominio, paridad par, simetría axial, cortes coordenados, tabla de signos,
      asíntotas verticales y horizontal, máximo local, rango y trazado cartesiano.

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica en 7 pasos con ecuaciones en LaTeX de gran legibilidad.
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
            font_size=16
        )

        # 2. Enunciado institucional permanente con fórmula prominente (y = 2.65)
        self.setup_statement(
            desc_text="Analice completamente y grafique la función racional de 3 ramas:",
            math_tex=r"{\color{amteal}f(x)} = \frac{{\color{amteal}x^2 - 1}}{{\color{amred}x^2 - 4}}",
            desc_font_size=18.0,
            math_font_size=29.0,
            box_pos=np.array([0.0, 2.65, 0.0]),
            read_time=3.5
        )

        # 3. Barra de Progreso Interactiva (7 pasos detallados)
        self.setup_progress_bar([
            "1/7: Dominio y Restricciones",
            "2/7: Paridad y Simetría",
            "3/7: Cortes con los Ejes",
            "4/7: Tabla de Signos",
            "5/7: Asíntotas Verticales y Horizontal",
            "6/7: Extremos Locales y Rango",
            "7/7: Gráfica Cartesiana y Verificación"
        ], dot_spacing=0.92, label_font_size=14.0)

        # ==========================================================
        # PASO 1 (C2): Dominio y Restricciones del Denominador
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Dominio y Restricciones:} \\[6pt]"
            r"&\text{Al ser una función racional, el denominador no debe anularse:} \\[5pt]"
            r"&x^2 - 4 \neq 0 \iff (x - 2)(x + 2) \neq 0 \implies x \neq \pm 2 \\[7pt]"
            r"&\mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R} \setminus \{-2, 2\}}} \\[6pt]"
            r"&\mathbf{\operatorname{Dom}(f) = {\color{amgreen}(-\infty, -2) \cup (-2, 2) \cup (2, +\infty)}} \\[7pt]"
            r"&\implies \text{El plano queda dividido en } \mathbf{3 \text{ regiones continuas}}."
            r"\end{aligned}",
            font_size=20.0,
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
            font_size=21.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.1)

        # ==========================================================
        # PASO 2: Paridad y Simetría Axial
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Paridad y Simetría:} \\[6pt]"
            r"&\text{Evaluación formal de paridad } f(-x): \\[5pt]"
            r"&f(-x) = \frac{(-x)^2 - 1}{(-x)^2 - 4} = \frac{x^2 - 1}{x^2 - 4} = f(x) \\[7pt]"
            r"&\implies {\color{amteal}f(-x) = f(x)} \implies \mathbf{\text{Función PAR}} \\[7pt]"
            r"&\implies \text{Presenta } \mathbf{\text{Simetría Axial respecto al eje vertical } y} \\[6pt]"
            r"&\implies \text{La rama izquierda } (x < -2) \text{ es reflejo de la derecha } (x > 2)."
            r"\end{aligned}",
            font_size=19.5,
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
            font_size=21.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq2, just2, box_color=THEME["highlight"], advance_to_step=1, wait_time=4.1)

        # ==========================================================
        # PASO 3: Intersecciones con los Ejes Coordenados
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Intersecciones con los Ejes Coordenados:} \\[5pt]"
            r"&\bullet \textbf{Intercepto vertical } (x = 0): \\[3pt]"
            r"&\quad f(0) = \frac{0^2 - 1}{0^2 - 4} = \frac{-1}{-4} = \frac{1}{4} \implies \mathbf{{\color{amteal}P_y = \left(0, \frac{1}{4}\right)}} \\[6pt]"
            r"&\bullet \textbf{Interceptos horizontales } (f(x) = 0): \\[3pt]"
            r"&\quad \frac{x^2 - 1}{x^2 - 4} = 0 \iff x^2 - 1 = 0 \implies x = \pm 1 \\[6pt]"
            r"&\quad \mathbf{{\color{amorange}x_1 = -1}}, \quad \mathbf{{\color{amorange}x_2 = 1}} \\[5pt]"
            r"&\quad \text{Puntos: } {\color{amorange}P_{x_1}(-1, 0)}, \quad {\color{amorange}P_{x_2}(1, 0)}."
            r"\end{aligned}",
            font_size=20.5,
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
            font_size=21.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=4.1)

        # ==========================================================
        # PASO 4: Factorización y Tabla de Signos
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Factorización y Tabla de Signos:} \\[3pt]"
            r"&{\color{amteal}f(x)} = \frac{(x + 1)(x - 1)}{(x + 2)(x - 2)} \\[3pt]"
            r"&\text{Puntos frontera ordenados: } \{{\color{amorange}-2, -1, 1, 2}\} \\[3pt]"
            r"&\bullet \left(-\infty, -2\right): \; \frac{(+)}{(+)} = \mathbf{{\color{amgreen}(+)}} \implies {\color{amgreen}f(x) > 0} \\[2.5pt]"
            r"&\bullet \left(-2, -1\right): \; \frac{(+)}{(-)} = \mathbf{{\color{amred}(-)}} \implies {\color{amred}f(x) < 0} \\[2.5pt]"
            r"&\bullet \left(-1, 1\right): \; \frac{(-)}{(-)} = \mathbf{{\color{amgreen}(+)}} \implies {\color{amgreen}f(x) > 0} \\[2.5pt]"
            r"&\bullet \left(1, 2\right): \; \frac{(+)}{(-)} = \mathbf{{\color{amred}(-)}} \implies {\color{amred}f(x) < 0} \\[2.5pt]"
            r"&\bullet \left(2, +\infty\right): \; \frac{(+)}{(+)} = \mathbf{{\color{amgreen}(+)}} \implies {\color{amgreen}f(x) > 0} \\[3pt]"
            r"&\mathbf{\text{Positiva en: } {\color{amgreen}\left(-\infty, -2\right) \cup (-1, 1) \cup \left(2, +\infty\right)}} \\[3pt]"
            r"&\mathbf{\text{Negativa en: } {\color{amred}\left(-2, -1\right) \cup \left(1, 2\right)}}."
            r"\end{aligned}",
            font_size=17.5,
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
            font_size=20.5,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=4.1)

        # ==========================================================
        # PASO 5: Asíntotas Verticales y Horizontal
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Asíntotas Verticales y Horizontal:} \\[5pt]"
            r"&\bullet \textbf{Asíntotas Verticales (A.V.):} \\[3pt]"
            r"&\quad \text{En los ceros del denominador que no se cancelan:} \\[3pt]"
            r"&\quad \mathbf{{\color{amred}x = -2}} \quad \text{y} \quad \mathbf{{\color{amred}x = 2}} \\[4pt]"
            r"&\quad \lim_{x \to 2^+} f(x) = +\infty, \quad \lim_{x \to 2^-} f(x) = -\infty \\[6pt]"
            r"&\bullet \textbf{Asíntota Horizontal (A.H.):} \\[3pt]"
            r"&\quad \lim_{x \to \pm\infty} \frac{x^2 - 1}{x^2 - 4} = \lim_{x \to \pm\infty} \frac{1 - 1/x^2}{1 - 4/x^2} = \mathbf{{\color{amgold}1}} \implies \mathbf{{\color{amgold}y = 1}} \\[5pt]"
            r"&\bullet \textbf{Corte con A.H.: } \frac{x^2 - 1}{x^2 - 4} = 1 \implies -1 = -4 \; (\text{No corta})."
            r"\end{aligned}",
            font_size=19.5,
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
            font_size=21.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=4.1)

        # ==========================================================
        # PASO 6: Extremos Locales y Rango
        # ==========================================================
        eq6 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Extremos Locales y Rango:} \\[5pt]"
            r"&\bullet \textbf{Máximo Local en la rama central:} \\[3pt]"
            r"&\quad \text{La cúspide central ocurre en: } \mathbf{{\color{amgold}M\left(0, \frac{1}{4}\right) = (0, 0.25)}} \\[6pt]"
            r"&\bullet \textbf{Rango por ramas de la función:} \\[3pt]"
            r"&\quad \text{Rama central vive en: } {\color{amteal}\left(-\infty, \frac{1}{4}\right]} \\[4pt]"
            r"&\quad \text{Ramas laterales viven en: } {\color{amteal}(1, +\infty)} \\[6pt]"
            r"&\quad \mathbf{\operatorname{Ran}(f) = {\color{amgold}\left(-\infty, \frac{1}{4}\right] \cup (1, +\infty)}}."
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{6. Extremos y Rango:}\\[6pt]"
            r"$\bullet$ La rama central sube hasta su máximo local:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgold}M\left(0, \frac{1}{4}\right)}$ y desciende a $-\infty$ en ambos lados.\\[5pt]"
            r"$\bullet$ Ramas laterales caen desde $+\infty$ hacia $y = 1$.\\[5pt]"
            r"$\bullet$ Región vacía intermedia: la curva jamás cruza $\left(\frac{1}{4}, 1\right]$.\\[5pt]"
            r"$\bullet$ Unión formal de imágenes: ${\color{amgold}\operatorname{Ran}(f) = (-\infty, 1/4] \cup (1, +\infty)}$."
            r"\end{minipage}",
            font_size=21.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq6, just6, box_color=THEME["highlight"], advance_to_step=5, wait_time=4.1)

        # ==========================================================
        # PASO 7: Gráfica Cartesiana y Verificación Visual
        # ==========================================================
        left_summary = MathTex(
            r"\begin{aligned}"
            r"&\textbf{7. Resumen Formal de Resultados:} \\[5pt]"
            r"&\bullet \mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R} \setminus \{-2, 2\}}} \\[5pt]"
            r"&\bullet \mathbf{\operatorname{Ran}(f) = {\color{amgold}\left(-\infty, \frac{1}{4}\right] \cup (1, +\infty)}} \\[5pt]"
            r"&\bullet \mathbf{\text{Paridad: }} {\color{amteal}\text{Par }} (f(-x) = f(x)) \\[5pt]"
            r"&\bullet \mathbf{\text{Asíntotas V.: }} {\color{amred}x = -2}, \quad {\color{amred}x = 2} \\[5pt]"
            r"&\bullet \mathbf{\text{Asíntota H.: }} {\color{amgold}y = 1} \quad (\text{sin intersección}) \\[5pt]"
            r"&\bullet \mathbf{\text{Máx. Local: }} {\color{amgold}M\left(0, \frac{1}{4}\right)}, \quad \mathbf{\text{Cortes: }} {\color{amorange}(\pm 1, 0)} \\[5pt]"
            r"&\bullet \mathbf{\text{Positiva: }} {\color{amgreen}(-\infty, -2) \cup (-1, 1) \cup (2, +\infty)} \quad {\color{amgreen}\blacksquare}"
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        box7 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.18, corner_radius=0.1)

        # Gráfico cartesiano de la función racional de 3 ramas
        axes, axes_labels = self.setup_axes(
            x_range=[-4.5, 4.5, 1],
            y_range=[-3.2, 3.5, 1],
            x_length=4.8,
            y_length=3.4,
            center=[3.25, -0.65, 0],
            include_numbers=True,
            numbers_font_size=15,
            labels_font_size=18
        )
        graph_title = Tex(
            r"Gráfica de ${\color{amteal}f(x)} = \frac{{\color{amteal}x^2 - 1}}{{\color{amred}x^2 - 4}}$",
            font_size=21.0,
            color=WHITE
        ).move_to([3.25, 1.70, 0])

        # Asíntotas verticales discontinuas (x = -2 y x = 2)
        asymp_v1 = DashedLine(
            axes.c2p(-2.0, -3.1), axes.c2p(-2.0, 3.3),
            dash_length=0.08, color=THEME["poncho_red"], stroke_width=2.0
        )
        lbl_av1 = MathTex(r"x = -2", font_size=11.5, color=THEME["poncho_red"]).next_to(axes.c2p(-2.0, -2.5), LEFT, buff=0.06)

        asymp_v2 = DashedLine(
            axes.c2p(2.0, -3.1), axes.c2p(2.0, 3.3),
            dash_length=0.08, color=THEME["poncho_red"], stroke_width=2.0
        )
        lbl_av2 = MathTex(r"x = 2", font_size=11.5, color=THEME["poncho_red"]).next_to(axes.c2p(2.0, -2.5), RIGHT, buff=0.06)

        # Asíntota horizontal discontinua (y = 1)
        asymp_h = DashedLine(
            axes.c2p(-4.3, 1.0), axes.c2p(4.3, 1.0),
            dash_length=0.08, color=THEME["highlight"], stroke_width=1.8
        )
        lbl_ah = MathTex(r"y = 1", font_size=11.5, color=THEME["highlight"]).next_to(axes.c2p(-4.1, 1.0), DOWN, buff=0.06)

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
        curve_lbl = MathTex(r"y = f(x)", font_size=13.5, color=THEME["curve"]).move_to(axes.c2p(3.2, 2.2))

        # Puntos notables: M(0, 1/4), P_x1(-1, 0), P_x2(1, 0)
        dot_max = Dot(axes.c2p(0.0, 0.25), radius=0.07, color=THEME["highlight"])
        lbl_max = MathTex(r"M\left(0, \frac{1}{4}\right)", font_size=12.0, color=THEME["highlight"]).next_to(dot_max, DOWN, buff=0.08)

        dot_x1 = Dot(axes.c2p(-1.0, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_x1 = MathTex(r"(-1, 0)", font_size=11.0, color=THEME["statement_text"]).next_to(dot_x1, DOWN + LEFT, buff=0.05)

        dot_x2 = Dot(axes.c2p(1.0, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_x2 = MathTex(r"(1, 0)", font_size=11.0, color=THEME["statement_text"]).next_to(dot_x2, DOWN + RIGHT, buff=0.05)

        prog_anims = self.get_advance_progress_anims(6)

        self.play(
            FadeOut(self.active_math),
            FadeOut(self.active_just),
            FadeOut(self.active_box),
            FadeIn(left_summary),
            Create(box7),
            Create(axes),
            Write(axes_labels),
            Write(graph_title),
            *prog_anims,
            run_time=1.8
        )
        self.active_box = box7
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
