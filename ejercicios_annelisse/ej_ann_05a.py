r"""
Precálculo Universitario · Tutorías Annelisse / Editorial Amarun
Capítulo: Funciones Reales y Gráficas
Ejercicio 5.a: Rango de Función Racional con Dominio Acotado
               f(x) = 1/(x - 2),  Dom(f) = [3, 5[

Estructura de la Demostración (8 Pasos):
      1. Dominio restringido y singularidad: denominador x - 2 = 0 ⟹ x = 2 ∉ [3, 5[ (función continua y suave en D).
      2. Monotonía decreciente: primera derivada f'(x) = -1/(x - 2)² < 0 en todo D (invierte el orden).
      3. Extremo izquierdo cerrado: f(3) = 1 (máximo absoluto global alcanzado en punto cerrado •).
      4. Extremo derecho abierto: lim x→5⁻ f(x) = 1/3 (ínfimo no alcanzable en punto abierto ∘).
      5. Deducción formal del rango: 3 ≤ x < 5 ⟹ 1 ≤ x - 2 < 3 ⟹ 1/3 < f(x) ≤ 1 ⟹ Ran(f) = ]1/3, 1].
      6. Ausencia de raíces y positividad universal: f(x) > 0 en todo D, sin cortes con los ejes coordenados.
      7. Tabla de valores notables y síntesis institucional de propiedades.
      8. Trazado cartesiano riguroso: asíntota vertical x = 2 exterior, arco hiperbólico turquesa y rango en Y.

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


class EjercicioAnn_05a(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Annelisse",
            exercise="Ejercicio 5.a",
            topic="Rango de Función Racional Acotada [3, 5[",
            font_size=17.0
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 5.a: Determine el rango de la función racional en el dominio acotado:",
            math_tex=r"{\color{amteal}f(x) = \frac{1}{x - 2}}, \quad \operatorname{Dom}(f) = [3, 5[",
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
            "2/8: Monotonía Decreciente",
            "3/8: Extremo Izquierdo Cerrado",
            "4/8: Extremo Derecho Abierto",
            "5/8: Deducción Formal del Rango",
            "6/8: Ceros y Positividad",
            "7/8: Tabla y Síntesis",
            "8/8: Trazado Cartesiano y Rango"
        ], dot_spacing=0.82, label_font_size=14.0)

        # ==========================================================
        # PASO 1: Dominio y Singularidad
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Dominio Restringido y Singularidad del Denominador:} \\[6pt]"
            r"&\text{Regla de correspondencia dada en } D = [3, 5[: \\[4pt]"
            r"&\quad f(x) = {\color{amteal}\frac{1}{x - 2}} \\[6pt]"
            r"&\textbf{Condición de Existencia en } \mathbb{R}: \\[4pt]"
            r"&\quad x - 2 = 0 \iff {\color{amred}x = 2} \quad (\text{Asíntota Vertical}) \\[6pt]"
            r"&\textbf{Posición de la Singularidad respecto al Dominio } D: \\[4pt]"
            r"&\quad 2 < 3 \le x < 5 \implies \mathbf{{\color{amgreen}2 \notin [3, 5[}} \\[6pt]"
            r"&\therefore \quad x - 2 \ge 1 > 0 \implies \mathbf{f(x) \text{ es continua y suave en todo } D.}"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Continuidad y Singularidad:}\\[6pt]"
            r"$\bullet$ La función racional tiene una singularidad en el cero del denominador: $x = 2$.\\[5pt]"
            r"$\bullet$ El dominio asignado es el intervalo acotado $D = [3, 5[$.\\[5pt]"
            r"$\bullet$ Como $x = 2 < 3$, la asíntota vertical queda completamente fuera de $D$.\\[5pt]"
            r"$\bullet$ En consecuencia, el denominador nunca se anula y es estrictamente positivo en $D$.\\[5pt]"
            r"$\bullet$ $f(x)$ es continua y diferenciable en todo su dominio."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=3.6)

        # ==========================================================
        # PASO 2: Monotonía Decreciente
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Análisis de Monotonía (Primera Derivada):} \\[6pt]"
            r"&\text{Diferenciando } f(x) = (x - 2)^{-1} \text{ para } x \in [3, 5[: \\[4pt]"
            r"&\quad f'(x) = -(x - 2)^{-2} = \mathbf{{\color{amred}-\frac{1}{(x - 2)^2}}} \\[6pt]"
            r"&\textbf{Evaluación del Signo en } D: \\[4pt]"
            r"&\quad (x - 2)^2 \ge 1^2 = 1 > 0 \implies \mathbf{{\color{amred}f'(x) < 0, \quad \forall x \in [3, 5[}} \\[6pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}f(x) \text{ es ESTRICTAMENTE DECRECIENTE en } D}} \\[6pt]"
            r"&\implies \forall x_1 < x_2 \in D: \quad \mathbf{f(x_1) > f(x_2)} \quad (\text{Invierte el orden})"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Monotonía Decreciente:}\\[6pt]"
            r"$\bullet$ La derivada $f'(x) = -1/(x-2)^2$ tiene numerador negativo y denominador positivo.\\[5pt]"
            r"$\bullet$ Al ser $f'(x) < 0$ para todo $x \in D$, la función decrece monótonamente sin oscilaciones.\\[5pt]"
            r"$\bullet$ La monotonía estricta garantiza que:\\[3pt]"
            r"\hspace*{1.0em}El mayor valor se alcanza en la frontera izquierda ($x = 3$).\\[3pt]"
            r"\hspace*{1.0em}El menor valor se aproxima en la frontera derecha ($x \to 5^-$).\\[5pt]"
            r"$\bullet$ El orden de las desigualdades se invierte ordenadamente."
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
            r"&\textbf{3. Evaluación en el Extremo Izquierdo Cerrado } (x = 3): \\[6pt]"
            r"&\text{Dado que } 3 \in D \text{ (corchete cerrado } [3\text{):} \\[4pt]"
            r"&\quad f(3) = \frac{1}{3 - 2} = \frac{1}{1} = \mathbf{{\color{amgold}1}} \\[6pt]"
            r"&\textbf{Naturaleza del Extremo:} \\[4pt]"
            r"&\text{Al ser } f \text{ decreciente en } [3, 5[, \text{ su valor máximo absoluto} \\[4pt]"
            r"&\text{ocurre en el punto inicial } x = 3: \\[4pt]"
            r"&\quad \mathbf{{\color{amgreen}M = \max_{x \in D} f(x) = 1}} \\[6pt]"
            r"&\therefore \quad \mathbf{\text{Punto de Frontera Cerrado: }} \mathbf{{\color{amgold}P_{\max}(3, 1)}} \quad (\text{Punto } \bullet)"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{3. Máximo Absoluto Global:}\\[6pt]"
            r"$\bullet$ En el extremo izquierdo $x = 3$, el denominador toma su valor mínimo: $3 - 2 = 1$.\\[5pt]"
            r"$\bullet$ El cociente alcanza su valor más alto: $f(3) = 1$.\\[5pt]"
            r"$\bullet$ Como $3 \in D$, este punto pertenece lícitamente a la gráfica ($\bullet$).\\[5pt]"
            r"$\bullet$ Representa la cota superior estricta y cerrada del rango: $y \le 1$.\\[5pt]"
            r"$\bullet$ $M = 1$ es el máximo global alcanzado en el dominio."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq3, just3, box_color=THEME["statement_box"], advance_to_step=2, wait_time=3.6)

        # ==========================================================
        # PASO 4: Extremo Derecho Abierto
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Evaluación en el Extremo Derecho Abierto } (x \to 5^-): \\[6pt]"
            r"&\text{Dado que } 5 \notin D \text{ (corchete abierto } 5[\text{):} \\[4pt]"
            r"&\quad \lim_{x \to 5^-} f(x) = \frac{1}{5 - 2} = \mathbf{{\color{amred}\frac{1}{3}}} \approx \mathbf{0.3333} \\[6pt]"
            r"&\textbf{Naturaleza del Extremo:} \\[4pt]"
            r"&\text{Al decrecer continuamente hacia } x = 5, \text{ los valores de } f(x) \\[4pt]"
            r"&\text{se aproximan por arriba a } 1/3, \text{ sin llegar jamás a tocarlo:} \\[4pt]"
            r"&\quad \mathbf{{\color{amgreen}m = \inf_{x \in D} f(x) = \frac{1}{3}}} \quad (\text{Ínfimo no alcanzable}) \\[6pt]"
            r"&\therefore \quad \mathbf{\text{Punto de Frontera Abierto: }} \mathbf{{\color{amteal}P_{\inf}\left(5, \frac{1}{3}\right)}} \quad (\text{Punto } \circ)"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Cota Inferior e Ínfimo:}\\[6pt]"
            r"$\bullet$ En $x \to 5^-$, el denominador alcanza su valor máximo: $5 - 2 = 3$.\\[5pt]"
            r"$\bullet$ La función desciende hasta aproximarse al valor límite $1/3$.\\[5pt]"
            r"$\bullet$ Dado que $x = 5 \notin D$, el valor $1/3$ no es parte de la imagen.\\[5pt]"
            r"$\bullet$ Constituye el ínfimo estricto (cota inferior abierta en $\circ$).\\[5pt]"
            r"$\bullet$ Todo valor de la función satisface $f(x) > 1/3$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq4, just4, box_color=THEME["error"], advance_to_step=3, wait_time=3.6)

        # ==========================================================
        # PASO 5: Deducción Formal del Rango
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Deducción Formal del Rango mediante Inecuaciones:} \\[6pt]"
            r"&\text{Partiendo de la definición formal del dominio } D: \\[4pt]"
            r"&\quad 3 \le x < 5 \\[6pt]"
            r"&\text{Restando } 2 \text{ a cada miembro de la desigualdad:} \\[4pt]"
            r"&\quad 3 - 2 \le x - 2 < 5 - 2 \iff \mathbf{{\color{amgold}1 \le x - 2 < 3}} \\[6pt]"
            r"&\text{Aplicando el inverso multiplicativo } (u > 0 \implies \text{invierte el orden}): \\[4pt]"
            r"&\quad \frac{1}{3} < \frac{1}{x - 2} \le \frac{1}{1} \iff \mathbf{{\color{amgreen}\frac{1}{3} < f(x) \le 1}} \\[6pt]"
            r"&\therefore \quad \mathbf{\operatorname{Ran}(f) = {\color{amgreen}\left]\frac{1}{3}, 1\right]}} = \mathbf{{\color{amgreen}\left(\frac{1}{3}, 1\right]}}"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Deducción Rigurosa del Rango:}\\[6pt]"
            r"$\bullet$ Partimos de la restricción del dominio: $3 \le x < 5$.\\[5pt]"
            r"$\bullet$ El argumento $x - 2$ recorre el intervalo positivo $[1, 3[$.\\[5pt]"
            r"$\bullet$ La función recíproca $1/u$ es estrictamente decreciente para $u > 0$.\\[5pt]"
            r"$\bullet$ Al invertir, el sentido de las desigualdades se voltea:\\[3pt]"
            r"\hspace*{1.0em}$1 \le u < 3 \iff 1/3 < 1/u \le 1$.\\[5pt]"
            r"$\bullet$ Por el Teorema del Valor Intermedio, cubre todo el intervalo:\\[3pt]"
            r"\hspace*{1.0em}${\color{amgreen}\operatorname{Ran}(f) = \left]\frac{1}{3}, 1\right]}$.\\[5pt]"
            r"$\bullet$ Extremo izquierdo abierto en $1/3$, extremo derecho cerrado en $1$."
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
            r"&\quad \frac{1}{x - 2} = 0 \iff 1 = 0 \cdot (x - 2) = 0 \quad (\textbf{Absurdo}) \\[4pt]"
            r"&\implies \mathbf{\text{No existen ceros reales}} \implies \mathbf{\text{Sin cortes con el eje } X.} \\[6pt]"
            r"&\textbf{Intersección con el Eje } Y \ (x = 0): \\[4pt]"
            r"&\quad 0 \notin [3, 5[ \implies \mathbf{\text{Sin corte con el eje } Y \text{ en } D.} \\[6pt]"
            r"&\textbf{Comportamiento de Signos en } D = [3, 5[: \\[4pt]"
            r"&\quad \text{Dado que } \operatorname{Ran}(f) = \left]\frac{1}{3}, 1\right] \subset \mathbb{R}^+: \\[4pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}\forall x \in [3, 5[: \quad f(x) > 0}} \quad (\textbf{Estrictamente Positiva})"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{6. Signos e Intersecciones:}\\[6pt]"
            r"$\bullet$ Una fracción con numerador constante no nulo jamás puede anularse: $1/(x-2) \ne 0$.\\[5pt]"
            r"$\bullet$ Por lo tanto, no existen raíces ni cortes con el eje $X$.\\[5pt]"
            r"$\bullet$ El origen $x = 0$ está fuera de $D \implies$ no hay corte con el eje $Y$.\\[5pt]"
            r"$\bullet$ Como todo valor en el rango pertenece a $]1/3, 1]$, la curva es $100\%$ positiva.\\[5pt]"
            r"$\bullet$ La gráfica flota en el primer cuadrante cartesiano."
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
            r"&\begin{array}{|c|c|c|c|c|} \hline "
            r"x & \mathbf{3} & 3.5 & 4 & \mathbf{5} \\ \hline "
            r"f(x) & \mathbf{{\color{amgreen}1}} & 2/3 \approx 0.67 & 1/2 = 0.5 & \mathbf{{\color{amred}1/3 \approx 0.33}} \\ \hline "
            r"\text{Rol} & \mathbf{\text{Máx } \bullet} & \text{Punto} & \text{Punto} & \mathbf{\text{Ínfimo } \circ} \\ \hline "
            r"\end{array} \\[8pt]"
            r"&\textbf{Síntesis de Propiedades Institucionales:} \\[5pt]"
            r"&\bullet \ \text{Tipo: Arco de hipérbola equilátera decreciente y convexa.} \\[4pt]"
            r"&\bullet \ \text{Asíntota vertical: } x = 2 \notin D \quad (\text{Exterior a la izquierda}). \\[4pt]"
            r"&\bullet \ \text{Dominio Restringido: } \operatorname{Dom}(f) = [3, 5[. \\[4pt]"
            r"&\bullet \ \textbf{Rango Deductivo Final: } \mathbf{\operatorname{Ran}(f) = {\color{amgreen}\left]\frac{1}{3}, 1\right]}}."
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{7. Síntesis y Puntos Notables:}\\[6pt]"
            r"$\bullet$ La tabla de valores ilustra numéricamente la curvatura hiperbólica convexa:\\[3pt]"
            r"\hspace*{1.0em}$f(3)=1$, $f(3.5)=2/3$, $f(4)=1/2$, $f(5)=1/3$.\\[5pt]"
            r"$\bullet$ Frontera izquierda cerrada en $(3, 1)$ con máximo global.\\[5pt]"
            r"$\bullet$ Frontera derecha abierta en $(5, 1/3)$ con límite inferior no alcanzable.\\[5pt]"
            r"$\bullet$ Todos los datos analíticos quedan listos para el trazado gráfico."
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
            r"\hspace*{0.8em}$x = 2$ exterior al dominio (línea punteada).\\[6pt]"
            r"$\bullet$ \textbf{Arco de Hipérbola:}\\[2pt]"
            r"\hspace*{0.8em}$f(x) = \frac{1}{x - 2}$ en $[3, 5[$.\\[6pt]"
            r"$\bullet$ \textbf{Máximo Cerrado:}\\[2pt]"
            r"\hspace*{0.8em}$P_{\max}(3, 1)$ \textbf{Punto Cerrado} ($\bullet$).\\[6pt]"
            r"$\bullet$ \textbf{Ínfimo Abierto:}\\[2pt]"
            r"\hspace*{0.8em}$P_{\inf}\left(5, \frac{1}{3}\right)$ \textbf{Punto Abierto} ($\circ$).\\[6pt]"
            r"$\bullet$ \textbf{Rango Proyectado:}\\[2pt]"
            r"\hspace*{0.8em}$\left]\frac{1}{3}, 1\right]$ sobre el eje vertical $Y$."
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
            x_range=[1.5, 5.8, 1],
            y_range=[0.0, 1.4, 0.5],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=13,
            labels_font_size=19
        )

        def f_val(x):
            return 1.0 / (x - 2.0)

        # Asíntota vertical en x = 2
        asymp_2 = DashedLine(
            axes.c2p(2.0, 0.0),
            axes.c2p(2.0, 1.35),
            color=THEME["axes"],
            stroke_width=1.8
        )
        lbl_asymp_2 = MathTex(
            r"x=2",
            font_size=13.0,
            color=THEME["axes"]
        ).next_to(axes.c2p(2.0, 1.35), UP, buff=0.06)

        # Curva de referencia tenue
        curve_ref = axes.plot(
            f_val,
            x_range=[2.75, 5.7],
            color=THEME["statement_box"],
            stroke_width=1.5,
            stroke_opacity=0.35
        )

        # Arco de curva restringido en [3.0, 4.96]
        curve_dom = axes.plot(
            f_val,
            x_range=[3.0, 4.96],
            color=THEME["amarun_teal"],
            stroke_width=4.0
        )
        lbl_curve = MathTex(
            r"f(x) \text{ en } D",
            font_size=14.0,
            color=THEME["amarun_teal"]
        ).next_to(axes.c2p(4.0, 0.5), UR, buff=0.10)

        # Extremo izquierdo cerrado P_max(3, 1)
        p_left = axes.c2p(3.0, 1.0)
        dot_left = Dot(p_left, radius=0.08, color=THEME["success"])
        lbl_left = MathTex(
            r"P_{\max}(3, 1)",
            font_size=12.5,
            color=THEME["success"]
        ).next_to(p_left, UR, buff=0.08)

        # Extremo derecho abierto P_inf(5, 1/3): círculo hueco
        p_right = axes.c2p(5.0, 1.0 / 3.0)
        dot_right = Circle(
            radius=0.07,
            color=THEME["error"],
            stroke_width=2.5,
            fill_color=THEME["bg_color"],
            fill_opacity=1.0
        ).move_to(p_right)
        lbl_right = MathTex(
            r"P_{\inf}\left(5, \frac{1}{3}\right)",
            font_size=12.5,
            color=THEME["error"]
        ).next_to(p_right, UR, buff=0.08)

        # Proyección del dominio en la base: [3, 5[
        dom_line = Line(
            axes.c2p(3.0, 0.05),
            axes.c2p(5.0, 0.05),
            color=THEME["highlight"],
            stroke_width=4.0
        )
        dom_dot_closed = Dot(axes.c2p(3.0, 0.05), radius=0.055, color=THEME["highlight"])
        dom_dot_open = Circle(
            radius=0.05,
            color=THEME["highlight"],
            stroke_width=2.0,
            fill_color=THEME["bg_color"],
            fill_opacity=1.0
        ).move_to(axes.c2p(5.0, 0.05))
        lbl_dom = MathTex(
            r"\operatorname{Dom}=[3, 5[",
            font_size=11.5,
            color=THEME["highlight"]
        ).next_to(axes.c2p(4.0, 0.05), DOWN, buff=0.10)

        # Proyección del rango sobre el eje Y: ]1/3, 1]
        range_line = Line(
            axes.c2p(1.5, 1.0 / 3.0),
            axes.c2p(1.5, 1.0),
            color=THEME["success"],
            stroke_width=5.0
        )
        dot_r_open = Circle(
            radius=0.06,
            color=THEME["error"],
            stroke_width=2.2,
            fill_color=THEME["bg_color"],
            fill_opacity=1.0
        ).move_to(axes.c2p(1.5, 1.0 / 3.0))
        dot_r_closed = Dot(axes.c2p(1.5, 1.0), radius=0.065, color=THEME["success"])
        lbl_range = MathTex(
            r"\operatorname{Ran}(f) = \left]\frac{1}{3}, 1\right]",
            font_size=12.0,
            color=THEME["success"]
        ).next_to(axes.c2p(1.5, 0.67), RIGHT, buff=0.10)

        # Transición hacia el paso 8
        self.play(
            FadeOut(self.active_box),
            FadeOut(self.active_math, shift=DOWN * 0.2),
            FadeOut(self.active_just, shift=DOWN * 0.2),
            FadeIn(info_grp, shift=DOWN * 0.2),
            Create(axes),
            Write(axes_labels),
            Create(asymp_2), Write(lbl_asymp_2),
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
            Create(dom_line), FadeIn(dom_dot_closed), FadeIn(dom_dot_open), Write(lbl_dom),
            run_time=2.2
        )

        # Proyección del rango y puntos notables
        self.play(
            Create(range_line), FadeIn(dot_r_open), FadeIn(dot_r_closed), Write(lbl_range),
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
            asymp_2, lbl_asymp_2, curve_ref,
            curve_dom, lbl_curve,
            dom_line, dom_dot_closed, dom_dot_open, lbl_dom,
            range_line, dot_r_open, dot_r_closed, lbl_range,
            dot_left, lbl_left,
            dot_right, lbl_right
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
