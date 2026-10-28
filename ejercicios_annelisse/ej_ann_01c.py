r"""
Precálculo Universitario · Tutorías Annelisse / Editorial Amarun
Capítulo: Funciones Reales y Gráficas
Ejercicio 1.c: Análisis Completo, Vértice y Rango de la Función Cuadrática
               f(x) = 7x² - 12

Estructura de la Demostración (8 Pasos):
      1. Dominio polinómico en ℝ y concavidad positiva (a = 7 > 0 ⟹ parábola cóncava hacia arriba).
      2. Forma canónica f(x) = 7(x - 0)² - 12 y determinación del vértice V(0, -12) (mínimo absoluto).
      3. Simetría par: f(-x) = f(x) y eje de simetría axial x = 0 (eje de ordenadas Y).
      4. Cortes con los ejes coordenados: corte Y en (0, -12); cortes X en (±2√21/7, 0) (Δ = 336 > 0).
      5. Signos y monotonía: raíces en ±√(12/7), decreciente en ]-∞, 0] y creciente en [0, +∞[.
      6. Deducción analítica formal del rango: x² ≥ 0 ⟹ 7x² - 12 ≥ -12 ⟹ Ran(f) = [-12, +∞[.
      7. Tabla de valores simétricos notables y síntesis institucional de propiedades.
      8. Trazado cartesiano riguroso: curva f(x), vértice V(0, -12), cortes X, eje axial y rayo del rango.

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


class EjercicioAnn_01c(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Annelisse",
            exercise="Ejercicio 1.c",
            topic="Vértice, Rango y Análisis de f(x) = 7x² - 12",
            font_size=17.0
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 1.c: Determine el vértice, rango y propiedades de la función cuadrática:",
            math_tex=r"{\color{amgold}f(x) = 7x^2 - 12}, \quad x \in \mathbb{R}",
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
            r"&\text{Al ser } {\color{amgold}f(x) = 7x^2 - 12} \text{ un polinomio cuadrático en } \mathbb{R}: \\[4pt]"
            r"&\quad \mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R}} = {\color{amgreen}]-\infty, +\infty[}} \\[6pt]"
            r"&\textbf{Identificación de Coeficientes } (ax^2 + bx + c): \\[4pt]"
            r"&\quad {\color{amgreen}a = 7}, \quad {\color{amteal}b = 0}, \quad {\color{amred}c = -12} \\[6pt]"
            r"&\text{Como } {\color{amgreen}a = 7 > 0} \implies \text{Parábola cóncava hacia arriba } (\cup). \\[4pt]"
            r"&\implies \text{El vértice } {\color{amgold}V} \text{ constituye un } \mathbf{\text{Mínimo Absoluto Global}}."
            r"\end{aligned}",
            font_size=22.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Dominio y Concavidad:}\\[6pt]"
            r"$\bullet$ Toda función polinómica cuadrática está definida en todo $\mathbb{R}$.\\[5pt]"
            r"$\bullet$ Coeficiente principal: ${\color{amgreen}a = 7 > 0}$.\\[5pt]"
            r"$\bullet$ La concavidad positiva orienta las ramas hacia arriba ($\cup$).\\[5pt]"
            r"$\bullet$ El vértice representará la cota inferior global (mínimo absoluto de la función)."
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
            r"&\text{Expresión canónica de traslación } f(x) = a(x - h)^2 + k: \\[4pt]"
            r"&\quad f(x) = {\color{amgreen}7}(x - {\color{amgold}0})^2 + ({\color{amred}-12}) \\[6pt]"
            r"&\text{Cálculo analítico de coordenadas:} \\[4pt]"
            r"&\quad {\color{amgold}h} = -\frac{b}{2a} = -\frac{0}{2(7)} = \mathbf{{\color{amgold}0}} \\[4pt]"
            r"&\quad {\color{amgold}k} = f(h) = f(0) = 7(0)^2 - 12 = \mathbf{{\color{amred}-12}} \\[6pt]"
            r"&\therefore \quad \mathbf{\text{Vértice: }} \mathbf{{\color{amgold}V(0, -12)}} \quad (\text{Sobre el eje vertical } Y)"
            r"\end{aligned}",
            font_size=22.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Vértice y Traslación:}\\[6pt]"
            r"$\bullet$ Al no existir término lineal en $x$ ($b = 0$), el vértice reposa en el eje $Y$ ($h = 0$).\\[5pt]"
            r"$\bullet$ Traslación vertical pura: la parábola elemental $y = 7x^2$ desciende $12$ unidades ($k = -12$).\\[5pt]"
            r"$\bullet$ Vértice confirmado: ${\color{amgold}V(0, -12)}$ (punto mínimo de la curva)."
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
            r"&\quad f(-x) = 7(-x)^2 - 12 = 7x^2 - 12 = \mathbf{{\color{amteal}f(x)}} \\[6pt]"
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
            r"$\bullet$ El exponente par $(-x)^2 = x^2$ mantiene idéntica la expresión analítica.\\[5pt]"
            r"$\bullet$ Simetría de espejo perfecta respecto al eje vertical de ordenadas.\\[5pt]"
            r"$\bullet$ Eje axial de simetría: recta vertical ${\color{amgold}x = 0}$.\\[5pt]"
            r"$\bullet$ Cualquier par de puntos simétricos $(\pm x_0, y_0)$ comparte idéntica ordenada."
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
            r"&\quad f(0) = 7(0)^2 - 12 = -12 \implies \mathbf{{\color{amgold}P_y(0, -12)}} \\[6pt]"
            r"&\bullet \ \textbf{Cortes con el eje } X \ (f(x) = 0): \\[3pt]"
            r"&\quad 7x^2 - 12 = 0 \iff 7x^2 = 12 \iff \mathbf{x^2 = \frac{12}{7}} \\[5pt]"
            r"&\quad \implies x = \pm \sqrt{\frac{12}{7}} = \pm \frac{2\sqrt{21}}{7} \approx \mathbf{\pm 1.31} \\[5pt]"
            r"&\quad \text{Discriminante: } \Delta = 0^2 - 4(7)(-12) = \mathbf{{\color{amgreen}+336 > 0}} \\[6pt]"
            r"&\therefore \quad \mathbf{{\color{amteal}P_{x1}\left(-\frac{2\sqrt{21}}{7}, 0\right)}}, \quad \mathbf{{\color{amteal}P_{x2}\left(\frac{2\sqrt{21}}{7}, 0\right)}}"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Cortes Coordenados:}\\[6pt]"
            r"$\bullet$ Intersección con el eje $Y$: coincide con el vértice en ${\color{amgold}(0, -12)}$.\\[5pt]"
            r"$\bullet$ Discriminante estrictamente positivo: ${\color{amgreen}\Delta = 336 > 0}$.\\[5pt]"
            r"$\bullet$ Existen dos raíces reales simétricas en $x = \pm \sqrt{12/7} \approx \pm 1.31$.\\[5pt]"
            r"$\bullet$ La parábola cruza el eje $X$ en dos puntos antes de extenderse a $+\infty$."
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
            r"&\textbf{Conjuntos de Signos } (x_{1,2} = \pm\sqrt{12/7} \approx \pm 1.31): \\[4pt]"
            r"&\bullet \ \mathbf{\text{Positividad } (f(x) > 0):} \ \mathbf{{\color{amgreen}\left]-\infty, -\sqrt{\frac{12}{7}}\right[ \cup \left]\sqrt{\frac{12}{7}}, +\infty\right[}} \\[4pt]"
            r"&\bullet \ \mathbf{\text{Negatividad } (f(x) < 0):} \ \mathbf{{\color{amred}\left]-\sqrt{\frac{12}{7}}, \sqrt{\frac{12}{7}}\right[}} \\[6pt]"
            r"&\textbf{Intervalos de Monotonía } (\text{cambio en } x_v = 0): \\[4pt]"
            r"&\bullet \ \mathbf{\text{Estrictamente Decreciente en: }} \mathbf{{\color{amteal}]-\infty, 0]}} \\[4pt]"
            r"&\bullet \ \mathbf{\text{Estrictamente Creciente en: }} \mathbf{{\color{amgreen}[0, +\infty[}}"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Signos y Monotonía:}\\[6pt]"
            r"$\bullet$ La función es negativa entre las dos raíces y positiva en los extremos exteriores.\\[5pt]"
            r"$\bullet$ Monotonía:\\"
            r"\hspace*{1.0em}1. Para $x \le 0$: desciende desde $+\infty$ hasta $-12$.\\[3pt]"
            r"\hspace*{1.0em}2. Para $x \ge 0$: asciende desde $-12$ hacia $+\infty$.\\[5pt]"
            r"$\bullet$ En el vértice $x = 0$ se alcanza el mínimo global absoluto."
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
            r"&\text{Multiplicando por } {\color{amgreen}7 > 0} \ (\text{preserva el orden}): \\[4pt]"
            r"&\quad 7x^2 \ge 0 \\[5pt]"
            r"&\text{Sumando } -12 \text{ en ambos miembros}: \\[4pt]"
            r"&\quad 7x^2 - 12 \ge 0 - 12 \iff \mathbf{{\color{amgreen}f(x) \ge -12}} \\[6pt]"
            r"&\text{Como } f(0) = -12 \text{ y } \lim_{x \to \pm\infty} f(x) = +\infty: \\[5pt]"
            r"&\therefore \quad \mathbf{\operatorname{Ran}(f) = {\color{amgreen}[-12, +\infty[}}"
            r"\end{aligned}",
            font_size=22.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{6. Deducción Formal del Rango:}\\[6pt]"
            r"$\bullet$ Demostración deductiva a partir de las propiedades de orden de los números reales.\\[5pt]"
            r"$\bullet$ El término cuadrático real $x^2 \ge 0$ garantiza que $7x^2 \ge 0$.\\[5pt]"
            r"$\bullet$ Cota inferior estricta alcanzada en $y = -12$.\\[5pt]"
            r"$\bullet$ Por continuidad, la imagen cubre todo el intervalo semi-infinito ${\color{amgreen}[-12, +\infty[}$."
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
            r"&\textbf{7. Puntos Notables y Tabla de Valores:} \\[6pt]"
            r"&\begin{array}{|c|c|c|c|c|c|} \hline "
            r"x & -2 & -1 & \mathbf{0} & 1 & 2 \\ \hline "
            r"f(x) & 16 & -5 & \mathbf{{\color{amgold}-12}} & -5 & 16 \\ \hline "
            r"\text{Rol} & \text{Rama } \cup & \text{Punto} & \mathbf{\text{Vértice}} & \text{Punto} & \text{Rama } \cup \\ \hline "
            r"\end{array} \\[8pt]"
            r"&\textbf{Síntesis de Propiedades de } {\color{amgold}f(x) = 7x^2 - 12}: \\[5pt]"
            r"&\bullet \ \mathbf{\text{Vértice: }} {\color{amgold}V(0, -12)} \quad (\text{Mínimo Absoluto Global}) \\[4pt]"
            r"&\bullet \ \mathbf{\text{Rango: }} {\color{amgreen}\operatorname{Ran}(f) = [-12, +\infty[} \\[4pt]"
            r"&\bullet \ \mathbf{\text{Eje Axial: }} x = 0 \quad (\text{Función Par, simetría en } Y)"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{7. Síntesis y Puntos Notables:}\\[6pt]"
            r"$\bullet$ La tabla confirma numéricamente la simetría par respecto a $x = 0$.\\[5pt]"
            r"$\bullet$ Valores reflejados: $f(-1) = f(1) = -5$ y $f(-2) = f(2) = 16$.\\[5pt]"
            r"$\bullet$ Raíces exactas en $x = \pm 2\sqrt{21}/7 \approx \pm 1.31$.\\[5pt]"
            r"$\bullet$ Puntos plenamente calibrados para el trazado cartesiano."
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
            r"$\bullet$ \textbf{Parábola Cóncava Arriba:}\\[2pt]"
            r"\hspace*{0.8em}$f(x) = 7x^2 - 12$.\\[6pt]"
            r"$\bullet$ \textbf{Vértice Mínimo:}\\[2pt]"
            r"\hspace*{0.8em}$V(0, -12)$ en verde esmeralda.\\[6pt]"
            r"$\bullet$ \textbf{Eje de Simetría Par:}\\[2pt]"
            r"\hspace*{0.8em}$x = 0$ (eje vertical $Y$).\\[6pt]"
            r"$\bullet$ \textbf{Cortes con el Eje $X$:}\\[2pt]"
            r"\hspace*{0.8em}$(\pm 1.31, 0)$ en turquesa.\\[6pt]"
            r"$\bullet$ \textbf{Rango Proyectado:}\\[2pt]"
            r"\hspace*{0.8em}$[-12, +\infty[$ en el eje $Y$."
            r"\end{minipage}",
            font_size=17.5,
            color=WHITE
        )
        info_box = SurroundingRectangle(
            t_card,
            color=THEME["statement_box"],
            buff=0.20,
            stroke_width=1.8,
            corner_radius=0.1
        )
        info_grp = VGroup(info_box, t_card).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos
        axes, axes_labels = self.setup_axes(
            x_range=[-2.6, 2.6, 1],
            y_range=[-14.0, 18.0, 4],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=14,
            labels_font_size=20
        )

        # Curva f(x) = 7x^2 - 12 en [-2.0, 2.0]
        curve = axes.plot(
            lambda x: 7.0 * (x**2) - 12.0,
            x_range=[-2.05, 2.05],
            color=THEME["highlight"],
            stroke_width=3.6
        )
        lbl_curve = MathTex(
            r"f(x) = 7x^2-12",
            font_size=15.0,
            color=THEME["highlight"]
        ).next_to(axes.c2p(1.2, 8.0), RIGHT, buff=0.08)

        # Eje de simetría axial x = 0
        asymp_axis = DashedLine(
            axes.c2p(0.0, -13.5),
            axes.c2p(0.0, 17.5),
            color=THEME["poncho_red"],
            stroke_width=1.8
        )
        lbl_axis = MathTex(
            r"x = 0",
            font_size=14.0,
            color=THEME["poncho_red"]
        ).next_to(axes.c2p(0.0, 17.5), UP, buff=0.08)

        # Vértice V(0, -12)
        v_pt = axes.c2p(0.0, -12.0)
        dot_v = Dot(v_pt, radius=0.08, color=THEME["success"])
        lbl_v = MathTex(r"V(0, -12)", font_size=15.0, color=THEME["success"]).next_to(v_pt, DOWN, buff=0.12)

        # Cortes con el eje X: x = ±√(12/7) ≈ ±1.3093
        r_val = np.sqrt(12.0 / 7.0)
        p_x1 = axes.c2p(-r_val, 0.0)
        p_x2 = axes.c2p(r_val, 0.0)
        dot_x1 = Dot(p_x1, radius=0.06, color=THEME["amarun_teal"])
        dot_x2 = Dot(p_x2, radius=0.06, color=THEME["amarun_teal"])
        lbl_x1 = MathTex(r"-1.31", font_size=13.0, color=THEME["amarun_teal"]).next_to(p_x1, UL, buff=0.08)
        lbl_x2 = MathTex(r"1.31", font_size=13.0, color=THEME["amarun_teal"]).next_to(p_x2, UR, buff=0.08)

        # Rayo del rango sobre el eje Y: [-12, +∞[
        range_ray = Line(
            axes.c2p(0.0, -12.0),
            axes.c2p(0.0, 17.8),
            color=THEME["success"],
            stroke_width=5.0
        )
        lbl_range = MathTex(
            r"\operatorname{Ran}(f) = [-12, +\infty[",
            font_size=13.5,
            color=THEME["success"]
        ).next_to(axes.c2p(0.0, -6.0), LEFT, buff=0.12)

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

        # Marcado del vértice y raíces
        self.play(
            FadeIn(dot_v), Write(lbl_v),
            FadeIn(dot_x1), Write(lbl_x1),
            FadeIn(dot_x2), Write(lbl_x2),
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
            dot_x1, lbl_x1, dot_x2, lbl_x2
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
