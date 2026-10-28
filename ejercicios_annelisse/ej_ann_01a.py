r"""
Precálculo Universitario · Tutorías Annelisse / Editorial Amarun
Capítulo: Funciones Reales y Gráficas
Ejercicio 1.a: Análisis Completo, Vértice y Rango de la Función Cuadrática
               f(x) = -9x² - 5

Estructura de la Demostración (8 Pasos):
      1. Dominio polinómico en ℝ y concavidad negativa (a = -9 < 0 ⟹ parábola cóncava hacia abajo).
      2. Forma canónica f(x) = -9(x - 0)² - 5 y determinación del vértice V(0, -5) (máximo absoluto).
      3. Simetría par: f(-x) = f(x) y eje de simetría axial x = 0 (eje de ordenadas Y).
      4. Cortes con los ejes coordenados: corte Y en (0, -5); sin cortes en el eje X (Δ = -180 < 0).
      5. Signos y monotonía: estrictamente negativa en ℝ, creciente en ]-∞, 0] y decreciente en [0, +∞[.
      6. Deducción analítica formal del rango: x² ≥ 0 ⟹ -9x² - 5 ≤ -5 ⟹ Ran(f) = ]-∞, -5].
      7. Tabla de valores simétricos notables y síntesis institucional de propiedades.
      8. Trazado cartesiano riguroso: curva f(x), vértice V(0, -5), eje axial y franja vertical del rango.

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica en 8 pasos con tipografía LaTeX HD generosa y legible.
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


class EjercicioAnn_01a(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Annelisse",
            exercise="Ejercicio 1.a",
            topic="Vértice, Rango y Análisis de f(x) = -9x² - 5",
            font_size=17.0
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 1.a: Determine el vértice, rango y propiedades de la función cuadrática:",
            math_tex=r"{\color{amred}f(x) = -9x^2 - 5}, \quad x \in \mathbb{R}",
            desc_font_size=20.0,
            math_font_size=28.0,
            arrange_direction=DOWN,
            buff=0.18,
            box_pos=np.array([0.0, 2.45, 0.0]),
            read_time=3.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (8 pasos unificados)
        # ==========================================================
        self.setup_progress_bar([
            "1/8: Dominio y Concavidad",
            "2/8: Forma Canónica y Vértice",
            "3/8: Simetría Par y Eje Axial",
            "4/8: Cortes con los Ejes",
            "5/8: Signos y Monotonía",
            "6/8: Deducción Formal del Rango",
            "7/8: Tabla de Puntos Notables",
            "8/8: Trazado Cartesiano y Rango"
        ], dot_spacing=0.82, label_font_size=14.0)

        # ==========================================================
        # PASO 1: Dominio y Concavidad Polinómica
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Dominio y Concavidad Polinómica:} \\[6pt]"
            r"&\text{Al ser } {\color{amred}f(x) = -9x^2 - 5} \text{ un polinomio cuadrático en } \mathbb{R}: \\[4pt]"
            r"&\quad \mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R}} = {\color{amgreen}]-\infty, +\infty[}} \\[6pt]"
            r"&\textbf{Identificación de Coeficientes } (ax^2 + bx + c): \\[4pt]"
            r"&\quad {\color{amred}a = -9}, \quad {\color{amteal}b = 0}, \quad {\color{amgold}c = -5} \\[6pt]"
            r"&\text{Como } {\color{amred}a = -9 < 0} \implies \text{Parábola cóncava hacia abajo } (\cap). \\[4pt]"
            r"&\implies \text{El vértice } {\color{amgold}V} \text{ constituye un } \mathbf{\text{Máximo Absoluto Global}}."
            r"\end{aligned}",
            font_size=22.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Dominio y Concavidad:}\\[6pt]"
            r"$\bullet$ Toda función polinómica cuadrática está definida en todo $\mathbb{R}$.\\[5pt]"
            r"$\bullet$ Coeficiente cuadrático: ${\color{amred}a = -9 < 0}$.\\[5pt]"
            r"$\bullet$ La concavidad negativa determina apertura de ramas hacia abajo ($\cap$).\\[5pt]"
            r"$\bullet$ El vértice representará la cota superior global (máximo absoluto de la función)."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=3.6)

        # ==========================================================
        # PASO 2: Forma Canónica y Vértice V(h, k)
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Forma Canónica y Vértice } V(h, k): \\[6pt]"
            r"&\text{Expresión de traslación canónica } f(x) = a(x - h)^2 + k: \\[4pt]"
            r"&\quad f(x) = {\color{amred}-9}(x - {\color{amgold}0})^2 + ({\color{amgold}-5}) \\[6pt]"
            r"&\text{Cálculo analítico de coordenadas:} \\[4pt]"
            r"&\quad {\color{amgold}h} = -\frac{b}{2a} = -\frac{0}{2(-9)} = \mathbf{{\color{amgold}0}} \\[4pt]"
            r"&\quad {\color{amgold}k} = f(h) = f(0) = -9(0)^2 - 5 = \mathbf{{\color{amgold}-5}} \\[6pt]"
            r"&\therefore \quad \mathbf{\text{Vértice: }} \mathbf{{\color{amgold}V(0, -5)}} \quad (\text{Sobre el eje vertical } Y)"
            r"\end{aligned}",
            font_size=22.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Vértice y Traslación:}\\[6pt]"
            r"$\bullet$ Al no existir término lineal en $x$ ($b = 0$), el eje de simetría coincide con el eje $Y$ ($h = 0$).\\[5pt]"
            r"$\bullet$ Traslación vertical pura: la parábola matriz $y = -9x^2$ se desplaza $5$ unidades hacia abajo ($k = -5$).\\[5pt]"
            r"$\bullet$ Vértice confirmado: ${\color{amgold}V(0, -5)}$ (punto más alto de la trayectoria)."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=3.6)

        # ==========================================================
        # PASO 3: Simetría Par y Eje Axial
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Simetría Par y Eje Axial:} \\[6pt]"
            r"&\text{Evaluando la función en } -x: \\[4pt]"
            r"&\quad f(-x) = -9(-x)^2 - 5 = -9x^2 - 5 = \mathbf{{\color{amteal}f(x)}} \\[6pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}f(-x) = f(x) \implies f \text{ es una función PAR}}} \\[6pt]"
            r"&\textbf{Propiedades geométricas de paridad:} \\[4pt]"
            r"&\bullet \ \text{Simetría axial bilateral respecto al eje } Y. \\[4pt]"
            r"&\bullet \ \mathbf{\text{Eje de Simetría: }} \mathbf{{\color{amgold}x = 0}}. \\[4pt]"
            r"&\bullet \ \forall x_0 \in \mathbb{R}: \quad f(-x_0) = f(x_0)."
            r"\end{aligned}",
            font_size=22.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{3. Paridad y Simetría:}\\[6pt]"
            r"$\bullet$ El exponente par $(-x)^2 = x^2$ preserva idéntica la regla de correspondencia.\\[5pt]"
            r"$\bullet$ La paridad matemática implica que el eje de ordenadas es un espejo para la curva.\\[5pt]"
            r"$\bullet$ Eje axial de simetría: recta vertical ${\color{amgold}x = 0}$.\\[5pt]"
            r"$\bullet$ Simplifica el análisis al requerir estudiar solo $x \ge 0$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq3, just3, box_color=THEME["statement_box"], advance_to_step=2, wait_time=3.6)

        # ==========================================================
        # PASO 4: Cortes con los Ejes Coordenados
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Intersecciones con los Ejes Coordenados:} \\[6pt]"
            r"&\bullet \ \textbf{Corte con el eje } Y \ (x = 0): \\[3pt]"
            r"&\quad f(0) = -9(0)^2 - 5 = -5 \implies \mathbf{{\color{amgold}P_y(0, -5)}} \\[6pt]"
            r"&\bullet \ \textbf{Cortes con el eje } X \ (f(x) = 0): \\[3pt]"
            r"&\quad -9x^2 - 5 = 0 \iff 9x^2 = -5 \iff \mathbf{x^2 = -\frac{5}{9} < 0} \\[5pt]"
            r"&\quad \text{Como } \forall x \in \mathbb{R}, \ x^2 \ge 0 \implies \mathbf{{\color{amred}\nexists x \in \mathbb{R}}} \\[5pt]"
            r"&\quad \text{Discriminante: } \Delta = 0^2 - 4(-9)(-5) = \mathbf{{\color{amred}-180 < 0}} \\[6pt]"
            r"&\therefore \quad \mathbf{\text{No existen intersecciones con el eje } X}."
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Cortes Coordenados:}\\[6pt]"
            r"$\bullet$ Intersección con el eje $Y$: coincide con el vértice en ${\color{amgold}(0, -5)}$.\\[5pt]"
            r"$\bullet$ Discriminante estrictamente negativo: ${\color{amred}\Delta = -180 < 0}$.\\[5pt]"
            r"$\bullet$ La ecuación no posee raíces reales; la parábola nunca cruza ni toca el eje $X$.\\[5pt]"
            r"$\bullet$ Toda la gráfica se ubica enteramente por debajo del eje horizontal."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq4, just4, box_color=THEME["curve"], advance_to_step=3, wait_time=3.6)

        # ==========================================================
        # PASO 5: Signos y Monotonía
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Análisis de Signos y Monotonía:} \\[6pt]"
            r"&\textbf{Signos de la Función en } \mathbb{R}: \\[4pt]"
            r"&\bullet \ \text{Dado que } a < 0 \text{ y } \Delta < 0 \implies \mathbf{{\color{amred}\forall x \in \mathbb{R}: \ f(x) \le -5 < 0}} \\[4pt]"
            r"&\quad \mathbf{\text{Conjunto de Negatividad: }} \mathbf{{\color{amred}]-\infty, +\infty[}} \\[3pt]"
            r"&\quad \mathbf{\text{Conjunto de Positividad: }} \mathbf{{\color{amred}\emptyset}} \\[6pt]"
            r"&\textbf{Intervalos de Monotonía } (\text{cambio en } x_v = 0): \\[4pt]"
            r"&\bullet \ \mathbf{\text{Estrictamente Creciente en: }} \mathbf{{\color{amgreen}]-\infty, 0]}} \\[4pt]"
            r"&\bullet \ \mathbf{\text{Estrictamente Decreciente en: }} \mathbf{{\color{amteal}[0, +\infty[}}"
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Signos y Monotonía:}\\[6pt]"
            r"$\bullet$ Negatividad estricta universal: $f(x) < 0$ para todo número real.\\[5pt]"
            r"$\bullet$ Monotonía:\\"
            r"\hspace*{1.0em}1. Para $x \le 0$: la función sube desde $-\infty$ hasta $-5$.\\[3pt]"
            r"\hspace*{1.0em}2. Para $x \ge 0$: desciende desde $-5$ hacia $-\infty$.\\[5pt]"
            r"$\bullet$ En el vértice $x = 0$ se alcanza el pico más alto."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq5, just5, box_color=THEME["error"], advance_to_step=4, wait_time=3.6)

        # ==========================================================
        # PASO 6: Deducción Formal del Rango
        # ==========================================================
        eq6 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Deducción Analítica del Rango:} \\[6pt]"
            r"&\text{Por el axioma de no-negatividad en } \mathbb{R}: \\[4pt]"
            r"&\quad \forall x \in \mathbb{R}: \quad x^2 \ge 0 \\[5pt]"
            r"&\text{Multiplicando por } {\color{amred}-9 < 0} \ (\text{invierte el orden}): \\[4pt]"
            r"&\quad -9x^2 \le 0 \\[5pt]"
            r"&\text{Sumando } -5 \text{ en ambos miembros}: \\[4pt]"
            r"&\quad -9x^2 - 5 \le -5 \iff \mathbf{{\color{amteal}f(x) \le -5}} \\[6pt]"
            r"&\text{Como } f(0) = -5 \text{ y } \lim_{x \to \pm\infty} f(x) = -\infty: \\[5pt]"
            r"&\therefore \quad \mathbf{\operatorname{Ran}(f) = {\color{amgreen}]-\infty, -5]}}"
            r"\end{aligned}",
            font_size=22.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{6. Deducción Formal del Rango:}\\[6pt]"
            r"$\bullet$ Demostración deductiva a partir de las propiedades de orden de los números reales.\\[5pt]"
            r"$\bullet$ El cuadrado real $x^2 \ge 0$ garantiza que $-9x^2 \le 0$.\\[5pt]"
            r"$\bullet$ Cota superior estricta alcanzada en $y = -5$.\\[5pt]"
            r"$\bullet$ Por el Teorema del Valor Intermedio, la imagen cubre todo ${\color{amgreen}]-\infty, -5]}$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq6, just6, box_color=THEME["success"], advance_to_step=5, wait_time=3.6)

        # ==========================================================
        # PASO 7: Tabla de Puntos Notables y Síntesis
        # ==========================================================
        eq7 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{\textbf{7. Puntos Notables y Tabla de Valores:}} \\[6pt]"
            r"&\begin{array}{|c|c|c|c|c|c|} \hline "
            r"x & -1 & -2/3 & 0 & 2/3 & 1 \\ \hline "
            r"f(x) & -14 & -9 & \mathbf{{\color{amgold}-5}} & -9 & -14 \\ \hline "
            r"\text{Rol} & \text{Rama } \cap & \text{Simétrico} & \mathbf{\text{Vértice}} & \text{Simétrico} & \text{Rama } \cap \\ \hline "
            r"\end{array} \\[8pt]"
            r"&\textbf{\textbf{Síntesis de Propiedades de }} {\color{amred}f(x) = -9x^2 - 5}: \\[5pt]"
            r"&\bullet \ \mathbf{\text{Vértice: }} {\color{amgold}V(0, -5)} \quad (\text{Máximo Absoluto}) \\[4pt]"
            r"&\bullet \ \mathbf{\text{Rango: }} {\color{amgreen}\operatorname{Ran}(f) = ]-\infty, -5]} \\[4pt]"
            r"&\bullet \ \mathbf{\text{Eje Axial: }} x = 0 \quad (\text{Función Par, simetría en } Y)"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{7. Síntesis y Puntos Notables:}\\[6pt]"
            r"$\bullet$ La tabla confirma numéricamente la simetría par respecto al origen de abscisas.\\[5pt]"
            r"$\bullet$ Conforme $|x|$ aumenta, los valores descienden rápidamente por el factor $a = -9$.\\[5pt]"
            r"$\bullet$ Parámetros plenamente determinados para el trazado cartesiano."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq7, just7, box_color=THEME["statement_box"], advance_to_step=6, wait_time=3.6)

        # ==========================================================
        # PASO 8: Trazado Cartesiano y Verificación Gráfica
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(7)

        # Panel izquierdo: Resumen geométrico
        t_card = Tex(
            r"\begin{minipage}{5.8cm}\raggedright "
            r"\textbf{{\color{amteal}Verificación Cartesiana:}}\\[6pt]"
            r"$\bullet$ \textbf{Parábola Cóncava Abajo:}\\[2pt]"
            r"\hspace*{0.8em}$f(x) = -9x^2 - 5$.\\[6pt]"
            r"$\bullet$ \textbf{Vértice Máximo:}\\[2pt]"
            r"\hspace*{0.8em}$V(0, -5)$ en verde esmeralda.\\[6pt]"
            r"$\bullet$ \textbf{Eje de Simetría Par:}\\[2pt]"
            r"\hspace*{0.8em}$x = 0$ (eje vertical $Y$).\\[6pt]"
            r"$\bullet$ \textbf{Rango Proyectado:}\\[2pt]"
            r"\hspace*{0.8em}$]-\infty, -5]$ en el eje $Y$."
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
            x_range=[-2.2, 2.2, 1],
            y_range=[-16.0, 2.0, 4],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=14,
            labels_font_size=20
        )

        # Curva f(x) = -9x^2 - 5 en [-1.1, 1.1]
        curve = axes.plot(
            lambda x: -9.0 * (x**2) - 5.0,
            x_range=[-1.1, 1.1],
            color=THEME["error"],
            stroke_width=3.6
        )
        lbl_curve = MathTex(
            r"f(x) = -9x^2-5",
            font_size=16.0,
            color=THEME["error"]
        ).next_to(axes.c2p(0.8, -10.0), RIGHT, buff=0.08)

        # Eje de simetría x = 0
        asymp_axis = DashedLine(
            axes.c2p(0, -15.5),
            axes.c2p(0, 1.5),
            color=THEME["highlight"],
            stroke_width=1.8
        )
        lbl_axis = MathTex(
            r"x = 0",
            font_size=14.0,
            color=THEME["highlight"]
        ).next_to(axes.c2p(0, 1.5), UP, buff=0.08)

        # Vértice V(0, -5)
        v_pt = axes.c2p(0.0, -5.0)
        dot_v = Dot(v_pt, radius=0.08, color=THEME["success"])
        lbl_v = MathTex(r"V(0, -5)", font_size=15.0, color=THEME["success"]).next_to(v_pt, UR, buff=0.10)

        # Puntos simétricos notables: (-2/3, -9) y (2/3, -9)
        p_left = axes.c2p(-2.0/3.0, -9.0)
        p_right = axes.c2p(2.0/3.0, -9.0)
        dot_l = Dot(p_left, radius=0.06, color=THEME["secondary"])
        dot_r = Dot(p_right, radius=0.06, color=THEME["secondary"])
        lbl_l = MathTex(r"(-2/3, -9)", font_size=13.0, color=THEME["secondary"]).next_to(p_left, LEFT, buff=0.08)
        lbl_r = MathTex(r"(2/3, -9)", font_size=13.0, color=THEME["secondary"]).next_to(p_right, RIGHT, buff=0.08)

        # Rayo del rango sobre el eje Y: ]-∞, -5]
        range_ray = Line(
            axes.c2p(0.0, -15.8),
            axes.c2p(0.0, -5.0),
            color=THEME["success"],
            stroke_width=5.0
        )
        lbl_range = MathTex(
            r"\operatorname{Ran}(f) = ]-\infty, -5]",
            font_size=13.5,
            color=THEME["success"]
        ).next_to(axes.c2p(0.0, -12.0), LEFT, buff=0.12)

        # Transición hacia el paso 8
        self.play(
            FadeOut(self.active_box),
            FadeOut(self.active_math, shift=DOWN * 0.2),
            FadeOut(self.active_just, shift=DOWN * 0.2),
            FadeIn(info_grp, shift=DOWN * 0.2),
            Create(axes),
            Write(axes_labels),
            Create(asymp_axis), Write(lbl_axis),
            *prog_anims,
            run_time=1.8
        )
        self.active_box = None
        self.active_math = None
        self.active_just = None

        # Trazado de la parábola y rango en eje Y
        self.play(
            Create(curve), Write(lbl_curve),
            Create(range_ray), Write(lbl_range),
            run_time=2.2
        )

        # Marcado del vértice y puntos simétricos
        self.play(
            FadeIn(dot_v), Write(lbl_v),
            FadeIn(dot_l), Write(lbl_l),
            FadeIn(dot_r), Write(lbl_r),
            run_time=1.8
        )
        self.wait(4.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            asymp_axis, lbl_axis,
            curve, lbl_curve,
            range_ray, lbl_range,
            dot_v, lbl_v,
            dot_l, lbl_l, dot_r, lbl_r
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
