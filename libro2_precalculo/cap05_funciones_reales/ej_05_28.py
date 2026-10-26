r"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.28 (Página 109 del libro / Página 128 del PDF)

Tema: Demostración de la Desigualdad Triangular Inversa:
      Sean x, y ∈ ℝ. Probar rigurosamente que:
      ||x| - |y|| ≤ |x - y|.

Estructura de la Demostración (6 Pasos):
      1. Criterio de acotación simétrica: |u| ≤ c ⟺ -c ≤ u ≤ c con u = |x| - |y| y c = |x - y| ≥ 0.
      2. Cota superior: x = (x - y) + y ⟹ |x| ≤ |x - y| + |y| ⟹ |x| - |y| ≤ |x - y|.
      3. Descomposición simétrica de |y|: y = (y - x) + x ⟹ |y| - |x| ≤ |y - x| = |x - y|.
      4. Cota inferior: |y| - |x| ≤ |x - y| ⟹ -(|x| - |y|) ≤ |x - y| ⟹ -|x - y| ≤ |x| - |y|.
      5. Integración y conclusión: -|x - y| ≤ |x| - |y| ≤ |x - y| ⟹ ||x| - |y|| ≤ |x - y| ■.
      6. Interpretación geométrica cartesiana: Comparación métrica de h(x) = ||x| - 2|
         frente a la distancia d(x) = |x - 2| en ℝ (coincidencia en x ≥ 0 y cota estricta en x < 0).

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


