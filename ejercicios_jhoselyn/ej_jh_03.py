"""
Ejercicio 3 - Tutorías y Preparación Quiz 4 (Jhoselyn)
Tema: Análisis Completo y Gráfica de Funciones:
      Polinomio Bicuadrático: f(x) = 1/4 x^4 - 3/2 x^2 + 5/4.
      Dominio, paridad par, simetría axial, cortes coordenados, tabla de signos,
      extremos locales y absolutos, monotonía, rango y trazado cartesiano en W.

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica en 6 pasos con ecuaciones en LaTeX de gran legibilidad.
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


class EjercicioJh_03(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Jhoselyn",
            exercise="Ejercicio 3",
            topic="Polinomio Bicuadrático",
            font_size=16
        )

        # 2. Enunciado institucional permanente con fórmula prominente (y = 2.65)
        self.setup_statement(
            desc_text="Analice completamente y grafique la función polinómica bicuadrática:",
            math_tex=r"{\color{amteal}f(x)} = {\color{amteal}\frac{1}{4}}x^4 - {\color{amred}\frac{3}{2}}x^2 + {\color{amgold}\frac{5}{4}}",
            desc_font_size=18.0,
            math_font_size=28.0,
            box_pos=np.array([0.0, 2.65, 0.0]),
            read_time=4.0
        )

        # 3. Barra de Progreso Interactiva (6 pasos)
        self.setup_progress_bar([
            "1/6: Dominio y Paridad",
            "2/6: Cortes Coordenados",
            "3/6: Factorización y Signos",
            "4/6: Extremos y Puntos Críticos",
            "5/6: Monotonía y Rango",
            "6/6: Gráfica Cartesiana y Verificación"
        ], label_font_size=14.5)

        # ==========================================================
        # PASO 1 (C2): Dominio y Simetría de Paridad
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Dominio y Simetría de Paridad:} \\[6pt]"
            r"&\text{Al ser } {\color{amteal}f(x)} \text{ una función polinómica de grado 4:} \\[5pt]"
            r"&\mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R}} = {\color{amgreen}(-\infty, +\infty)}} \\[8pt]"
            r"&\textbf{Evaluación formal de paridad } f(-x): \\[5pt]"
            r"&f(-x) = \frac{1}{4}(-x)^4 - \frac{3}{2}(-x)^2 + \frac{5}{4} = \frac{1}{4}x^4 - \frac{3}{2}x^2 + \frac{5}{4} = f(x) \\[7pt]"
            r"&\implies {\color{amteal}f(-x) = f(x)} \implies \mathbf{\text{Función PAR}} \\[6pt]"
            r"&\implies \text{Presenta } \mathbf{\text{Simetría Axial respecto al eje } y}."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{1. Dominio y Paridad:}\\[6pt]"
            r"$\bullet$ Toda función polinómica tiene ${\color{amgold}\operatorname{Dom}(f) = \mathbb{R}}$.\\[5pt]"
            r"$\bullet$ Evaluamos $f(-x)$ sustituyendo $-x$ en las potencias pares:\\[3pt]"
            r"\hspace*{1.2em}$(-x)^4 = x^4, \quad (-x)^2 = x^2$.\\[5pt]"
            r"$\bullet$ Concluimos formalmente: ${\color{amteal}f \text{ es PAR}}$.\\[5pt]"
            r"$\bullet$ La gráfica es un reflejo especular sobre el eje ${\color{amteal}y}$.\\[2pt]"
            r"\end{minipage}",
            font_size=21.5,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=5.4)

        # ==========================================================
        # PASO 2: Cortes con los Ejes Coordenados
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Intersecciones con los Ejes Coordenados:} \\[4pt]"
            r"&\bullet \textbf{Intercepto vertical } (x = 0): \\[3pt]"
            r"&\quad f(0) = \frac{1}{4}(0)^4 - \frac{3}{2}(0)^2 + \frac{5}{4} = \frac{5}{4} \implies \mathbf{{\color{amteal}P_y = \left(0, \frac{5}{4}\right)}} \\[5pt]"
            r"&\bullet \textbf{Interceptos horizontales } (f(x) = 0): \\[3pt]"
            r"&\quad \frac{1}{4}\left(x^4 - 6x^2 + 5\right) = 0 \iff (x^2 - 1)(x^2 - 5) = 0 \\[4pt]"
            r"&\quad x^2 = 1 \implies x = \pm 1, \quad x^2 = 5 \implies x = \pm\sqrt{5} \\[5pt]"
            r"&\quad \mathbf{{\color{amorange}x_1 = -\sqrt{5} \approx -2.24}}, \quad \mathbf{{\color{amorange}x_2 = -1}} \\[3pt]"
            r"&\quad \mathbf{{\color{amorange}x_3 = 1}}, \quad \mathbf{{\color{amorange}x_4 = \sqrt{5} \approx 2.24}} \\[4pt]"
            r"&\quad \text{Puntos: } {\color{amorange}P_{x_1}(-\sqrt{5}, 0)}, \; {\color{amorange}P_{x_2}(-1, 0)}, \; {\color{amorange}P_{x_3}(1, 0)}, \; {\color{amorange}P_{x_4}(\sqrt{5}, 0)}."
            r"\end{aligned}",
            font_size=19.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{2. Cortes Coordenados:}\\[6pt]"
            r"$\bullet$ Corte con el eje $y$ ($x = 0$): ${\color{amteal}P_y\left(0, \frac{5}{4}\right) = (0, 1.25)}$.\\[5pt]"
            r"$\bullet$ Cortes con el eje $x$ ($f(x) = 0$):\\[3pt]"
            r"\hspace*{1.2em}Ecuación bicuadrática: $(x^2 - 1)(x^2 - 5) = 0$.\\[5pt]"
            r"$\bullet$ Cuatro ceros reales por paridad:\\[3pt]"
            r"\hspace*{1.2em}${\color{amorange}x = \pm 1} \quad \text{y} \quad {\color{amorange}x = \pm\sqrt{5} \approx \pm 2.24}$.\\[5pt]"
            r"$\bullet$ Cuatro intersecciones simétricas respecto al eje $y$."
            r"\end{minipage}",
            font_size=21.5,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq2, just2, box_color=THEME["highlight"], advance_to_step=1, wait_time=5.4)

        # ==========================================================
        # PASO 3: Factorización y Tabla de Signos
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Factorización y Tabla de Signos:} \\[3pt]"
            r"&{\color{amteal}f(x)} = \frac{1}{4}(x + 1)(x - 1)\left(x + \sqrt{5}\right)\left(x - \sqrt{5}\right) \\[3pt]"
            r"&\text{Intervalos definidos por las 4 raíces: } \\[3pt]"
            r"&\bullet \left(-\infty, -\sqrt{5}\right): \; (+) \cdot (+) = \mathbf{{\color{amgreen}(+)}} \implies {\color{amgreen}f(x) > 0} \\[2.5pt]"
            r"&\bullet \left(-\sqrt{5}, -1\right): \; (+) \cdot (-) = \mathbf{{\color{amred}(-)}} \implies {\color{amred}f(x) < 0} \\[2.5pt]"
            r"&\bullet \left(-1, 1\right): \; (-) \cdot (-) = \mathbf{{\color{amgreen}(+)}} \implies {\color{amgreen}f(x) > 0} \\[2.5pt]"
            r"&\bullet \left(1, \sqrt{5}\right): \; (+) \cdot (-) = \mathbf{{\color{amred}(-)}} \implies {\color{amred}f(x) < 0} \\[2.5pt]"
            r"&\bullet \left(\sqrt{5}, +\infty\right): \; (+) \cdot (+) = \mathbf{{\color{amgreen}(+)}} \implies {\color{amgreen}f(x) > 0} \\[3pt]"
            r"&\mathbf{\text{Positiva en: } {\color{amgreen}\left(-\infty, -\sqrt{5}\right) \cup (-1, 1) \cup \left(\sqrt{5}, +\infty\right)}} \\[3pt]"
            r"&\mathbf{\text{Negativa en: } {\color{amred}\left(-\sqrt{5}, -1\right) \cup \left(1, \sqrt{5}\right)}}."
            r"\end{aligned}",
            font_size=18.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{3. Intervalos de Signo:}\\[6pt]"
            r"$\bullet$ Las 4 raíces dividen la recta en 5 intervalos.\\[5pt]"
            r"$\bullet$ $(-\infty, -\sqrt{5})$: $(+)\cdot(+) = {\color{amgreen}(+)} \implies {\color{amgreen}f(x) > 0}$.\\[4pt]"
            r"$\bullet$ $(-\sqrt{5}, -1)$: $(+)\cdot(-) = {\color{amred}(-)} \implies {\color{amred}f(x) < 0}$.\\[4pt]"
            r"$\bullet$ $(-1, 1)$: $(-)\cdot(-) = {\color{amgreen}(+)} \implies {\color{amgreen}f(x) > 0}$.\\[4pt]"
            r"$\bullet$ $(1, \sqrt{5})$: $(+)\cdot(-) = {\color{amred}(-)} \implies {\color{amred}f(x) < 0}$.\\[4pt]"
            r"$\bullet$ $(\sqrt{5}, +\infty)$: $(+)\cdot(+) = {\color{amgreen}(+)} \implies {\color{amgreen}f(x) > 0}$."
            r"\end{minipage}",
            font_size=21.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=5.4)

        # ==========================================================
        # PASO 4: Puntos Críticos y Extremos Absolutos
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Puntos Críticos y Extremos Absolutos:} \\[5pt]"
            r"&\bullet \textbf{Máximo Local en el eje } y: \\[3pt]"
            r"&\quad f(0) = \frac{5}{4} \implies \mathbf{{\color{amgold}M\left(0, \frac{5}{4}\right) = (0, 1.25)}} \\[6pt]"
            r"&\bullet \textbf{Mínimos Absolutos en } x = \pm\sqrt{3}: \\[3pt]"
            r"&\quad f(\pm\sqrt{3}) = \frac{1}{4}(9) - \frac{3}{2}(3) + \frac{5}{4} = \frac{9 - 18 + 5}{4} = \mathbf{{\color{amteal}-1}} \\[5pt]"
            r"&\quad \mathbf{{\color{amteal}m_1\left(-\sqrt{3}, -1\right)}}, \quad \mathbf{{\color{amteal}m_2\left(\sqrt{3}, -1\right)}} \\[6pt]"
            r"&\bullet \textbf{Simetría Par de Extremos:} \\[3pt]"
            r"&\quad f(-\sqrt{3}) = f(\sqrt{3}) = -1 \quad (\text{Ambos pozos a la misma altura})."
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{4. Extremos y Puntos Notables:}\\[6pt]"
            r"$\bullet$ Máximo local: la cúspide central en ${\color{amgold}M\left(0, \frac{5}{4}\right)}$.\\[5pt]"
            r"$\bullet$ Mínimos absolutos: los dos fondos idénticos en:\\[3pt]"
            r"\hspace*{1.2em}${\color{amteal}m_1(-\sqrt{3}, -1)}$ y ${\color{amteal}m_2(\sqrt{3}, -1)}$.\\[5pt]"
            r"$\bullet$ Simetría de extremos: $f(-\sqrt{3}) = f(\sqrt{3}) = -1$.\\[5pt]"
            r"$\bullet$ La gráfica presenta la silueta característica en forma de ``W''."
            r"\end{minipage}",
            font_size=21.5,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=5.4)

        # ==========================================================
        # PASO 5: Monotonía y Rango
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Intervalos de Monotonía y Rango:} \\[6pt]"
            r"&\bullet \textbf{Monotonía (Silueta en ``W''):} \\[4pt]"
            r"&\quad \mathbf{{\color{amred}f \text{ es decreciente en } \left(-\infty, -\sqrt{3}\right] \cup \left[0, \sqrt{3}\right]}} \\[5pt]"
            r"&\quad \mathbf{{\color{amgreen}f \text{ es creciente en } \left[-\sqrt{3}, 0\right] \cup \left[\sqrt{3}, +\infty\right)}} \\[7pt]"
            r"&\bullet \textbf{Rango (Recorrido de la Función):} \\[4pt]"
            r"&\quad \text{Valor mínimo absoluto alcanzado: } y_{\min} = -1 \\[4pt]"
            r"&\quad \lim_{x \to \pm\infty} f(x) = +\infty \\[4pt]"
            r"&\quad \mathbf{\operatorname{Ran}(f) = {\color{amgold}[-1, +\infty)}}."
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{5. Monotonía y Rango:}\\[6pt]"
            r"$\bullet$ Decreciente en ${\color{amred}(-\infty, -\sqrt{3}] \cup [0, \sqrt{3}]}$.\\[5pt]"
            r"$\bullet$ Creciente en ${\color{amgreen}[-\sqrt{3}, 0] \cup [\sqrt{3}, +\infty)}$.\\[5pt]"
            r"$\bullet$ Ramas laterales crecen sin límite: $\lim_{x \to \pm\infty} f(x) = +\infty$.\\[5pt]"
            r"$\bullet$ El valor más bajo de la curva es $y = -1$:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgold}\operatorname{Ran}(f) = [-1, +\infty)}$."
            r"\end{minipage}",
            font_size=21.5,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=5.4)

        # ==========================================================
        # PASO 6: Gráfica Cartesiana y Verificación Visual
        # ==========================================================
        left_summary = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Resumen Formal de Resultados:} \\[5pt]"
            r"&\bullet \mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R}}}, \quad \mathbf{\operatorname{Ran}(f) = {\color{amgold}[-1, +\infty)}} \\[5pt]"
            r"&\bullet \mathbf{\text{Paridad: }} {\color{amteal}\text{Par }} (f(-x) = f(x)) \\[5pt]"
            r"&\bullet \mathbf{\text{Simetría: }} \text{Axial respecto al eje } {\color{amteal}y} \\[5pt]"
            r"&\bullet \mathbf{\text{Máx. Local: }} {\color{amgold}M\left(0, \frac{5}{4}\right)}, \quad \mathbf{\text{Mín. Abs: }} {\color{amteal}m_{1,2}\left(\pm\sqrt{3}, -1\right)} \\[5pt]"
            r"&\bullet \mathbf{\text{Cortes en } x: } {\color{amorange}\pm 1, \; \pm\sqrt{5}}, \quad \mathbf{\text{Corte en } y: } {\color{amorange}\left(0, \frac{5}{4}\right)} \\[5pt]"
            r"&\bullet \mathbf{\text{Decreciente: }} {\color{amred}(-\infty, -\sqrt{3}] \cup [0, \sqrt{3}]} \\[5pt]"
            r"&\bullet \mathbf{\text{Creciente: }} {\color{amgreen}[-\sqrt{3}, 0] \cup [\sqrt{3}, +\infty)} \quad {\color{amgreen}\blacksquare}"
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        box6 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.18, corner_radius=0.1)

        # Gráfico cartesiano de la función bicuadrática en forma de "W"
        axes, axes_labels = self.setup_axes(
            x_range=[-3.0, 3.0, 1],
            y_range=[-1.8, 2.5, 1],
            x_length=4.8,
            y_length=3.4,
            center=[3.25, -0.65, 0],
            include_numbers=True,
            numbers_font_size=16,
            labels_font_size=19
        )
        graph_title = Tex(
            r"Gráfica de ${\color{amteal}f(x)} = {\color{amteal}\frac{1}{4}x^4} - {\color{amred}\frac{3}{2}x^2} + {\color{amgold}\frac{5}{4}}$",
            font_size=20.5,
            color=WHITE
        ).move_to([3.25, 1.70, 0])

        # Curva bicuadrática
        quartic_curve = axes.plot(
            lambda x: 0.25 * x**4 - 1.5 * x**2 + 1.25,
            x_range=[-2.55, 2.55],
            color=THEME["curve"],
            stroke_width=2.5
        )
        curve_lbl = MathTex(r"y = f(x)", font_size=14.0, color=THEME["curve"]).move_to(axes.c2p(1.6, 1.6))

        # Máximo local M(0, 5/4) = (0, 1.25)
        dot_max = Dot(axes.c2p(0.0, 1.25), radius=0.075, color=THEME["highlight"])
        lbl_max = MathTex(r"M\left(0, \frac{5}{4}\right)", font_size=13.5, color=THEME["highlight"]).next_to(dot_max, UP + RIGHT, buff=0.07)

        # Mínimos absolutos en x = +-sqrt(3)
        sqrt3_val = np.sqrt(3)
        dot_min1 = Dot(axes.c2p(-sqrt3_val, -1.0), radius=0.075, color=THEME["secondary"])
        lbl_min1 = MathTex(r"m_1(-\sqrt{3}, -1)", font_size=12.5, color=THEME["secondary"]).next_to(dot_min1, DOWN, buff=0.08)

        dot_min2 = Dot(axes.c2p(sqrt3_val, -1.0), radius=0.075, color=THEME["secondary"])
        lbl_min2 = MathTex(r"m_2(\sqrt{3}, -1)", font_size=12.5, color=THEME["secondary"]).next_to(dot_min2, DOWN, buff=0.08)

        # Cortes con el eje x: x = +-1 y x = +-sqrt(5)
        sqrt5_val = np.sqrt(5)
        dot_r1 = Dot(axes.c2p(-sqrt5_val, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_r1 = MathTex(r"-\sqrt{5}", font_size=12.5, color=THEME["statement_text"]).next_to(dot_r1, UP + LEFT, buff=0.06)

        dot_r2 = Dot(axes.c2p(-1.0, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_r2 = MathTex(r"-1", font_size=12.5, color=THEME["statement_text"]).next_to(dot_r2, UP + RIGHT, buff=0.06)

        dot_r3 = Dot(axes.c2p(1.0, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_r3 = MathTex(r"1", font_size=12.5, color=THEME["statement_text"]).next_to(dot_r3, UP + LEFT, buff=0.06)

        dot_r4 = Dot(axes.c2p(sqrt5_val, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_r4 = MathTex(r"\sqrt{5}", font_size=12.5, color=THEME["statement_text"]).next_to(dot_r4, UP + RIGHT, buff=0.06)

        prog_anims = self.get_advance_progress_anims(5)

        self.play(
            FadeOut(self.active_math),
            FadeOut(self.active_just),
            FadeOut(self.active_box),
            FadeIn(left_summary),
            Create(box6),
            Create(axes),
            Write(axes_labels),
            Write(graph_title),
            *prog_anims,
            run_time=1.8
        )
        self.active_box = box6
        self.active_math = left_summary
        self.active_just = None

        self.play(
            Create(quartic_curve),
            Write(curve_lbl),
            FadeIn(dot_max),
            Write(lbl_max),
            FadeIn(dot_min1),
            Write(lbl_min1),
            FadeIn(dot_min2),
            Write(lbl_min2),
            FadeIn(dot_r1),
            Write(lbl_r1),
            FadeIn(dot_r2),
            Write(lbl_r2),
            FadeIn(dot_r3),
            Write(lbl_r3),
            FadeIn(dot_r4),
            Write(lbl_r4),
            run_time=2.2
        )
        self.wait(8.5)

        # Cierre institucional
        graph_group = VGroup(
            axes, axes_labels, graph_title,
            quartic_curve, curve_lbl,
            dot_max, lbl_max,
            dot_min1, lbl_min1,
            dot_min2, lbl_min2,
            dot_r1, lbl_r1,
            dot_r2, lbl_r2,
            dot_r3, lbl_r3,
            dot_r4, lbl_r4
        )
        self.play(
            FadeOut(graph_group),
            FadeOut(self.active_math),
            FadeOut(self.active_box),
            run_time=1.4
        )
        self.wait(1.0)
