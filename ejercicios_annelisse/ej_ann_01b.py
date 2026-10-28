r"""
Precálculo Universitario · Tutorías Annelisse / Editorial Amarun
Capítulo: Funciones Reales y Gráficas
Ejercicio 1.b: Análisis Completo, Vértice y Rango de la Función Cuadrática
               f(x) = (x + 3)² + 4

Estructura de la Demostración (8 Pasos):
      1. Dominio polinómico en ℝ y concavidad positiva (a = 1 > 0 ⟹ parábola cóncava hacia arriba).
      2. Forma canónica f(x) = (x - (-3))² + 4 y determinación del vértice V(-3, 4) (mínimo absoluto).
      3. Simetría axial: verificación f(-3 + u) = f(-3 - u) y eje de simetría axial x = -3.
      4. Cortes con los ejes coordenados: corte Y en (0, 13); sin cortes en el eje X (Δ = -16 < 0).
      5. Signos y monotonía: estrictamente positiva en ℝ, decreciente en ]-∞, -3] y creciente en [-3, +∞[.
      6. Deducción analítica formal del rango: (x + 3)² ≥ 0 ⟹ (x + 3)² + 4 ≥ 4 ⟹ Ran(f) = [4, +∞[.
      7. Tabla de valores simétricos notables y síntesis institucional de propiedades.
      8. Trazado cartesiano riguroso: curva f(x), vértice V(-3, 4), eje axial y rayo vertical del rango.

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


class EjercicioAnn_01b(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Annelisse",
            exercise="Ejercicio 1.b",
            topic="Vértice, Rango y Análisis de f(x) = (x + 3)² + 4",
            font_size=17.0
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 1.b: Determine el vértice, rango y propiedades de la función cuadrática:",
            math_tex=r"{\color{amteal}f(x) = (x + 3)^2 + 4}, \quad x \in \mathbb{R}",
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
            "3/8: Simetría Axial y Eje",
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
            r"&\text{Dada la función cuadrática } {\color{amteal}f(x) = (x + 3)^2 + 4}: \\[4pt]"
            r"&\quad \mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R}} = {\color{amgreen}]-\infty, +\infty[}} \\[6pt]"
            r"&\textbf{Desarrollo a Forma General } (ax^2 + bx + c): \\[4pt]"
            r"&\quad f(x) = x^2 + 6x + 9 + 4 = \mathbf{x^2 + 6x + 13} \\[4pt]"
            r"&\quad {\color{amgreen}a = 1 > 0}, \quad {\color{amteal}b = 6}, \quad {\color{amgold}c = 13} \\[6pt]"
            r"&\text{Como } {\color{amgreen}a = 1 > 0} \implies \text{Parábola cóncava hacia arriba } (\cup). \\[4pt]"
            r"&\implies \text{El vértice } {\color{amgold}V} \text{ constituye un } \mathbf{\text{Mínimo Absoluto Global}}."
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Dominio y Concavidad:}\\[6pt]"
            r"$\bullet$ Toda función polinómica cuadrática está definida en todo $\mathbb{R}$.\\[5pt]"
            r"$\bullet$ Al desarrollar el binomio se obtiene: $f(x) = x^2 + 6x + 13$.\\[5pt]"
            r"$\bullet$ Coeficiente cuadrático: ${\color{amgreen}a = 1 > 0}$.\\[5pt]"
            r"$\bullet$ La concavidad positiva orienta las ramas hacia arriba ($\cup$).\\[5pt]"
            r"$\bullet$ El vértice representará el punto más bajo (mínimo absoluto global)."
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
            r"&\text{Forma canónica estándar: } f(x) = a(x - h)^2 + k: \\[4pt]"
            r"&\quad f(x) = {\color{amgreen}1}\cdot (x - ({\color{amgold}-3}))^2 + {\color{amgold}4} \\[6pt]"
            r"&\text{Lectura analítica directa de parámetros:} \\[4pt]"
            r"&\quad {\color{amgold}h = -3}, \quad {\color{amgold}k = 4} \\[6pt]"
            r"&\text{Comprobación por fórmula de coeficientes:} \\[4pt]"
            r"&\quad {\color{amgold}h} = -\frac{b}{2a} = -\frac{6}{2(1)} = \mathbf{{\color{amgold}-3}} \\[4pt]"
            r"&\quad {\color{amgold}k} = f(-3) = (-3 + 3)^2 + 4 = \mathbf{{\color{amgold}4}} \\[6pt]"
            r"&\therefore \quad \mathbf{\text{Vértice: }} \mathbf{{\color{amgold}V(-3, 4)}} \quad (\text{Mínimo Absoluto})"
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Vértice y Traslación:}\\[6pt]"
            r"$\bullet$ La expresión inicial ya se encuentra en su forma canónica.\\[5pt]"
            r"$\bullet$ Traslación horizontal: $h = -3$ ($3$ unidades a la izquierda).\\[5pt]"
            r"$\bullet$ Traslación vertical: $k = 4$ ($4$ unidades hacia arriba).\\[5pt]"
            r"$\bullet$ Vértice confirmado: ${\color{amgold}V(-3, 4)}$ (cota inferior de la gráfica)."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=3.6)

        # ==========================================================
        # PASO 3: Simetría Axial y Eje de la Parábola
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Simetría Axial y Eje de la Parábola:} \\[6pt]"
            r"&\text{Toda parábola es simétrica respecto a la vertical } x = h: \\[4pt]"
            r"&\quad \mathbf{\text{Eje de Simetría: }} \mathbf{{\color{amgold}x = -3}} \\[6pt]"
            r"&\textbf{Comprobación analítica } (\forall u \in \mathbb{R}): \\[4pt]"
            r"&\quad f(-3 + u) = ((-3 + u) + 3)^2 + 4 = u^2 + 4 \\[4pt]"
            r"&\quad f(-3 - u) = ((-3 - u) + 3)^2 + 4 = (-u)^2 + 4 = u^2 + 4 \\[6pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}f(-3 + u) = f(-3 - u)}} \quad (\text{Simetría axial}) \\[6pt]"
            r"&\text{Paridad respecto al origen } (x = 0): \\[4pt]"
            r"&\quad f(-x) = (-x + 3)^2 + 4 \ne f(x) \implies \text{No es par ni impar}."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{3. Simetría y Paridad:}\\[6pt]"
            r"$\bullet$ Al estar el vértice desplazado ($h = -3 \ne 0$), la función no posee simetría respecto al eje $Y$.\\[5pt]"
            r"$\bullet$ El eje de simetría axial es la recta vertical ${\color{amgold}x = -3}$.\\[5pt]"
            r"$\bullet$ A distancias iguales $u$ del eje, las alturas son exactamente iguales: $f(-3+u) = f(-3-u)$.\\[5pt]"
            r"$\bullet$ Permite calcular valores simétricos por parejas."
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
            r"&\quad f(0) = (0 + 3)^2 + 4 = 9 + 4 = 13 \implies \mathbf{{\color{amgold}P_y(0, 13)}} \\[6pt]"
            r"&\bullet \ \textbf{Cortes con el eje } X \ (f(x) = 0): \\[3pt]"
            r"&\quad (x + 3)^2 + 4 = 0 \iff \mathbf{(x + 3)^2 = -4 < 0} \\[5pt]"
            r"&\quad \text{Como } \forall x \in \mathbb{R}, \ (x+3)^2 \ge 0 \implies \mathbf{{\color{amred}\nexists x \in \mathbb{R}}} \\[5pt]"
            r"&\quad \text{Discriminante: } \Delta = 6^2 - 4(1)(13) = 36 - 52 = \mathbf{{\color{amred}-16 < 0}} \\[6pt]"
            r"&\therefore \quad \mathbf{\text{No existen intersecciones con el eje } X}."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Cortes Coordenados:}\\[6pt]"
            r"$\bullet$ Intersección con el eje $Y$: ordenada al origen en ${\color{amgold}(0, 13)}$.\\[5pt]"
            r"$\bullet$ La ecuación $(x+3)^2 = -4$ carece de soluciones reales.\\[5pt]"
            r"$\bullet$ Discriminante negativo: ${\color{amred}\Delta = -16 < 0}$.\\[5pt]"
            r"$\bullet$ La gráfica flota íntegramente por encima del eje horizontal ($y \ge 4 > 0$)."
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
            r"&\bullet \ \text{Dado que } a > 0 \text{ y } k = 4 > 0 \implies \mathbf{{\color{amgreen}\forall x \in \mathbb{R}: \ f(x) \ge 4 > 0}} \\[4pt]"
            r"&\quad \mathbf{\text{Conjunto de Positividad: }} \mathbf{{\color{amgreen}\mathbb{R} = ]-\infty, +\infty[}} \\[3pt]"
            r"&\quad \mathbf{\text{Conjunto de Negatividad: }} \mathbf{{\color{amred}\emptyset}} \\[6pt]"
            r"&\textbf{Intervalos de Monotonía } (\text{cambio en } x_v = -3): \\[4pt]"
            r"&\bullet \ \mathbf{\text{Estrictamente Decreciente en: }} \mathbf{{\color{amteal}]-\infty, -3]}} \\[4pt]"
            r"&\bullet \ \mathbf{\text{Estrictamente Creciente en: }} \mathbf{{\color{amgreen}[-3, +\infty[}}"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Signos y Monotonía:}\\[6pt]"
            r"$\bullet$ Positividad universal: $f(x) > 0$ para todo número real.\\[5pt]"
            r"$\bullet$ Monotonía:\\"
            r"\hspace*{1.0em}1. Para $x \le -3$: desciende desde $+\infty$ hasta el mínimo $4$.\\[3pt]"
            r"\hspace*{1.0em}2. Para $x \ge -3$: asciende desde $4$ hacia $+\infty$.\\[5pt]"
            r"$\bullet$ En el vértice $x = -3$ se alcanza el mínimo global absoluto."
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
            r"&\quad \forall x \in \mathbb{R}: \quad (x + 3)^2 \ge 0 \\[5pt]"
            r"&\text{Sumando } 4 \text{ en ambos miembros}: \\[4pt]"
            r"&\quad (x + 3)^2 + 4 \ge 0 + 4 \\[5pt]"
            r"&\quad \iff \mathbf{{\color{amgreen}f(x) \ge 4}} \\[6pt]"
            r"&\text{Como } f(-3) = 4 \text{ y } \lim_{x \to \pm\infty} f(x) = +\infty: \\[5pt]"
            r"&\therefore \quad \mathbf{\operatorname{Ran}(f) = {\color{amgreen}[4, +\infty[}}"
            r"\end{aligned}",
            font_size=22.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{6. Deducción Formal del Rango:}\\[6pt]"
            r"$\bullet$ Demostración deductiva a partir de las propiedades de orden en $\mathbb{R}$.\\[5pt]"
            r"$\bullet$ El término cuadrático $(x+3)^2 \ge 0$ garantiza una cota inferior básica.\\[5pt]"
            r"$\bullet$ La traslación $+4$ fija el mínimo valor alcanzable en $y = 4$.\\[5pt]"
            r"$\bullet$ Por continuidad, la imagen cubre todo el intervalo semi-infinito ${\color{amgreen}[4, +\infty[}$."
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
            r"&\begin{array}{|c|c|c|c|c|c|c|c|} \hline "
            r"x & -6 & -5 & -4 & \mathbf{-3} & -2 & -1 & 0 \\ \hline "
            r"f(x) & 13 & 8 & 5 & \mathbf{{\color{amgold}4}} & 5 & 8 & 13 \\ \hline "
            r"\text{Rol} & \text{Sim.} & \text{Pto.} & \text{Pto.} & \mathbf{\text{Vértice}} & \text{Pto.} & \text{Pto.} & \text{Corte } Y \\ \hline "
            r"\end{array} \\[8pt]"
            r"&\textbf{Síntesis de Propiedades de } {\color{amteal}f(x) = (x + 3)^2 + 4}: \\[5pt]"
            r"&\bullet \ \mathbf{\text{Vértice: }} {\color{amgold}V(-3, 4)} \quad (\text{Mínimo Absoluto Global}) \\[4pt]"
            r"&\bullet \ \mathbf{\text{Rango: }} {\color{amgreen}\operatorname{Ran}(f) = [4, +\infty[} \\[4pt]"
            r"&\bullet \ \mathbf{\text{Eje Axial: }} x = -3 \quad (\text{Simetría Bilateral})"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{7. Síntesis y Puntos Notables:}\\[6pt]"
            r"$\bullet$ La tabla confirma numéricamente la simetría en pares respecto a $x = -3$.\\[5pt]"
            r"$\bullet$ El corte $Y(0, 13)$ tiene su simétrico correspondiente en $(-6, 13)$.\\[5pt]"
            r"$\bullet$ Coordenadas calibradas para la construcción cartesiana."
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
            r"\hspace*{0.8em}$f(x) = (x+3)^2 + 4$.\\[6pt]"
            r"$\bullet$ \textbf{Vértice Mínimo:}\\[2pt]"
            r"\hspace*{0.8em}$V(-3, 4)$ en verde esmeralda.\\[6pt]"
            r"$\bullet$ \textbf{Eje de Simetría Axial:}\\[2pt]"
            r"\hspace*{0.8em}$x = -3$ (recta vertical dorada).\\[6pt]"
            r"$\bullet$ \textbf{Corte con el Eje $Y$:}\\[2pt]"
            r"\hspace*{0.8em}$P_y(0, 13)$ y simétrico $(-6, 13)$.\\[6pt]"
            r"$\bullet$ \textbf{Rango Proyectado:}\\[2pt]"
            r"\hspace*{0.8em}$[4, +\infty[$ sobre el eje vertical $Y$."
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
            x_range=[-7.5, 2.0, 2],
            y_range=[-1.0, 15.5, 3],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=14,
            labels_font_size=20
        )

        # Curva f(x) = (x + 3)^2 + 4 en [-6.1, 0.1]
        curve = axes.plot(
            lambda x: (x + 3.0)**2 + 4.0,
            x_range=[-6.15, 0.15],
            color=THEME["amarun_teal"],
            stroke_width=3.6
        )
        lbl_curve = MathTex(
            r"f(x) = (x+3)^2+4",
            font_size=15.0,
            color=THEME["amarun_teal"]
        ).next_to(axes.c2p(-0.2, 13.5), RIGHT, buff=0.08)

        # Eje de simetría axial x = -3
        asymp_axis = DashedLine(
            axes.c2p(-3.0, -0.5),
            axes.c2p(-3.0, 15.0),
            color=THEME["highlight"],
            stroke_width=1.8
        )
        lbl_axis = MathTex(
            r"x = -3",
            font_size=14.0,
            color=THEME["highlight"]
        ).next_to(axes.c2p(-3.0, 15.0), UP, buff=0.08)

        # Vértice V(-3, 4)
        v_pt = axes.c2p(-3.0, 4.0)
        dot_v = Dot(v_pt, radius=0.08, color=THEME["success"])
        lbl_v = MathTex(r"V(-3, 4)", font_size=15.0, color=THEME["success"]).next_to(v_pt, DOWN, buff=0.12)

        # Puntos notables: corte Y(0, 13) y simétrico (-6, 13)
        p_y = axes.c2p(0.0, 13.0)
        p_sym = axes.c2p(-6.0, 13.0)
        dot_y = Dot(p_y, radius=0.06, color=THEME["secondary"])
        dot_sym = Dot(p_sym, radius=0.06, color=THEME["secondary"])
        lbl_y = MathTex(r"(0, 13)", font_size=13.0, color=THEME["secondary"]).next_to(p_y, RIGHT, buff=0.08)
        lbl_sym = MathTex(r"(-6, 13)", font_size=13.0, color=THEME["secondary"]).next_to(p_sym, LEFT, buff=0.08)

        # Rayo del rango sobre el eje Y: [4, +∞[
        range_ray = Line(
            axes.c2p(0.0, 4.0),
            axes.c2p(0.0, 15.2),
            color=THEME["success"],
            stroke_width=5.0
        )
        lbl_range = MathTex(
            r"\operatorname{Ran}(f) = [4, +\infty[",
            font_size=13.5,
            color=THEME["success"]
        ).next_to(axes.c2p(0.0, 7.5), LEFT, buff=0.12)

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
            FadeIn(dot_y), Write(lbl_y),
            FadeIn(dot_sym), Write(lbl_sym),
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
            dot_y, lbl_y, dot_sym, lbl_sym
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
