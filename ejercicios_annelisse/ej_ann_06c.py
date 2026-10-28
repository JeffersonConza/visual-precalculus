r"""
Precálculo Universitario · Tutorías Annelisse / Editorial Amarun
Capítulo: Funciones Reales y Gráficas
Ejercicio 6.c: Rango de Valor Absoluto Anidado con Dominio Acotado
               f(x) = ||x + 1| + 2|,  Dom(f) = [-7, -3]

Estructura de la Demostración (8 Pasos):
      1. Estructura de valor absoluto anidado y análisis del argumento interior: x + 1 en [-7, -3].
      2. Desanidamiento y reducción analítica: x + 1 < 0 ⟹ |x + 1| = -x - 1, |-x + 1| = -x + 1.
      3. Monotonía decreciente: pendiente afín m = -1 < 0 ⟹ x₁ < x₂ ⟹ f(x₁) > f(x₂) (invierte el orden).
      4. Evaluación en extremo izquierdo cerrado: f(-7) = 8 (máximo absoluto en punto cerrado •).
      5. Evaluación en extremo derecho cerrado: f(-3) = 4 (mínimo absoluto en punto cerrado •).
      6. Deducción formal del rango: -7 ≤ x ≤ -3 ⟹ 4 ≤ -x + 1 ≤ 8 ⟹ Ran(f) = [4, 8] (intervalo compacto).
      7. Tabla de valores notables, vértice exterior en V(-1, 2) y positividad universal.
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


class EjercicioAnn_06c(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Annelisse",
            exercise="Ejercicio 6.c",
            topic="Rango de Valor Absoluto Anidado [-7, -3]",
            font_size=17.0
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 6.c: Determine el rango de la función con valor absoluto en el dominio acotado:",
            math_tex=r"{\color{amteal}f(x) = \big||x + 1| + 2\big|}, \quad \operatorname{Dom}(f) = [-7, -3]",
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
            "1/8: Valor Absoluto Anidado",
            "2/8: Desanidamiento y Reducción",
            "3/8: Monotonía Decreciente",
            "4/8: Extremo Izquierdo Cerrado",
            "5/8: Extremo Derecho Cerrado",
            "6/8: Deducción Formal del Rango",
            "7/8: Tabla y Positividad",
            "8/8: Trazado Cartesiano y Rango"
        ], dot_spacing=0.82, label_font_size=14.0)

        # ==========================================================
        # PASO 1: Estructura de Valor Absoluto Anidado
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Estructura de Valor Absoluto Anidado y Dominio:} \\[6pt]"
            r"&\text{Se tiene la función compuesta con doble módulo:} \\[4pt]"
            r"&\quad f(x) = \big|{\color{amgold}|x + 1|} + 2\big|, \quad \text{definida en } D = [-7, -3] \\[6pt]"
            r"&\textbf{Análisis del Argumento Interior } u(x) = x + 1: \\[4pt]"
            r"&\quad x \in [-7, -3] \iff -7 \le x \le -3 \\[5pt]"
            r"&\quad \implies -7 + 1 \le x + 1 \le -3 + 1 \\[5pt]"
            r"&\quad \iff \mathbf{{\color{amred}-6 \le x + 1 \le -2 < 0}} \\[6pt]"
            r"&\therefore \quad \text{El argumento interior es estrictamente negativo en todo } D."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Módulo Interior en el Dominio:}\\[6pt]"
            r"$\bullet$ La función posee un valor absoluto anidado dentro de otro:\\[3pt]"
            r"\hspace*{1.0em}$f(x) = \big||x + 1| + 2\big|$.\\[5pt]"
            r"$\bullet$ Evaluamos el comportamiento de $x + 1$ en el dominio compacto $[-7, -3]$:\\[3pt]"
            r"\hspace*{1.0em}$-6 \le x + 1 \le -2 < 0$.\\[5pt]"
            r"$\bullet$ Como el argumento es estrictamente menor que cero en todo $D$, no cambia de signo en el intervalo.\\[5pt]"
            r"$\bullet$ No hay necesidad de partir el dominio en subintervalos."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=3.6)

        # ==========================================================
        # PASO 2: Desanidamiento y Reducción Lineal
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Desanidamiento y Reducción Analítica:} \\[6pt]"
            r"&\text{Por definición formal de valor absoluto } (u < 0 \implies |u| = -u): \\[4pt]"
            r"&\quad {\color{amgold}|x + 1|} = -(x + 1) = \mathbf{{\color{amgold}-x - 1}}, \quad \forall x \in [-7, -3] \\[6pt]"
            r"&\textbf{Sustitución en el Módulo Exterior:} \\[4pt]"
            r"&\quad f(x) = \big|({\color{amgold}-x - 1}) + 2\big| = \mathbf{{\color{amteal}|-x + 1|}} \\[6pt]"
            r"&\textbf{Signo del Argumento Exterior } v(x) = -x + 1: \\[4pt]"
            r"&\quad -7 \le x \le -3 \iff 3 \le -x \le 7 \iff \mathbf{{\color{amgreen}4 \le -x + 1 \le 8 > 0}} \\[6pt]"
            r"&\therefore \quad |-x + 1| = \mathbf{{\color{amteal}-x + 1}} \implies \mathbf{f(x) = -x + 1} \quad (\text{Función Afín})"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Desanidamiento Sucesivo:}\\[6pt]"
            r"$\bullet$ Al ser $x + 1 < 0$, su valor absoluto es $-(x+1) = -x - 1$.\\[5pt]"
            r"$\bullet$ Sumamos $2$ al interior del módulo externo:\\[3pt]"
            r"\hspace*{1.0em}$(-x - 1) + 2 = -x + 1$.\\[5pt]"
            r"$\bullet$ Verificamos el signo de $-x + 1$ en $[-7, -3]$:\\[3pt]"
            r"\hspace*{1.0em}$-x \in [3, 7] \implies -x + 1 \in [4, 8] > 0$.\\[5pt]"
            r"$\bullet$ Al ser $100\%$ positivo, el módulo externo se elimina directamente: $f(x) = {\color{amteal}-x + 1}$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=3.6)

        # ==========================================================
        # PASO 3: Monotonía Decreciente por Inecuaciones
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Monotonía Estricta por Pendiente e Inecuaciones:} \\[6pt]"
            r"&\text{Para la función afín } f(x) = -x + 1 \text{ en } D = [-7, -3]: \\[4pt]"
            r"&\quad \text{Pendiente afín constante: } \mathbf{{\color{amred}m = -1 < 0}} \\[6pt]"
            r"&\textbf{Demostración por Definición de Monotonía:} \\[4pt]"
            r"&\quad \text{Sean } x_1, x_2 \in D \text{ tales que } x_1 < x_2: \\[4pt]"
            r"&\quad x_1 < x_2 \iff -x_1 > -x_2 \iff \mathbf{{\color{amred}-x_1 + 1 > -x_2 + 1}} \\[6pt]"
            r"&\implies \mathbf{f(x_1) > f(x_2)} \quad (\mathbf{{\color{amred}\text{ESTRICTAMENTE DECRECIENTE}}}) \\[6pt]"
            r"&\therefore \quad \text{La función invierte estrictamente el orden de los extremos de } D."
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{3. Monotonía en Precálculo:}\\[6pt]"
            r"$\bullet$ Se demuestra directamente por la definición algebraica formal:\\[3pt]"
            r"\hspace*{1.0em}$x_1 < x_2 \implies -x_1 > -x_2$.\\[3pt]"
            r"\hspace*{1.0em}$-x_1 + 1 > -x_2 + 1 \implies f(x_1) > f(x_2)$.\\[5pt]"
            r"$\bullet$ Su pendiente constante es negativa: $m = -1 < 0$.\\[5pt]"
            r"$\bullet$ Al ser estrictamente decreciente:\\[3pt]"
            r"\hspace*{1.0em}El valor máximo ocurre al inicio ($x = -7$).\\[3pt]"
            r"\hspace*{1.0em}El valor mínimo ocurre al final ($x = -3$).\\[5pt]"
            r"$\bullet$ Sin cálculo diferencial: $100\%$ álgebra de desigualdades."
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
            r"&\textbf{4. Evaluación en el Extremo Izquierdo Cerrado } (x = -7): \\[6pt]"
            r"&\text{Dado que } -7 \in D \text{ (corchete cerrado } [-7\text{):} \\[4pt]"
            r"&\quad f(-7) = -(-7) + 1 = 7 + 1 = \mathbf{{\color{amgold}8}} \\[6pt]"
            r"&\text{Verificación en la fórmula original con doble valor absoluto:} \\[4pt]"
            r"&\quad f(-7) = \big||-7 + 1| + 2\big| = \big||-6| + 2\big| = |6 + 2| = \mathbf{{\color{amgold}8}} \\[6pt]"
            r"&\textbf{Naturaleza del Extremo:} \\[4pt]"
            r"&\quad \mathbf{{\color{amgreen}M = \max_{x \in D} f(x) = 8}} \quad (\text{Máximo Absoluto Global}) \\[6pt]"
            r"&\therefore \quad \mathbf{\text{Punto de Frontera Cerrado: }} \mathbf{{\color{amgold}P_{\max}(-7, 8)}} \quad (\text{Punto } \bullet)"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Máximo Absoluto Global:}\\[6pt]"
            r"$\bullet$ Evaluamos en la frontera inferior $x = -7$, incluida en el dominio $D$.\\[5pt]"
            r"$\bullet$ Obtenemos de forma exacta $f(-7) = 8$.\\[5pt]"
            r"$\bullet$ Al ser $f$ decreciente, ningún punto en $D$ supera el valor $y = 8$.\\[5pt]"
            r"$\bullet$ Como $-7 \in D$, este punto pertenece formalmente a la gráfica ($\bullet$).\\[5pt]"
            r"$\bullet$ Constituye la cota superior estricta y cerrada del rango: $y \le 8$."
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
            r"&\textbf{5. Evaluación en el Extremo Derecho Cerrado } (x = -3): \\[6pt]"
            r"&\text{Dado que } -3 \in D \text{ (corchete cerrado } -3]\text{):} \\[4pt]"
            r"&\quad f(-3) = -(-3) + 1 = 3 + 1 = \mathbf{{\color{amgold}4}} \\[6pt]"
            r"&\text{Verificación en la fórmula original con doble valor absoluto:} \\[4pt]"
            r"&\quad f(-3) = \big||-3 + 1| + 2\big| = \big||-2| + 2\big| = |2 + 2| = \mathbf{{\color{amgold}4}} \\[6pt]"
            r"&\textbf{Naturaleza del Extremo:} \\[4pt]"
            r"&\quad \mathbf{{\color{amgreen}m = \min_{x \in D} f(x) = 4}} \quad (\text{Mínimo Absoluto Global}) \\[6pt]"
            r"&\therefore \quad \mathbf{\text{Punto de Frontera Cerrado: }} \mathbf{{\color{amteal}P_{\min}(-3, 4)}} \quad (\text{Punto } \bullet)"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Mínimo Absoluto Global:}\\[6pt]"
            r"$\bullet$ Evaluamos en la frontera superior $x = -3$, incluida en el dominio $D$.\\[5pt]"
            r"$\bullet$ Obtenemos de forma exacta $f(-3) = 4$.\\[5pt]"
            r"$\bullet$ Al ser $f$ decreciente, la función desciende continuamente hasta tocar $4$.\\[5pt]"
            r"$\bullet$ Como $-3 \in D$, el valor inferior es plenamente alcanzable ($\bullet$).\\[5pt]"
            r"$\bullet$ Constituye la cota inferior estricta y cerrada del rango: $y \ge 4$."
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
            r"&\quad -7 \le x \le -3 \\[6pt]"
            r"&\text{Multiplicando por } -1 \ (\text{se invierten las desigualdades}): \\[4pt]"
            r"&\quad 3 \le -x \le 7 \\[6pt]"
            r"&\text{Sumando } 1 \text{ en todos los términos:} \\[4pt]"
            r"&\quad 3 + 1 \le -x + 1 \le 7 + 1 \iff \mathbf{{\color{amgreen}4 \le f(x) \le 8}} \\[6pt]"
            r"&\therefore \quad \mathbf{\operatorname{Ran}(f) = {\color{amgreen}[4, 8]}} \quad (\text{Intervalo Cerrado Compacto})"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{6. Conclusión Formal del Rango:}\\[6pt]"
            r"$\bullet$ El álgebra de inecuaciones demuestra analíticamente las cotas exactas de la imagen.\\[5pt]"
            r"$\bullet$ Por el Teorema del Valor Intermedio sobre una función afín continua:\\[5pt]"
            r"$\bullet$ La imagen cubre sin huecos todos los valores reales entre $4$ y $8$.\\[5pt]"
            r"$\bullet$ Ambos extremos de frontera son cerrados porque $-7, -3 \in D$.\\[5pt]"
            r"$\bullet$ Rango final: ${\color{amgreen}\operatorname{Ran}(f) = [4, 8]}$."
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
            r"x & \mathbf{-7} & -6 & \mathbf{-5} & -4 & \mathbf{-3} \\ \hline "
            r"f(x) & \mathbf{{\color{amgreen}8}} & 7 & \mathbf{6} & 5 & \mathbf{{\color{amgreen}4}} \\ \hline "
            r"\text{Rol} & \mathbf{\text{Máx } \bullet} & \text{Punto} & \text{Medio} & \text{Punto} & \mathbf{\text{Mín } \bullet} \\ \hline "
            r"\end{array} \\[8pt]"
            r"&\textbf{Propiedades Analíticas en } D = [-7, -3]: \\[5pt]"
            r"&\bullet \ \text{Vértice global modular: } V(-1, 2) \notin D \quad (\text{Exterior a la derecha}) \\[4pt]"
            r"&\bullet \ \text{Cortes con los ejes: Sin corte con } X \ (f(x) \ge 2 > 0), \ \text{sin corte con } Y \ (0 \notin D) \\[4pt]"
            r"&\bullet \ \text{Signos: } \mathbf{{\color{amgreen}\forall x \in D: \ f(x) \in [4, 8] > 0}} \quad (\text{Estrictamente Positiva})"
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{7. Síntesis y Propiedades:}\\[6pt]"
            r"$\bullet$ La tabla de valores muestra un descenso aritmético lineal exacto con paso $-1$.\\[5pt]"
            r"$\bullet$ El vértice del valor absoluto se ubica en $(-1, 2)$, fuera del dominio.\\[5pt]"
            r"$\bullet$ Al estar comprendida entre $4$ y $8$, la función es estrictamente positiva en todo $D$.\\[5pt]"
            r"$\bullet$ La gráfica pertenece íntegramente al segundo cuadrante ($x < 0, y > 0$).\\[5pt]"
            r"$\bullet$ Datos analíticos completos para la representación cartesiana."
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
            r"$\bullet$ \textbf{Función de Valor Absoluto:}\\[2pt]"
            r"\hspace*{0.8em}$f(x) = \big||x+1|+2\big| = -x+1$ en $[-7, -3]$.\\[6pt]"
            r"$\bullet$ \textbf{Máximo Cerrado:}\\[2pt]"
            r"\hspace*{0.8em}$P_{\max}(-7, 8)$ \textbf{Punto Cerrado} ($\bullet$).\\[6pt]"
            r"$\bullet$ \textbf{Mínimo Cerrado:}\\[2pt]"
            r"\hspace*{0.8em}$P_{\min}(-3, 4)$ \textbf{Punto Cerrado} ($\bullet$).\\[6pt]"
            r"$\bullet$ \textbf{Vértice Modular:}\\[2pt]"
            r"\hspace*{0.8em}$V(-1, 2) \notin D$ exterior a la derecha.\\[6pt]"
            r"$\bullet$ \textbf{Rango Proyectado:}\\[2pt]"
            r"\hspace*{0.8em}$[4, 8]$ sobre el eje vertical $Y$."
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
            x_range=[-8.5, 0.5, 1],
            y_range=[0.0, 9.5, 2],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=12,
            labels_font_size=19
        )

        def f_val(x):
            return abs(abs(x + 1.0) + 2.0)

        # Curva modular completa referencial tenue (muestra la V y el vértice)
        curve_ref = axes.plot(
            f_val,
            x_range=[-8.0, 0.2],
            color=THEME["statement_box"],
            stroke_width=1.5,
            stroke_opacity=0.35
        )

        # Segmento afín restringido en [-7.0, -3.0]
        curve_dom = axes.plot(
            f_val,
            x_range=[-7.0, -3.0],
            color=THEME["amarun_teal"],
            stroke_width=4.0
        )
        lbl_curve = MathTex(
            r"f(x) = -x + 1",
            font_size=13.5,
            color=THEME["amarun_teal"]
        ).next_to(axes.c2p(-5.0, 6.0), UR, buff=0.10)

        # Vértice de la V modular exterior V(-1, 2)
        p_v = axes.c2p(-1.0, 2.0)
        dot_v = Dot(p_v, radius=0.06, color=THEME["axes"])
        lbl_v = MathTex(
            r"V(-1, 2)",
            font_size=11.5,
            color=THEME["axes"]
        ).next_to(p_v, DOWN, buff=0.08)

        # Extremo izquierdo cerrado P_max(-7, 8)
        p_left = axes.c2p(-7.0, 8.0)
        dot_left = Dot(p_left, radius=0.08, color=THEME["success"])
        lbl_left = MathTex(
            r"P_{\max}(-7, 8)",
            font_size=12.0,
            color=THEME["success"]
        ).next_to(p_left, UR, buff=0.08)

        # Extremo derecho cerrado P_min(-3, 4)
        p_right = axes.c2p(-3.0, 4.0)
        dot_right = Dot(p_right, radius=0.08, color=THEME["success"])
        lbl_right = MathTex(
            r"P_{\min}(-3, 4)",
            font_size=12.0,
            color=THEME["success"]
        ).next_to(p_right, UR, buff=0.08)

        # Proyección del dominio en la base: [-7, -3]
        dom_line = Line(
            axes.c2p(-7.0, 0.25),
            axes.c2p(-3.0, 0.25),
            color=THEME["highlight"],
            stroke_width=4.0
        )
        dom_dot_left = Dot(axes.c2p(-7.0, 0.25), radius=0.055, color=THEME["highlight"])
        dom_dot_right = Dot(axes.c2p(-3.0, 0.25), radius=0.055, color=THEME["highlight"])
        lbl_dom = MathTex(
            r"\operatorname{Dom}=[-7, -3]",
            font_size=11.5,
            color=THEME["highlight"]
        ).next_to(axes.c2p(-5.0, 0.25), UP, buff=0.08)

        # Proyección del rango sobre el borde izquierdo: [4, 8]
        range_line = Line(
            axes.c2p(-8.5, 4.0),
            axes.c2p(-8.5, 8.0),
            color=THEME["success"],
            stroke_width=5.0
        )
        dot_r_bottom = Dot(axes.c2p(-8.5, 4.0), radius=0.065, color=THEME["success"])
        dot_r_top = Dot(axes.c2p(-8.5, 8.0), radius=0.065, color=THEME["success"])
        lbl_range = MathTex(
            r"\operatorname{Ran}=[4, 8]",
            font_size=12.0,
            color=THEME["success"]
        ).next_to(axes.c2p(-8.5, 6.0), RIGHT, buff=0.10)

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
