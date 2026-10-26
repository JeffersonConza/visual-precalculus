r"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.30 (Página 109 del libro / Página 128 del PDF)

Tema: Inecuaciones con Radicales (Método del Ejemplo 5.40):
      Resuelve las inecuaciones con radicales en el conjunto de los números reales:
      (I₁): √(x² - 5x + 4) ≥ x - 3,  x ∈ ℝ.
      (I₂): √(x² + 9x + 18) ≥ √(2x) √(3x - 2),  x ∈ ℝ.

Estructura de la Demostración (6 Pasos):
      1. (I₁) Dominio de existencia y análisis de casos:
         RMD: x² - 5x + 4 ≥ 0 ⟺ x ∈ ]-∞, 1] ∪ [4, +∞[. Partición por el signo de x - 3.
      2. (I₁) Resolución de casos y CS₁:
         - Caso A (x < 3): segundo miembro negativo ⟹ S_A = ]-∞, 1].
         - Caso B (x ≥ 3): elevación al cuadrado en [4, +∞[ ⟹ x ≥ 5 ⟹ S_B = [5, +∞[.
         - Unión: CS₁ = ]-∞, 1] ∪ [5, +∞[.
      3. (I₂) Dominio múltiple de existencia:
         Intersección de las tres restricciones de no-negatividad ⟹ D = [2/3, +∞[.
      4. (I₂) Elevación al cuadrado en D:
         x² + 9x + 18 ≥ 2x(3x - 2) = 6x² - 4x ⟹ 5x² - 13x - 18 ≤ 0.
      5. (I₂) Factorización y CS₂:
         (5x - 18)(x + 1) ≤ 0 ⟹ x ∈ [-1, 18/5]. Intersecando con D: CS₂ = [2/3, 18/5].
      6. Interpretación geométrica cartesiana de (I₁): Curva en dos ramas f(x) = √(x² - 5x + 4),
         recta afín g(x) = x - 3, punto de corte P(5, 2) y proyección de CS₁ sobre el eje X.

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


class Ejercicio05_30(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.30",
            topic="Inecuaciones con Radicales",
            font_size=18.0
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 5.30: Resuelve las inecuaciones con radicales en ℝ (Método Ejemplo 5.40):",
            math_tex=r"{\color{amgold}(I_1): \sqrt{x^2 - 5x + 4} \ge x - 3} \quad \text{y} \quad {\color{amteal}(I_2): \sqrt{x^2 + 9x + 18} \ge \sqrt{2x}\,\sqrt{3x - 2}}",
            desc_font_size=20.0,
            math_font_size=21.0,
            arrange_direction=DOWN,
            buff=0.18,
            box_pos=np.array([0.0, 2.45, 0.0]),
            read_time=4.2
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: (I₁) Dominio y Casos",
            "2/6: (I₁) Resolución y CS₁",
            "3/6: (I₂) Dominio Múltiple",
            "4/6: (I₂) Cuadrado de Miembros",
            "5/6: (I₂) Factorización y CS₂",
            "6/6: Gráfica Cartesiana de (I₁)"
        ], dot_spacing=0.96, label_font_size=14.5)

        # ==========================================================
        # PASO 1: (I₁) Dominio de Existencia y Casos de Signo
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\mathbf{(I_1):} \quad \sqrt{x^2 - 5x + 4} \ge x - 3, \quad x \in \mathbb{R} \\[6pt]"
            r"&\text{RMD: } x^2 - 5x + 4 \ge 0 \iff (x - 1)(x - 4) \ge 0 \\[6pt]"
            r"&\implies \mathbf{{\color{amgold}U_1 = \; ]-\infty, 1] \;\cup\; [4, +\infty[}} \\[8pt]"
            r"&\text{Partición según el signo de } x - 3: \\[4pt]"
            r"&\quad \bullet \ \text{Caso A: } x - 3 < 0 \quad \lor \quad \bullet \ \text{Caso B: } x - 3 \ge 0"
            r"\end{aligned}",
            font_size=22.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Inecuación } $(I_1)$: Dominio y Partición:\\[6pt]"
            r"$\bullet$ El radicando debe ser no-negativo (RMD):\\ "
            r"\hspace*{1.2em}$(x - 1)(x - 4) \ge 0 \implies {\color{amgold}U_1 = ]-\infty, 1] \cup [4, +\infty[}$.\\[6pt]"
            r"$\bullet$ Particionamos según el signo del segundo miembro:\\[3pt]"
            r"\hspace*{1.2em}1. Caso A ($x < 3$): segundo miembro negativo.\\ "
            r"\hspace*{1.2em}2. Caso B ($x \ge 3$): ambos miembros no-negativos."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: (I₁) Resolución de Casos y CS₁
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\text{Caso A } (x < 3): \quad \sqrt{\dots} \ge 0 > x - 3 \implies \mathbf{{\color{amteal}S_A = \; ]-\infty, 1]}} \\[6pt]"
            r"&\text{Caso B } (x \ge 3): \quad \text{En } [4, +\infty[, \text{ elevando al cuadrado:} \\[4pt]"
            r"&\quad x^2 - 5x + 4 \ge (x - 3)^2 = x^2 - 6x + 9 \\[4pt]"
            r"&\quad -5x + 4 \ge -6x + 9 \implies \mathbf{{\color{amteal}x \ge 5 \implies S_B = [5, +\infty[}} \\[8pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}CS_1 = S_A \cup S_B = \; ]-\infty, 1] \;\cup\; [5, +\infty[}}"
            r"\end{aligned}",
            font_size=22.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Inecuación } $(I_1)$: Resolución Completa:\\[6pt]"
            r"$\bullet$ \textbf{Caso A ($x < 3$):} Un radical siempre supera\\ "
            r"\hspace*{1.2em}a un valor negativo en $U_1 \implies {\color{amteal}S_A = ]-\infty, 1]}$.\\[6pt]"
            r"$\bullet$ \textbf{Caso B ($x \ge 3$):} En $[4, +\infty[$, elevamos al cuadrado:\\ "
            r"\hspace*{1.2em}$-5x + 4 \ge -6x + 9 \implies x \ge 5 \implies {\color{amteal}S_B = [5, +\infty[}$.\\[6pt]"
            r"$\bullet$ Unión final:\\ "
            r"\hspace*{1.2em}${\color{amgreen}CS_1 = ]-\infty, 1] \cup [5, +\infty[}$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: (I₂) Dominio Múltiple de Existencia
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\mathbf{(I_2):} \quad \sqrt{x^2 + 9x + 18} \ge \sqrt{2x}\,\sqrt{3x - 2} \\[6pt]"
            r"&\text{Condiciones de no-negatividad simultáneas:} \\[4pt]"
            r"&\bullet \ x^2 + 9x + 18 \ge 0 \iff (x + 3)(x + 6) \ge 0 \implies x \in \; ]-\infty, -6] \cup [-3, +\infty[ \\[4pt]"
            r"&\bullet \ 2x \ge 0 \implies x \ge 0 \quad \land \quad 3x - 2 \ge 0 \implies x \ge 2/3 \\[6pt]"
            r"&\therefore \quad \mathbf{{\color{amteal}D = [2/3, +\infty[}} \quad \text{--- [Dominio común]}"
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{3. Inecuación } $(I_2)$: Dominio Múltiple:\\[6pt]"
            r"$\bullet$ Exigimos que los tres radicandos sean $\ge 0$:\\[3pt]"
            r"\hspace*{1.2em}1. $x^2 + 9x + 18 \ge 0 \implies x \le -6 \lor x \ge -3$.\\ "
            r"\hspace*{1.2em}2. $2x \ge 0 \implies x \ge 0$.\\ "
            r"\hspace*{1.2em}3. $3x - 2 \ge 0 \implies x \ge 2/3$.\\[6pt]"
            r"$\bullet$ Intersección simultánea de existencia:\\ "
            r"\hspace*{1.2em}${\color{amteal}D = [2/3, +\infty[}$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: (I₂) Elevación al Cuadrado
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\text{En } D = [2/3, +\infty[, \text{ ambos miembros son } \ge 0: \\[6pt]"
            r"&\left(\sqrt{x^2 + 9x + 18}\right)^2 \ge \left(\sqrt{2x}\,\sqrt{3x - 2}\right)^2 \\[6pt]"
            r"&x^2 + 9x + 18 \ge 2x(3x - 2) = 6x^2 - 4x \\[6pt]"
            r"&0 \ge 5x^2 - 13x - 18 \iff \mathbf{{\color{amgold}5x^2 - 13x - 18 \le 0}}"
            r"\end{aligned}",
            font_size=23.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Inecuación } $(I_2)$: Elevación al Cuadrado:\\[6pt]"
            r"$\bullet$ Dado que $t \mapsto t^2$ es estrictamente creciente\\ "
            r"\hspace*{1.2em}en $[0, +\infty[$, elevamos al cuadrado en $D$:\\[4pt]"
            r"\hspace*{1.2em}$x^2 + 9x + 18 \ge 2x(3x - 2) = 6x^2 - 4x$.\\[6pt]"
            r"$\bullet$ Trasponiendo todos los términos a la derecha:\\ "
            r"\hspace*{1.2em}${\color{amgold}5x^2 - 13x - 18 \le 0}$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=4.8)

        # ==========================================================
        # PASO 5: (I₂) Factorización y CS₂
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&5x^2 - 13x - 18 \le 0 \iff (5x - 18)(x + 1) \le 0 \\[6pt]"
            r"&\text{Raíces: } x = -1 \quad \text{y} \quad x = 18/5 = 3.6 \\[6pt]"
            r"&\implies x \in [-1, 18/5] \\[6pt]"
            r"&\text{Intersecando con el dominio } D = [2/3, +\infty[: \\[6pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}CS_2 = [2/3, 18/5] = [2/3, 3.6]}}"
            r"\end{aligned}",
            font_size=23.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Inecuación } $(I_2)$: Factorización y Solución:\\[6pt]"
            r"$\bullet$ Discriminante $\Delta = (-13)^2 - 4(5)(-18) = 529 = 23^2$.\\[4pt]"
            r"$\bullet$ Factorizamos: $(5x - 18)(x + 1) \le 0 \implies x \in [-1, 18/5]$.\\[6pt]"
            r"$\bullet$ Intersecamos con el dominio real $D = [2/3, +\infty[$:\\[4pt]"
            r"\hspace*{1.2em}${\color{amgreen}CS_2 = [2/3, 18/5] = [2/3, 3.6]}$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana de (I₁)
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen geométrico
        t_card = Tex(
            r"\begin{minipage}{5.8cm}\raggedright "
            r"\textbf{{\color{amteal}Geometría Cartesiana de } $(I_1)$:}\\[6pt]"
            r"$\bullet$ \textbf{Curva radical } $f(x) = \sqrt{x^2 - 5x + 4}$:\\[2pt]"
            r"\hspace*{0.8em}Discontinua en $]1, 4[$, ceros en $1$ y $4$.\\[6pt]"
            r"$\bullet$ \textbf{Recta afín } $g(x) = x - 3$:\\[2pt]"
            r"\hspace*{0.8em}Corte con el eje $Y$ en $(0, -3)$.\\[6pt]"
            r"$\bullet$ \textbf{Punto de corte único } $P(5, 2)$:\\[2pt]"
            r"\hspace*{0.8em}$\sqrt{25 - 25 + 4} = 2 = 5 - 3$.\\[6pt]"
            r"$\bullet$ \textbf{Regiones } $f(x) \ge g(x)$:\\[2pt]"
            r"\hspace*{0.8em}${\color{amgreen}CS_1 = \; ]-\infty, 1] \cup [5, +\infty[}$ (verde)."
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
            x_range=[-2.0, 7.0, 1],
            y_range=[-3.5, 4.5, 1],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=15,
            labels_font_size=21
        )

        # Curva f(x) = √(x² - 5x + 4) en dos ramas
        curve_f_left = axes.plot(
            lambda x: np.sqrt(x**2 - 5.0*x + 4.0),
            x_range=[-1.8, 1.0],
            color=THEME["highlight"],
            stroke_width=3.2
        )
        curve_f_right = axes.plot(
            lambda x: np.sqrt(x**2 - 5.0*x + 4.0),
            x_range=[4.0, 6.8],
            color=THEME["highlight"],
            stroke_width=3.2
        )
        lbl_f = MathTex(
            r"f(x) = \sqrt{x^2-5x+4}",
            font_size=16.5,
            color=THEME["highlight"]
        ).next_to(axes.c2p(4.0, 3.2), UR, buff=0.10)

        # Recta g(x) = x - 3
        line_g = axes.plot(
            lambda x: x - 3.0,
            x_range=[-0.5, 6.8],
            color=THEME["secondary"],
            stroke_width=2.5
        )
        lbl_g = MathTex(
            r"g(x) = x - 3",
            font_size=16.5,
            color=THEME["secondary"]
        ).next_to(axes.c2p(6.2, 3.2), DR, buff=0.10)

        # Punto de corte P(5, 2)
        p_corte = axes.c2p(5.0, 2.0)
        dot_corte = Dot(p_corte, radius=0.07, color=THEME["success"])
        lbl_corte = MathTex(r"P(5, 2)", font_size=16.5, color=THEME["success"]).next_to(p_corte, UL, buff=0.10)

        # Intervalos solución en el eje X: ]-∞, 1] y [5, +∞[
        ray_left = Line(axes.c2p(-1.8, 0), axes.c2p(1.0, 0), color=THEME["success"], stroke_width=4.8)
        dot_1 = Dot(axes.c2p(1.0, 0), radius=0.07, color=THEME["success"])
        ray_right = Line(axes.c2p(5.0, 0), axes.c2p(6.8, 0), color=THEME["success"], stroke_width=4.8)
        dot_5 = Dot(axes.c2p(5.0, 0), radius=0.07, color=THEME["success"])

        lbl_cs_x = MathTex(
            r"CS_1 = \; ]-\infty, 1] \cup [5, +\infty[",
            font_size=14.5,
            color=THEME["success"]
        ).next_to(axes.c2p(2.5, 0), DOWN, buff=0.20)

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
            Create(curve_f_left), Create(curve_f_right), Write(lbl_f),
            Create(line_g), Write(lbl_g),
            run_time=2.2
        )

        # Marcado de intersección y regiones solución
        self.play(
            FadeIn(dot_corte), Write(lbl_corte),
            Create(ray_left), FadeIn(dot_1),
            Create(ray_right), FadeIn(dot_5),
            Write(lbl_cs_x),
            run_time=1.6
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_f_left, curve_f_right, lbl_f,
            line_g, lbl_g,
            dot_corte, lbl_corte,
            ray_left, dot_1, ray_right, dot_5, lbl_cs_x
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
