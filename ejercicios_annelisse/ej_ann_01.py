r"""
Precálculo Universitario · Tutorías Annelisse / Editorial Amarun
Tema: Determinación del Vértice y Cálculo del Rango de Funciones Cuadráticas
Ejercicio 1: Determinar el vértice y hallar el rango de cada función:
      a) f(x) = -9x² - 5
      b) f(x) = (x + 3)² + 4
      c) f(x) = 7x² - 12

Estructura de la Demostración (6 Pasos):
      1. Marco teórico: Forma canónica f(x) = a(x - h)² + k, vértice V(h, k) y criterio de concavidad/rango.
      2. Función a): f(x) = -9(x - 0)² - 5 ⟹ a = -9 < 0, V(0, -5) y Ran(f) = ]-∞, -5].
      3. Función b): f(x) = 1·(x - (-3))² + 4 ⟹ a = 1 > 0, V(-3, 4) y Ran(f) = [4, +∞[.
      4. Función c): f(x) = 7(x - 0)² - 12 ⟹ a = 7 > 0, V(0, -12) y Ran(f) = [-12, +∞[.
      5. Consolidación y matriz comparativa de resultados de los tres literales.
      6. Interpretación geométrica cartesiana: trazado conjunto de las 3 parábolas, ubicación de vértices y cotas de rango.

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


class EjercicioAnn_01(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Annelisse",
            exercise="Ejercicio 1",
            topic="Vértice y Rango de Funciones Cuadráticas",
            font_size=17.5
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 1: Determina el vértice y halla el rango de cada función cuadrática:",
            math_tex=r"{\color{amred}\mathbf{a)} \; f(x) = -9x^2 - 5} \qquad {\color{amteal}\mathbf{b)} \; f(x) = (x+3)^2 + 4} \qquad {\color{amgold}\mathbf{c)} \; f(x) = 7x^2 - 12}",
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
            "1/6: Marco Teórico y Forma Canónica",
            "2/6: Función a) f(x) = -9x² - 5",
            "3/6: Función b) f(x) = (x+3)² + 4",
            "4/6: Función c) f(x) = 7x² - 12",
            "5/6: Consolidación de Resultados",
            "6/6: Gráfica Cartesiana y Verificación"
        ], dot_spacing=0.96, label_font_size=14.0)

        # ==========================================================
        # PASO 1: Marco Teórico de la Forma Canónica y Criterio de Rango
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Forma Canónica y Criterio de Rango:} \\[6pt]"
            r"&\text{Toda función cuadrática se expresa en la forma canónica:} \\[5pt]"
            r"&\quad \mathbf{{\color{amteal}f(x) = a(x - h)^2 + k}}, \quad \text{con vértice en } \mathbf{{\color{amgold}V(h, k)}} \\[7pt]"
            r"&\textbf{Comportamiento según el signo del coeficiente principal } a: \\[5pt]"
            r"&\bullet \ \mathbf{{\color{amgreen}a > 0}} \ (\text{abre hacia arriba } \cup) \implies \text{Mínimo absoluto en } y = k: \\[4pt]"
            r"&\quad \mathbf{\operatorname{Ran}(f) = {\color{amgreen}[k, +\infty[}} \\[6pt]"
            r"&\bullet \ \mathbf{{\color{amred}a < 0}} \ (\text{abre hacia abajo } \cap) \implies \text{Máximo absoluto en } y = k: \\[4pt]"
            r"&\quad \mathbf{\operatorname{Ran}(f) = {\color{amred}]-\infty, k]}}"
            r"\end{aligned}",
            font_size=22.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Fundamento de la Forma Canónica:}\\[6pt]"
            r"$\bullet$ La traslación horizontal de la parábola está dada por ${\color{amgold}h}$ y la vertical por ${\color{amgold}k}$.\\[5pt]"
            r"$\bullet$ Por el axioma de no-negatividad de cuadrados:\\"
            r"\hspace*{1.0em}$\forall x \in \mathbb{R}: \quad (x - h)^2 \ge 0$.\\[5pt]"
            r"$\bullet$ Al multiplicar por el escalar $a$:\\[3pt]"
            r"\hspace*{1.0em}1. Si ${\color{amgreen}a > 0}$, $a(x-h)^2 \ge 0 \implies f(x) \ge k$.\\[3pt]"
            r"\hspace*{1.0em}2. Si ${\color{amred}a < 0}$, $a(x-h)^2 \le 0 \implies f(x) \le k$.\\[5pt]"
            r"$\bullet$ El vértice ${\color{amgold}V(h, k)}$ determina el extremo global."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Función a) f(x) = -9x² - 5
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Función a): } \mathbf{{\color{amred}f(x) = -9x^2 - 5}} \\[6pt]"
            r"&\text{Escritura en forma canónica:} \\[4pt]"
            r"&\quad f(x) = {\color{amred}-9}(x - {\color{amgold}0})^2 + ({\color{amgold}-5}) \\[6pt]"
            r"&\text{Parámetros: } {\color{amred}a = -9 < 0}, \quad {\color{amgold}h = 0}, \quad {\color{amgold}k = -5} \\[6pt]"
            r"&\mathbf{\text{Vértice: }} \mathbf{{\color{amgold}V_a(0, -5)}} \quad (\text{Máximo Absoluto}) \\[7pt]"
            r"&\text{Deducción analítica de rango en } \mathbb{R}: \\[4pt]"
            r"&\quad \forall x \in \mathbb{R}: \ x^2 \ge 0 \implies -9x^2 \le 0 \implies -9x^2 - 5 \le -5 \\[6pt]"
            r"&\therefore \quad \mathbf{\operatorname{Ran}(f_a) = {\color{amgreen}]-\infty, -5]}}"
            r"\end{aligned}",
            font_size=22.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Análisis de $f(x) = -9x^2 - 5$:}\\[6pt]"
            r"$\bullet$ Al carecer de término lineal en $x$, el vértice se sitúa sobre el eje vertical (${\color{amgold}h = 0}$).\\[5pt]"
            r"$\bullet$ El coeficiente ${\color{amred}a = -9 < 0}$ indica que las ramas de la parábola abren hacia abajo ($\cap$).\\[5pt]"
            r"$\bullet$ El vértice es un ${\color{amgold}\text{máximo global}}$ en $y = -5$.\\[5pt]"
            r"$\bullet$ La imagen de la función cubre todos los reales menores o iguales a $-5$:\\[3pt]"
            r"\hspace*{1.0em}${\color{amgreen}\operatorname{Ran}(f_a) = \; ]-\infty, -5]}$.\\[5pt]"
            r"$\bullet$ Vértice confirmado: ${\color{amgold}V_a(0, -5)}$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq2, just2, box_color=THEME["error"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Función b) f(x) = (x + 3)² + 4
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Función b): } \mathbf{{\color{amteal}f(x) = (x + 3)^2 + 4}} \\[6pt]"
            r"&\text{Escritura en forma canónica explícita:} \\[4pt]"
            r"&\quad f(x) = {\color{amteal}1} \cdot (x - ({\color{amgold}-3}))^2 + {\color{amgold}4} \\[6pt]"
            r"&\text{Parámetros: } {\color{amteal}a = 1 > 0}, \quad {\color{amgold}h = -3}, \quad {\color{amgold}k = 4} \\[6pt]"
            r"&\mathbf{\text{Vértice: }} \mathbf{{\color{amgold}V_b(-3, 4)}} \quad (\text{Mínimo Absoluto}) \\[7pt]"
            r"&\text{Deducción analítica de rango en } \mathbb{R}: \\[4pt]"
            r"&\quad \forall x \in \mathbb{R}: \ (x + 3)^2 \ge 0 \implies (x + 3)^2 + 4 \ge 4 \\[6pt]"
            r"&\therefore \quad \mathbf{\operatorname{Ran}(f_b) = {\color{amgreen}[4, +\infty[}}"
            r"\end{aligned}",
            font_size=22.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{3. Análisis de $f(x) = (x + 3)^2 + 4$:}\\[6pt]"
            r"$\bullet$ Ya se encuentra expresada en forma canónica con binomio al cuadrado explícito.\\[5pt]"
            r"$\bullet$ Traslación horizontal de 3 unidades a la izquierda: $x - h = x + 3 \implies {\color{amgold}h = -3}$.\\[5pt]"
            r"$\bullet$ Traslación vertical de 4 unidades arriba: ${\color{amgold}k = 4}$.\\[5pt]"
            r"$\bullet$ Como ${\color{amteal}a = 1 > 0}$, la parábola abre hacia arriba ($\cup$) y $y = 4$ es el ${\color{amgold}\text{mínimo absoluto}}$.\\[5pt]"
            r"$\bullet$ ${\color{amgreen}\operatorname{Ran}(f_b) = [4, +\infty[}$ y vértice ${\color{amgold}V_b(-3, 4)}$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq3, just3, box_color=THEME["secondary"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Función c) f(x) = 7x² - 12
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Función c): } \mathbf{{\color{amgold}f(x) = 7x^2 - 12}} \\[6pt]"
            r"&\text{Escritura en forma canónica:} \\[4pt]"
            r"&\quad f(x) = {\color{amgold}7}(x - {\color{amgold}0})^2 + ({\color{amgold}-12}) \\[6pt]"
            r"&\text{Parámetros: } {\color{amgold}a = 7 > 0}, \quad {\color{amgold}h = 0}, \quad {\color{amgold}k = -12} \\[6pt]"
            r"&\mathbf{\text{Vértice: }} \mathbf{{\color{amgold}V_c(0, -12)}} \quad (\text{Mínimo Absoluto}) \\[7pt]"
            r"&\text{Deducción analítica de rango en } \mathbb{R}: \\[4pt]"
            r"&\quad \forall x \in \mathbb{R}: \ x^2 \ge 0 \implies 7x^2 \ge 0 \implies 7x^2 - 12 \ge -12 \\[6pt]"
            r"&\therefore \quad \mathbf{\operatorname{Ran}(f_c) = {\color{amgreen}[-12, +\infty[}}"
            r"\end{aligned}",
            font_size=22.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Análisis de $f(x) = 7x^2 - 12$:}\\[6pt]"
            r"$\bullet$ Sin término lineal $\implies$ simetría axial respecto al eje de ordenadas (${\color{amgold}h = 0}$).\\[5pt]"
            r"$\bullet$ Coeficiente ${\color{amgold}a = 7 > 0}$: parábola con dilatación vertical que abre hacia arriba ($\cup$).\\[5pt]"
            r"$\bullet$ El vértice constituye un ${\color{amgold}\text{mínimo absoluto}}$ en la cota $y = -12$.\\[5pt]"
            r"$\bullet$ Todos los valores de la imagen son mayores o iguales a $-12$:\\[3pt]"
            r"\hspace*{1.0em}${\color{amgreen}\operatorname{Ran}(f_c) = [-12, +\infty[}$.\\[5pt]"
            r"$\bullet$ Vértice confirmado: ${\color{amgold}V_c(0, -12)}$."
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
            r"&\textbf{\textbf{5. Cuadro Resumen Consolidado (Ejercicio 1):}} \\[7pt]"
            r"&\mathbf{a)} \; f(x) = -9x^2 - 5: \\[3pt]"
            r"&\quad a = -9 < 0 \implies \mathbf{{\color{amgold}V_a(0, -5)}}, \quad \mathbf{\operatorname{Ran}(f_a) = {\color{amgreen}]-\infty, -5]}} \\[6pt]"
            r"&\mathbf{b)} \; f(x) = (x + 3)^2 + 4: \\[3pt]"
            r"&\quad a = 1 > 0 \implies \mathbf{{\color{amgold}V_b(-3, 4)}}, \quad \mathbf{\operatorname{Ran}(f_b) = {\color{amgreen}[4, +\infty[}} \\[6pt]"
            r"&\mathbf{c)} \; f(x) = 7x^2 - 12: \\[3pt]"
            r"&\quad a = 7 > 0 \implies \mathbf{{\color{amgold}V_c(0, -12)}}, \quad \mathbf{\operatorname{Ran}(f_c) = {\color{amgreen}[-12, +\infty[}}"
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Matriz Comparativa de Vértices y Rangos:}\\[6pt]"
            r"$\bullet$ \textbf{Función a):} Abre hacia abajo ($\cap$); vértice en $(0, -5)$, rango acotado superiormente por $-5$.\\[5pt]"
            r"$\bullet$ \textbf{Función b):} Abre hacia arriba ($\cup$); vértice desplazado a $(-3, 4)$, rango con cota inferior $4$.\\[5pt]"
            r"$\bullet$ \textbf{Función c):} Abre hacia arriba ($\cup$); vértice centrado en $(0, -12)$, rango con cota inferior $-12$.\\[5pt]"
            r"$\bullet$ Los 3 literales quedan resueltos de forma analítica rigurosa."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana Conjunta
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen geométrico
        t_card = Tex(
            r"\begin{minipage}{5.8cm}\raggedright "
            r"\textbf{{\color{amteal}Verificación Cartesiana:}}\\[6pt]"
            r"$\bullet$ \textbf{Parábola a) (Roja):}\\[2pt]"
            r"\hspace*{0.8em}$f_a(x) = -9x^2 - 5$.\\[2pt]"
            r"\hspace*{0.8em}Vértice $V_a(0, -5)$ (máx.), $\cap$.\\[6pt]"
            r"$\bullet$ \textbf{Parábola b) (Turquesa):}\\[2pt]"
            r"\hspace*{0.8em}$f_b(x) = (x + 3)^2 + 4$.\\[2pt]"
            r"\hspace*{0.8em}Vértice $V_b(-3, 4)$ (mín.), $\cup$.\\[6pt]"
            r"$\bullet$ \textbf{Parábola c) (Dorada):}\\[2pt]"
            r"\hspace*{0.8em}$f_c(x) = 7x^2 - 12$.\\[2pt]"
            r"\hspace*{0.8em}Vértice $V_c(0, -12)$ (mín.), $\cup$."
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
            x_range=[-5.0, 4.0, 1],
            y_range=[-14.0, 16.0, 4],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=14,
            labels_font_size=20
        )

        # Curva a: f(x) = -9x^2 - 5
        curve_a = axes.plot(
            lambda x: -9.0 * (x**2) - 5.0,
            x_range=[-1.0, 1.0],
            color=THEME["error"],
            stroke_width=3.0
        )
        lbl_a = MathTex(
            r"f_a(x)",
            font_size=16.5,
            color=THEME["error"]
        ).next_to(axes.c2p(0.8, -10.5), RIGHT, buff=0.08)

        # Curva b: f(x) = (x+3)^2 + 4
        curve_b = axes.plot(
            lambda x: (x + 3.0)**2 + 4.0,
            x_range=[-4.8, -0.5],
            color=THEME["secondary"],
            stroke_width=3.0
        )
        lbl_b = MathTex(
            r"f_b(x)",
            font_size=16.5,
            color=THEME["secondary"]
        ).next_to(axes.c2p(-1.0, 8.0), RIGHT, buff=0.08)

        # Curva c: f(x) = 7x^2 - 12
        curve_c = axes.plot(
            lambda x: 7.0 * (x**2) - 12.0,
            x_range=[-1.8, 1.8],
            color=THEME["highlight"],
            stroke_width=3.0
        )
        lbl_c = MathTex(
            r"f_c(x)",
            font_size=16.5,
            color=THEME["highlight"]
        ).next_to(axes.c2p(1.7, 8.0), RIGHT, buff=0.08)

        # Vértices destacados
        va_pt = axes.c2p(0.0, -5.0)
        vb_pt = axes.c2p(-3.0, 4.0)
        vc_pt = axes.c2p(0.0, -12.0)

        dot_va = Dot(va_pt, radius=0.07, color=THEME["success"])
        dot_vb = Dot(vb_pt, radius=0.07, color=THEME["success"])
        dot_vc = Dot(vc_pt, radius=0.07, color=THEME["success"])

        lbl_va = MathTex(r"V_a(0, -5)", font_size=15.0, color=THEME["success"]).next_to(va_pt, RIGHT, buff=0.10)
        lbl_vb = MathTex(r"V_b(-3, 4)", font_size=15.0, color=THEME["success"]).next_to(vb_pt, UP, buff=0.10)
        lbl_vc = MathTex(r"V_c(0, -12)", font_size=15.0, color=THEME["success"]).next_to(vc_pt, DOWN, buff=0.10)

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

        # Trazado progresivo de las 3 curvas
        self.play(
            Create(curve_a), Write(lbl_a),
            Create(curve_b), Write(lbl_b),
            Create(curve_c), Write(lbl_c),
            run_time=2.2
        )

        # Marcado de los 3 vértices
        self.play(
            FadeIn(dot_va), Write(lbl_va),
            FadeIn(dot_vb), Write(lbl_vb),
            FadeIn(dot_vc), Write(lbl_vc),
            run_time=1.8
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_a, lbl_a,
            curve_b, lbl_b,
            curve_c, lbl_c,
            dot_va, dot_vb, dot_vc,
            lbl_va, lbl_vb, lbl_vc
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
