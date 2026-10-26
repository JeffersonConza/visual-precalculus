r"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.26 (Página 108 del libro / Página 127 del PDF)

Tema: Inecuación con Valor Absoluto Anidado:
      Resolver la inecuación en el conjunto de los números reales:
      |3|x| - 1| ≤ 5,  x ∈ ℝ.

Estructura de la Demostración (6 Pasos):
      1. Acotación exterior: |u| ≤ c ⟺ -c ≤ u ≤ c con u = 3|x| - 1 y c = 5 ⟹ -5 ≤ 3|x| - 1 ≤ 5.
      2. Despeje de |x|: aislamiento algebraico ⟹ -4 ≤ 3|x| ≤ 6 ⟹ -4/3 ≤ |x| ≤ 2.
      3. Conjunción de condiciones: (-4/3 ≤ |x| ≤ 2) ⟺ (|x| ≥ -4/3) ∧ (|x| ≤ 2).
      4. Análisis deductivo de ramas:
         - Rama 1: |x| ≥ -4/3 es universal por axioma (|x| ≥ 0 > -4/3) ⟹ S₁ = ℝ.
         - Rama 2: |x| ≤ 2 ⟺ -2 ≤ x ≤ 2 ⟹ S₂ = [-2, 2].
      5. Conjunto solución final: CS = S₁ ∩ S₂ = ℝ ∩ [-2, 2] = [-2, 2].
      6. Interpretación geométrica cartesiana: Curva en forma de 'W' f(x) = |3|x| - 1|,
         recta horizontal y = 5, puntos de corte P₁(−2, 5) y P₂(2, 5), y proyección
         del intervalo continuo CS = [-2, 2] sobre el eje de abscisas.

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


