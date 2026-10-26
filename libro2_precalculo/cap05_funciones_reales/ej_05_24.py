r"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.24 (Página 108 del libro / Página 127 del PDF)

Tema: Inecuación con Valor Absoluto Anidado:
      Determinar si A ⊆ ℝ es el conjunto solución de:
      ||x| - 5| ≥ 3,  x ∈ ℝ,  A = ]-∞, -8] ∪ [-2, 2] ∪ [8, +∞[.

Estructura de la Demostración (6 Pasos):
      1. Desdoblamiento del valor absoluto exterior: |u| ≥ 3 ⟺ u ≤ -3 ∨ u ≥ 3 con u = |x| - 5.
      2. Rama Interior: |x| - 5 ≤ -3 ⟹ |x| ≤ 2 ⟹ CS₁ = [-2, 2].
      3. Rama Exterior: |x| - 5 ≥ 3 ⟹ |x| ≥ 8 ⟹ CS₂ = ]-∞, -8] ∪ [8, +∞[.
      4. Unión de soluciones: CS = CS₁ ∪ CS₂ = ]-∞, -8] ∪ [-2, 2] ∪ [8, +∞[.
      5. Veredicto final: CS = A ⟹ VERDADERO.
      6. Interpretación geométrica cartesiana: Curva en forma de 'W' f(x) = ||x| - 5|,
         recta y = 3, y los 3 intervalos solución proyectados sobre el eje X.

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


class Ejercicio05_24(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.24",
            topic="Inecuación con Valor Absoluto Anidado",
            font_size=18.0
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 5.24: Determina si A es el conjunto solución de la inecuación:",
            math_tex=r"{\color{amgold}||x| - 5| \ge 3}, \quad x \in \mathbb{R} \quad \implies \quad {\color{amteal}A = \; ]-\infty, -8] \;\cup\; [-2, 2] \;\cup\; [8, +\infty[}",
            desc_font_size=20.0,
            math_font_size=23.0,
            arrange_direction=DOWN,
            buff=0.18,
            box_pos=np.array([0.0, 2.45, 0.0]),
            read_time=4.2
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Desdoblamiento Exterior",
            "2/6: Rama Interior (|x| ≤ 2)",
            "3/6: Rama Exterior (|x| ≥ 8)",
            "4/6: Unión de Intervalos",
            "5/6: Veredicto Final (CS = A)",
            "6/6: Gráfica de ||x|-5| ≥ 3"
        ], dot_spacing=0.96, label_font_size=14.5)

        # ==========================================================
        # PASO 1: Desdoblamiento del Valor Absoluto Exterior
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Desdoblamiento del Valor Absoluto Exterior:} \\[7pt]"
            r"&\text{Propiedad: } \forall u \in \mathbb{R}, \ c > 0: \\[5pt]"
            r"&\quad |u| \ge c \iff \mathbf{{\color{amgold}u \le -c \quad \lor \quad u \ge c}} \\[8pt]"
            r"&\text{Sustituyendo el argumento } u = |x| - 5 \text{ y } c = 3: \\[6pt]"
            r"&\quad \mathbf{{\color{amteal}|x| - 5 \le -3}} \quad \lor \quad \mathbf{{\color{amteal}|x| - 5 \ge 3}}"
            r"\end{aligned}",
            font_size=24.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Desdoblamiento Exterior:}\\[6pt]"
            r"$\bullet$ Aplicamos la propiedad de orden en valor absoluto:\\ "
            r"\hspace*{1.2em}$|u| \ge c \iff u \le -c \lor u \ge c$.\\[6pt]"
            r"$\bullet$ La distancia al origen debe ser al menos $3$:\\ "
            r"\hspace*{1.2em}$u$ queda fuera del intervalo abierto $]-3, 3[$.\\[6pt]"
            r"$\bullet$ Obtenemos dos ramas independientes vinculadas\\ "
            r"\hspace*{1.2em}por la disyunción lógica ($\lor$)."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Rama Interior (|x| - 5 ≤ -3)
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Rama Interior } (|x| - 5 \le -3): \\[7pt]"
            r"&|x| - 5 \le -3 \iff |x| \le 5 - 3 \\[6pt]"
            r"&\quad \mathbf{{\color{amorange}|x| \le 2}} \\[8pt]"
            r"&\text{Por acotación bilateral en valor absoluto:} \\[6pt]"
            r"&\quad |x| \le 2 \iff -2 \le x \le 2 \\[8pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}CS_1 = [-2, 2]}}"
            r"\end{aligned}",
            font_size=24.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Resolución de la Rama Interior:}\\[6pt]"
            r"$\bullet$ Despejamos el valor absoluto sumando $5$:\\ "
            r"\hspace*{1.2em}$|x| \le 2$.\\[6pt]"
            r"$\bullet$ Aplicamos la propiedad de vecindad cerrada:\\ "
            r"\hspace*{1.2em}$|x| \le d \iff -d \le x \le d$.\\[6pt]"
            r"$\bullet$ Obtenemos el intervalo cerrado central:\\ "
            r"\hspace*{1.2em}${\color{amgreen}CS_1 = [-2, 2]}$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Rama Exterior (|x| - 5 ≥ 3)
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Rama Exterior } (|x| - 5 \ge 3): \\[7pt]"
            r"&|x| - 5 \ge 3 \iff |x| \ge 3 + 5 \\[6pt]"
            r"&\quad \mathbf{{\color{amteal}|x| \ge 8}} \\[8pt]"
            r"&\text{Desdoblando el valor absoluto en } \mathbb{R}: \\[6pt]"
            r"&\quad |x| \ge 8 \iff x \le -8 \quad \lor \quad x \ge 8 \\[8pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}CS_2 = \; ]-\infty, -8] \;\cup\; [8, +\infty[}}"
            r"\end{aligned}",
            font_size=24.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{3. Resolución de la Rama Exterior:}\\[6pt]"
            r"$\bullet$ Despejamos sumando $5$ a ambos lados:\\ "
            r"\hspace*{1.2em}$|x| \ge 8$.\\[6pt]"
            r"$\bullet$ Aplicamos la propiedad exterior:\\ "
            r"\hspace*{1.2em}$|x| \ge 8 \iff x \le -8 \lor x \ge 8$.\\[6pt]"
            r"$\bullet$ Obtenemos dos rayos infinitos cerrados:\\ "
            r"\hspace*{1.2em}${\color{amgreen}CS_2 = \; ]-\infty, -8] \cup [8, +\infty[}$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Unión de las Ramas (Conjunto Solución)
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Unión Lógica de Soluciones:} \\[7pt]"
            r"&CS = CS_1 \;\cup\; CS_2 \\[8pt]"
            r"&= [-2, 2] \;\cup\; \left( ]-\infty, -8] \;\cup\; [8, +\infty[ \right) \\[9pt]"
            r"&\text{Ordenando de izquierda a derecha en } \mathbb{R}: \\[6pt]"
            r"&\quad \mathbf{{\color{amgold}CS = \; ]-\infty, -8] \;\cup\; [-2, 2] \;\cup\; [8, +\infty[}}"
            r"\end{aligned}",
            font_size=24.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Unión de Intervalos:}\\[6pt]"
            r"$\bullet$ El conectivo lógico disyuntivo ($\lor$) entre\\ "
            r"\hspace*{1.2em}ambas ramas exige la unión conjuntista:\\[4pt]"
            r"\hspace*{1.2em}$CS = CS_1 \cup CS_2$.\\[6pt]"
            r"$\bullet$ Los intervalos son mutuamente disyuntos.\\[6pt]"
            r"$\bullet$ Ordenamos canónicamente en la recta real:\\ "
            r"\hspace*{1.2em}${\color{amgold}CS = \; ]-\infty, -8] \cup [-2, 2] \cup [8, +\infty[}$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=4.8)

        # ==========================================================
        # PASO 5: Veredicto Final (CS = A)
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Veredicto Final:} \\[7pt]"
            r"&CS = \; ]-\infty, -8] \;\cup\; [-2, 2] \;\cup\; [8, +\infty[ \\[8pt]"
            r"&\text{Comparando con el conjunto propuesto } A: \\[6pt]"
            r"&\quad A = \; ]-\infty, -8] \;\cup\; [-2, 2] \;\cup\; [8, +\infty[ \\[9pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}CS = A \implies \text{La afirmación es VERDADERA}}} \quad \blacksquare"
            r"\end{aligned}",
            font_size=24.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Veredicto Formal:}\\[6pt]"
            r"$\bullet$ Contrastamos el conjunto solución analítico $CS$\\ "
            r"\hspace*{1.2em}con el conjunto propuesto $A$ del libro.\\[6pt]"
            r"$\bullet$ Se constata una coincidencia exacta en todos\\ "
            r"\hspace*{1.2em}los intervalos y puntos frontera.\\[6pt]"
            r"$\bullet$ \textbf{Veredicto}: ${\color{amgreen}\textbf{VERDADERO}}$. $\blacksquare$"
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
            r"\textbf{{\color{amteal}Geometría de } $\mathbf{||x| - 5| \ge 3}$:}\\[6pt]"
            r"$\bullet$ \textbf{Curva en W } $f(x) = ||x| - 5|$:\\[2pt]"
            r"\hspace*{0.8em}Función par simétrica en el eje Y.\\[2pt]"
            r"\hspace*{0.8em}Vértice superior en $(0, 5)$.\\[2pt] "
            r"\hspace*{0.8em}Valles en el eje X: $(\pm 5, 0)$.\\[6pt]"
            r"$\bullet$ \textbf{Recta horizontal } $y = 3$:\\[2pt]"
            r"\hspace*{0.8em}Cortes en $x \in \{-8, -2, 2, 8\}$.\\[6pt]"
            r"$\bullet$ \textbf{Regiones } $f(x) \ge 3$:\\[2pt]"
            r"\hspace*{0.8em}$]-\infty, -8] \cup [-2, 2] \cup [8, +\infty[$.\\[2pt]"
            r"\hspace*{0.8em}(Tres zonas en verde sobre el eje X)."
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
            x_range=[-10.0, 10.0, 2],
            y_range=[-1.0, 7.0, 2],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=15,
            labels_font_size=21
        )

        # Curva en W: f(x) = ||x| - 5|
        curve_f = axes.plot(
            lambda x: np.abs(np.abs(x) - 5.0),
            x_range=[-9.8, 9.8],
            color=THEME["highlight"],
            stroke_width=3.0
        )
        lbl_f = MathTex(
            r"f(x) = ||x|-5|",
            font_size=16.5,
            color=THEME["highlight"]
        ).next_to(axes.c2p(0, 5.0), UP, buff=0.10)

        # Recta horizontal y = 3
        horiz_line = axes.plot(
            lambda x: 3.0,
            x_range=[-9.8, 9.8],
            color=THEME["secondary"],
            stroke_width=2.4
        )
        lbl_horiz = MathTex(
            r"y = 3",
            font_size=16.5,
            color=THEME["secondary"]
        ).next_to(axes.c2p(7.0, 3.0), UP, buff=0.10)

        # 4 Puntos de intersección en y = 3
        pts_inter = [-8.0, -2.0, 2.0, 8.0]
        dots_inter = VGroup(*[
            Dot(axes.c2p(x, 3.0), radius=0.065, color=THEME["success"])
            for x in pts_inter
        ])

        # Resaltado de los 3 intervalos solución sobre el eje X
        ray_left = Line(
            axes.c2p(-9.8, 0),
            axes.c2p(-8.0, 0),
            color=THEME["success"],
            stroke_width=4.8
        )
        seg_mid = Line(
            axes.c2p(-2.0, 0),
            axes.c2p(2.0, 0),
            color=THEME["success"],
            stroke_width=4.8
        )
        ray_right = Line(
            axes.c2p(8.0, 0),
            axes.c2p(9.8, 0),
            color=THEME["success"],
            stroke_width=4.8
        )

        dot_b1 = Dot(axes.c2p(-8.0, 0), radius=0.065, color=THEME["success"])
        dot_b2 = Dot(axes.c2p(-2.0, 0), radius=0.065, color=THEME["success"])
        dot_b3 = Dot(axes.c2p(2.0, 0), radius=0.065, color=THEME["success"])
        dot_b4 = Dot(axes.c2p(8.0, 0), radius=0.065, color=THEME["success"])

        lbl_sol = MathTex(
            r"CS = \; ]-\infty, -8] \cup [-2, 2] \cup [8, +\infty[",
            font_size=14.5,
            color=THEME["success"]
        ).next_to(axes.c2p(0, 0), DOWN, buff=0.20)

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
            Create(horiz_line), Write(lbl_horiz),
            run_time=2.0
        )

        # Marcado de intersecciones y regiones solución
        self.play(
            FadeIn(dots_inter),
            Create(ray_left), Create(seg_mid), Create(ray_right),
            FadeIn(dot_b1), FadeIn(dot_b2), FadeIn(dot_b3), FadeIn(dot_b4),
            Write(lbl_sol),
            run_time=1.8
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_f, lbl_f,
            horiz_line, lbl_horiz,
            dots_inter,
            ray_left, seg_mid, ray_right,
            dot_b1, dot_b2, dot_b3, dot_b4,
            lbl_sol
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
