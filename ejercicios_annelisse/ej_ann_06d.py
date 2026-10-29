r"""
Precálculo Universitario · Tutorías Annelisse / Editorial Amarun
Capítulo: Funciones Reales y Gráficas
Ejercicio 6.d: Rango de Función Radical con Trinomio Cuadrado y Dominio Acotado
               f(x) = √(x² + 10x + 25),  Dom(f) = [-10, -7]

Estructura de la Demostración (100% Precálculo Universitario - Sin Derivadas):
      1. Radicando y trinomio cuadrado perfecto: x² + 10x + 25 = (x + 5)².
      2. Identidad modular y reducción analítica: √(u²) = |u| ⟹ f(x) = |x + 5| = -x - 5 en [-10, -7].
      3. Monotonía decreciente: función afín con pendiente m = -1 < 0 (invierte el orden por desigualdades).
      4. Evaluación en extremo izquierdo cerrado: f(-10) = 5 (máximo absoluto en punto cerrado •).
      5. Evaluación en extremo derecho cerrado: f(-7) = 2 (mínimo absoluto en punto cerrado •).
      6. Deducción formal del rango: -10 ≤ x ≤ -7 ⟹ 2 ≤ -x - 5 ≤ 5 ⟹ Ran(f) = [2, 5] (intervalo compacto).
      7. Tabla de valores notables, vértice exterior en V(-5, 0) y positividad universal.
      8. Trazado cartesiano riguroso: V modular tenue, segmento afín turquesa y proyecciones de Dom y Ran.

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


class EjercicioAnn_06d(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Annelisse",
            exercise="Ejercicio 6.d",
            topic="Rango de Función Radical con Módulo [-10, -7]",
            font_size=17.0
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 6.d: Determine el rango de la función radical en el dominio acotado:",
            math_tex=r"{\color{amteal}f(x) = \sqrt{x^2 + 10x + 25}}, \quad \operatorname{Dom}(f) = [-10, -7]",
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
            "1/8: Trinomio Cuadrado",
            "2/8: Identidad Modular",
            "3/8: Monotonía Decreciente",
            "4/8: Extremo Izquierdo Cerrado",
            "5/8: Extremo Derecho Cerrado",
            "6/8: Deducción Formal del Rango",
            "7/8: Tabla y Positividad",
            "8/8: Trazado Cartesiano y Rango"
        ], dot_spacing=0.82, label_font_size=14.0)

        # ==========================================================
        # PASO 1: Trinomio Cuadrado Perfecto en el Radicando
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Reconocimiento del Trinomio Cuadrado Perfecto:} \\[6pt]"
            r"&\text{Analizando el radicando de } f(x) \text{ en } D = [-10, -7]: \\[4pt]"
            r"&\quad u(x) = x^2 + 10x + 25 \\[6pt]"
            r"&\textbf{Factorización Canónica:} \\[4pt]"
            r"&\quad x^2 + 10x + 25 = x^2 + 2(5)x + 5^2 = \mathbf{{\color{amgold}(x + 5)^2}} \\[6pt]"
            r"&\textbf{Sustitución en el Radical:} \\[4pt]"
            r"&\quad f(x) = \sqrt{{\color{amgold}(x + 5)^2}} \\[6pt]"
            r"&\therefore \quad \text{La expresión bajo la raíz es un cuadrado no negativo } \forall x \in \mathbb{R}."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Trinomio Cuadrado Perfecto:}\\[6pt]"
            r"$\bullet$ El polinomio cuadrático interior tiene discriminante nulo:\\[3pt]"
            r"\hspace*{1.0em}$\Delta = 10^2 - 4(1)(25) = 100 - 100 = 0$.\\[5pt]"
            r"$\bullet$ Se factoriza exactamente como binomio al cuadrado: $(x + 5)^2$.\\[5pt]"
            r"$\bullet$ Dado que $(x+5)^2 \ge 0$, la condición de existencia de la raíz real se cumple universalmente.\\[5pt]"
            r"$\bullet$ El dominio natural es todo $\mathbb{R}$, y está bien definida en $D$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=3.6)

        # ==========================================================
        # PASO 2: Identidad Modular y Reducción Analítica
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Identidad Modular Fundamental y Reducción:} \\[6pt]"
            r"&\text{Por definición formal de la raíz cuadrada principal:} \\[4pt]"
            r"&\quad \sqrt{u^2} = |u| \implies f(x) = \mathbf{{\color{amred}|x + 5|}} \quad (\text{¡No } x + 5\text{!}) \\[6pt]"
            r"&\textbf{Evaluación del Signo del Argumento en } D = [-10, -7]: \\[4pt]"
            r"&\quad -10 \le x \le -7 \iff \mathbf{{\color{amgold}-5 \le x + 5 \le -2 < 0}} \\[6pt]"
            r"&\text{Al ser estrictamente negativo } (u < 0 \implies |u| = -u): \\[4pt]"
            r"&\quad f(x) = -(x + 5) = \mathbf{{\color{amteal}-x - 5}}, \quad \forall x \in [-10, -7] \\[6pt]"
            r"&\therefore \quad \mathbf{f(x) \text{ se reduce a un segmento de recta afín continuo.}}"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Propiedad del Valor Absoluto:}\\[6pt]"
            r"$\bullet$ Recordar la identidad rigurosa $\sqrt{z^2} = |z|$ para todo $z \in \mathbb{R}$.\\[5pt]"
            r"$\bullet$ En el intervalo asignado $D = [-10, -7]$, sumamos $5$:\\[3pt]"
            r"\hspace*{1.0em}$-5 \le x + 5 \le -2 < 0$.\\[5pt]"
            r"$\bullet$ Como el argumento es $100\%$ negativo, el valor absoluto invierte su signo:\\[3pt]"
            r"\hspace*{1.0em}$|x + 5| = -(x + 5) = {\color{amteal}-x - 5}$.\\[5pt]"
            r"$\bullet$ Desmitifica el error común de ignorar el módulo."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=3.6)

        # ==========================================================
        # PASO 3: Monotonía Decreciente por Propiedades de Orden (Precálculo)
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Monotonía Formal por Desigualdades (Precálculo):} \\[6pt]"
            r"&\text{Forma lineal afín reducida: } f(x) = mx + b = \mathbf{{\color{amteal}-x - 5}} \\[6pt]"
            r"&\textbf{Criterio de la Pendiente Afín } (m = -1): \\[4pt]"
            r"&\quad \mathbf{{\color{amgold}m = -1 < 0 \implies \text{Función Estrictamente Decreciente}}} \\[6pt]"
            r"&\textbf{Demostración Directa por Desigualdades:} \\[4pt]"
            r"&\text{Sean } x_1, x_2 \in [-10, -7] \text{ tales que } x_1 < x_2: \\[4pt]"
            r"&\quad \text{Multiplicando por } -1 \ (\text{invierte el orden}): \quad \mathbf{-x_1 > -x_2} \\[4pt]"
            r"&\quad \text{Restando } 5: \quad \mathbf{{\color{amgreen}-x_1 - 5 > -x_2 - 5}} \iff \mathbf{f(x_1) > f(x_2)} \\[6pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}f(x) \text{ es ESTRICTAMENTE DECRECIENTE en } [-10, -7]}} \\[4pt]"
            r"&\implies \text{La función invierte estrictamente el orden de los extremos de } D."
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{3. Monotonía en Precálculo:}\\[6pt]"
            r"$\bullet$ En Precálculo, la monotonía de una función afín $f(x) = mx + b$ se rige por el signo de su pendiente $m$.\\[5pt]"
            r"$\bullet$ Al ser $m = -1 < 0$, la función es estrictamente decreciente.\\[5pt]"
            r"$\bullet$ Demostración directa por propiedades de orden: multiplicar por un número negativo invierte la desigualdad:\\[3pt]"
            r"\hspace*{1.0em}$x_1 < x_2 \implies -x_1 > -x_2 \implies f(x_1) > f(x_2)$.\\[5pt]"
            r"$\bullet$ Sin derivadas: demostración $100\%$ algebraica elemental."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq3, just3, box_color=THEME["statement_box"], advance_to_step=2, wait_time=3.6)

        # ==========================================================
        # PASO 4: Extremo Izquierdo Cerrado (Máximo Absoluto)
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Evaluación en el Extremo Izquierdo Cerrado } (x = -10): \\[6pt]"
            r"&\text{Dado que } -10 \in D \text{ (corchete cerrado } [-10\text{):} \\[4pt]"
            r"&\quad f(-10) = -(-10) - 5 = 10 - 5 = \mathbf{{\color{amgold}5}} \\[6pt]"
            r"&\text{Verificación modular directa:} \\[4pt]"
            r"&\quad f(-10) = |-10 + 5| = |-5| = \mathbf{{\color{amgold}5}} \\[6pt]"
            r"&\textbf{Naturaleza del Extremo:} \\[4pt]"
            r"&\quad \mathbf{{\color{amgreen}M = \max_{x \in D} f(x) = 5}} \quad (\text{Máximo Absoluto Global}) \\[6pt]"
            r"&\therefore \quad \mathbf{\text{Punto de Frontera Cerrado: }} \mathbf{{\color{amgold}P_{\max}(-10, 5)}} \quad (\text{Punto } \bullet)"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Máximo Absoluto Global:}\\[6pt]"
            r"$\bullet$ Evaluamos en la frontera inferior $x = -10$ incluida en $D$.\\[5pt]"
            r"$\bullet$ Obtenemos de forma exacta $f(-10) = 5$.\\[5pt]"
            r"$\bullet$ Al ser $f$ decreciente, ningún punto en $D$ supera la cota $y = 5$.\\[5pt]"
            r"$\bullet$ Como $-10 \in D$, este punto pertenece formalmente a la gráfica ($\bullet$).\\[5pt]"
            r"$\bullet$ Constituye la cota superior estricta y cerrada del rango: $y \le 5$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq4, just4, box_color=THEME["error"], advance_to_step=3, wait_time=3.6)

        # ==========================================================
        # PASO 5: Extremo Derecho Cerrado (Mínimo Absoluto)
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Evaluación en el Extremo Derecho Cerrado } (x = -7): \\[6pt]"
            r"&\text{Dado que } -7 \in D \text{ (corchete cerrado } -7]\text{):} \\[4pt]"
            r"&\quad f(-7) = -(-7) - 5 = 7 - 5 = \mathbf{{\color{amgold}2}} \\[6pt]"
            r"&\text{Verificación modular directa:} \\[4pt]"
            r"&\quad f(-7) = |-7 + 5| = |-2| = \mathbf{{\color{amgold}2}} \\[6pt]"
            r"&\textbf{Naturaleza del Extremo:} \\[4pt]"
            r"&\quad \mathbf{{\color{amgreen}m = \min_{x \in D} f(x) = 2}} \quad (\text{Mínimo Absoluto Global}) \\[6pt]"
            r"&\therefore \quad \mathbf{\text{Punto de Frontera Cerrado: }} \mathbf{{\color{amteal}P_{\min}(-7, 2)}} \quad (\text{Punto } \bullet)"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Mínimo Absoluto Global:}\\[6pt]"
            r"$\bullet$ Evaluamos en la frontera superior $x = -7$ incluida en $D$.\\[5pt]"
            r"$\bullet$ Obtenemos de forma exacta $f(-7) = 2$.\\[5pt]"
            r"$\bullet$ Al ser $f$ decreciente, la curva desciende hasta tocar el valor $2$.\\[5pt]"
            r"$\bullet$ Como $-7 \in D$, el extremo inferior es plenamente alcanzable ($\bullet$).\\[5pt]"
            r"$\bullet$ Constituye la cota inferior estricta y cerrada del rango: $y \ge 2$."
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
            r"&\quad -10 \le x \le -7 \\[6pt]"
            r"&\text{Multiplicando por } -1 \ (\text{invierte el sentido de las desigualdades}): \\[4pt]"
            r"&\quad 7 \le -x \le 10 \\[6pt]"
            r"&\text{Restando } 5 \text{ en todos los términos:} \\[4pt]"
            r"&\quad 7 - 5 \le -x - 5 \le 10 - 5 \iff \mathbf{{\color{amgreen}2 \le f(x) \le 5}} \\[6pt]"
            r"&\therefore \quad \mathbf{\operatorname{Ran}(f) = {\color{amgreen}[2, 5]}} \quad (\text{Intervalo Cerrado Compacto})"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{6. Conclusión Formal del Rango:}\\[6pt]"
            r"$\bullet$ Las inecuaciones confirman analíticamente los límites de la imagen.\\[5pt]"
            r"$\bullet$ Por el Teorema del Valor Intermedio sobre una función continua:\\[5pt]"
            r"$\bullet$ La imagen cubre continuamente todos los valores reales entre $2$ y $5$.\\[5pt]"
            r"$\bullet$ Ambos extremos de frontera son cerrados porque $-10, -7 \in D$.\\[5pt]"
            r"$\bullet$ Rango final: ${\color{amgreen}\operatorname{Ran}(f) = [2, 5]}$."
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
            r"x & \mathbf{-10} & -9 & \mathbf{-8.5} & -8 & \mathbf{-7} \\ \hline "
            r"f(x) & \mathbf{{\color{amgreen}5}} & 4 & \mathbf{3.5} & 3 & \mathbf{{\color{amgreen}2}} \\ \hline "
            r"\text{Rol} & \mathbf{\text{Máx } \bullet} & \text{Punto} & \text{Medio} & \text{Punto} & \mathbf{\text{Mín } \bullet} \\ \hline "
            r"\end{array} \\[8pt]"
            r"&\textbf{Propiedades Analíticas en } D = [-10, -7]: \\[5pt]"
            r"&\bullet \ \text{Vértice de la V modular: } V(-5, 0) \notin D \quad (\text{Exterior a la derecha}) \\[4pt]"
            r"&\bullet \ \text{Cortes con los ejes: Sin corte con } X \ (x=-5 \notin D), \ \text{sin corte con } Y \ (0 \notin D) \\[4pt]"
            r"&\bullet \ \text{Signos: } \mathbf{{\color{amgreen}\forall x \in D: \ f(x) \in [2, 5] > 0}} \quad (\text{Estrictamente Positiva})"
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{7. Síntesis y Propiedades:}\\[6pt]"
            r"$\bullet$ La tabla de valores muestra el descenso aritmético uniforme de paso $-1$.\\[5pt]"
            r"$\bullet$ El vértice del valor absoluto está en $(-5, 0)$, fuera del dominio.\\[5pt]"
            r"$\bullet$ Al estar comprendida entre $2$ y $5$, la función es $100\%$ positiva.\\[5pt]"
            r"$\bullet$ La curva se sitúa en el segundo cuadrante ($x < 0, y > 0$).\\[5pt]"
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
            r"$\bullet$ \textbf{Rama de Valor Absoluto:}\\[2pt]"
            r"\hspace*{0.8em}$f(x) = |x + 5| = -x - 5$ en $[-10, -7]$.\\[6pt]"
            r"$\bullet$ \textbf{Máximo Cerrado:}\\[2pt]"
            r"\hspace*{0.8em}$P_{\max}(-10, 5)$ \textbf{Punto Cerrado} ($\bullet$).\\[6pt]"
            r"$\bullet$ \textbf{Mínimo Cerrado:}\\[2pt]"
            r"\hspace*{0.8em}$P_{\min}(-7, 2)$ \textbf{Punto Cerrado} ($\bullet$).\\[6pt]"
            r"$\bullet$ \textbf{Vértice Modular:}\\[2pt]"
            r"\hspace*{0.8em}$V(-5, 0) \notin D$ exterior a la derecha.\\[6pt]"
            r"$\bullet$ \textbf{Rango Proyectado:}\\[2pt]"
            r"\hspace*{0.8em}$[2, 5]$ sobre el eje vertical $Y$."
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
            x_range=[-11.0, -4.0, 1],
            y_range=[0.0, 6.0, 1],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=13,
            labels_font_size=19
        )

        def f_val(x):
            return abs(x + 5.0)

        # V modular completa referencial tenue
        curve_ref = axes.plot(
            f_val,
            x_range=[-10.8, -4.2],
            color=THEME["statement_box"],
            stroke_width=1.5,
            stroke_opacity=0.35
        )

        # Segmento restringido en [-10.0, -7.0]
        curve_dom = axes.plot(
            f_val,
            x_range=[-10.0, -7.0],
            color=THEME["amarun_teal"],
            stroke_width=4.0
        )
        lbl_curve = MathTex(
            r"f(x) = -x - 5",
            font_size=13.5,
            color=THEME["amarun_teal"]
        ).next_to(axes.c2p(-8.5, 3.5), UR, buff=0.10)

        # Vértice de la V modular exterior V(-5, 0)
        p_v = axes.c2p(-5.0, 0.0)
        dot_v = Dot(p_v, radius=0.06, color=THEME["axes"])
        lbl_v = MathTex(
            r"V(-5, 0)",
            font_size=11.5,
            color=THEME["axes"]
        ).next_to(p_v, UP, buff=0.08)

        # Extremo izquierdo cerrado P_max(-10, 5)
        p_left = axes.c2p(-10.0, 5.0)
        dot_left = Dot(p_left, radius=0.08, color=THEME["success"])
        lbl_left = MathTex(
            r"P_{\max}(-10, 5)",
            font_size=12.0,
            color=THEME["success"]
        ).next_to(p_left, UP, buff=0.08)

        # Extremo derecho cerrado P_min(-7, 2)
        p_right = axes.c2p(-7.0, 2.0)
        dot_right = Dot(p_right, radius=0.08, color=THEME["success"])
        lbl_right = MathTex(
            r"P_{\min}(-7, 2)",
            font_size=12.0,
            color=THEME["success"]
        ).next_to(p_right, UR, buff=0.08)

        # Proyección del dominio en la base: [-10, -7]
        dom_line = Line(
            axes.c2p(-10.0, 0.15),
            axes.c2p(-7.0, 0.15),
            color=THEME["highlight"],
            stroke_width=4.0
        )
        dom_dot_left = Dot(axes.c2p(-10.0, 0.15), radius=0.055, color=THEME["highlight"])
        dom_dot_right = Dot(axes.c2p(-7.0, 0.15), radius=0.055, color=THEME["highlight"])
        lbl_dom = MathTex(
            r"\operatorname{Dom}=[-10, -7]",
            font_size=11.5,
            color=THEME["highlight"]
        ).next_to(axes.c2p(-8.5, 0.15), DOWN, buff=0.10)

        # Proyección del rango sobre el borde izquierdo: [2, 5]
        range_line = Line(
            axes.c2p(-11.0, 2.0),
            axes.c2p(-11.0, 5.0),
            color=THEME["success"],
            stroke_width=5.0
        )
        dot_r_bottom = Dot(axes.c2p(-11.0, 2.0), radius=0.065, color=THEME["success"])
        dot_r_top = Dot(axes.c2p(-11.0, 5.0), radius=0.065, color=THEME["success"])
        lbl_range = MathTex(
            r"\operatorname{Ran}=[2, 5]",
            font_size=12.0,
            color=THEME["success"]
        ).next_to(axes.c2p(-11.0, 3.5), RIGHT, buff=0.10)

        # Transición hacia el paso 8
        self.play(
            FadeOut(self.active_box),
            FadeOut(self.active_math, shift=DOWN * 0.2),
            FadeOut(self.active_just, shift=DOWN * 0.2),
            FadeIn(info_grp, shift=DOWN * 0.2),
            Create(axes),
            Write(axes_labels),
            Create(curve_ref),
            FadeIn(dot_v), Write(lbl_v),
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
            curve_ref, dot_v, lbl_v,
            curve_dom, lbl_curve,
            dom_line, dom_dot_left, dom_dot_right, lbl_dom,
            range_line, dot_r_bottom, dot_r_top, lbl_range,
            dot_left, lbl_left,
            dot_right, lbl_right
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
