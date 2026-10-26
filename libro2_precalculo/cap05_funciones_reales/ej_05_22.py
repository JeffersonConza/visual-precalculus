r"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.22 (Página 108 del libro / Página 127 del PDF)

Tema: Ecuaciones con Valor Absoluto y Verificación de Conjuntos Solución:
      Determinar si A ⊆ ℝ es el conjunto solución de cada ecuación:
      1. |x+3| - |2x-5| = 7,  x ∈ ℝ,  A = ∅  (VERDADERO).
      2. |x| + |x-5| = 6,  x ∈ ℝ,  A = {-1/2, 11/2}  (VERDADERO).
      3. |2|x| - 2| = -1,  x ∈ ℝ,  A = {-1/2, 1/2}  (FALSO, |u| ≥ 0 > -1 ⟹ CS = ∅ ≠ A).
      4. |x² - 9| = 2x + 6,  x ∈ ℝ,  A = {-3, 1, 5}  (VERDADERO).

Estructura de la Demostración (6 Pasos):
      1. Ecuación 1: Zonas críticas en x = -3 y x = 5/2, ninguna rama tiene solución en su rango ⟹ CS₁ = ∅ = A (VERDADERO).
      2. Ecuación 2: Partición en x = 0 y x = 5, soluciones en x = -1/2 y x = 11/2 ⟹ CS₂ = {-1/2, 11/2} = A (VERDADERO).
      3. Ecuación 3: No-negatividad del valor absoluto (|u| ≥ 0 > -1) ⟹ CS₃ = ∅ ≠ A (FALSO).
      4. Ecuación 4: Condición 2x+6 ≥ 0 (x ≥ -3) y desglose en casos (+/-) ⟹ x ∈ {-3, 1, 5}.
      5. Consolidación de veredictos: CS₄ = {-3, 1, 5} = A y resumen de los 4 literales.
      6. Interpretación geométrica cartesiana: intersección de f(x) = |x² - 9| y g(x) = 2x + 6 en (-3, 0), (1, 8) y (5, 16).

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica en 6 pasos con tipografía LaTeX HD generosa y legible.
"""

from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
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


class Ejercicio05_22(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.22",
            topic="Ecuaciones con Valor Absoluto",
            font_size=18.0
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 5.22: Determina si A es el conjunto solución de cada ecuación con valor absoluto:",
            math_tex=r"{\color{amgold}\mathbf{1.} \; |x+3|-|2x-5|=7} \quad \mathbf{2.} \; |x|+|x-5|=6 \quad \mathbf{3.} \; |2|x|-2|=-1 \quad {\color{amteal}\mathbf{4.} \; |x^2-9|=2x+6}",
            desc_font_size=20.0,
            math_font_size=21.5,
            arrange_direction=DOWN,
            buff=0.18,
            box_pos=np.array([0.0, 2.45, 0.0]),
            read_time=4.2
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Ecuación 1 (Zonas Críticas)",
            "2/6: Ecuación 2 (Partición en ℝ)",
            "3/6: Ecuación 3 (No Negatividad)",
            "4/6: Ecuación 4 (Desglose de Casos)",
            "5/6: Consolidación de Veredictos",
            "6/6: Gráfica de |x²-9| = 2x+6"
        ], dot_spacing=0.96, label_font_size=14.5)

        # ==========================================================
        # PASO 1: Ecuación 1: |x+3| - |2x-5| = 7
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Ecuación: } |x+3| - |2x-5| = 7, \quad A = \emptyset \\[6pt]"
            r"&\text{Puntos críticos en } \mathbb{R}: \quad x \in \{-3, 5/2\} \\[6pt]"
            r"&\bullet \ x < -3: \quad -x-3 - (-2x+5) = 7 \implies x = 15 \notin \; ]-\infty, -3[ \\[4pt]"
            r"&\bullet \ -3 \le x < \frac{5}{2}: \quad x+3 - (-2x+5) = 7 \implies x = 3 \notin [-3, 5/2[ \\[4pt]"
            r"&\bullet \ x \ge \frac{5}{2}: \quad x+3 - (2x-5) = 7 \implies x = 1 \notin [5/2, +\infty[ \\[6pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}CS_1 = \emptyset = A \implies \text{VERDADERO}}}"
            r"\end{aligned}",
            font_size=23.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Análisis por Zonas Críticas:}\\[6pt]"
            r"$\bullet$ Los ceros de los valores absolutos son\\ "
            r"\hspace*{1.2em}$x = -3$ y $x = 5/2 = 2.5$.\\[6pt]"
            r"$\bullet$ Evaluamos los tres intervalos disyuntos:\\ "
            r"\hspace*{1.2em}1. $x < -3 \implies x = 15$ (incompatible).\\ "
            r"\hspace*{1.2em}2. $[-3, 2.5[ \implies x = 3$ (fuera de rango).\\ "
            r"\hspace*{1.2em}3. $x \ge 2.5 \implies x = 1$ (fuera de rango).\\[6pt]"
            r"$\bullet$ Ninguna rama aporta solución real:\\ "
            r"\hspace*{1.2em}${\color{amgreen}CS_1 = \emptyset = A \implies \text{VERDADERO}}$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Ecuación 2: |x| + |x-5| = 6
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Ecuación: } |x| + |x-5| = 6, \quad A = \{-1/2, 11/2\} \\[6pt]"
            r"&\text{Puntos críticos en } \mathbb{R}: \quad x \in \{0, 5\} \\[6pt]"
            r"&\bullet \ x < 0: \quad -x - (x-5) = 6 \implies -2x = 1 \implies \mathbf{{\color{amgold}x = -1/2}} \\[4pt]"
            r"&\bullet \ 0 \le x < 5: \quad x - (x-5) = 6 \implies 5 = 6 \quad (\text{Imposible}) \\[4pt]"
            r"&\bullet \ x \ge 5: \quad x + (x-5) = 6 \implies 2x = 11 \implies \mathbf{{\color{amteal}x = 11/2}} \\[6pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}CS_2 = \{-1/2, 11/2\} = A \implies \text{VERDADERO}}}"
            r"\end{aligned}",
            font_size=23.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Partición de Intervalos:}\\[6pt]"
            r"$\bullet$ Puntos de corte en $x = 0$ y $x = 5$:\\[4pt]"
            r"\hspace*{1.2em}1. $x < 0 \implies -2x + 5 = 6 \implies {\color{amgold}x = -1/2 < 0}$ (válido).\\[4pt]"
            r"\hspace*{1.2em}2. $0 \le x < 5 \implies 5 = 6$ (sin solución).\\[4pt]"
            r"\hspace*{1.2em}3. $x \ge 5 \implies 2x - 5 = 6 \implies {\color{amteal}x = 11/2 \ge 5}$ (válido).\\[6pt]"
            r"$\bullet$ Conjunto solución confirmado:\\ "
            r"\hspace*{1.2em}${\color{amgreen}CS_2 = \{-1/2, 11/2\} = A \implies \text{VERDADERO}}$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Ecuación 3: |2|x| - 2| = -1
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Ecuación: } |2|x| - 2| = -1, \quad A = \{-1/2, 1/2\} \\[7pt]"
            r"&\text{Por axioma del valor absoluto en } \mathbb{R}: \\[6pt]"
            r"&\quad \forall u \in \mathbb{R}: \quad \mathbf{{\color{amred}|u| \ge 0}} \\[7pt]"
            r"&\text{Evaluando la ecuación:} \\[6pt]"
            r"&\quad |2|x| - 2| \ge 0 > -1 \quad (\text{Contradicción estricta}) \\[8pt]"
            r"&\therefore \quad \mathbf{{\color{amred}CS_3 = \emptyset \neq A \implies \text{FALSO}}}"
            r"\end{aligned}",
            font_size=24.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{3. Principio de No-Negatividad:}\\[6pt]"
            r"$\bullet$ Por definición axiomática, la función valor\\ "
            r"\hspace*{1.2em}absoluto siempre es no-negativa:\\[4pt]"
            r"\hspace*{1.2em}${\color{amred}|u| \ge 0}$ para todo $u \in \mathbb{R}$.\\[6pt]"
            r"$\bullet$ El miembro izquierdo jamás puede igualar\\ "
            r"\hspace*{1.2em}a una constante negativa: $|2|x| - 2| \ge 0 > -1$.\\[6pt]"
            r"$\bullet$ La ecuación es incompatible en $\mathbb{R}$:\\ "
            r"\hspace*{1.2em}$CS_3 = \emptyset \neq A \implies {\color{amred}\textbf{FALSO}}$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq3, just3, box_color=THEME["statement_box"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Ecuación 4: |x² - 9| = 2x + 6 (Desglose de Casos)
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Ecuación: } |x^2 - 9| = 2x + 6, \quad A = \{-3, 1, 5\} \\[6pt]"
            r"&\text{Condición de existencia: } 2x + 6 \ge 0 \iff \mathbf{{\color{amgold}x \ge -3}} \\[7pt]"
            r"&\text{Caso (+): } x^2 - 9 = 2x + 6 \implies x^2 - 2x - 15 = 0 \\[4pt]"
            r"&\quad (x - 5)(x + 3) = 0 \implies \mathbf{{\color{amteal}x = 5 \;\lor\; x = -3}} \\[6pt]"
            r"&\text{Caso (-): } x^2 - 9 = -(2x + 6) \implies x^2 + 2x - 3 = 0 \\[4pt]"
            r"&\quad (x + 3)(x - 1) = 0 \implies \mathbf{{\color{amteal}x = -3 \;\lor\; x = 1}}"
            r"\end{aligned}",
            font_size=23.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Desglose y Condición de Existencia:}\\[6pt]"
            r"$\bullet$ Para que $|u| = v$ tenga solución real se\\ "
            r"\hspace*{1.2em}requiere $v \ge 0 \implies 2x + 6 \ge 0 \iff {\color{amgold}x \ge -3}$.\\[6pt]"
            r"$\bullet$ Caso positivo ($x^2 - 9 \ge 0$):\\ "
            r"\hspace*{1.2em}$x^2 - 2x - 15 = 0 \implies x = 5, -3$ (válidos).\\[6pt]"
            r"$\bullet$ Caso negativo ($x^2 - 9 < 0$):\\ "
            r"\hspace*{1.2em}$x^2 + 2x - 3 = 0 \implies x = 1, -3$ (válidos).\\[6pt]"
            r"$\bullet$ Todas las raíces satisfacen $x \ge -3$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq4, just4, box_color=THEME["curve"], advance_to_step=3, wait_time=5.0)

        # ==========================================================
        # PASO 5: Consolidación de Veredictos del Ejercicio 5.22
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Veredicto Ecuación 4 y Cuadro Resumen:} \\[6pt]"
            r"&CS_4 = \{-3, 1, 5\} = A \implies \mathbf{{\color{amgreen}\text{VERDADERO}}} \\[8pt]"
            r"&\text{\textbf{Consolidación de Veredictos (Ejercicio 5.22):}} \\[6pt]"
            r"&\mathbf{1.} \; |x+3|-|2x-5|=7, \; A = \emptyset \implies \mathbf{{\color{amgreen}\text{VERDADERO}}} \\[4pt]"
            r"&\mathbf{2.} \; |x|+|x-5|=6, \; A = \{-1/2, 11/2\} \implies \mathbf{{\color{amgreen}\text{VERDADERO}}} \\[4pt]"
            r"&\mathbf{3.} \; |2|x|-2|=-1, \; A = \{-1/2, 1/2\} \implies \mathbf{{\color{amred}\text{FALSO}}} \\[4pt]"
            r"&\mathbf{4.} \; |x^2-9|=2x+6, \; A = \{-3, 1, 5\} \implies \mathbf{{\color{amgreen}\text{VERDADERO}}}"
            r"\end{aligned}",
            font_size=22.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Veredicto Final Consolidado:}\\[6pt]"
            r"$\bullet$ Para la ecuación 4, el conjunto obtenido\\ "
            r"\hspace*{1.2em}$CS_4 = \{-3, 1, 5\}$ coincide exactamente con $A$.\\[6pt]"
            r"$\bullet$ \textbf{Resumen general de los 4 literales}:\\[3pt]"
            r"\hspace*{1.2em}1. $|x+3|-|2x-5|=7 \implies {\color{amgreen}\textbf{VERDADERO}}$.\\[3pt]"
            r"\hspace*{1.2em}2. $|x|+|x-5|=6 \implies {\color{amgreen}\textbf{VERDADERO}}$.\\[3pt]"
            r"\hspace*{1.2em}3. $|2|x|-2|=-1 \implies {\color{amred}\textbf{FALSO}}$.\\[3pt]"
            r"\hspace*{1.2em}4. $|x^2-9|=2x+6 \implies {\color{amgreen}\textbf{VERDADERO}}$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana (Ecuación 4)
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen geométrico
        t_card = Tex(
            r"\begin{minipage}{5.8cm}\raggedright "
            r"\textbf{{\color{amteal}Intersección Gráfica:}}\\[6pt]"
            r"$\bullet$ \textbf{Curva con valor absoluto:}\\[2pt]"
            r"\hspace*{0.8em}$f(x) = |x^2 - 9|$.\\[2pt]"
            r"\hspace*{0.8em}Refleja el tramo negativo $[-3, 3]$.\\[6pt]"
            r"$\bullet$ \textbf{Recta afín secante:}\\[2pt]"
            r"\hspace*{0.8em}$g(x) = 2x + 6$ con pendiente $2$.\\[6pt]"
            r"$\bullet$ \textbf{Tres puntos de corte:}\\[2pt]"
            r"\hspace*{0.8em}$P_1(-3, 0)$, $P_2(1, 8)$, $P_3(5, 16)$.\\[6pt]"
            r"$\bullet$ \textbf{Conclusión cartesiana:}\\[2pt]"
            r"\hspace*{0.8em}$CS_4 = \{-3, 1, 5\}$ corroborado."
            r"\end{minipage}",
            font_size=18.5,
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
            x_range=[-4.5, 6.0, 2],
            y_range=[-2.0, 18.0, 4],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=15,
            labels_font_size=21
        )

        # Curva f(x) = |x² - 9|
        curve_f = axes.plot(
            lambda x: np.abs(x**2 - 9.0),
            x_range=[-4.2, 5.2],
            color=THEME["curve"],
            stroke_width=3.2
        )
        lbl_f = MathTex(
            r"f(x) = |x^2-9|",
            font_size=16.5,
            color=THEME["curve"]
        ).next_to(axes.c2p(-3.8, 6.5), LEFT, buff=0.10)

        # Recta g(x) = 2x + 6
        line_g = axes.plot(
            lambda x: 2.0 * x + 6.0,
            x_range=[-3.5, 5.5],
            color=THEME["highlight"],
            stroke_width=2.8
        )
        lbl_g = MathTex(
            r"g(x) = 2x+6",
            font_size=16.5,
            color=THEME["highlight"]
        ).next_to(axes.c2p(4.5, 15.0), LEFT, buff=0.10)

        # Puntos de intersección notables
        p1 = axes.c2p(-3.0, 0.0)
        p2 = axes.c2p(1.0, 8.0)
        p3 = axes.c2p(5.0, 16.0)

        dot1 = Dot(p1, radius=0.07, color=THEME["success"])
        dot2 = Dot(p2, radius=0.07, color=THEME["success"])
        dot3 = Dot(p3, radius=0.07, color=THEME["success"])

        lbl_p1 = MathTex(r"(-3, 0)", font_size=16.5, color=THEME["success"]).next_to(p1, DOWN, buff=0.10)
        lbl_p2 = MathTex(r"(1, 8)", font_size=16.5, color=THEME["success"]).next_to(p2, RIGHT, buff=0.10)
        lbl_p3 = MathTex(r"(5, 16)", font_size=16.5, color=THEME["success"]).next_to(p3, DR, buff=0.10)

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

        # Trazado de las curvas f(x) y g(x)
        self.play(
            Create(curve_f), Write(lbl_f),
            Create(line_g), Write(lbl_g),
            run_time=2.2
        )

        # Marcado de las tres intersecciones
        self.play(
            FadeIn(dot1), Write(lbl_p1),
            FadeIn(dot2), Write(lbl_p2),
            FadeIn(dot3), Write(lbl_p3),
            run_time=1.6
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_f, lbl_f,
            line_g, lbl_g,
            dot1, dot2, dot3,
            lbl_p1, lbl_p2, lbl_p3
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
