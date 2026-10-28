r"""
Precálculo Universitario · Tutorías Annelisse / Editorial Amarun
Capítulo: Funciones Reales y Gráficas
Ejercicio 5.c: Rango de Función Racional Homográfica con Dominio Acotado
               f(x) = (3x - 1)/(2x + 4),  Dom(f) = [-8, -5]

Estructura de la Demostración (8 Pasos):
      1. Dominio restringido y singularidad: denominador 2x + 4 = 0 ⟹ x = -2 ∉ [-8, -5] (función continua y suave en D).
      2. Monotonía por la derivada: f'(x) = 14/(2x + 4)² > 0 en todo D ⟹ función estrictamente creciente.
      3. Evaluación en extremo izquierdo cerrado: f(-8) = 25/12 ≈ 2.083 (mínimo absoluto en punto cerrado •).
      4. Evaluación en extremo derecho cerrado: f(-5) = 8/3 ≈ 2.667 (máximo absoluto en punto cerrado •).
      5. Deducción formal por inecuaciones: forma canónica f(x) = 3/2 - 7/(2x + 4) ⟹ Ran(f) = [25/12, 8/3].
      6. Ausencia de raíces en D y positividad universal: f(x) > 0 en todo D, sin cortes con los ejes coordenados.
      7. Tabla de valores notables y síntesis institucional de propiedades analíticas.
      8. Trazado cartesiano riguroso: asíntota x = -2 exterior, arco hiperbólico turquesa y rango en Y.

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


class EjercicioAnn_05c(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Annelisse",
            exercise="Ejercicio 5.c",
            topic="Rango de Función Homográfica Acotada [-8, -5]",
            font_size=17.0
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 5.c: Determine el rango de la función racional en el dominio acotado:",
            math_tex=r"{\color{amteal}f(x) = \frac{3x - 1}{2x + 4}}, \quad \operatorname{Dom}(f) = [-8, -5]",
            desc_font_size=20.0,
            math_font_size=24.0,
            arrange_direction=DOWN,
            buff=0.18,
            box_pos=np.array([0.0, 2.45, 0.0]),
            read_time=3.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (8 pasos unificados)
        # ==========================================================
        self.setup_progress_bar([
            "1/8: Dominio y Singularidad",
            "2/8: Monotonía por Derivada",
            "3/8: Extremo Izquierdo Cerrado",
            "4/8: Extremo Derecho Cerrado",
            "5/8: Deducción Formal del Rango",
            "6/8: Ceros y Positividad",
            "7/8: Tabla y Síntesis",
            "8/8: Trazado Cartesiano y Rango"
        ], dot_spacing=0.82, label_font_size=14.0)

        # ==========================================================
        # PASO 1: Dominio Restringido y Singularidad
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Dominio Restringido y Singularidad del Denominador:} \\[6pt]"
            r"&\text{Regla de correspondencia homográfica en } D = [-8, -5]: \\[4pt]"
            r"&\quad f(x) = {\color{amteal}\frac{3x - 1}{2x + 4}} \\[6pt]"
            r"&\textbf{Condición de Existencia en } \mathbb{R}: \\[4pt]"
            r"&\quad 2x + 4 = 0 \iff {\color{amred}x = -2} \quad (\text{Asíntota Vertical}) \\[6pt]"
            r"&\textbf{Posición de la Singularidad respecto al Dominio } D: \\[4pt]"
            r"&\quad -8 \le x \le -5 < -2 \implies \mathbf{{\color{amgreen}-2 \notin [-8, -5]}} \\[6pt]"
            r"&\therefore \quad 2x + 4 \le -6 < 0 \implies \mathbf{f(x) \text{ es continua y suave en todo } D.}"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Continuidad y Singularidad:}\\[6pt]"
            r"$\bullet$ La función racional tiene una singularidad en el cero del denominador: $x = -2$.\\[5pt]"
            r"$\bullet$ El dominio asignado es el intervalo cerrado $D = [-8, -5]$.\\[5pt]"
            r"$\bullet$ Como $x = -2 > -5$, la asíntota vertical queda totalmente a la derecha de $D$.\\[5pt]"
            r"$\bullet$ El denominador varía de $-12$ a $-6$, manteniéndose estrictamente negativo.\\[5pt]"
            r"$\bullet$ $f(x)$ es continua y diferenciable en todo su dominio."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=3.6)

        # ==========================================================
        # PASO 2: Monotonía por la Derivada
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Análisis de Monotonía (Primera Derivada):} \\[6pt]"
            r"&\text{Diferenciando mediante la regla del cociente para } x \in [-8, -5]: \\[4pt]"
            r"&\quad f'(x) = \frac{3(2x + 4) - 2(3x - 1)}{(2x + 4)^2} = \frac{12 - (-2)}{(2x + 4)^2} = \mathbf{{\color{amgreen}\frac{14}{(2x + 4)^2}}} \\[6pt]"
            r"&\textbf{Determinante Homográfico Positivo:} \\[4pt]"
            r"&\quad ad - bc = (3)(4) - (-1)(2) = 14 > 0 \\[6pt]"
            r"&\textbf{Evaluación del Signo en } D: \\[4pt]"
            r"&\quad (2x + 4)^2 \ge 36 > 0 \implies \mathbf{{\color{amgreen}f'(x) > 0, \quad \forall x \in [-8, -5]}} \\[6pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}f(x) \text{ es ESTRICTAMENTE CRECIENTE en todo } D.}}"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Monotonía Creciente:}\\[6pt]"
            r"$\bullet$ La derivada presenta un numerador positivo constante: $ad - bc = 14 > 0$.\\[5pt]"
            r"$\bullet$ El denominador $(2x+4)^2$ es un cuadrado perfecto estrictamente positivo.\\[5pt]"
            r"$\bullet$ Al ser $f'(x) > 0$ en todo $D$, la función asciende monótonamente:\\[3pt]"
            r"\hspace*{1.0em}Mínimo en el extremo izquierdo ($x = -8$).\\[3pt]"
            r"\hspace*{1.0em}Máximo en el extremo derecho ($x = -5$).\\[5pt]"
            r"$\bullet$ Las desigualdades preservan estrictamente su orden."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=3.6)

        # ==========================================================
        # PASO 3: Extremo Izquierdo Cerrado
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Evaluación en el Extremo Izquierdo Cerrado } (x = -8): \\[6pt]"
            r"&\text{Dado que } -8 \in D \text{ (corchete cerrado } [-8\text{):} \\[4pt]"
            r"&\quad f(-8) = \frac{3(-8) - 1}{2(-8) + 4} = \frac{-24 - 1}{-16 + 4} = \frac{-25}{-12} = \mathbf{{\color{amgold}\frac{25}{12}}} \approx \mathbf{2.0833} \\[6pt]"
            r"&\textbf{Naturaleza del Extremo:} \\[4pt]"
            r"&\text{Al ser } f \text{ creciente en } [-8, -5], \text{ su valor mínimo absoluto} \\[4pt]"
            r"&\text{ocurre en el punto inicial } x = -8: \\[4pt]"
            r"&\quad \mathbf{{\color{amgreen}m = \min_{x \in D} f(x) = \frac{25}{12}}} \\[6pt]"
            r"&\therefore \quad \mathbf{\text{Punto de Frontera Cerrado: }} \mathbf{{\color{amgold}P_{\min}\left(-8, \frac{25}{12}\right)}} \quad (\text{Punto } \bullet)"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{3. Mínimo Absoluto Global:}\\[6pt]"
            r"$\bullet$ Evaluamos en el extremo izquierdo $x = -8$ incluido en $D$.\\[5pt]"
            r"$\bullet$ El cociente de signos negativos resulta positivo:\\[3pt]"
            r"\hspace*{1.0em}$f(-8) = (-25)/(-12) = 25/12 \approx 2.083$.\\[5pt]"
            r"$\bullet$ Como $-8 \in D$, este punto pertenece formalmente a la curva ($\bullet$).\\[5pt]"
            r"$\bullet$ Constituye la cota inferior estricta y cerrada del rango: $y \ge 25/12$.\\[5pt]"
            r"$\bullet$ $m = 25/12$ es el mínimo global alcanzado en $D$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq3, just3, box_color=THEME["statement_box"], advance_to_step=2, wait_time=3.6)

        # ==========================================================
        # PASO 4: Extremo Derecho Cerrado
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Evaluación en el Extremo Derecho Cerrado } (x = -5): \\[6pt]"
            r"&\text{Dado que } -5 \in D \text{ (corchete cerrado } -5]\text{):} \\[4pt]"
            r"&\quad f(-5) = \frac{3(-5) - 1}{2(-5) + 4} = \frac{-15 - 1}{-10 + 4} = \frac{-16}{-6} = \mathbf{{\color{amgold}\frac{8}{3}}} \approx \mathbf{2.6667} \\[6pt]"
            r"&\textbf{Naturaleza del Extremo:} \\[4pt]"
            r"&\text{Al ser } f \text{ creciente en } [-8, -5], \text{ su valor máximo absoluto} \\[4pt]"
            r"&\text{se alcanza en el punto final } x = -5: \\[4pt]"
            r"&\quad \mathbf{{\color{amgreen}M = \max_{x \in D} f(x) = \frac{8}{3}}} \\[6pt]"
            r"&\therefore \quad \mathbf{\text{Punto de Frontera Cerrado: }} \mathbf{{\color{amteal}P_{\max}\left(-5, \frac{8}{3}\right)}} \quad (\text{Punto } \bullet)"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Máximo Absoluto Global:}\\[6pt]"
            r"$\bullet$ Evaluamos en el extremo derecho $x = -5$ incluido en $D$.\\[5pt]"
            r"$\bullet$ Simplificando la fracción: $(-16)/(-6) = 8/3 \approx 2.667$.\\[5pt]"
            r"$\bullet$ Como $-5 \in D$, el extremo superior es plenamente alcanzable ($\bullet$).\\[5pt]"
            r"$\bullet$ Constituye la cota superior estricta y cerrada del rango: $y \le 8/3$.\\[5pt]"
            r"$\bullet$ $M = 8/3$ es el máximo global alcanzado en $D$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq4, just4, box_color=THEME["error"], advance_to_step=3, wait_time=3.6)

        # ==========================================================
        # PASO 5: Deducción Formal por Inecuaciones
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Deducción Formal del Rango mediante Inecuaciones:} \\[6pt]"
            r"&\text{Descomposición en forma canónica homográfica:} \\[4pt]"
            r"&\quad f(x) = \frac{3x - 1}{2x + 4} = \mathbf{{\color{amteal}\frac{3}{2} - \frac{7}{2x + 4}}} \\[6pt]"
            r"&\text{Partiendo del dominio } -8 \le x \le -5: \\[4pt]"
            r"&\quad -16 \le 2x \le -10 \iff \mathbf{{\color{amgold}-12 \le 2x + 4 \le -6}} \\[6pt]"
            r"&\text{Invirtiendo con signos negativos } (6 \le -(2x + 4) \le 12): \\[4pt]"
            r"&\quad \frac{7}{12} \le -\frac{7}{2x + 4} \le \frac{7}{6} \iff \frac{18}{12} + \frac{7}{12} \le f(x) \le \frac{18}{12} + \frac{14}{12} \\[6pt]"
            r"&\therefore \quad \mathbf{\operatorname{Ran}(f) = {\color{amgreen}\left[\frac{25}{12}, \frac{8}{3}\right]}} \quad (\text{Intervalo Cerrado Compacto})"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Deducción Rigurosa del Rango:}\\[6pt]"
            r"$\bullet$ La forma canónica $f(x) = 3/2 - 7/(2x+4)$ desacopla la variable $x$.\\[5pt]"
            r"$\bullet$ El denominador $2x+4$ varía en el intervalo negativo $[-12, -6]$.\\[5pt]"
            r"$\bullet$ Al invertir y multiplicar por $-7$, los límites se transforman con rigor algebraico.\\[5pt]"
            r"$\bullet$ Al sumar la asíntota horizontal $3/2$, se confirman exactamente las cotas:\\[3pt]"
            r"\hspace*{1.0em}${\color{amgreen}\operatorname{Ran}(f) = \left[\frac{25}{12}, \frac{8}{3}\right]}$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq5, just5, box_color=THEME["curve"], advance_to_step=4, wait_time=3.6)

        # ==========================================================
        # PASO 6: Ceros y Positividad Universal
        # ==========================================================
        eq6 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Ausencia de Ceros y Positividad Universal en } D: \\[6pt]"
            r"&\textbf{Intersección con el Eje } X \ (f(x) = 0): \\[4pt]"
            r"&\quad 3x - 1 = 0 \iff x = \frac{1}{3} \notin [-8, -5] \implies \mathbf{\text{Sin cortes con el eje } X.} \\[6pt]"
            r"&\textbf{Intersección con el Eje } Y \ (x = 0): \\[4pt]"
            r"&\quad 0 \notin [-8, -5] \implies \mathbf{\text{Sin corte con el eje } Y \text{ en } D.} \\[6pt]"
            r"&\textbf{Comportamiento de Signos en } D = [-8, -5]: \\[4pt]"
            r"&\quad \text{Dado que } \operatorname{Ran}(f) = \left[\frac{25}{12}, \frac{8}{3}\right] \subset \mathbb{R}^+: \\[4pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}\forall x \in [-8, -5]: \quad f(x) > 0}} \quad (\textbf{Estrictamente Positiva})"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{6. Signos e Intersecciones:}\\[6pt]"
            r"$\bullet$ La única raíz real de la función es $x = 1/3$, externa al dominio $D$.\\[5pt]"
            r"$\bullet$ El origen $x = 0$ también queda fuera de $D \implies$ sin corte con el eje $Y$.\\[5pt]"
            r"$\bullet$ Como los valores del rango están entre $2.083$ y $2.667$, la función es $100\%$ positiva.\\[5pt]"
            r"$\bullet$ La curva se sitúa en el segundo cuadrante cartesiano ($x < 0, y > 0$)."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq6, just6, box_color=THEME["statement_box"], advance_to_step=5, wait_time=3.6)

        # ==========================================================
        # PASO 7: Tabla y Síntesis Institucional
        # ==========================================================
        eq7 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{7. Tabla de Valores Notables y Síntesis en } D: \\[6pt]"
            r"&\begin{array}{|c|c|c|c|c|c|} \hline "
            r"x & \mathbf{-8} & -7 & \mathbf{-6.5} & -6 & \mathbf{-5} \\ \hline "
            r"f(x) & \mathbf{{\color{amgreen}\frac{25}{12}}} & \frac{11}{5} = 2.20 & \mathbf{\frac{41}{18} \approx 2.28} & \frac{19}{8} = 2.375 & \mathbf{{\color{amgreen}\frac{8}{3}}} \\ \hline "
            r"\text{Rol} & \mathbf{\text{Mín } \bullet} & \text{Punto} & \text{Medio} & \text{Punto} & \mathbf{\text{Máx } \bullet} \\ \hline "
            r"\end{array} \\[8pt]"
            r"&\textbf{Síntesis de Propiedades Institucionales:} \\[5pt]"
            r"&\bullet \ \text{Tipo: Arco de hipérbola homográfica creciente y convexa.} \\[4pt]"
            r"&\bullet \ \text{Asíntotas en } \mathbb{R}: \text{Vertical } x = -2 \ (\text{a la derecha}), \ \text{Horizontal } y = 1.5. \\[4pt]"
            r"&\bullet \ \textbf{Rango Deductivo Final: } \mathbf{\operatorname{Ran}(f) = {\color{amgreen}\left[\frac{25}{12}, \frac{8}{3}\right]}} \approx [2.083, 2.667]."
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{7. Síntesis y Puntos Notables:}\\[6pt]"
            r"$\bullet$ La tabla de valores ilustra el ascenso monótono continuo:\\[3pt]"
            r"\hspace*{1.0em}$2.083 < 2.200 < 2.278 < 2.375 < 2.667$.\\[5pt]"
            r"$\bullet$ Ambos extremos de frontera son cerrados ($\bullet$).\\[5pt]"
            r"$\bullet$ La curvatura es convexa ($f''(x) = -56/(2x+4)^3 > 0$ ya que $2x+4 < 0$).\\[5pt]"
            r"$\bullet$ Parámetros listos para el trazado gráfico."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq7, just7, box_color=THEME["success"], advance_to_step=6, wait_time=3.6)

        # ==========================================================
        # PASO 8: Trazado Cartesiano y Rango
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(7)

        # Panel izquierdo: Resumen geométrico
        t_card = Tex(
            r"\begin{minipage}{5.8cm}\raggedright "
            r"\textbf{{\color{amteal}Verificación Cartesiana:}}\\[6pt]"
            r"$\bullet$ \textbf{Asíntota Vertical:}\\[2pt]"
            r"\hspace*{0.8em}$x = -2$ exterior al dominio (línea punteada).\\[6pt]"
            r"$\bullet$ \textbf{Arco Homográfico:}\\[2pt]"
            r"\hspace*{0.8em}$f(x) = \frac{3x - 1}{2x + 4}$ en $[-8, -5]$.\\[6pt]"
            r"$\bullet$ \textbf{Mínimo Cerrado:}\\[2pt]"
            r"\hspace*{0.8em}$P_{\min}\left(-8, \frac{25}{12}\right)$ \textbf{Punto Cerrado} ($\bullet$).\\[6pt]"
            r"$\bullet$ \textbf{Máximo Cerrado:}\\[2pt]"
            r"\hspace*{0.8em}$P_{\max}\left(-5, \frac{8}{3}\right)$ \textbf{Punto Cerrado} ($\bullet$).\\[6pt]"
            r"$\bullet$ \textbf{Rango Proyectado:}\\[2pt]"
            r"\hspace*{0.8em}$\left[\frac{25}{12}, \frac{8}{3}\right]$ sobre el eje vertical $Y$."
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
            x_range=[-9.0, -1.5, 1],
            y_range=[0.0, 3.2, 0.5],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=13,
            labels_font_size=19
        )

        def f_val(x):
            return (3.0 * x - 1.0) / (2.0 * x + 4.0)

        # Asíntota vertical en x = -2
        asymp_m2 = DashedLine(
            axes.c2p(-2.0, 0.0),
            axes.c2p(-2.0, 3.1),
            color=THEME["axes"],
            stroke_width=1.8
        )
        lbl_asymp_m2 = MathTex(
            r"x=-2",
            font_size=13.0,
            color=THEME["axes"]
        ).next_to(axes.c2p(-2.0, 3.1), UP, buff=0.06)

        # Asíntota horizontal en y = 1.5
        asymp_h = DashedLine(
            axes.c2p(-9.0, 1.5),
            axes.c2p(-1.6, 1.5),
            color=THEME["axes"],
            stroke_width=1.2,
            stroke_opacity=0.6
        )

        # Curva de referencia tenue
        curve_ref = axes.plot(
            f_val,
            x_range=[-8.8, -3.5],
            color=THEME["statement_box"],
            stroke_width=1.5,
            stroke_opacity=0.35
        )

        # Arco de curva restringido en [-8.0, -5.0]
        curve_dom = axes.plot(
            f_val,
            x_range=[-8.0, -5.0],
            color=THEME["amarun_teal"],
            stroke_width=4.0
        )
        lbl_curve = MathTex(
            r"f(x) \text{ en } D",
            font_size=14.0,
            color=THEME["amarun_teal"]
        ).next_to(axes.c2p(-6.5, 2.28), UP, buff=0.10)

        # Extremo izquierdo cerrado P_min(-8, 25/12)
        p_left = axes.c2p(-8.0, 25.0 / 12.0)
        dot_left = Dot(p_left, radius=0.08, color=THEME["success"])
        lbl_left = MathTex(
            r"P_{\min}\left(-8, \frac{25}{12}\right)",
            font_size=12.0,
            color=THEME["success"]
        ).next_to(p_left, DOWN, buff=0.08)

        # Extremo derecho cerrado P_max(-5, 8/3)
        p_right = axes.c2p(-5.0, 8.0 / 3.0)
        dot_right = Dot(p_right, radius=0.08, color=THEME["success"])
        lbl_right = MathTex(
            r"P_{\max}\left(-5, \frac{8}{3}\right)",
            font_size=12.0,
            color=THEME["success"]
        ).next_to(p_right, UP, buff=0.08)

        # Proyección del dominio en la base: [-8, -5]
        dom_line = Line(
            axes.c2p(-8.0, 0.1),
            axes.c2p(-5.0, 0.1),
            color=THEME["highlight"],
            stroke_width=4.0
        )
        dom_dot_left = Dot(axes.c2p(-8.0, 0.1), radius=0.055, color=THEME["highlight"])
        dom_dot_right = Dot(axes.c2p(-5.0, 0.1), radius=0.055, color=THEME["highlight"])
        lbl_dom = MathTex(
            r"\operatorname{Dom}=[-8, -5]",
            font_size=11.5,
            color=THEME["highlight"]
        ).next_to(axes.c2p(-6.5, 0.1), DOWN, buff=0.10)

        # Proyección del rango sobre el borde izquierdo: [25/12, 8/3]
        range_line = Line(
            axes.c2p(-9.0, 25.0 / 12.0),
            axes.c2p(-9.0, 8.0 / 3.0),
            color=THEME["success"],
            stroke_width=5.0
        )
        dot_r_bottom = Dot(axes.c2p(-9.0, 25.0 / 12.0), radius=0.065, color=THEME["success"])
        dot_r_top = Dot(axes.c2p(-9.0, 8.0 / 3.0), radius=0.065, color=THEME["success"])
        lbl_range = MathTex(
            r"\operatorname{Ran}=\left[\frac{25}{12}, \frac{8}{3}\right]",
            font_size=11.5,
            color=THEME["success"]
        ).next_to(axes.c2p(-9.0, 2.38), RIGHT, buff=0.10)

        # Transición hacia el paso 8
        self.play(
            FadeOut(self.active_box),
            FadeOut(self.active_math, shift=DOWN * 0.2),
            FadeOut(self.active_just, shift=DOWN * 0.2),
            FadeIn(info_grp, shift=DOWN * 0.2),
            Create(axes),
            Write(axes_labels),
            Create(asymp_m2), Write(lbl_asymp_m2),
            Create(asymp_h),
            Create(curve_ref),
            *prog_anims,
            run_time=1.8
        )
        self.active_box = None
        self.active_math = None
        self.active_just = None

        # Trazado del arco restringido y dominio
        self.play(
            Create(curve_dom), Write(lbl_curve),
            Create(dom_line), FadeIn(dom_dot_left), FadeIn(dom_dot_right), Write(lbl_dom),
            run_time=2.2
        )

        # Proyección del rango y puntos notables
        self.play(
            Create(range_line), FadeIn(dot_r_bottom), FadeIn(dot_r_top), Write(lbl_range),
            FadeIn(dot_left), Write(lbl_left),
            FadeIn(dot_right), Write(lbl_right),
            run_time=1.8
        )
        self.wait(4.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            asymp_m2, lbl_asymp_m2, asymp_h, curve_ref,
            curve_dom, lbl_curve,
            dom_line, dom_dot_left, dom_dot_right, lbl_dom,
            range_line, dot_r_bottom, dot_r_top, lbl_range,
            dot_left, lbl_left,
            dot_right, lbl_right
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
