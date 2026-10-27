r"""
Precálculo Universitario · Tutorías Annelisse / Editorial Amarun
Tema: Determinación del Rango de Funciones Cuadráticas con Dominio Acotado
Ejercicio 3: Hallar el rango de cada función con el dominio dado:
      a) f(x) = -2x² - (3/2)x + 5/4, con Dom f: ]-3/2, -1/2]
      b) f(x) = -(2/3)x² + (7/6)x + 5/8, con Dom f: [1/2, 3/2[
      c) f(x) = x² - 6x + 5, con Dom f: [3, 9/2[

Estructura de la Demostración (6 Pasos):
      1. Fundamento metodológico: Posición del vértice xv = -b/(2a) frente al dominio acotado [p, q].
      2. Función a): xv = -3/8 ∉ ]-3/2, -1/2] (vértice exterior) ⟹ f es estrictamente creciente ⟹ Ran(fa) = ]-1, 3/2].
      3. Función b): xv = 7/8 ∈ [1/2, 3/2[ (vértice interior) ⟹ Máximo absoluto en y = 109/96 ⟹ Ran(fb) = ]7/8, 109/96].
      4. Función c): xv = 3 (vértice en extremo izquierdo cerrado) ⟹ f es estrictamente creciente ⟹ Ran(fc) = [-4, -7/4[.
      5. Consolidación y matriz comparativa de los tres literales.
      6. Interpretación geométrica cartesiana: arcos de parábola, puntos de frontera y visualización del rango.

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica en 6 pasos con tipografía LaTeX HD generosa y legible.
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
\usepackage{cancel}
\definecolor{amgold}{HTML}{F6B840}
\definecolor{amteal}{HTML}{5CE1E6}
\definecolor{amred}{HTML}{E53E3E}
\definecolor{amgreen}{HTML}{48BB78}
\definecolor{amorange}{HTML}{DB5A38}
\definecolor{amwhite}{HTML}{FDFBF7}
""")
config.tex_template = AMARUN_TEX_TEMPLATE


