"""
Ejercicio 1 - Tutorías y Preparación Quiz 4 (Jhoselyn)
Tema: Análisis Completo y Gráfica de Funciones:
      Parábola Cuadrática: f(x) = -1/2 x^2 + 3/2 x + 27/8.
      Dominio, concavidad, vértice, cortes coordenados, tabla de signos,
      monotonía, rango y trazado cartesiano riguroso.

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica en 6 pasos con ecuaciones de gran tamaño y legibilidad HD.
"""

from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME


class EjercicioJh_01(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Jhoselyn",
            exercise="Ejercicio 1",
            topic="Análisis y Gráfica de Función Cuadrática",
            font_size=18
        )

        # 2. Enunciado institucional permanente con fórmula prominente (y = 2.65)
        self.setup_statement(
            desc_text="Analice completamente y grafique la función polinómica:",
            math_tex=r"f(x) = -\frac{1}{2}x^2 + \frac{3}{2}x + \frac{27}{8}",
            desc_font_size=20.0,
            math_font_size=32.0,
            box_pos=np.array([0.0, 2.65, 0.0]),
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (6 pasos)
        self.setup_progress_bar([
            "1/6: Dominio y Concavidad",
            "2/6: Vértice y Extremo Absoluto",
            "3/6: Cortes con los Ejes Coordenados",
            "4/6: Factorización y Tabla de Signos",
            "5/6: Monotonía y Rango",
            "6/6: Gráfica Cartesiana y Verificación"
        ], label_font_size=14.5)

        # ==========================================================
        # PASO 1 (C2): Dominio y Concavidad
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Dominio y Concavidad Polinómica:} \\[6pt]"
            r"&\text{Al ser } f(x) \text{ una función polinómica cuadrática:} \\[5pt]"
            r"&\mathbf{\operatorname{Dom}(f) = \mathbb{R} = (-\infty, +\infty)} \\[8pt]"
            r"&\textbf{Identificación de Coeficientes:} \\[5pt]"
            r"&a = -\frac{1}{2}, \quad b = \frac{3}{2}, \quad c = \frac{27}{8} \\[7pt]"
            r"&\text{Como } a = -\frac{1}{2} < 0 \implies \text{Parábola cóncava hacia abajo } (\cap) \\[6pt]"
            r"&\implies \text{El vértice } V(x_v, y_v) \text{ es un } \mathbf{\text{Máximo Absoluto}}."
            r"\end{aligned}",
            font_size=23.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{1. Dominio y Concavidad:}\\[6pt]"
            r"$\bullet$ El dominio de toda función cuadrática es $\mathbb{R}$.\\[5pt]"
            r"$\bullet$ Coeficiente principal: $a = -\frac{1}{2} < 0$.\\[5pt]"
            r"$\bullet$ Las ramas de la parábola abren hacia abajo ($\cap$).\\[5pt]"
            r"$\bullet$ El vértice $V$ representa la cota superior global\\[2pt]"
            r"\hspace*{1.2em}(máximo absoluto de la función)."
            r"\end{minipage}",
            font_size=21.5,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=5.5)

        # ==========================================================
        # PASO 2 (C3): Vértice y Extremo Absoluto
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Coordenadas del Vértice } V(x_v, y_v): \\[6pt]"
            r"&x_v = -\frac{b}{2a} = -\frac{3/2}{2\left(-\frac{1}{2}\right)} = -\frac{3/2}{-1} = \mathbf{\frac{3}{2} = 1.5} \\[8pt]"
            r"&y_v = f\left(\frac{3}{2}\right) = -\frac{1}{2}\left(\frac{3}{2}\right)^2 + \frac{3}{2}\left(\frac{3}{2}\right) + \frac{27}{8} \\[7pt]"
            r"&y_v = -\frac{9}{8} + \frac{18}{8} + \frac{27}{8} = \frac{36}{8} = \mathbf{\frac{9}{2} = 4.5} \\[8pt]"
            r"&\mathbf{V = \left(\frac{3}{2}, \frac{9}{2}\right) = (1.5, 4.5)} \quad (\text{Máximo Absoluto})"
            r"\end{aligned}",
            font_size=23.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{2. Vértice y Extremo:}\\[6pt]"
            r"$\bullet$ Eje de simetría: $x_v = -\frac{b}{2a} = 1.5$.\\[5pt]"
            r"$\bullet$ Evaluando la abscisa en la función:\\[3pt]"
            r"\hspace*{1.2em}$y_v = f(1.5) = -\frac{9}{8} + \frac{18}{8} + \frac{27}{8} = \frac{9}{2} = 4.5$.\\[5pt]"
            r"$\bullet$ El vértice es el punto $V(1.5, 4.5)$.\\[5pt]"
            r"$\bullet$ Al ser cóncava ($\cap$), $y = 4.5$ es el máximo absoluto."
            r"\end{minipage}",
            font_size=21.5,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq2, just2, box_color=THEME["highlight"], advance_to_step=1, wait_time=5.5)

        # ==========================================================
        # PASO 3 (C1 / C4): Cortes con los Ejes Coordenados
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Intersecciones con los Ejes Coordenados:} \\[5pt]"
            r"&\bullet \textbf{Intercepto vertical } (x = 0): \\[3pt]"
            r"&\quad f(0) = \frac{27}{8} = 3.375 \implies \mathbf{P_y = \left(0, \frac{27}{8}\right)} \\[6pt]"
            r"&\bullet \textbf{Interceptos horizontales } (f(x) = 0): \\[3pt]"
            r"&\quad -\frac{1}{2}x^2 + \frac{3}{2}x + \frac{27}{8} = 0 \quad (\times -8) \\[5pt]"
            r"&\quad 4x^2 - 12x - 27 = 0 \iff (2x - 9)(2x + 3) = 0 \\[5pt]"
            r"&\quad \mathbf{x_1 = \frac{9}{2} = 4.5}, \qquad \mathbf{x_2 = -\frac{3}{2} = -1.5} \\[5pt]"
            r"&\quad \text{Puntos: } P_{x_1} = (4.5, 0), \quad P_{x_2} = (-1.5, 0)."
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{3. Puntos de Corte:}\\[6pt]"
            r"$\bullet$ Corte con el eje $y$ ($x = 0$): $f(0) = \frac{27}{8} = 3.375$.\\[5pt]"
            r"$\bullet$ Cortes con el eje $x$ ($f(x) = 0$):\\[3pt]"
            r"\hspace*{1.2em}Multiplicando por $-8$: $4x^2 - 12x - 27 = 0$.\\[5pt]"
            r"$\bullet$ Factorización directa: $(2x - 9)(2x + 3) = 0$.\\[5pt]"
            r"$\bullet$ Intersecciones: $P_{x_1} = (4.5, 0)$ y $P_{x_2} = (-1.5, 0)$."
            r"\end{minipage}",
            font_size=21.5,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=5.5)

        # ==========================================================
        # PASO 4: Factorización y Tabla de Signos
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Factorización Canónica y Signos:} \\[3pt]"
            r"&f(x) = -\frac{1}{2}\left(x + \frac{3}{2}\right)\left(x - \frac{9}{2}\right) \\[3pt]"
            r"&\text{Intervalos con raíces } \{-1.5, 4.5\}: \\[3pt]"
            r"&\bullet \left(-\infty, -\frac{3}{2}\right): \; (-) \cdot (-) \cdot (-) = \mathbf{(-)} \implies f(x) < 0 \\[3pt]"
            r"&\bullet \left(-\frac{3}{2}, \frac{9}{2}\right): \; (-) \cdot (+) \cdot (-) = \mathbf{(+)} \implies f(x) > 0 \\[3pt]"
            r"&\bullet \left(\frac{9}{2}, +\infty\right): \; (-) \cdot (+) \cdot (+) = \mathbf{(-)} \implies f(x) < 0 \\[3pt]"
            r"&\mathbf{\text{Positiva en: } \left(-\frac{3}{2}, \frac{9}{2}\right)} \\[3pt]"
            r"&\mathbf{\text{Negativa en: } \left(-\infty, -\frac{3}{2}\right) \cup \left(\frac{9}{2}, \infty\right)}."
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{4. Intervalos de Signo:}\\[6pt]"
            r"$\bullet$ Las raíces dividen la recta real en 3 intervalos.\\[5pt]"
            r"$\bullet$ $(-\infty, -1.5)$: $(-)\cdot(-)\cdot(-) = (-) \implies f(x) < 0$.\\[5pt]"
            r"$\bullet$ $(-1.5, 4.5)$: $(-)\cdot(+)\cdot(-) = (+) \implies f(x) > 0$.\\[5pt]"
            r"$\bullet$ $(4.5, +\infty)$: $(-)\cdot(+)\cdot(+) = (-) \implies f(x) < 0$."
            r"\end{minipage}",
            font_size=21.5,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=5.5)

        # ==========================================================
        # PASO 5: Monotonía y Rango
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Intervalos de Monotonía y Rango:} \\[6pt]"
            r"&\bullet \textbf{Monotonía (Crecimiento / Decrecimiento):} \\[4pt]"
            r"&\quad \mathbf{f \text{ es creciente en } \left(-\infty, \frac{3}{2}\right] = (-\infty, 1.5]} \\[5pt]"
            r"&\quad \mathbf{f \text{ es decreciente en } \left[\frac{3}{2}, +\infty\right) = [1.5, +\infty)} \\[7pt]"
            r"&\bullet \textbf{Rango (Recorrido de la Función):} \\[4pt]"
            r"&\quad \text{Como } y_v = 4.5 \text{ es el máximo absoluto de } f: \\[4pt]"
            r"&\quad \mathbf{\operatorname{Ran}(f) = \left(-\infty, \frac{9}{2}\right] = (-\infty, 4.5]}."
            r"\end{aligned}",
            font_size=23.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{5. Monotonía y Rango:}\\[6pt]"
            r"$\bullet$ La curva asciende desde $-\infty$ hasta alcanzar\\[2pt]"
            r"\hspace*{1.2em}la cima en el vértice $x = 1.5$ (crecimiento).\\[5pt]"
            r"$\bullet$ A partir de $x = 1.5$, la función desciende\\[2pt]"
            r"\hspace*{1.2em}hacia $-\infty$ (decrecimiento).\\[5pt]"
            r"$\bullet$ Proyección vertical sobre el eje $y$ hasta $y = 4.5$:\\[3pt]"
            r"\hspace*{1.2em}$\operatorname{Ran}(f) = \left(-\infty, \frac{9}{2}\right] = (-\infty, 4.5]$."
            r"\end{minipage}",
            font_size=21.5,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=5.5)

        # ==========================================================
        # PASO 6 (C5): Gráfica Cartesiana y Verificación Visual
        # ==========================================================
        left_summary = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Resumen Formal de Resultados:} \\[5pt]"
            r"&\bullet \mathbf{\operatorname{Dom}(f) = \mathbb{R}}, \quad \mathbf{\operatorname{Ran}(f) = \left(-\infty, \frac{9}{2}\right]} \\[5pt]"
            r"&\bullet \mathbf{\text{Vértice: }} V\left(\frac{3}{2}, \frac{9}{2}\right) = (1.5, 4.5) \quad (\text{Máx.}) \\[5pt]"
            r"&\bullet \mathbf{\text{Eje de Simetría: }} x = 1.5 \\[5pt]"
            r"&\bullet \mathbf{\text{Cortes en } x: } \left(-\frac{3}{2}, 0\right) \text{ y } \left(\frac{9}{2}, 0\right) \\[5pt]"
            r"&\bullet \mathbf{\text{Corte en } y: } \left(0, \frac{27}{8}\right) = (0, 3.375) \\[5pt]"
            r"&\bullet \mathbf{\text{Positiva en: }} \left(-\frac{3}{2}, \frac{9}{2}\right) \quad \blacksquare"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        box6 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.18, corner_radius=0.1)

        # Gráfico cartesiano de la función cuadrática
        axes, axes_labels = self.setup_axes(
            x_range=[-3.0, 6.0, 1],
            y_range=[-3.0, 5.2, 1],
            x_length=4.5,
            y_length=3.3,
            center=[3.15, -0.75, 0],
            include_numbers=True,
            numbers_font_size=17,
            labels_font_size=20
        )
        graph_title = Tex(
            r"Gráfica de $f(x) = -\frac{1}{2}x^2 + \frac{3}{2}x + \frac{27}{8}$",
            font_size=23.0,
            color=WHITE
        ).move_to([3.15, 1.65, 0])

        # Parábola
        parabola = axes.plot(
            lambda x: -0.5 * x**2 + 1.5 * x + 27/8,
            x_range=[-2.4, 5.4],
            color=THEME["curve"],
            stroke_width=2.5
        )
        parabola_lbl = MathTex(r"y = f(x)", font_size=15.0, color=THEME["curve"]).move_to(axes.c2p(5.2, -1.2))

        # Eje de simetría punteado (x = 1.5)
        sym_line = DashedVMobject(
            Line(axes.c2p(1.5, -2.8), axes.c2p(1.5, 4.5), color=THEME["statement_box"], stroke_width=1.6),
            num_dashes=14
        )
        lbl_sym = MathTex(r"x = 1.5", font_size=15.0, color="#e57373").next_to(axes.c2p(1.5, -2.8), DOWN, buff=0.10)

        # Vértice
        dot_v = Dot(axes.c2p(1.5, 4.5), radius=0.08, color=THEME["highlight"])
        lbl_v = MathTex(r"V(1.5, 4.5)", font_size=16.0, color=THEME["highlight"]).next_to(dot_v, UP, buff=0.10)

        # Cortes en eje x: (-1.5, 0) y (4.5, 0) ubicados arriba de los puntos con máximo contraste
        dot_x1 = Dot(axes.c2p(-1.5, 0.0), radius=0.07, color=THEME["secondary"])
        lbl_x1 = MathTex(r"(-1.5, 0)", font_size=14.5, color=THEME["statement_text"]).next_to(dot_x1, UP + LEFT, buff=0.08)

        dot_x2 = Dot(axes.c2p(4.5, 0.0), radius=0.07, color=THEME["secondary"])
        lbl_x2 = MathTex(r"(4.5, 0)", font_size=14.5, color=THEME["statement_text"]).next_to(dot_x2, UP + RIGHT, buff=0.08)

        # Corte en eje y: (0, 3.375)
        dot_y = Dot(axes.c2p(0.0, 3.375), radius=0.07, color=THEME["curve"])
        lbl_y = MathTex(r"P_y(0, 3.38)", font_size=14.5, color=THEME["curve"]).next_to(dot_y, LEFT, buff=0.10)

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
            Create(sym_line),
            Write(lbl_sym),
            Create(parabola),
            Write(parabola_lbl),
            FadeIn(dot_v),
            Write(lbl_v),
            FadeIn(dot_x1),
            Write(lbl_x1),
            FadeIn(dot_x2),
            Write(lbl_x2),
            FadeIn(dot_y),
            Write(lbl_y),
            run_time=2.2
        )
        self.wait(9.2)

        # Cierre institucional
        graph_group = VGroup(
            axes, axes_labels, graph_title,
            sym_line, lbl_sym,
            parabola, parabola_lbl,
            dot_v, lbl_v,
            dot_x1, lbl_x1,
            dot_x2, lbl_x2,
            dot_y, lbl_y
        )
        self.play(
            FadeOut(graph_group),
            FadeOut(self.active_math),
            FadeOut(self.active_box),
            run_time=1.4
        )
        self.wait(1.0)
