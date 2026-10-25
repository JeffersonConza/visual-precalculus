"""
Ejercicio 2 - Tutorías y Preparación Quiz 4 (Jhoselyn)
Tema: Análisis Completo y Gráfica de Funciones:
      Polinomio Cúbico Impar: f(x) = 1/2 x^3 - 3/2 x.
      Dominio, paridad, simetría central, cortes coordenados, tabla de signos,
      extremos locales, monotonía, rango y trazado cartesiano riguroso.

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


class EjercicioJh_02(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Jhoselyn",
            exercise="Ejercicio 2",
            topic="Función Cúbica Impar",
            font_size=16
        )

        # 2. Enunciado institucional permanente con fórmula prominente (y = 2.65)
        self.setup_statement(
            desc_text="Analice completamente y grafique la función polinómica cúbica:",
            math_tex=r"{\color{amteal}f(x)} = {\color{amteal}\frac{1}{2}}x^3 - {\color{amred}\frac{3}{2}}x",
            desc_font_size=19.0,
            math_font_size=30.0,
            box_pos=np.array([0.0, 2.65, 0.0]),
            read_time=3.8
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
            r"&\text{Al ser } {\color{amteal}f(x)} \text{ una función polinómica de grado 3:} \\[5pt]"
            r"&\mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R}} = {\color{amgreen}(-\infty, +\infty)}} \\[8pt]"
            r"&\textbf{Evaluación formal de paridad } f(-x): \\[5pt]"
            r"&f(-x) = \frac{1}{2}(-x)^3 - \frac{3}{2}(-x) = -\frac{1}{2}x^3 + \frac{3}{2}x = -f(x) \\[7pt]"
            r"&\implies {\color{amteal}f(-x) = -f(x)} \implies \mathbf{\text{Función IMPAR}} \\[6pt]"
            r"&\implies \text{Presenta } \mathbf{\text{Simetría Central respecto al origen } (0, 0)}."
            r"\end{aligned}",
            font_size=22.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{1. Dominio y Paridad:}\\[6pt]"
            r"$\bullet$ Toda función polinómica cúbica tiene ${\color{amgold}\operatorname{Dom}(f) = \mathbb{R}}$.\\[5pt]"
            r"$\bullet$ Evaluamos $f(-x)$ sustituyendo $-x$ en cada potencia:\\[3pt]"
            r"\hspace*{1.2em}$f(-x) = \frac{1}{2}(-x)^3 - \frac{3}{2}(-x) = -f(x)$.\\[5pt]"
            r"$\bullet$ Concluimos formalmente: ${\color{amteal}f \text{ es IMPAR}}$.\\[5pt]"
            r"$\bullet$ Presenta simetría central respecto al origen ${\color{amteal}(0, 0)}$.\\[2pt]"
            r"\end{minipage}",
            font_size=21.5,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=5.2)

        # ==========================================================
        # PASO 2 (C1 / C4): Cortes con los Ejes Coordenados
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Intersecciones con los Ejes Coordenados:} \\[5pt]"
            r"&\bullet \textbf{Intercepto vertical } (x = 0): \\[3pt]"
            r"&\quad f(0) = \frac{1}{2}(0)^3 - \frac{3}{2}(0) = 0 \implies \mathbf{{\color{amteal}P_0 = (0, 0)}} \\[6pt]"
            r"&\bullet \textbf{Interceptos horizontales } (f(x) = 0): \\[3pt]"
            r"&\quad \frac{1}{2}x^3 - \frac{3}{2}x = 0 \iff \frac{1}{2}x(x^2 - 3) = 0 \\[5pt]"
            r"&\quad x = 0 \quad \lor \quad x^2 - 3 = 0 \implies x = \pm\sqrt{3} \\[6pt]"
            r"&\quad \mathbf{{\color{amorange}x_1 = 0}}, \quad \mathbf{{\color{amorange}x_2 = \sqrt{3} \approx 1.73}}, \quad \mathbf{{\color{amorange}x_3 = -\sqrt{3} \approx -1.73}} \\[5pt]"
            r"&\quad \text{Puntos: } {\color{amorange}P_0(0,0)}, \; {\color{amorange}P_{x_1}(\sqrt{3}, 0)}, \; {\color{amorange}P_{x_2}(-\sqrt{3}, 0)}."
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{2. Cortes Coordenados:}\\[6pt]"
            r"$\bullet$ Corte con el eje $y$ ($x = 0$): ${\color{amteal}f(0) = 0 \implies P_0(0, 0)}$.\\[5pt]"
            r"$\bullet$ Cortes con el eje $x$ ($f(x) = 0$):\\[3pt]"
            r"\hspace*{1.2em}Extraemos factor común: $\frac{1}{2}x(x^2 - 3) = 0$.\\[5pt]"
            r"$\bullet$ Ceros reales: ${\color{amorange}x = 0}$ y ${\color{amorange}x = \pm\sqrt{3} \approx \pm 1.73}$.\\[5pt]"
            r"$\bullet$ Tres intersecciones: ${\color{amorange}P_0(0, 0)}$, ${\color{amorange}P_{x_1}(1.73, 0)}$ y ${\color{amorange}P_{x_2}(-1.73, 0)}$."
            r"\end{minipage}",
            font_size=21.5,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq2, just2, box_color=THEME["highlight"], advance_to_step=1, wait_time=5.2)

        # ==========================================================
        # PASO 3: Factorización y Tabla de Signos
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Factorización y Tabla de Signos:} \\[3pt]"
            r"&{\color{amteal}f(x)} = \frac{1}{2}x\left(x + \sqrt{3}\right)\left(x - \sqrt{3}\right) \\[3pt]"
            r"&\text{Intervalos definidos por las raíces } \{{\color{amorange}-\sqrt{3}, 0, \sqrt{3}}\}: \\[3pt]"
            r"&\bullet \left(-\infty, -\sqrt{3}\right): \; (-) \cdot (-) \cdot (-) = \mathbf{{\color{amred}(-)}} \implies {\color{amred}f(x) < 0} \\[3pt]"
            r"&\bullet \left(-\sqrt{3}, 0\right): \; (-) \cdot (+) \cdot (-) = \mathbf{{\color{amgreen}(+)}} \implies {\color{amgreen}f(x) > 0} \\[3pt]"
            r"&\bullet \left(0, \sqrt{3}\right): \; (+) \cdot (+) \cdot (-) = \mathbf{{\color{amred}(-)}} \implies {\color{amred}f(x) < 0} \\[3pt]"
            r"&\bullet \left(\sqrt{3}, +\infty\right): \; (+) \cdot (+) \cdot (+) = \mathbf{{\color{amgreen}(+)}} \implies {\color{amgreen}f(x) > 0} \\[3pt]"
            r"&\mathbf{\text{Positiva en: } {\color{amgreen}\left(-\sqrt{3}, 0\right) \cup \left(\sqrt{3}, +\infty\right)}} \\[3pt]"
            r"&\mathbf{\text{Negativa en: } {\color{amred}\left(-\infty, -\sqrt{3}\right) \cup \left(0, \sqrt{3}\right)}}."
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{3. Intervalos de Signo:}\\[6pt]"
            r"$\bullet$ Las 3 raíces dividen la recta real en 4 intervalos.\\[5pt]"
            r"$\bullet$ $(-\infty, -\sqrt{3})$: $(-)\cdot(-)\cdot(-) = {\color{amred}(-)} \implies {\color{amred}f(x) < 0}$.\\[5pt]"
            r"$\bullet$ $(-\sqrt{3}, 0)$: $(-)\cdot(+)\cdot(-) = {\color{amgreen}(+)} \implies {\color{amgreen}f(x) > 0}$.\\[5pt]"
            r"$\bullet$ $(0, \sqrt{3})$: $(+)\cdot(+)\cdot(-) = {\color{amred}(-)} \implies {\color{amred}f(x) < 0}$.\\[5pt]"
            r"$\bullet$ $(\sqrt{3}, +\infty)$: $(+)\cdot(+)\cdot(+) = {\color{amgreen}(+)} \implies {\color{amgreen}f(x) > 0}$."
            r"\end{minipage}",
            font_size=21.5,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=5.2)

        # ==========================================================
        # PASO 4 (C3): Extremos Locales y Puntos Notables
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Puntos Críticos y Extremos Locales:} \\[6pt]"
            r"&\bullet \textbf{Máximo Local en } {\color{amgold}M(-1, 1)}: \\[3pt]"
            r"&\quad f(-1) = \frac{1}{2}(-1)^3 - \frac{3}{2}(-1) = -\frac{1}{2} + \frac{3}{2} = \mathbf{{\color{amgold}1}} \\[6pt]"
            r"&\bullet \textbf{Mínimo Local en } {\color{amteal}m(1, -1)}: \\[3pt]"
            r"&\quad f(1) = \frac{1}{2}(1)^3 - \frac{3}{2}(1) = \frac{1}{2} - \frac{3}{2} = \mathbf{{\color{amteal}-1}} \\[6pt]"
            r"&\bullet \textbf{Punto de Inflexión (Centro de Simetría):} \\[3pt]"
            r"&\quad \text{En } {\color{amgold}I(0, 0)} \text{ la curva cambia su curvatura} \\[3pt]"
            r"&\quad \text{de cóncava }(\cap)\text{ en } (-\infty, 0) \text{ a convexa }(\cup)\text{ en } (0, +\infty)."
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{4. Extremos y Puntos Notables:}\\[6pt]"
            r"$\bullet$ Máximo local: la curva sube hasta ${\color{amgold}M(-1, 1)}$.\\[5pt]"
            r"$\bullet$ Mínimo local: la curva baja hasta ${\color{amteal}m(1, -1)}$.\\[5pt]"
            r"$\bullet$ Simetría de extremos: $f(-1) = 1 = -f(1)$.\\[5pt]"
            r"$\bullet$ En el origen ${\color{amgold}I(0, 0)}$ ocurre la inflexión:\\[2pt]"
            r"\hspace*{1.2em}la curva transiciona de cóncava ($\cap$) a convexa ($\cup$)."
            r"\end{minipage}",
            font_size=21.5,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=5.2)

        # ==========================================================
        # PASO 5: Monotonía y Rango
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Intervalos de Monotonía y Rango:} \\[6pt]"
            r"&\bullet \textbf{Monotonía (Crecimiento / Decrecimiento):} \\[4pt]"
            r"&\quad \mathbf{{\color{amgreen}f \text{ es creciente en } (-\infty, -1] \cup [1, +\infty)}} \\[5pt]"
            r"&\quad \mathbf{{\color{amred}f \text{ es decreciente en } [-1, 1]}} \\[7pt]"
            r"&\bullet \textbf{Rango (Recorrido de la Función):} \\[4pt]"
            r"&\quad \lim_{x \to -\infty} f(x) = -\infty, \quad \lim_{x \to +\infty} f(x) = +\infty \\[4pt]"
            r"&\quad \mathbf{\operatorname{Ran}(f) = {\color{amgold}\mathbb{R} = (-\infty, +\infty)}}."
            r"\end{aligned}",
            font_size=22.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{5. Monotonía y Rango:}\\[6pt]"
            r"$\bullet$ Creciente en ${\color{amgreen}(-\infty, -1] \cup [1, +\infty)}$.\\[5pt]"
            r"$\bullet$ Decreciente en el tramo central ${\color{amred}[-1, 1]}$.\\[5pt]"
            r"$\bullet$ Las ramas divergen hacia los infinitos:\\[3pt]"
            r"\hspace*{1.2em}$\lim_{x \to -\infty} f(x) = -\infty, \quad \lim_{x \to +\infty} f(x) = +\infty$.\\[5pt]"
            r"$\bullet$ Proyección vertical cubre toda la recta: ${\color{amgold}\operatorname{Ran}(f) = \mathbb{R}}$."
            r"\end{minipage}",
            font_size=21.5,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=5.2)

        # ==========================================================
        # PASO 6 (C5): Gráfica Cartesiana y Verificación Visual
        # ==========================================================
        left_summary = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Resumen Formal de Resultados:} \\[5pt]"
            r"&\bullet \mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R}}}, \quad \mathbf{\operatorname{Ran}(f) = {\color{amgold}\mathbb{R}}} \\[5pt]"
            r"&\bullet \mathbf{\text{Paridad: }} {\color{amteal}\text{Impar }} (f(-x) = -f(x)) \\[5pt]"
            r"&\bullet \mathbf{\text{Simetría: }} \text{Central respecto al origen } {\color{amteal}(0, 0)} \\[5pt]"
            r"&\bullet \mathbf{\text{Máx. Local: }} {\color{amgold}M(-1, 1)}, \quad \mathbf{\text{Mín. Local: }} {\color{amteal}m(1, -1)} \\[5pt]"
            r"&\bullet \mathbf{\text{Cortes en } x: } {\color{amorange}(-\sqrt{3}, 0), \; (0, 0), \; (\sqrt{3}, 0)} \\[5pt]"
            r"&\bullet \mathbf{\text{Creciente: }} {\color{amgreen}(-\infty, -1] \cup [1, +\infty)} \\[5pt]"
            r"&\bullet \mathbf{\text{Decreciente: }} {\color{amred}[-1, 1]} \quad {\color{amgreen}\blacksquare}"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        box6 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.18, corner_radius=0.1)

        # Gráfico cartesiano de la función cúbica
        axes, axes_labels = self.setup_axes(
            x_range=[-2.6, 2.6, 1],
            y_range=[-2.2, 2.2, 1],
            x_length=4.6,
            y_length=3.4,
            center=[3.25, -0.65, 0],
            include_numbers=True,
            numbers_font_size=16,
            labels_font_size=19
        )
        graph_title = Tex(
            r"Gráfica de ${\color{amteal}f(x)} = {\color{amteal}\frac{1}{2}x^3} - {\color{amred}\frac{3}{2}x}$",
            font_size=21.0,
            color=WHITE
        ).move_to([3.25, 1.70, 0])

        # Curva cúbica
        cubic_curve = axes.plot(
            lambda x: 0.5 * x**3 - 1.5 * x,
            x_range=[-2.2, 2.2],
            color=THEME["curve"],
            stroke_width=2.5
        )
        curve_lbl = MathTex(r"y = f(x)", font_size=14.0, color=THEME["curve"]).move_to(axes.c2p(1.4, 1.65))

        # Máximo local M(-1, 1)
        dot_max = Dot(axes.c2p(-1.0, 1.0), radius=0.075, color=THEME["highlight"])
        lbl_max = MathTex(r"M(-1, 1)", font_size=14.5, color=THEME["highlight"]).next_to(dot_max, UP, buff=0.08)

        # Mínimo local m(1, -1)
        dot_min = Dot(axes.c2p(1.0, -1.0), radius=0.075, color=THEME["secondary"])
        lbl_min = MathTex(r"m(1, -1)", font_size=14.5, color=THEME["secondary"]).next_to(dot_min, DOWN, buff=0.08)

        # Raíces: (-sqrt(3), 0), (0, 0), (sqrt(3), 0)
        sqrt3_val = np.sqrt(3)
        dot_r1 = Dot(axes.c2p(-sqrt3_val, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_r1 = MathTex(r"-\sqrt{3}", font_size=13.5, color=THEME["statement_text"]).next_to(dot_r1, UP + LEFT, buff=0.08)

        dot_r0 = Dot(axes.c2p(0.0, 0.0), radius=0.065, color=THEME["header_color"])
        lbl_r0 = MathTex(r"(0, 0)", font_size=13.5, color=THEME["header_color"]).next_to(dot_r0, UP + RIGHT, buff=0.07)

        dot_r2 = Dot(axes.c2p(sqrt3_val, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_r2 = MathTex(r"\sqrt{3}", font_size=13.5, color=THEME["statement_text"]).next_to(dot_r2, UP + RIGHT, buff=0.06)

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
            Create(cubic_curve),
            Write(curve_lbl),
            FadeIn(dot_max),
            Write(lbl_max),
            FadeIn(dot_min),
            Write(lbl_min),
            FadeIn(dot_r1),
            Write(lbl_r1),
            FadeIn(dot_r0),
            Write(lbl_r0),
            FadeIn(dot_r2),
            Write(lbl_r2),
            run_time=2.2
        )
        self.wait(8.5)

        # Cierre institucional
        graph_group = VGroup(
            axes, axes_labels, graph_title,
            cubic_curve, curve_lbl,
            dot_max, lbl_max,
            dot_min, lbl_min,
            dot_r1, lbl_r1,
            dot_r0, lbl_r0,
            dot_r2, lbl_r2
        )
        self.play(
            FadeOut(graph_group),
            FadeOut(self.active_math),
            FadeOut(self.active_box),
            run_time=1.4
        )
        self.wait(1.0)