class EjercicioAnn_03(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Annelisse",
            exercise="Ejercicio 3",
            topic="Rango con Dominio Restringido",
            font_size=17.5
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 3: Halla el rango de cada función cuadrática en el dominio acotado dado:",
            math_tex=r"{\color{amred}\mathbf{a)} \; f(x) = -2x^2 - \frac{3}{2}x + \frac{5}{4}} \quad {\color{amteal}\mathbf{b)} \; f(x) = -\frac{2}{3}x^2 + \frac{7}{6}x + \frac{5}{8}} \quad {\color{amgold}\mathbf{c)} \; f(x) = x^2 - 6x + 5}",
            desc_font_size=20.0,
            math_font_size=19.5,
            arrange_direction=DOWN,
            buff=0.18,
            box_pos=np.array([0.0, 2.45, 0.0]),
            read_time=4.2
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Criterio: Vértice vs. Dominio",
            "2/6: Función a) (Vértice Exterior)",
            "3/6: Función b) (Vértice Interior)",
            "4/6: Función c) (Vértice en Frontera)",
            "5/6: Consolidación de Resultados",
            "6/6: Trazado Cartesiano de los 3 Arcos"
        ], dot_spacing=0.96, label_font_size=14.0)

        # ==========================================================
        # PASO 1: Fundamento Teórico: Vértice frente al Dominio Acotado
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Criterio de Rango en Intervalos } [p, q]: \\[6pt]"
            r"&\text{Para } {\color{amteal}f(x) = ax^2 + bx + c}, \quad \text{abscisa del vértice: } \mathbf{{\color{amgold}x_v = -\frac{b}{2a}}} \\[7pt]"
            r"&\textbf{Regla de Inclusión del Vértice:} \\[5pt]"
            r"&\bullet \ \mathbf{{\color{amorange}x_v \notin [p, q]}}: \text{ La función es monótona en todo el intervalo.} \\[3pt]"
            r"&\quad \implies \text{El rango depende únicamente de los extremos } {\color{amgold}f(p)} \text{ y } {\color{amgold}f(q)}. \\[6pt]"
            r"&\bullet \ \mathbf{{\color{amgreen}x_v \in [p, q]}}: \text{ El vértice constituye un extremo absoluto local.} \\[3pt]"
            r"&\quad \implies \operatorname{Ran}(f) \text{ abarca desde } \min\{f(p), f(q), {\color{amgold}f(x_v)}\} \text{ hasta } \max."
            r"\end{aligned}",
            font_size=22.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Metodología de Rango Acotado:}\\[6pt]"
            r"$\bullet$ Es un error común evaluar solo los extremos; se debe verificar si el vértice ${\color{amgold}x_v}$ pertenece al dominio.\\[5pt]"
            r"$\bullet$ Si ${\color{amorange}x_v \notin \operatorname{Dom}(f)}$, la función no cambia de sentido de crecimiento (monotonía estricta).\\[5pt]"
            r"$\bullet$ Si ${\color{amgreen}x_v \in \operatorname{Dom}(f)}$, el vértice aporta la cota extrema (mínimo si $a>0$, máximo si $a<0$).\\[5pt]"
            r"$\bullet$ Los corchetes o paréntesis del rango reflejan si el extremo es alcanzado o límite abierto."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Función a): f(x) = -2x² - (3/2)x + 5/4 en ]-3/2, -1/2]
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Función a): } \mathbf{{\color{amred}f(x) = -2x^2 - \frac{3}{2}x + \frac{5}{4}}}, \quad \operatorname{Dom}(f) = \left] -\frac{3}{2}, -\frac{1}{2} \right] \\[6pt]"
            r"&\text{Abscisa del vértice: } x_v = -\frac{-3/2}{2(-2)} = \mathbf{{\color{amorange}-\frac{3}{8} = -0.375}} \\[6pt]"
            r"&\text{Verificación: } -0.375 > -0.5 \implies \mathbf{{\color{amred}x_v \notin \left] -\frac{3}{2}, -\frac{1}{2} \right]}} \quad (\text{Exterior}) \\[6pt]"
            r"&\text{Como } a = -2 < 0 \text{ y } x < x_v \implies f(x) \text{ es } \mathbf{\text{estrictamente creciente:}} \\[5pt]"
            r"&\bullet \ x \to -\frac{3}{2}^+: \ f(-3/2) = -2(9/4) + 9/4 + 5/4 = \mathbf{{\color{amgold}-1}} \ (\text{abierto}) \\[4pt]"
            r"&\bullet \ x = -\frac{1}{2}: \ f(-1/2) = -2(1/4) + 3/4 + 5/4 = \mathbf{{\color{amgreen}\frac{3}{2}}} \ (\text{cerrado}) \\[6pt]"
            r"&\therefore \quad \mathbf{\operatorname{Ran}(f_a) = {\color{amgreen}\left] -1, \frac{3}{2} \right]}}"
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Análisis de la Función a):}\\[6pt]"
            r"$\bullet$ El vértice $x_v = -0.375$ queda a la derecha del intervalo $[-1.5, -0.5]$ (${\color{amred}x_v \notin \operatorname{Dom}(f)}$).\\[5pt]"
            r"$\bullet$ La parábola abre hacia abajo ($a = -2 < 0$), luego a la izquierda del vértice siempre crece.\\[5pt]"
            r"$\bullet$ Extremo izquierdo abierto en $-3/2$:\\"
            r"\hspace*{1.0em}$\lim_{x \to -3/2^+} f(x) = {\color{amgold}-1}$ (ínfimo excluido).\\[5pt]"
            r"$\bullet$ Extremo derecho cerrado en $-1/2$:\\"
            r"\hspace*{1.0em}$f(-1/2) = {\color{amgreen}3/2}$ (máximo alcanzado).\\[5pt]"
            r"$\bullet$ ${\color{amgreen}\operatorname{Ran}(f_a) = \; ]-1, 3/2]}$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq2, just2, box_color=THEME["error"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Función b): f(x) = -(2/3)x² + (7/6)x + 5/8 en [1/2, 3/2[
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Función b): } \mathbf{{\color{amteal}f(x) = -\frac{2}{3}x^2 + \frac{7}{6}x + \frac{5}{8}}}, \quad \operatorname{Dom}(f) = \left[ \frac{1}{2}, \frac{3}{2} \right[ \\[6pt]"
            r"&\text{Abscisa del vértice: } x_v = -\frac{7/6}{2(-2/3)} = \frac{7/6}{4/3} = \mathbf{{\color{amgreen}\frac{7}{8} = 0.875}} \\[6pt]"
            r"&\text{Verificación: } \frac{1}{2} \le \frac{7}{8} < \frac{3}{2} \implies \mathbf{{\color{amgreen}x_v \in \left[ \frac{1}{2}, \frac{3}{2} \right[}} \quad (\text{Interior}) \\[6pt]"
            r"&\text{Como } a < 0 \implies \mathbf{\text{Máximo absoluto en el vértice:}} \\[4pt]"
            r"&\quad y_v = f(7/8) = -\frac{2}{3}\left(\frac{49}{64}\right) + \frac{7}{6}\left(\frac{7}{8}\right) + \frac{5}{8} = \mathbf{{\color{amgreen}\frac{109}{96} \approx 1.135}} \\[5pt]"
            r"&\text{Fronteras: } f(1/2) = \frac{25}{24} = \frac{100}{96}, \quad f(3/2) = \mathbf{{\color{amgold}\frac{7}{8} = \frac{84}{96}}} \ (\text{abierto}) \\[6pt]"
            r"&\therefore \quad \mathbf{\operatorname{Ran}(f_b) = {\color{amgreen}\left] \frac{7}{8}, \frac{109}{96} \right]}}"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{3. Análisis de la Función b):}\\[6pt]"
            r"$\bullet$ El vértice $x_v = 7/8 = 0.875$ sí pertenece al dominio $[0.5, 1.5[$ (${\color{amgreen}x_v \in \operatorname{Dom}(f)}$).\\[5pt]"
            r"$\bullet$ Al abrir hacia abajo ($a = -2/3 < 0$), el vértice proporciona el ${\color{amgreen}\text{máximo absoluto}}$ en $y = 109/96$.\\[5pt]"
            r"$\bullet$ Comparación de extremos:\\"
            r"\hspace*{1.0em}$f(1/2) = 25/24 \approx 1.042$,\\"
            r"\hspace*{1.0em}$f(3/2) = 7/8 = 0.875$ (valor mínimo abierto).\\[5pt]"
            r"$\bullet$ ${\color{amgreen}\operatorname{Ran}(f_b) = \left] \frac{7}{8}, \frac{109}{96} \right]}$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq3, just3, box_color=THEME["secondary"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Función c): f(x) = x² - 6x + 5 en [3, 9/2[
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Función c): } \mathbf{{\color{amgold}f(x) = x^2 - 6x + 5}}, \quad \operatorname{Dom}(f) = \left[ 3, \frac{9}{2} \right[ \\[6pt]"
            r"&\text{Abscisa del vértice: } x_v = -\frac{-6}{2(1)} = \mathbf{{\color{amgreen}3}} \quad (\text{Frontera izquierda}) \\[6pt]"
            r"&\text{Como } a = 1 > 0 \text{ y } x \ge 3 \implies f(x) \text{ es } \mathbf{\text{estrictamente creciente:}} \\[6pt]"
            r"&\bullet \ \text{Mínimo absoluto en el vértice } (x = 3): \\[4pt]"
            r"&\quad f(3) = 3^2 - 6(3) + 5 = 9 - 18 + 5 = \mathbf{{\color{amgreen}-4}} \ (\text{cerrado}) \\[5pt]"
            r"&\bullet \ \text{Extremo superior } (x \to 9/2^-): \\[4pt]"
            r"&\quad f(9/2) = \left(\frac{9}{2}\right)^2 - 6\left(\frac{9}{2}\right) + 5 = \frac{81}{4} - 22 = \mathbf{{\color{amgold}-\frac{7}{4} = -1.75}} \ (\text{abierto}) \\[6pt]"
            r"&\therefore \quad \mathbf{\operatorname{Ran}(f_c) = {\color{amgreen}\left[ -4, -\frac{7}{4} \right[}}"
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Análisis de la Función c):}\\[6pt]"
            r"$\bullet$ El vértice $x_v = 3$ coincide exactamente con el límite inferior cerrado del dominio.\\[5pt]"
            r"$\bullet$ Como $a = 1 > 0$ (abre hacia arriba), la rama a la derecha del vértice es estrictamente creciente.\\[5pt]"
            r"$\bullet$ El vértice aporta el ${\color{amgreen}\text{mínimo absoluto}}$ cerrado: $f(3) = -4$.\\[5pt]"
            r"$\bullet$ El límite superior se aproxima a $f(9/2) = -7/4$ (extremo abierto).\\[5pt]"
            r"$\bullet$ ${\color{amgreen}\operatorname{Ran}(f_c) = \left[ -4, -\frac{7}{4} \right[}$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq4, just4, box_color=THEME["curve"], advance_to_step=3, wait_time=4.8)

        # ==========================================================
        # PASO 5: Consolidación y Cuadro Resumen Comparativo
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{\textbf{5. Cuadro Resumen de Rangos Acotados:}} \\[7pt]"
            r"&\mathbf{a)} \; f(x) = -2x^2 - \tfrac{3}{2}x + \tfrac{5}{4}, \quad \operatorname{Dom}(f) = \; \left] -\frac{3}{2}, -\frac{1}{2} \right]: \\[3pt]"
            r"&\quad x_v = -\frac{3}{8} \notin \operatorname{Dom}(f) \implies \mathbf{\operatorname{Ran}(f_a) = {\color{amgreen}\left] -1, \frac{3}{2} \right]}} \\[6pt]"
            r"&\mathbf{b)} \; f(x) = -\tfrac{2}{3}x^2 + \tfrac{7}{6}x + \tfrac{5}{8}, \quad \operatorname{Dom}(f) = \left[ \frac{1}{2}, \frac{3}{2} \right[: \\[3pt]"
            r"&\quad x_v = \frac{7}{8} \in \operatorname{Dom}(f) \implies \mathbf{\operatorname{Ran}(f_b) = {\color{amgreen}\left] \frac{7}{8}, \frac{109}{96} \right]}} \\[6pt]"
            r"&\mathbf{c)} \; f(x) = x^2 - 6x + 5, \quad \operatorname{Dom}(f) = \left[ 3, \frac{9}{2} \right[: \\[3pt]"
            r"&\quad x_v = 3 \in \text{Frontera} \implies \mathbf{\operatorname{Ran}(f_c) = {\color{amgreen}\left[ -4, -\frac{7}{4} \right[}}"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Síntesis Metodológica:}\\[6pt]"
            r"$\bullet$ \textbf{Caso a) (Vértice exterior):} La función preserva monotonía; el rango se obtiene en los extremos de la definición.\\[5pt]"
            r"$\bullet$ \textbf{Caso b) (Vértice interior):} El vértice actúa como cota superior máxima cerrada ($109/96$).\\[5pt]"
            r"$\bullet$ \textbf{Caso c) (Vértice en frontera):} El vértice es el punto de arranque mínimo cerrado ($-4$).\\[5pt]"
            r"$\bullet$ Tres comportamientos canónicos totalmente caracterizados."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana de los 3 Arcos
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen geométrico
        t_card = Tex(
            r"\begin{minipage}{5.8cm}\raggedright "
            r"\textbf{{\color{amteal}Visualización de Arcos:}}\\[6pt]"
            r"$\bullet$ \textbf{Arco a) (Rojo Poncho):}\\[2pt]"
            r"\hspace*{0.8em}$x \in \; ]-1.5, -0.5]$.\\[2pt]"
            r"\hspace*{0.8em}Extremo abierto en $(-1.5, -1)$;\\[2pt]"
            r"\hspace*{0.8em}Cerrado en $(-0.5, 1.5)$.\\[6pt]"
            r"$\bullet$ \textbf{Arco b) (Turquesa):}\\[2pt]"
            r"\hspace*{0.8em}$x \in [0.5, 1.5[$.\\[2pt]"
            r"\hspace*{0.8em}Pico en $(7/8, 109/96)$;\\[2pt]"
            r"\hspace*{0.8em}Abierto en $(1.5, 7/8)$.\\[6pt]"
            r"$\bullet$ \textbf{Arco c) (Oro Inca):}\\[2pt]"
            r"\hspace*{0.8em}$x \in [3, 4.5[$.\\[2pt]"
            r"\hspace*{0.8em}Vértice cerrado en $(3, -4)$;\\[2pt]"
            r"\hspace*{0.8em}Abierto en $(4.5, -1.75)$."
            r"\end{minipage}",
            font_size=18.0,
            color=WHITE
        )
        info_box = SurroundingRectangle(
            t_card,
            color=THEME["statement_box"],
            buff=0.22,
            stroke_width=1.8,
            corner_radius=0.1
        )
        info_grp = VGroup(info_box, t_card).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos
        axes, axes_labels = self.setup_axes(
            x_range=[-2.5, 5.5, 1],
            y_range=[-5.0, 3.0, 1],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=14,
            labels_font_size=20
        )

        # Curva a: f(x) = -2x^2 - (3/2)x + 5/4 en [-1.5, -0.5]
        curve_a = axes.plot(
            lambda x: -2.0 * (x**2) - 1.5 * x + 1.25,
            x_range=[-1.5, -0.5],
            color=THEME["error"],
            stroke_width=3.6
        )
        dot_a_open = Dot(axes.c2p(-1.5, -1.0), radius=0.07, stroke_width=2.0, stroke_color=THEME["error"], fill_color=THEME["bg_color"])
        dot_a_closed = Dot(axes.c2p(-0.5, 1.5), radius=0.07, color=THEME["error"])
        lbl_a = MathTex(r"f_a", font_size=16.0, color=THEME["error"]).next_to(axes.c2p(-0.5, 1.5), UP, buff=0.08)

        # Curva b: f(x) = -(2/3)x^2 + (7/6)x + 5/8 en [0.5, 1.5]
        curve_b = axes.plot(
            lambda x: -(2.0/3.0) * (x**2) + (7.0/6.0) * x + (5.0/8.0),
            x_range=[0.5, 1.5],
            color=THEME["secondary"],
            stroke_width=3.6
        )
        dot_b_closed = Dot(axes.c2p(0.5, 25.0/24.0), radius=0.06, color=THEME["secondary"])
        dot_b_vertex = Dot(axes.c2p(7.0/8.0, 109.0/96.0), radius=0.07, color=THEME["success"])
        dot_b_open = Dot(axes.c2p(1.5, 7.0/8.0), radius=0.07, stroke_width=2.0, stroke_color=THEME["secondary"], fill_color=THEME["bg_color"])
        lbl_b = MathTex(r"f_b", font_size=16.0, color=THEME["secondary"]).next_to(axes.c2p(7.0/8.0, 109.0/96.0), UP, buff=0.08)

        # Curva c: f(x) = x^2 - 6x + 5 en [3.0, 4.5]
        curve_c = axes.plot(
            lambda x: x**2 - 6.0 * x + 5.0,
            x_range=[3.0, 4.5],
            color=THEME["highlight"],
            stroke_width=3.6
        )
        dot_c_vertex = Dot(axes.c2p(3.0, -4.0), radius=0.07, color=THEME["success"])
        dot_c_open = Dot(axes.c2p(4.5, -1.75), radius=0.07, stroke_width=2.0, stroke_color=THEME["highlight"], fill_color=THEME["bg_color"])
        lbl_c = MathTex(r"f_c", font_size=16.0, color=THEME["highlight"]).next_to(axes.c2p(4.5, -1.75), RIGHT, buff=0.08)

        # Transición hacia el paso 6
        self.play(
            FadeOut(self.active_box),
            FadeOut(self.active_math, shift=DOWN * 0.2),
            FadeOut(self.active_just, shift=DOWN * 0.2),
            FadeIn(info_grp, shift=DOWN * 0.2),
            Create(axes),
            Write(axes_labels),
            *prog_anims,
            run_time=1.8
        )
        self.active_box = None
        self.active_math = None
        self.active_just = None

        # Trazado progresivo de los 3 arcos
        self.play(
            Create(curve_a), Write(lbl_a),
            Create(curve_b), Write(lbl_b),
            Create(curve_c), Write(lbl_c),
            run_time=2.2
        )

        # Marcado de nodos de frontera y vértices
        self.play(
            FadeIn(dot_a_open), FadeIn(dot_a_closed),
            FadeIn(dot_b_closed), FadeIn(dot_b_vertex), FadeIn(dot_b_open),
            FadeIn(dot_c_vertex), FadeIn(dot_c_open),
            run_time=1.8
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_a, lbl_a, dot_a_open, dot_a_closed,
            curve_b, lbl_b, dot_b_closed, dot_b_vertex, dot_b_open,
            curve_c, lbl_c, dot_c_vertex, dot_c_open
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
