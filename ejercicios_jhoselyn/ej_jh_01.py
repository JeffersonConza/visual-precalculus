"""
Ejercicio 1 - Tutorías y Preparación Quiz 4 (Jhoselyn)
Tema: Análisis Completo y Gráfica de Funciones:
      Parábola Cuadrática: f(x) = -1/2 x^2 + 3/2 x + 27/8.
      Dominio, concavidad, vértice, forma canónica, cortes coordenados,
      tabla horizontal de signos por factores, monotonía, rango,
      cuadro horizontal de variación (estilo Vista.webp) y trazado cartesiano riguroso.

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica en 8 pasos con ecuaciones legibles HD.
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


class EjercicioJh_01(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Jhoselyn",
            exercise="Ejercicio 1",
            topic="Análisis y Gráfica de Función Cuadrática",
            font_size=17.0
        )

        # 2. Enunciado institucional permanente con fórmula prominente (y = 2.65)
        self.setup_statement(
            desc_text="Analice completamente y grafique la función polinómica:",
            math_tex=r"{\color{amteal}f(x)} = {\color{amred}-\frac{1}{2}}x^2 + {\color{amteal}\frac{3}{2}}x + {\color{amgold}\frac{27}{8}}",
            desc_font_size=19.0,
            math_font_size=31.0,
            box_pos=np.array([0.0, 2.65, 0.0]),
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (8 pasos unificados)
        self.setup_progress_bar([
            "1/8: Dominio y Concavidad",
            "2/8: Vértice y Eje de Simetría",
            "3/8: Forma Canónica",
            "4/8: Cortes con los Ejes",
            "5/8: Tabla de Signos",
            "6/8: Monotonía y Rango",
            "7/8: Cuadro de Variación",
            "8/8: Gráfica Cartesiana y Verificación"
        ], dot_spacing=0.82, label_font_size=14.0)

        # ==========================================================
        # PASO 1: Dominio y Concavidad Polinómica
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Dominio y Concavidad Polinómica:} \\[6pt]"
            r"&\text{Al ser } {\color{amteal}f(x)} \text{ un polinomio cuadrático en todo } \mathbb{R}: \\[5pt]"
            r"&\mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R}} = {\color{amgreen}(-\infty, +\infty)}} \\[8pt]"
            r"&\textbf{Identificación de Coeficientes:} \\[5pt]"
            r"&{\color{amred}a = -\frac{1}{2}}, \quad {\color{amteal}b = \frac{3}{2}}, \quad {\color{amgold}c = \frac{27}{8}} \\[7pt]"
            r"&\text{Como } {\color{amred}a = -\frac{1}{2} < 0} \implies \text{Parábola cóncava hacia abajo } (\cap) \\[6pt]"
            r"&\implies \text{El vértice } {\color{amgold}V} \text{ constituye un } \mathbf{\text{Máximo Absoluto}}."
            r"\end{aligned}",
            font_size=22.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{1. Dominio y Concavidad:}\\[6pt]"
            r"$\bullet$ El dominio de toda función polinómica es ${\color{amgold}\mathbb{R}}$.\\[5pt]"
            r"$\bullet$ Coeficiente principal: ${\color{amred}a = -\frac{1}{2} < 0}$.\\[5pt]"
            r"$\bullet$ La concavidad negativa determina apertura hacia abajo ($\cap$).\\[5pt]"
            r"$\bullet$ El vértice representará la cota superior global\\[2pt]"
            r"\hspace*{1.2em}(máximo absoluto de la parábola)."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=3.2)

        # ==========================================================
        # PASO 2: Vértice y Eje de Simetría
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Coordenadas del Vértice } {\color{amgold}V(x_v, y_v)}: \\[6pt]"
            r"&{\color{amteal}x_v} = -\frac{b}{2a} = -\frac{3/2}{2\left(-\frac{1}{2}\right)} = \mathbf{{\color{amteal}\frac{3}{2} = 1.5}} \\[7pt]"
            r"&{\color{amgold}y_v} = f\left(\frac{3}{2}\right) = -\frac{1}{2}\left(\frac{3}{2}\right)^2 + \frac{3}{2}\left(\frac{3}{2}\right) + \frac{27}{8} \\[6pt]"
            r"&{\color{amgold}y_v} = -\frac{9}{8} + \frac{18}{8} + \frac{27}{8} = \frac{36}{8} = \mathbf{{\color{amgold}\frac{9}{2} = 4.5}} \\[7pt]"
            r"&\mathbf{\text{Vértice: }} \mathbf{{\color{amgold}V\left(\frac{3}{2}, \frac{9}{2}\right) = (1.5, 4.5)}} \quad (\text{Máximo Absoluto}) \\[6pt]"
            r"&\mathbf{\text{Eje de Simetría: }} \mathbf{{\color{amteal}x = 1.5}} \text{ (recta vertical axial)}."
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{2. Vértice y Eje de Simetría:}\\[6pt]"
            r"$\bullet$ La abscisa del vértice es el centro: ${\color{amteal}x_v = -\frac{b}{2a} = 1.5}$.\\[5pt]"
            r"$\bullet$ Evaluación directa del valor funcional:\\[3pt]"
            r"\hspace*{1.2em}$y_v = f(1.5) = -\frac{9}{8} + \frac{18}{8} + \frac{27}{8} = {\color{amgold}\frac{9}{2} = 4.5}$.\\[5pt]"
            r"$\bullet$ El punto culminante es ${\color{amgold}V(1.5, 4.5)}$.\\[5pt]"
            r"$\bullet$ La recta ${\color{amteal}x = 1.5}$ actúa como eje de simetría bilateral."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq2, just2, box_color=THEME["highlight"], advance_to_step=1, wait_time=3.2)

        # ==========================================================
        # PASO 3: Forma Canónica y Transformaciones
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Forma Canónica } a(x-h)^2 + k: \\[6pt]"
            r"&f(x) = -\frac{1}{2}\left(x^2 - 3x\right) + \frac{27}{8} \\[5pt]"
            r"&f(x) = -\frac{1}{2}\left[\left(x - \frac{3}{2}\right)^2 - \frac{9}{4}\right] + \frac{27}{8} \\[5pt]"
            r"&f(x) = -\frac{1}{2}\left(x - \frac{3}{2}\right)^2 + \frac{9}{8} + \frac{27}{8} \\[6pt]"
            r"&\mathbf{{\color{amteal}f(x) = -\frac{1}{2}\left(x - 1.5\right)^2 + 4.5}} \\[7pt]"
            r"&\bullet \mathbf{\text{Parámetros: }} {\color{amred}a = -0.5}, \; {\color{amteal}h = 1.5}, \; {\color{amgold}k = 4.5} \implies {\color{amgold}V(1.5, 4.5)} \\[4pt]"
            r"&\bullet \mathbf{\text{Transformaciones: }} \text{Desplaza } 1.5 \to, \text{ refl. eje } X, \text{ sube } 4.5."
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{3. Forma Canónica (Guía 2.5):}\\[6pt]"
            r"$\bullet$ Completación de cuadrados según Guía de Estudio 2.5.\\[5pt]"
            r"$\bullet$ Expresa la parábola como $a(x - h)^2 + k$.\\[5pt]"
            r"$\bullet$ Confirma analíticamente el vértice ${\color{amgold}(h, k) = (1.5, 4.5)}$.\\[5pt]"
            r"$\bullet$ Describe las transformaciones de la curva base $y = x^2$:\\[2pt]"
            r"\hspace*{1.2em}traslación horizontal, contracción, reflexión y alza vertical."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=3.2)

        # ==========================================================
        # PASO 4: Cortes con los Ejes Coordenados
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Intersecciones con los Ejes Coordenados:} \\[5pt]"
            r"&\bullet \textbf{Intercepto vertical } (x = 0): \\[3pt]"
            r"&\quad f(0) = \frac{27}{8} = 3.375 \implies \mathbf{{\color{amteal}P_y = \left(0, \frac{27}{8}\right) = (0, 3.38)}} \\[6pt]"
            r"&\bullet \textbf{Interceptos horizontales } (f(x) = 0): \\[3pt]"
            r"&\quad -\frac{1}{2}x^2 + \frac{3}{2}x + \frac{27}{8} = 0 \quad (\times -8) \\[5pt]"
            r"&\quad 4x^2 - 12x - 27 = 0 \iff (2x - 9)(2x + 3) = 0 \\[5pt]"
            r"&\quad \mathbf{{\color{amorange}x_1 = \frac{9}{2} = 4.5}}, \qquad \mathbf{{\color{amorange}x_2 = -\frac{3}{2} = -1.5}} \\[5pt]"
            r"&\quad \text{Puntos: } {\color{amorange}P_{x_1} = (4.5, 0)}, \quad {\color{amorange}P_{x_2} = (-1.5, 0)}."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{4. Cortes Coordenados:}\\[6pt]"
            r"$\bullet$ Eje $y$: Evaluamos $x = 0 \implies {\color{amteal}P_y(0, 3.38)}$.\\[5pt]"
            r"$\bullet$ Eje $x$: Resolvemos $f(x) = 0$.\\[5pt]"
            r"$\bullet$ Multiplicamos por $-8$ para enteros: $4x^2 - 12x - 27 = 0$.\\[5pt]"
            r"$\bullet$ Factorización directa: $(2x - 9)(2x + 3) = 0$.\\[5pt]"
            r"$\bullet$ Raíces reales: ${\color{amorange}P_{x_1}(4.5, 0)}$ y ${\color{amorange}P_{x_2}(-1.5, 0)}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=3.2)

        # ==========================================================
        # PASO 5: Factorización y Tabla Horizontal de Signos
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Factorización y Tabla Horizontal de Signos:} \\[4pt]"
            r"&{\color{amteal}f(x)} = -\frac{1}{2}\left(x + \frac{3}{2}\right)\left(x - \frac{9}{2}\right) \\[5pt]"
            r"&\begin{array}{c|c|c|c}"
            r"\text{Intervalo} & (-\infty, -1.5) & (-1.5, 4.5) & (4.5, +\infty) \\ \hline "
            r"x + 3/2 & - & + & + \\ \hline "
            r"x - 9/2 & - & - & + \\ \hline "
            r"-1/2 & - & - & - \\ \hline "
            r"f(x) & {\color{amred}\mathbf{-}} & {\color{amgreen}\mathbf{+}} & {\color{amred}\mathbf{-}}"
            r"\end{array} \\[6pt]"
            r"&\bullet \mathbf{\text{Positiva en: }} {\color{amgreen}\left(-\frac{3}{2}, \frac{9}{2}\right) = (-1.5, 4.5)} \quad (f(x) > 0). \\[3pt]"
            r"&\bullet \mathbf{\text{Negativa en: }} {\color{amred}\left(-\infty, -1.5\right) \cup \left(4.5, +\infty\right)} \quad (f(x) < 0)."
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{5. Tabla de Signos (Guía Pág. 7):}\\[6pt]"
            r"$\bullet$ Tabla horizontal idéntica a la guía oficial de Quiz 4.\\[5pt]"
            r"$\bullet$ El factor constante negativo ($-1/2$) invierte los signos.\\[5pt]"
            r"$\bullet$ Positividad en $(-1.5, 4.5)$: La curva se sitúa\\[2pt]"
            r"\hspace*{1.2em}por encima del eje horizontal $X$.\\[5pt]"
            r"$\bullet$ Negatividad en extremos: La parábola desciende\\[2pt]"
            r"\hspace*{1.2em}por debajo del eje $X$ hacia $-\infty$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=3.2)

        # ==========================================================
        # PASO 6: Intervalos de Monotonía y Rango
        # ==========================================================
        eq6 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Intervalos de Monotonía y Rango:} \\[6pt]"
            r"&\bullet \textbf{Monotonía (Crecimiento / Decrecimiento):} \\[4pt]"
            r"&\quad \mathbf{{\color{amgreen}f \text{ es creciente en } \left(-\infty, \frac{3}{2}\right] = (-\infty, 1.5]}} \\[5pt]"
            r"&\quad \mathbf{{\color{amred}f \text{ es decreciente en } \left[\frac{3}{2}, +\infty\right) = [1.5, +\infty)}} \\[7pt]"
            r"&\bullet \textbf{Rango (Recorrido de la Función):} \\[4pt]"
            r"&\quad \text{Como } {\color{amgold}y_v = 4.5} \text{ es el valor máximo alcanzado por } f: \\[4pt]"
            r"&\quad \mathbf{\operatorname{Ran}(f) = {\color{amgold}\left(-\infty, \frac{9}{2}\right] = (-\infty, 4.5]}} = (-\infty, y_v]."
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{6. Monotonía y Rango:}\\[6pt]"
            r"$\bullet$ La rama izquierda asciende de $-\infty$ hasta\\[2pt]"
            r"\hspace*{1.2em}alcanzar el vértice en ${\color{amteal}x = 1.5}$ (${\color{amgreen}\nearrow}$).\\[5pt]"
            r"$\bullet$ Desde ${\color{amteal}x = 1.5}$, la rama derecha desciende\\[2pt]"
            r"\hspace*{1.2em}indefinidamente hacia $-\infty$ (${\color{amred}\searrow}$).\\[5pt]"
            r"$\bullet$ Proyección vertical completa sobre el eje $Y$:\\[2pt]"
            r"\hspace*{1.2em}$\operatorname{Ran}(f) = {\color{amgold}\left(-\infty, 4.5\right]}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq6, just6, box_color=THEME["highlight"], advance_to_step=5, wait_time=3.2)

        # ==========================================================
        # PASO 7: Cuadro Horizontal de Variación y Puntos Notables
        # ==========================================================
        eq7 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{7. Cuadro de Variación y Puntos Notables:} \\[6pt]"
            r"&\begin{array}{c|c|c}"
            r"x & (-\infty, 1.5) & (1.5, +\infty) \\ \hline "
            r"\text{Pendiente / Comportamiento} & {\color{amgreen}\mathbf{\text{Ascendente }(+)}} & {\color{amred}\mathbf{\text{Descendente }(-)}} \\ \hline "
            r"f(x) & \nearrow & \searrow"
            r"\end{array} \\[8pt]"
            r"&\bullet \mathbf{\text{Vértice / Extremo: }} x = 1.5 \implies {\color{amgold}V(1.5, 4.5)} \text{ (Máximo Absoluto)}. \\[3pt]"
            r"&\bullet \mathbf{\text{Eje de Simetría: }} x = 1.5 \text{ (Divide las ramas con simetría axial)}. \\[3pt]"
            r"&\bullet \mathbf{\text{Cortes } X: } P_{x_2}(-1.5, 0) \text{ (en subida)} \text{ y } P_{x_1}(4.5, 0) \text{ (en bajada)}. \\[3pt]"
            r"&\bullet \mathbf{\text{Corte } Y: } P_y(0, 3.38) \text{ en el tramo de ascenso central}."
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{7. Síntesis Horizontal:}\\[6pt]"
            r"$\bullet$ Cuadro horizontal consolidado de variación.\\[5pt]"
            r"$\bullet$ Flechas confirman el ascenso continuo ($\nearrow$) hacia\\[2pt]"
            r"\hspace*{1.2em}el vértice ${\color{amgold}V(1.5, 4.5)}$ y el posterior descenso ($\searrow$).\\[5pt]"
            r"$\bullet$ Eje de simetría axial en ${\color{amteal}x = 1.5}$.\\[5pt]"
            r"$\bullet$ Coordenadas de anclaje para el trazo cartesiano."
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
            r"&\textbf{8. Resumen Formal de Resultados:} \\[5pt]"
            r"&\bullet \mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R}}}, \quad \mathbf{\operatorname{Ran}(f) = {\color{amgold}\left(-\infty, 4.5\right]}} \\[5pt]"
            r"&\bullet \mathbf{\text{Vértice: }} {\color{amgold}V(1.5, 4.5)} \quad (\text{Máximo Absoluto}) \\[5pt]"
            r"&\bullet \mathbf{\text{Forma: }} {\color{amteal}f(x) = -0.5(x - 1.5)^2 + 4.5} \\[5pt]"
            r"&\bullet \mathbf{\text{Eje de Simetría: }} {\color{amteal}x = 1.5} \\[5pt]"
            r"&\bullet \mathbf{\text{Cortes } X: } {\color{amorange}(-1.5, 0)} \quad \text{y} \quad {\color{amorange}(4.5, 0)} \\[5pt]"
            r"&\bullet \mathbf{\text{Corte } Y: } {\color{amteal}(0, 3.38)} \\[5pt]"
            r"&\bullet \mathbf{\text{Positiva en: }} {\color{amgreen}(-1.5, 4.5)} \quad {\color{amgreen}\blacksquare}"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        box8 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.18, corner_radius=0.1)

        # Gráfico cartesiano de la función cuadrática
        axes, axes_labels = self.setup_axes(
            x_range=[-3.0, 6.0, 1],
            y_range=[-3.0, 5.5, 1],
            x_length=4.5,
            y_length=3.3,
            center=[3.15, -0.75, 0],
            include_numbers=True,
            numbers_font_size=17,
            labels_font_size=20
        )
        graph_title = Tex(
            r"Gráfica de ${\color{amteal}f(x)} = {\color{amred}-\frac{1}{2}}x^2 + {\color{amteal}\frac{3}{2}}x + {\color{amgold}\frac{27}{8}}$",
            font_size=21.5,
            color=WHITE
        ).move_to([3.15, 1.65, 0])

        # Parábola continua
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
        lbl_sym = MathTex(r"x = 1.5", font_size=14.5, color="#e57373").next_to(axes.c2p(1.5, -2.8), DOWN, buff=0.10)

        # Vértice
        dot_v = Dot(axes.c2p(1.5, 4.5), radius=0.08, color=THEME["highlight"])
        lbl_v = MathTex(r"V(1.5, 4.5)", font_size=15.5, color=THEME["highlight"]).next_to(dot_v, UP, buff=0.10)

        # Cortes en eje x: (-1.5, 0) y (4.5, 0)
        dot_x1 = Dot(axes.c2p(-1.5, 0.0), radius=0.07, color=THEME["secondary"])
        lbl_x1 = MathTex(r"(-1.5, 0)", font_size=13.5, color=THEME["statement_text"]).next_to(dot_x1, UP + LEFT, buff=0.08)

        dot_x2 = Dot(axes.c2p(4.5, 0.0), radius=0.07, color=THEME["secondary"])
        lbl_x2 = MathTex(r"(4.5, 0)", font_size=13.5, color=THEME["statement_text"]).next_to(dot_x2, UP + RIGHT, buff=0.08)

        # Corte en eje y: (0, 3.375)
        dot_y = Dot(axes.c2p(0.0, 3.375), radius=0.07, color=THEME["curve"])
        lbl_y = MathTex(r"P_y(0, 3.38)", font_size=13.5, color=THEME["curve"]).next_to(dot_y, LEFT, buff=0.10)

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
        self.wait(8.5)

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
