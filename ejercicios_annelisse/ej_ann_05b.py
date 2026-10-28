r"""
Precálculo Universitario · Tutorías Annelisse / Editorial Amarun
Capítulo: Funciones Reales y Gráficas
Ejercicio 5.b: Rango de Función Racional Reducible con Dominio Acotado
               f(x) = (x² - 1)/(x - 1),  Dom(f) = [9, 17]

Estructura de la Demostración (8 Pasos):
      1. Dominio restringido y factorización: cociente racional con diferencia de cuadrados (x-1)(x+1)/(x-1).
      2. Discontinuidad evitable excluida: singularidad en x = 1 ∉ [9, 17] ⟹ simplificación exacta f(x) = x + 1.
      3. Monotonía estricta: función lineal afín con pendiente m = 1 > 0 ⟹ f'(x) = 1 > 0 (estrictamente creciente).
      4. Evaluación en extremo izquierdo: x = 9 ∈ D ⟹ f(9) = 10 (mínimo absoluto en punto cerrado •).
      5. Evaluación en extremo derecho: x = 17 ∈ D ⟹ f(17) = 18 (máximo absoluto en punto cerrado •).
      6. Deducción formal del rango: 9 ≤ x ≤ 17 ⟹ 10 ≤ x + 1 ≤ 18 ⟹ Ran(f) = [10, 18] (intervalo compacto).
      7. Tabla de valores notables, ausencia de raíces en D y positividad universal.
      8. Trazado cartesiano riguroso: segmento de recta turquesa, nodos cerrados • y proyecciones de Dom y Ran.

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


class EjercicioAnn_05b(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Annelisse",
            exercise="Ejercicio 5.b",
            topic="Rango de Función Racional Reducible [9, 17]",
            font_size=17.0
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 5.b: Determine el rango de la función racional en el dominio acotado:",
            math_tex=r"{\color{amteal}f(x) = \frac{x^2 - 1}{x - 1}}, \quad \operatorname{Dom}(f) = [9, 17]",
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
            "1/8: Dominio y Factorización",
            "2/8: Simplificación Exacta",
            "3/8: Monotonía Creciente",
            "4/8: Extremo Izquierdo Cerrado",
            "5/8: Extremo Derecho Cerrado",
            "6/8: Deducción Formal del Rango",
            "7/8: Tabla y Positividad",
            "8/8: Trazado Cartesiano y Rango"
        ], dot_spacing=0.82, label_font_size=14.0)

        # ==========================================================
        # PASO 1: Dominio Restringido y Factorización
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Dominio Restringido y Factorización del Cociente:} \\[6pt]"
            r"&\text{Regla de correspondencia dada en el intervalo cerrado } D = [9, 17]: \\[4pt]"
            r"&\quad f(x) = {\color{amteal}\frac{x^2 - 1}{x - 1}} \\[6pt]"
            r"&\textbf{Factorización del Numerador por Diferencia de Cuadrados:} \\[4pt]"
            r"&\quad x^2 - 1 = (x - 1)(x + 1) \\[6pt]"
            r"&\implies f(x) = \frac{(x - 1)(x + 1)}{x - 1} \\[6pt]"
            r"&\therefore \quad \text{El factor común } (x - 1) \text{ revela una discontinuidad en } x = 1."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Factorización y Cociente:}\\[6pt]"
            r"$\bullet$ La función es un cociente de polinomios con dominio acotado $D = [9, 17]$.\\[5pt]"
            r"$\bullet$ El numerador admite descomposición inmediata por diferencia de cuadrados:\\[3pt]"
            r"\hspace*{1.0em}$x^2 - 1 = (x - 1)(x + 1)$.\\[5pt]"
            r"$\bullet$ El factor binomio $(x - 1)$ se comparte con el denominador.\\[5pt]"
            r"$\bullet$ Esto indica la presencia de una discontinuidad evitable en $x = 1$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=3.6)

        # ==========================================================
        # PASO 2: Discontinuidad Evitable Excluida y Reducción
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Discontinuidad Evitable Excluida del Dominio:} \\[6pt]"
            r"&\textbf{Condición de Existencia en } \mathbb{R}: \\[4pt]"
            r"&\quad x - 1 = 0 \iff {\color{amred}x = 1} \quad (\text{Discontinuidad Evitable / Agujero}) \\[6pt]"
            r"&\textbf{Posición de la Singularidad respecto al Dominio } D: \\[4pt]"
            r"&\quad 1 < 9 \le x \le 17 \implies \mathbf{{\color{amgreen}1 \notin [9, 17]}} \\[6pt]"
            r"&\text{Como } x \neq 1 \text{ para todo } x \in D, \text{ simplificamos lícitamente:} \\[4pt]"
            r"&\quad f(x) = \frac{\cancel{(x - 1)}(x + 1)}{\cancel{x - 1}} = \mathbf{{\color{amteal}x + 1}}, \quad \forall x \in [9, 17] \\[6pt]"
            r"&\therefore \quad \mathbf{f(x) \text{ es una función lineal continua y suave en todo } D.}"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Simplificación Lícita:}\\[6pt]"
            r"$\bullet$ La discontinuidad removible ocurre únicamente en $x = 1$.\\[5pt]"
            r"$\bullet$ Dado que $1 \notin [9, 17]$, la variable jamás toma el valor prohibido.\\[5pt]"
            r"$\bullet$ Al cancelar lícitamente $(x - 1) \neq 0$, la regla se reduce exactamente a:\\[3pt]"
            r"\hspace*{1.0em}${\color{amteal}f(x) = x + 1}$ para todo $x \in [9, 17]$.\\[5pt]"
            r"$\bullet$ En este intervalo cerrado, la curva es idéntica a un segmento de recta."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=3.6)

        # ==========================================================
        # PASO 3: Monotonía Estrictamente Creciente
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Monotonía Estricta y Pendiente Positiva:} \\[6pt]"
            r"&\text{Para la forma reducida } f(x) = x + 1 \text{ en } D = [9, 17]: \\[4pt]"
            r"&\quad f'(x) = \frac{d}{dx}(x + 1) = \mathbf{{\color{amgreen}1 > 0}}, \quad \forall x \in [9, 17] \\[6pt]"
            r"&\textbf{Comportamiento de la Función Afín:} \\[4pt]"
            r"&\bullet \ \text{Pendiente } m = 1 > 0 \implies \mathbf{{\color{amgreen}\text{ESTRICTAMENTE CRECIENTE}}} \\[6pt]"
            r"&\implies \forall x_1 < x_2 \in [9, 17]: \quad \mathbf{f(x_1) < f(x_2)} \\[6pt]"
            r"&\therefore \quad \text{La función preserva estrictamente el orden de los extremos.}"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{3. Monotonía Creciente:}\\[6pt]"
            r"$\bullet$ La función reducida $f(x) = x + 1$ tiene pendiente constante positiva $m = 1$.\\[5pt]"
            r"$\bullet$ Su derivada es $f'(x) = 1 > 0$ en cada punto del dominio.\\[5pt]"
            r"$\bullet$ Al ser monótona estrictamente creciente:\\[3pt]"
            r"\hspace*{1.0em}El valor mínimo ocurre en el extremo izquierdo ($x = 9$).\\[3pt]"
            r"\hspace*{1.0em}El valor máximo ocurre en el extremo derecho ($x = 17$).\\[5pt]"
            r"$\bullet$ El orden de las desigualdades se preserva sin cambios."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq3, just3, box_color=THEME["statement_box"], advance_to_step=2, wait_time=3.6)

        # ==========================================================
        # PASO 4: Evaluación en el Extremo Izquierdo Cerrado
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Evaluación en el Extremo Izquierdo Cerrado } (x = 9): \\[6pt]"
            r"&\text{Dado que } 9 \in D \text{ (corchete cerrado } [9\text{):} \\[4pt]"
            r"&\quad f(9) = 9 + 1 = \mathbf{{\color{amgold}10}} \\[6pt]"
            r"&\textbf{Naturaleza del Extremo:} \\[4pt]"
            r"&\text{Al ser } f \text{ creciente en } [9, 17], \text{ su valor mínimo absoluto} \\[4pt]"
            r"&\text{ocurre en el punto inicial } x = 9: \\[4pt]"
            r"&\quad \mathbf{{\color{amgreen}m = \min_{x \in D} f(x) = 10}} \\[6pt]"
            r"&\therefore \quad \mathbf{\text{Punto de Frontera Cerrado: }} \mathbf{{\color{amgold}P_{\min}(9, 10)}} \quad (\text{Punto } \bullet)"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Mínimo Absoluto Global:}\\[6pt]"
            r"$\bullet$ Evaluamos en la frontera inferior $x = 9$ incluida en el dominio.\\[5pt]"
            r"$\bullet$ Obtenemos directamente $f(9) = 9 + 1 = 10$.\\[5pt]"
            r"$\bullet$ Como $9 \in D$, este punto pertenece formalmente a la gráfica ($\bullet$).\\[5pt]"
            r"$\bullet$ Constituye la cota inferior estricta y cerrada del rango: $y \ge 10$.\\[5pt]"
            r"$\bullet$ $m = 10$ es el valor mínimo absoluto alcanzado en $D$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq4, just4, box_color=THEME["error"], advance_to_step=3, wait_time=3.6)

        # ==========================================================
        # PASO 5: Evaluación en el Extremo Derecho Cerrado
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Evaluación en el Extremo Derecho Cerrado } (x = 17): \\[6pt]"
            r"&\text{Dado que } 17 \in D \text{ (corchete cerrado } 17]\text{):} \\[4pt]"
            r"&\quad f(17) = 17 + 1 = \mathbf{{\color{amgold}18}} \\[6pt]"
            r"&\textbf{Naturaleza del Extremo:} \\[4pt]"
            r"&\text{Al ser } f \text{ creciente en } [9, 17], \text{ su valor máximo absoluto} \\[4pt]"
            r"&\text{se alcanza en el punto final } x = 17: \\[4pt]"
            r"&\quad \mathbf{{\color{amgreen}M = \max_{x \in D} f(x) = 18}} \\[6pt]"
            r"&\therefore \quad \mathbf{\text{Punto de Frontera Cerrado: }} \mathbf{{\color{amteal}P_{\max}(17, 18)}} \quad (\text{Punto } \bullet)"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Máximo Absoluto Global:}\\[6pt]"
            r"$\bullet$ Evaluamos en la frontera superior $x = 17$ incluida en el dominio.\\[5pt]"
            r"$\bullet$ Obtenemos de forma exacta $f(17) = 17 + 1 = 18$.\\[5pt]"
            r"$\bullet$ Al ser $17 \in D$, el extremo superior es plenamente alcanzable ($\bullet$).\\[5pt]"
            r"$\bullet$ Constituye la cota superior estricta y cerrada del rango: $y \le 18$.\\[5pt]"
            r"$\bullet$ $M = 18$ es el valor máximo absoluto alcanzado en $D$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq5, just5, box_color=THEME["curve"], advance_to_step=4, wait_time=3.6)

        # ==========================================================
        # PASO 6: Deducción Formal del Rango por Inecuaciones
        # ==========================================================
        eq6 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Deducción Formal del Rango mediante Inecuaciones:} \\[6pt]"
            r"&\text{Partiendo de la definición formal del dominio compacto } D: \\[4pt]"
            r"&\quad 9 \le x \le 17 \\[6pt]"
            r"&\text{Sumando } 1 \text{ a cada miembro de la desigualdad:} \\[4pt]"
            r"&\quad 9 + 1 \le x + 1 \le 17 + 1 \iff \mathbf{{\color{amgold}10 \le x + 1 \le 18}} \\[6pt]"
            r"&\text{Sustituyendo la regla simplificada } f(x) = x + 1: \\[4pt]"
            r"&\quad \mathbf{{\color{amgreen}10 \le f(x) \le 18}} \\[6pt]"
            r"&\therefore \quad \mathbf{\operatorname{Ran}(f) = {\color{amgreen}[10, 18]}} \quad (\text{Intervalo Cerrado Compacto})"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{6. Conclusión Formal del Rango:}\\[6pt]"
            r"$\bullet$ Por el Teorema del Valor Intermedio sobre un intervalo conexo cerrado:\\[5pt]"
            r"$\bullet$ La imagen cubre continuamente todos los valores entre $10$ y $18$.\\[5pt]"
            r"$\bullet$ El extremo inferior está cerrado en $10$ porque $9 \in D$.\\[5pt]"
            r"$\bullet$ El extremo superior está cerrado en $18$ porque $17 \in D$.\\[5pt]"
            r"$\bullet$ Rango final: ${\color{amgreen}\operatorname{Ran}(f) = [10, 18]}$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq6, just6, box_color=THEME["statement_box"], advance_to_step=5, wait_time=3.6)

        # ==========================================================
        # PASO 7: Tabla y Positividad Universal
        # ==========================================================
        eq7 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{7. Tabla de Valores Notables y Síntesis en } D: \\[6pt]"
            r"&\begin{array}{|c|c|c|c|c|c|} \hline "
            r"x & \mathbf{9} & 11 & \mathbf{13} & 15 & \mathbf{17} \\ \hline "
            r"f(x) & \mathbf{{\color{amgreen}10}} & 12 & \mathbf{14} & 16 & \mathbf{{\color{amgreen}18}} \\ \hline "
            r"\text{Rol} & \mathbf{\text{Mín } \bullet} & \text{Punto} & \text{Medio} & \text{Punto} & \mathbf{\text{Máx } \bullet} \\ \hline "
            r"\end{array} \\[8pt]"
            r"&\textbf{Propiedades Analíticas en } D = [9, 17]: \\[5pt]"
            r"&\bullet \ \text{Raíz real: } x = -1 \notin D \implies \mathbf{\text{Sin cortes con el eje } X} \\[4pt]"
            r"&\bullet \ \text{Corte eje } Y: 0 \notin D \implies \mathbf{\text{Sin corte con el eje } Y} \\[4pt]"
            r"&\bullet \ \text{Signos: } \mathbf{{\color{amgreen}\forall x \in D: \ f(x) \in [10, 18] > 0}} \quad (\text{Estrictamente Positiva})"
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{7. Síntesis y Propiedades:}\\[6pt]"
            r"$\bullet$ La tabla de valores muestra la progresión aritmética uniforme de paso $+2$.\\[5pt]"
            r"$\bullet$ La única raíz de la recta es $x = -1$, muy alejada de $[9, 17]$.\\[5pt]"
            r"$\bullet$ Al estar comprendida entre $10$ y $18$, la función es $100\%$ positiva.\\[5pt]"
            r"$\bullet$ Ambos extremos de frontera son cerrados ($\bullet$).\\[5pt]"
            r"$\bullet$ Datos analíticos listos para el trazado cartesiano."
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
            r"$\bullet$ \textbf{Segmento Lineal:}\\[2pt]"
            r"\hspace*{0.8em}$f(x) = x + 1$ en $[9, 17]$.\\[6pt]"
            r"$\bullet$ \textbf{Mínimo Cerrado:}\\[2pt]"
            r"\hspace*{0.8em}$P_{\min}(9, 10)$ \textbf{Punto Cerrado} ($\bullet$).\\[6pt]"
            r"$\bullet$ \textbf{Máximo Cerrado:}\\[2pt]"
            r"\hspace*{0.8em}$P_{\max}(17, 18)$ \textbf{Punto Cerrado} ($\bullet$).\\[6pt]"
            r"$\bullet$ \textbf{Dominio Proyectado:}\\[2pt]"
            r"\hspace*{0.8em}$[9, 17]$ sobre el eje horizontal $X$.\\[6pt]"
            r"$\bullet$ \textbf{Rango Proyectado:}\\[2pt]"
            r"\hspace*{0.8em}$[10, 18]$ sobre el eje vertical $Y$."
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
            x_range=[8.0, 18.0, 2],
            y_range=[8.0, 20.0, 2],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=13,
            labels_font_size=19
        )

        def f_val(x):
            return x + 1.0

        # Curva de referencia tenue
        curve_ref = axes.plot(
            f_val,
            x_range=[8.2, 17.8],
            color=THEME["statement_box"],
            stroke_width=1.5,
            stroke_opacity=0.35
        )

        # Segmento restringido en [9.0, 17.0]
        curve_dom = axes.plot(
            f_val,
            x_range=[9.0, 17.0],
            color=THEME["amarun_teal"],
            stroke_width=4.0
        )
        lbl_curve = MathTex(
            r"f(x) = x + 1",
            font_size=13.5,
            color=THEME["amarun_teal"]
        ).next_to(axes.c2p(13.0, 14.0), UL, buff=0.10)

        # Extremo izquierdo cerrado P_min(9, 10)
        p_left = axes.c2p(9.0, 10.0)
        dot_left = Dot(p_left, radius=0.08, color=THEME["success"])
        lbl_left = MathTex(
            r"P_{\min}(9, 10)",
            font_size=12.5,
            color=THEME["success"]
        ).next_to(p_left, UR, buff=0.08)

        # Extremo derecho cerrado P_max(17, 18)
        p_right = axes.c2p(17.0, 18.0)
        dot_right = Dot(p_right, radius=0.08, color=THEME["success"])
        lbl_right = MathTex(
            r"P_{\max}(17, 18)",
            font_size=12.5,
            color=THEME["success"]
        ).next_to(p_right, UL, buff=0.08)

        # Proyección del dominio en la base: [9, 17]
        dom_line = Line(
            axes.c2p(9.0, 8.2),
            axes.c2p(17.0, 8.2),
            color=THEME["highlight"],
            stroke_width=4.0
        )
        dom_dot_left = Dot(axes.c2p(9.0, 8.2), radius=0.055, color=THEME["highlight"])
        dom_dot_right = Dot(axes.c2p(17.0, 8.2), radius=0.055, color=THEME["highlight"])
        lbl_dom = MathTex(
            r"\operatorname{Dom}=[9, 17]",
            font_size=11.5,
            color=THEME["highlight"]
        ).next_to(axes.c2p(13.0, 8.2), DOWN, buff=0.10)

        # Proyección del rango sobre el eje Y: [10, 18]
        range_line = Line(
            axes.c2p(8.0, 10.0),
            axes.c2p(8.0, 18.0),
            color=THEME["success"],
            stroke_width=5.0
        )
        dot_r_bottom = Dot(axes.c2p(8.0, 10.0), radius=0.065, color=THEME["success"])
        dot_r_top = Dot(axes.c2p(8.0, 18.0), radius=0.065, color=THEME["success"])
        lbl_range = MathTex(
            r"\operatorname{Ran}(f) = [10, 18]",
            font_size=12.0,
            color=THEME["success"]
        ).next_to(axes.c2p(8.0, 14.0), RIGHT, buff=0.10)

        # Transición hacia el paso 8
        self.play(
            FadeOut(self.active_box),
            FadeOut(self.active_math, shift=DOWN * 0.2),
            FadeOut(self.active_just, shift=DOWN * 0.2),
            FadeIn(info_grp, shift=DOWN * 0.2),
            Create(axes),
            Write(axes_labels),
            Create(curve_ref),
            *prog_anims,
            run_time=1.8
        )
        self.active_box = None
        self.active_math = None
        self.active_just = None

        # Trazado del segmento restringido y dominio
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
            curve_ref,
            curve_dom, lbl_curve,
            dom_line, dom_dot_left, dom_dot_right, lbl_dom,
            range_line, dot_r_bottom, dot_r_top, lbl_range,
            dot_left, lbl_left,
            dot_right, lbl_right
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