class Ejercicio05_28(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.28",
            topic="Desigualdad Triangular Inversa",
            font_size=18.0
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 5.28: Sean x, y números reales cualesquiera. Probar que:",
            math_tex=r"{\color{amgold}\big| |x| - |y| \big|} \le {\color{amteal}|x - y|}, \quad \forall x, y \in \mathbb{R}",
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
            "1/6: Criterio de Acotación",
            "2/6: Cota Superior (|x| - |y|)",
            "3/6: Descomposición Simétrica",
            "4/6: Cota Inferior (-|x - y|)",
            "5/6: Integración y Conclusión",
            "6/6: Comparación Geométrica"
        ], dot_spacing=0.96, label_font_size=14.5)

        # ==========================================================
        # PASO 1: Criterio de Acotación Simétrica
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Criterio de Acotación Simétrica:} \\[6pt]"
            r"&\forall u \in \mathbb{R}, \; c \ge 0: \quad \mathbf{{\color{amgold}|u| \le c \iff -c \le u \le c}} \\[8pt]"
            r"&\text{Haciendo } u = |x| - |y| \quad \text{y} \quad c = |x - y| \ge 0: \\[6pt]"
            r"&\quad \mathbf{{\color{amteal}\big| |x| - |y| \big| \le |x - y| \iff -|x - y| \le |x| - |y| \le |x - y|}}"
            r"\end{aligned}",
            font_size=23.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Criterio de Acotación:}\\[6pt]"
            r"$\bullet$ Para probar una cota del tipo $|u| \le c$,\\ "
            r"\hspace*{1.2em}basta demostrar la doble desigualdad:\\ "
            r"\hspace*{1.2em}${\color{amgold}-c \le u \le c}$.\\[6pt]"
            r"$\bullet$ Asignamos $u = |x| - |y|$ y $c = |x - y| \ge 0$.\\[6pt]"
            r"$\bullet$ El objetivo se desdobla en probar:\\ "
            r"\hspace*{1.2em}1. Cota superior: $|x| - |y| \le |x - y|$.\\ "
            r"\hspace*{1.2em}2. Cota inferior: $-|x - y| \le |x| - |y|$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Cota Superior (|x| - |y| ≤ |x - y|)
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Demostración de la Cota Superior:} \\[6pt]"
            r"&x = (x - y) + y \quad (\text{Artificio aditivo } -y + y) \\[6pt]"
            r"&|x| = |(x - y) + y| \le |x - y| + |y| \quad (\text{Desig. Triangular}) \\[6pt]"
            r"&\text{Restando } |y| \text{ en ambos miembros:} \\[6pt]"
            r"&\quad \mathbf{{\color{amgreen}|x| - |y| \le |x - y|}} \quad \text{--- [Cota Superior]}"
            r"\end{aligned}",
            font_size=23.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Cota Superior:}\\[6pt]"
            r"$\bullet$ Expresamos $x$ como la suma $(x - y) + y$.\\[6pt]"
            r"$\bullet$ Aplicamos la desigualdad triangular directa:\\ "
            r"\hspace*{1.2em}$|a + b| \le |a| + |b|$\\ "
            r"\hspace*{1.2em}con $a = x - y$ y $b = y$.\\[6pt]"
            r"$\bullet$ Restamos $|y|$ miembro a miembro:\\ "
            r"\hspace*{1.2em}${\color{amgreen}|x| - |y| \le |x - y|}$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Descomposición Simétrica de |y|
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Intercambio Simétrico de Variables:} \\[6pt]"
            r"&y = (y - x) + x \quad (\text{Artificio aditivo } -x + x) \\[6pt]"
            r"&|y| = |(y - x) + x| \le |y - x| + |x| \\[6pt]"
            r"&\text{Por simetría métrica: } |y - x| = |-(x - y)| = |x - y|: \\[6pt]"
            r"&|y| \le |x - y| + |x| \implies \mathbf{{\color{amteal}|y| - |x| \le |x - y|}}"
            r"\end{aligned}",
            font_size=23.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{3. Descomposición Simétrica:}\\[6pt]"
            r"$\bullet$ Intercambiamos los roles de $x$ e $y$:\\ "
            r"\hspace*{1.2em}$y = (y - x) + x$.\\[6pt]"
            r"$\bullet$ Por simetría métrica del valor absoluto:\\ "
            r"\hspace*{1.2em}$|y - x| = |-(x - y)| = |x - y|$.\\[6pt]"
            r"$\bullet$ Aplicando la desigualdad triangular y restando $|x|$:\\ "
            r"\hspace*{1.2em}${\color{amteal}|y| - |x| \le |x - y|}$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Cota Inferior (-|x - y| ≤ |x| - |y|)
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Obtención de la Cota Inferior:} \\[6pt]"
            r"&|y| - |x| \le |x - y| \\[6pt]"
            r"&-(|x| - |y|) \le |x - y| \\[6pt]"
            r"&\text{Multiplicando por } -1 \text{ (se invierte el sentido):} \\[6pt]"
            r"&|x| - |y| \ge -|x - y| \iff \mathbf{{\color{amgold}-|x - y| \le |x| - |y|}}"
            r"\end{aligned}",
            font_size=23.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Cota Inferior:}\\[6pt]"
            r"$\bullet$ Notamos la identidad fundamental:\\ "
            r"\hspace*{1.2em}$|y| - |x| = -(|x| - |y|)$.\\[6pt]"
            r"$\bullet$ Al multiplicar por $-1$, el sentido\\ "
            r"\hspace*{1.2em}de la desigualdad se invierte en $\mathbb{R}$:\\ "
            r"\hspace*{1.2em}$|x| - |y| \ge -|x - y|$.\\[6pt]"
            r"$\bullet$ Obtenemos la cota inferior:\\ "
            r"\hspace*{1.2em}${\color{amgold}-|x - y| \le |x| - |y|}$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=4.8)

        # ==========================================================
        # PASO 5: Integración y Conclusión
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Cadena de Desigualdades y Conclusión:} \\[6pt]"
            r"&-|x - y| \le |x| - |y| \quad \land \quad |x| - |y| \le |x - y| \\[8pt]"
            r"&\implies \mathbf{{\color{amteal}-|x - y| \le |x| - |y| \le |x - y|}} \\[8pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}\big| |x| - |y| \big| \le |x - y|}} \quad \blacksquare"
            r"\end{aligned}",
            font_size=24.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Conclusión Formal:}\\[6pt]"
            r"$\bullet$ Unificamos la cota inferior del Paso 4\\ "
            r"\hspace*{1.2em}con la cota superior del Paso 2:\\[4pt]"
            r"\hspace*{1.2em}${\color{amteal}-|x - y| \le |x| - |y| \le |x - y|}$.\\[6pt]"
            r"$\bullet$ Por el criterio de acotación del Paso 1, concluimos:\\[4pt]"
            r"\hspace*{1.2em}${\color{amgreen}\big| |x| - |y| \big| \le |x - y|}$.\\[6pt]"
            r"$\bullet$ Válido para cualesquiera $x, y \in \mathbb{R}$."
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
            r"\textbf{{\color{amteal}Comparación Métrica (} $y = 2$ fijo):}\\[6pt]"
            r"$\bullet$ \textbf{Distancia euclídea usual:}\\[2pt]"
            r"\hspace*{0.8em}$d(x) = |x - 2|$ con vértice en $(2, 0)$.\\[6pt]"
            r"$\bullet$ \textbf{Diferencia de módulos:}\\[2pt]"
            r"\hspace*{0.8em}$h(x) = \big| |x| - 2 \big|$ con cúspide en $(0, 2)$.\\[6pt]"
            r"$\bullet$ \textbf{Comportamiento en } $\mathbb{R}$:\\[2pt]"
            r"\hspace*{0.8em}$x \ge 0: \; h(x) = d(x)$ (coincidencia exact),\\[2pt]"
            r"\hspace*{0.8em}$x < 0: \; h(x) < d(x)$ (desigualdad estricta).\\[6pt]"
            r"$\bullet$ La curva $h(x)$ jamás supera a $d(x)$."
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
            x_range=[-4.0, 5.0, 1],
            y_range=[-1.0, 6.0, 1],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=15,
            labels_font_size=21
        )

        # Curva de cota superior: d(x) = |x - 2|
        curve_d = axes.plot(
            lambda x: np.abs(x - 2.0),
            x_range=[-3.8, 4.8],
            color=THEME["secondary"],
            stroke_width=2.6
        )
        lbl_d = MathTex(
            r"d(x) = |x - 2|",
            font_size=16.5,
            color=THEME["secondary"]
        ).next_to(axes.c2p(-3.0, 5.0), RIGHT, buff=0.10)

        # Curva acotada: h(x) = ||x| - 2|
        curve_h = axes.plot(
            lambda x: np.abs(np.abs(x) - 2.0),
            x_range=[-3.8, 4.8],
            color=THEME["highlight"],
            stroke_width=3.2
        )
        lbl_h = MathTex(
            r"h(x) = \big| |x| - 2 \big|",
            font_size=16.5,
            color=THEME["highlight"]
        ).next_to(axes.c2p(0, 2.0), UP, buff=0.10)

        # Puntos notables: vértice en (2,0) y cúspide en (0,2)
        p_corte = axes.c2p(2.0, 0.0)
        p_cusp = axes.c2p(0.0, 2.0)
        dot_corte = Dot(p_corte, radius=0.07, color=THEME["success"])
        dot_cusp = Dot(p_cusp, radius=0.07, color=THEME["highlight"])

        lbl_corte = MathTex(r"(2, 0)", font_size=16.5, color=THEME["success"]).next_to(p_corte, DOWN, buff=0.10)
        lbl_cusp = MathTex(r"(0, 2)", font_size=16.5, color=THEME["highlight"]).next_to(p_cusp, LEFT, buff=0.10)

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

        # Trazado de ambas curvas
        self.play(
            Create(curve_d), Write(lbl_d),
            Create(curve_h), Write(lbl_h),
            run_time=2.2
        )

        # Marcado de puntos de coincidencia y cúspide
        self.play(
            FadeIn(dot_corte), Write(lbl_corte),
            FadeIn(dot_cusp), Write(lbl_cusp),
            run_time=1.4
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_d, lbl_d,
            curve_h, lbl_h,
            dot_corte, dot_cusp,
            lbl_corte, lbl_cusp
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