class Ejercicio05_26(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.26",
            topic="Inecuación con Valor Absoluto Anidado",
            font_size=18.0
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 5.26: Resuelve la inecuación con valor absoluto en los números reales:",
            math_tex=r"{\color{amgold}\big|3|x| - 1\big| \le 5}, \quad x \in \mathbb{R}",
            desc_font_size=20.0,
            math_font_size=24.0,
            arrange_direction=DOWN,
            buff=0.18,
            box_pos=np.array([0.0, 2.45, 0.0]),
            read_time=4.2
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Acotación Exterior",
            "2/6: Despeje de |x|",
            "3/6: Conjunción Lógica (∧)",
            "4/6: Análisis de Ramas",
            "5/6: Conjunto Solución (CS)",
            "6/6: Gráfica de |3|x|-1| ≤ 5"
        ], dot_spacing=0.96, label_font_size=14.5)

        # ==========================================================
        # PASO 1: Acotación Exterior del Valor Absoluto
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Teorema de Acotación Simétrica:} \\[6pt]"
            r"&\forall u \in \mathbb{R}, \; c > 0: \quad \mathbf{{\color{amgold}|u| \le c \iff -c \le u \le c}} \\[8pt]"
            r"&\text{Aplicando con } u = 3|x| - 1 \text{ y } c = 5: \\[6pt]"
            r"&\quad \mathbf{{\color{amteal}-5 \le 3|x| - 1 \le 5}}"
            r"\end{aligned}",
            font_size=23.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Acotación Exterior:}\\[6pt]"
            r"$\bullet$ Para una constante positiva $c = 5$, la\\ "
            r"\hspace*{1.2em}condición $|u| \le c$ acota simétricamente:\\ "
            r"\hspace*{1.2em}${\color{amgold}-c \le u \le c}$.\\[6pt]"
            r"$\bullet$ Tomamos el argumento interior\\ "
            r"\hspace*{1.2em}$u = 3|x| - 1$.\\[6pt]"
            r"$\bullet$ Obtenemos la doble desigualdad lineal:\\ "
            r"\hspace*{1.2em}${\color{amteal}-5 \le 3|x| - 1 \le 5}$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Despeje del Valor Absoluto Interior
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Aislamiento algebraico de } |x|: \\[6pt]"
            r"&\text{Sumamos } 1 \text{ en todos los miembros:} \\[4pt]"
            r"&\quad -5 + 1 \le 3|x| \le 5 + 1 \\[4pt]"
            r"&\quad -4 \le 3|x| \le 6 \\[6pt]"
            r"&\text{Dividiendo entre } 3 > 0 \text{ (preserva el orden):} \\[6pt]"
            r"&\quad \mathbf{{\color{amgreen}-\frac{4}{3} \le |x| \le 2}}"
            r"\end{aligned}",
            font_size=23.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Despeje de } $|x|$:\\[6pt]"
            r"$\bullet$ Sumamos $1$ en los tres miembros por axiomas\\ "
            r"\hspace*{1.2em}de orden en $\mathbb{R}$: $-4 \le 3|x| \le 6$.\\[6pt]"
            r"$\bullet$ Dividimos entre $3 > 0$:\\ "
            r"\hspace*{1.2em}Como $3$ es estrictamente positivo, el sentido\\ "
            r"\hspace*{1.2em}de las desigualdades se preserva sin cambios.\\[6pt]"
            r"$\bullet$ Cotas obtenidas:\\ "
            r"\hspace*{1.2em}${\color{amgreen}-4/3 \le |x| \le 2}$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Conjunción de Condiciones Lógicas
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Desglose en Conjunción Lógica } (\land): \\[6pt]"
            r"&-\frac{4}{3} \le |x| \le 2 \iff \mathbf{\left(|x| \ge -\frac{4}{3}\right) \;\land\; (|x| \le 2)} \\[8pt]"
            r"&\text{El conjunto solución es la intersección } S_1 \cap S_2: \\[6pt]"
            r"&\quad S_1 = \left\{x \in \mathbb{R} : |x| \ge -\frac{4}{3}\right\} \\[5pt]"
            r"&\quad S_2 = \left\{x \in \mathbb{R} : |x| \le 2\right\}"
            r"\end{aligned}",
            font_size=23.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{3. Conjunción de Condiciones:}\\[6pt]"
            r"$\bullet$ Toda doble desigualdad simultánea equivale\\ "
            r"\hspace*{1.2em}estrictamente a una conjunción lógica ($\land$):\\[4pt]"
            r"\hspace*{1.2em}$a \le |x| \le b \iff (|x| \ge a) \land (|x| \le b)$.\\[6pt]"
            r"$\bullet$ Se divide en dos problemas independientes:\\[3pt]"
            r"\hspace*{1.2em}1. Rama 1: Cota inferior $|x| \ge -4/3$.\\[3pt]"
            r"\hspace*{1.2em}2. Rama 2: Cota superior $|x| \le 2$.\\[6pt]"
            r"$\bullet$ La solución global será $CS = S_1 \cap S_2$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Análisis Deductivo de Ramas
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Resolución de cada Rama:} \\[6pt]"
            r"&\mathbf{Rama \; 1:} \quad |x| \ge -\frac{4}{3} \\[4pt]"
            r"&\quad \forall x \in \mathbb{R}: \; |x| \ge 0 > -\frac{4}{3} \implies \mathbf{{\color{amteal}S_1 = \mathbb{R}}} \quad (\text{Universal}) \\[8pt]"
            r"&\mathbf{Rama \; 2:} \quad |x| \le 2 \\[4pt]"
            r"&\quad \iff -2 \le x \le 2 \implies \mathbf{{\color{amgold}S_2 = [-2, 2]}}"
            r"\end{aligned}",
            font_size=23.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Análisis Deductivo de Ramas:}\\[6pt]"
            r"$\bullet$ \textbf{Rama 1 (Cota inferior):}\\[2pt]"
            r"\hspace*{1.2em}Por axioma, $|x| \ge 0$ para todo $x \in \mathbb{R}$.\\[2pt]"
            r"\hspace*{1.2em}Como $0 > -4/3$, la cota se cumple siempre:\\ "
            r"\hspace*{1.2em}${\color{amteal}S_1 = \mathbb{R}}$ (solución universal trivial).\\[6pt]"
            r"$\bullet$ \textbf{Rama 2 (Cota superior):}\\[2pt]"
            r"\hspace*{1.2em}Por propiedad: $|x| \le 2 \iff -2 \le x \le 2$.\\[2pt]"
            r"\hspace*{1.2em}Genera el intervalo cerrado ${\color{amgold}S_2 = [-2, 2]}$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=5.0)

        # ==========================================================
        # PASO 5: Conjunto Solución Final (CS)
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Intersección y Conjunto Solución:} \\[6pt]"
            r"&CS = S_1 \;\cap\; S_2 \\[6pt]"
            r"&CS = \mathbb{R} \;\cap\; [-2, 2] \\[8pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}CS = [-2, 2] = \{x \in \mathbb{R} : -2 \le x \le 2\}}}"
            r"\end{aligned}",
            font_size=24.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Conjunto Solución Concluido:}\\[6pt]"
            r"$\bullet$ Intersecamos la solución universal con el\\ "
            r"\hspace*{1.2em}intervalo acotado:\\[4pt]"
            r"\hspace*{1.2em}$CS = \mathbb{R} \cap [-2, 2] = {\color{amgreen}[-2, 2]}$.\\[6pt]"
            r"$\bullet$ Todo número real en el intervalo cerrado\\ "
            r"\hspace*{1.2em}$[-2, 2]$ satisface la inecuación original.\\[6pt]"
            r"$\bullet$ Los extremos $\pm 2$ producen la igualdad exacta:\\ "
            r"\hspace*{1.2em}$\big|3|\pm 2| - 1\big| = |6 - 1| = 5 \le 5$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen geométrico
        t_card = Tex(
            r"\begin{minipage}{5.8cm}\raggedright "
            r"\textbf{{\color{amteal}Geometría Cartesiana:}}\\[6pt]"
            r"$\bullet$ \textbf{Función par } $f(x) = \big|3|x| - 1\big|$:\\[2pt]"
            r"\hspace*{0.8em}Simétrica, vértice en $(0, 1)$,\\[2pt]"
            r"\hspace*{0.8em}y valles en $(\pm 1/3, 0)$.\\[6pt]"
            r"$\bullet$ \textbf{Recta horizontal } $y = 5$:\\[2pt]"
            r"\hspace*{0.8em}Cortes en $P_1(-2, 5)$ y $P_2(2, 5)$.\\[6pt]"
            r"$\bullet$ \textbf{Zona } $f(x) \le 5$ (curva bajo recta):\\[2pt]"
            r"\hspace*{0.8em}Proyección sobre el eje $X$:\\[2pt]"
            r"\hspace*{0.8em}${\color{amgreen}CS = [-2, 2]}$ (tramo en verde)."
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
            x_range=[-3.5, 3.5, 1],
            y_range=[-1.0, 7.0, 2],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=15,
            labels_font_size=21
        )

        # Curva f(x) = |3|x| - 1|
        curve_f = axes.plot(
            lambda x: np.abs(3.0 * np.abs(x) - 1.0),
            x_range=[-2.4, 2.4],
            color=THEME["highlight"],
            stroke_width=3.2
        )
        lbl_f = MathTex(
            r"f(x) = |3|x|-1|",
            font_size=16.5,
            color=THEME["highlight"]
        ).next_to(axes.c2p(0, 1.0), UP, buff=0.10)

        # Recta horizontal y = 5
        line_g = axes.plot(
            lambda x: 5.0,
            x_range=[-3.2, 3.2],
            color=THEME["secondary"],
            stroke_width=2.5
        )
        lbl_g = MathTex(
            r"y = 5",
            font_size=16.5,
            color=THEME["secondary"]
        ).next_to(axes.c2p(2.5, 5.0), UP, buff=0.10)

        # Puntos de corte (-2, 5) y (2, 5)
        p1 = axes.c2p(-2.0, 5.0)
        p2 = axes.c2p(2.0, 5.0)
        dot1 = Dot(p1, radius=0.07, color=THEME["success"])
        dot2 = Dot(p2, radius=0.07, color=THEME["success"])
        lbl_p1 = MathTex(r"(-2, 5)", font_size=16.5, color=THEME["success"]).next_to(p1, UL, buff=0.10)
        lbl_p2 = MathTex(r"(2, 5)", font_size=16.5, color=THEME["success"]).next_to(p2, UR, buff=0.10)

        # Líneas guía discontinuas desde los puntos de corte al eje X
        proj_l = DashedLine(p1, axes.c2p(-2.0, 0), color=THEME["statement_box"], stroke_width=1.6)
        proj_r = DashedLine(p2, axes.c2p(2.0, 0), color=THEME["statement_box"], stroke_width=1.6)

        # Segmento solución en el eje X: [-2, 2]
        sol_segment = Line(axes.c2p(-2.0, 0), axes.c2p(2.0, 0), color=THEME["success"], stroke_width=5.0)
        dot_sol_l = Dot(axes.c2p(-2.0, 0), radius=0.07, color=THEME["success"])
        dot_sol_r = Dot(axes.c2p(2.0, 0), radius=0.07, color=THEME["success"])
        lbl_cs = MathTex(r"CS = [-2, 2]", font_size=15.0, color=THEME["success"]).next_to(axes.c2p(0, 0), DOWN, buff=0.20)

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

        # Trazado de la curva y la recta horizontal
        self.play(
            Create(curve_f), Write(lbl_f),
            Create(line_g), Write(lbl_g),
            run_time=2.2
        )

        # Marcado de intersecciones y proyección
        self.play(
            FadeIn(dot1), Write(lbl_p1),
            FadeIn(dot2), Write(lbl_p2),
            Create(proj_l), Create(proj_r),
            run_time=1.4
        )

        # Resaltado del intervalo solución [-2, 2] en el eje X
        self.play(
            Create(sol_segment),
            FadeIn(dot_sol_l), FadeIn(dot_sol_r),
            Write(lbl_cs),
            run_time=1.4
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_f, lbl_f,
            line_g, lbl_g,
            dot1, dot2, lbl_p1, lbl_p2,
            proj_l, proj_r,
            sol_segment, dot_sol_l, dot_sol_r, lbl_cs
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
