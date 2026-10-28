r"""
Precálculo Universitario · Tutorías Annelisse / Editorial Amarun
Capítulo: Funciones Reales y Gráficas
Ejercicio 3.b: Rango de Función Cuadrática con Dominio Restringido
               f(x) = -(2/3)x² + (7/6)x + 5/8,  Dom(f) = [1/2, 3/2[

Estructura de la Demostración (8 Pasos):
      1. Coeficientes y concavidad: a = -2/3 < 0 (parábola cóncava hacia abajo ∩).
      2. Localización analítica del vértice: xv = 7/8 ∈ [1/2, 3/2[ (vértice interior en D).
      3. Ordenada del vértice: y_max = f(7/8) = 109/96 (máximo absoluto de la función en D).
      4. Evaluación en los extremos: f(1/2) = 25/24 (cerrado) y f(3/2) = 7/8 (abierto, ínfimo).
      5. Monotonía bipartita: creciente en [1/2, 7/8] y decreciente en [7/8, 3/2[.
      6. Deducción formal del rango: Ran(f) = ]7/8, 109/96].
      7. Tabla de valores simétricos y síntesis institucional de propiedades.
      8. Trazado cartesiano riguroso: arco de curva, vértice interior, extremos cerrado/abierto y rango.

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


class EjercicioAnn_03b(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Annelisse",
            exercise="Ejercicio 3.b",
            topic="Rango con Vértice Interior en [1/2, 3/2[",
            font_size=17.0
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 3.b: Determine el rango de la función cuadrática en el dominio acotado:",
            math_tex=r"{\color{amteal}f(x) = -\frac{2}{3}x^2 + \frac{7}{6}x + \frac{5}{8}}, \quad \operatorname{Dom}(f) = \left[\frac{1}{2}, \frac{3}{2}\right[",
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
            "1/8: Coeficientes y Concavidad",
            "2/8: Vértice Interior xv",
            "3/8: Máximo Absoluto yv",
            "4/8: Evaluación en Extremos",
            "5/8: Monotonía Bipartita",
            "6/8: Deducción del Rango",
            "7/8: Tabla y Síntesis",
            "8/8: Trazado Cartesiano y Rango"
        ], dot_spacing=0.82, label_font_size=14.0)

        # ==========================================================
        # PASO 1: Coeficientes y Concavidad
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Coeficientes y Concavidad Polinómica:} \\[6pt]"
            r"&\text{Dada la función cuadrática en el dominio } D = \left[\frac{1}{2}, \frac{3}{2}\right]: \\[4pt]"
            r"&\quad f(x) = {\color{amred}-\frac{2}{3}}x^2 + {\color{amteal}\frac{7}{6}}x + {\color{amgold}\frac{5}{8}} \\[6pt]"
            r"&\textbf{Identificación de Coeficientes:} \\[4pt]"
            r"&\quad {\color{amred}a = -\frac{2}{3}}, \quad {\color{amteal}b = \frac{7}{6}}, \quad {\color{amgold}c = \frac{5}{8}} \\[6pt]"
            r"&\text{Como } {\color{amred}a = -\frac{2}{3} < 0} \implies \text{Parábola cóncava hacia abajo } (\cap). \\[4pt]"
            r"&\implies \text{Si el vértice pertenece a } D, \text{ determinará el Máximo Absoluto}."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Coeficientes y Concavidad:}\\[6pt]"
            r"$\bullet$ Función cuadrática restringida al intervalo semiabierto $D = [1/2, 3/2[$.\\[5pt]"
            r"$\bullet$ Coeficiente cuadrático: ${\color{amred}a = -2/3 < 0}$.\\[5pt]"
            r"$\bullet$ Concavidad negativa ($\cap$): la curva alcanza su cúspide en el vértice.\\[5pt]"
            r"$\bullet$ Primer paso fundamental: calcular la abscisa del vértice y verificar si cae dentro de $D$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=3.6)

        # ==========================================================
        # PASO 2: Vértice Interior xv
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Localización de la Abscisa del Vértice } x_v: \\[6pt]"
            r"&\text{Aplicando la fórmula de abscisa extremal:} \\[4pt]"
            r"&\quad x_v = -\frac{b}{2a} = -\frac{7/6}{2(-2/3)} = \frac{7/6}{4/3} = \frac{7}{6} \cdot \frac{3}{4} = \mathbf{{\color{amgold}\frac{7}{8}}} = \mathbf{0.875} \\[6pt]"
            r"&\textbf{Comparación de pertenencia con } D = \left[\frac{1}{2}, \frac{3}{2}\right[: \\[4pt]"
            r"&\quad \frac{1}{2} = \frac{4}{8} = 0.5 < \mathbf{{\color{amgold}x_v = \frac{7}{8}}} = 0.875 < \frac{3}{2} = \frac{12}{8} = 1.5 \\[6pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}x_v = \frac{7}{8} \in \left[\frac{1}{2}, \frac{3}{2}\right[}} \quad (\textbf{Vértice Interior en } D)"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Vértice Interior en D:}\\[6pt]"
            r"$\bullet$ La abscisa del eje axial es $x_v = 7/8 = 0.875$.\\[5pt]"
            r"$\bullet$ Dominio evaluado: desde $0.5$ hasta $1.5$.\\[5pt]"
            r"$\bullet$ Al cumplirse $0.5 < 0.875 < 1.5$, el vértice se encuentra en el interior de $D$.\\[5pt]"
            r"$\bullet$ Consecuencia: el máximo absoluto del rango coincide con la ordenada del vértice."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=3.6)

        # ==========================================================
        # PASO 3: Máximo Absoluto yv
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Cálculo del Máximo Absoluto Global } y_v: \\[6pt]"
            r"&\text{Evaluando la función en } x_v = \frac{7}{8}: \\[4pt]"
            r"&\quad y_v = f\left(\frac{7}{8}\right) = -\frac{2}{3}\left(\frac{7}{8}\right)^2 + \frac{7}{6}\left(\frac{7}{8}\right) + \frac{5}{8} \\[5pt]"
            r"&\quad = -\frac{2}{3}\left(\frac{49}{64}\right) + \frac{49}{48} + \frac{5}{8} = -\frac{49}{96} + \frac{98}{96} + \frac{60}{96} \\[6pt]"
            r"&\quad = \frac{-49 + 98 + 60}{96} = \mathbf{{\color{amgreen}\frac{109}{96}}} \approx \mathbf{1.1354} \\[6pt]"
            r"&\therefore \quad \mathbf{\text{Cota Superior Máxima: }} \mathbf{{\color{amgreen}y_{\max} = \frac{109}{96}}} \quad (\text{Alcanzada en } \bullet)"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{3. Máximo Absoluto:}\\[6pt]"
            r"$\bullet$ La cúspide de la parábola se ubica en $y_v = 109/96 \approx 1.135$.\\[5pt]"
            r"$\bullet$ Como $x_v \in D$, este punto pertenece efectivamente a la gráfica.\\[5pt]"
            r"$\bullet$ Constituye la cota superior del rango en un extremo cerrado ($\bullet$).\\[5pt]"
            r"$\bullet$ El extremo inferior dependerá del menor valor alcanzado en los bordes."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq3, just3, box_color=THEME["statement_box"], advance_to_step=2, wait_time=3.6)

        # ==========================================================
        # PASO 4: Evaluación en los Extremos del Dominio
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Evaluación en los Extremos de Frontera:} \\[6pt]"
            r"&\bullet \ \textbf{Extremo Izquierdo Cerrado } (x = 1/2): \\[3pt]"
            r"&\quad f\left(\frac{1}{2}\right) = -\frac{2}{3}\left(\frac{1}{4}\right) + \frac{7}{6}\left(\frac{1}{2}\right) + \frac{5}{8} = -\frac{1}{6} + \frac{7}{12} + \frac{5}{8} \\[4pt]"
            r"&\quad = \frac{-4 + 14 + 15}{24} = \mathbf{{\color{amteal}\frac{25}{24}}} = \frac{100}{96} \approx \mathbf{1.0417} \\[6pt]"
            r"&\bullet \ \textbf{Extremo Derecho Abierto } (x \to 3/2^-): \\[3pt]"
            r"&\quad f\left(\frac{3}{2}\right) = -\frac{2}{3}\left(\frac{9}{4}\right) + \frac{7}{6}\left(\frac{3}{2}\right) + \frac{5}{8} = -\frac{3}{2} + \frac{7}{4} + \frac{5}{8} \\[4pt]"
            r"&\quad = \frac{-12 + 14 + 5}{8} = \mathbf{{\color{amred}\frac{7}{8}}} = \frac{84}{96} = \mathbf{0.875} \quad (\text{Ínfimo en } \circ)"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Valores de Frontera:}\\[6pt]"
            r"$\bullet$ En $x = 1/2$: $f(1/2) = 25/24 = 100/96 \approx 1.042$.\\[5pt]"
            r"$\bullet$ En $x = 3/2$: $f(3/2) = 7/8 = 84/96 = 0.875$.\\[5pt]"
            r"$\bullet$ Como $3/2$ está más distante del vértice ($|3/2 - 7/8| = 5/8$) que $1/2$ ($|1/2 - 7/8| = 3/8$), desciende más.\\[5pt]"
            r"$\bullet$ El ínfimo no alcanzable es $y = 7/8$ (abierto)."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq4, just4, box_color=THEME["curve"], advance_to_step=3, wait_time=3.6)

        # ==========================================================
        # PASO 5: Monotonía Bipartita en D
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Análisis de Monotonía Bipartita en } D: \\[6pt]"
            r"&\text{Al estar el vértice } x_v = \frac{7}{8} \text{ en el interior de } D = \left[\frac{1}{2}, \frac{3}{2}\right[: \\[4pt]"
            r"&\bullet \ \text{En } \left[\frac{1}{2}, \frac{7}{8}\right]: \ f \text{ es } \mathbf{{\color{amgreen}\text{Estrictamente Creciente}}} \\[4pt]"
            r"&\quad \text{Asciende desde } f(1/2) = \frac{25}{24} \text{ hasta el vértice } f(7/8) = \frac{109}{96}. \\[6pt]"
            r"&\bullet \ \text{En } \left[\frac{7}{8}, \frac{3}{2}\right[: \ f \text{ es } \mathbf{{\color{amteal}\text{Estrictamente Decreciente}}} \\[4pt]"
            r"&\quad \text{Desciende desde } \frac{109}{96} \text{ hacia el extremo abierto } f(3/2) = \frac{7}{8}. \\[6pt]"
            r"&\therefore \quad \mathbf{\text{Cota Inferior Estricta: }} \mathbf{{\color{amred}y_{\min} = \frac{7}{8}}} \quad (\text{Valor ínfimo abierto})"
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Monotonía Bipartita:}\\[6pt]"
            r"$\bullet$ La presencia del vértice divide el comportamiento en dos fases:\\[5pt]"
            r"\hspace*{0.8em}1. Subida: de $x = 0.5$ a $x = 0.875$.\\[3pt]"
            r"\hspace*{0.8em}2. Bajada: de $x = 0.875$ a $x = 1.5$.\\[5pt]"
            r"$\bullet$ En el extremo derecho la curva baja hasta $7/8 = 0.875$.\\[5pt]"
            r"$\bullet$ Toda la función es estrictamente positiva: $f(x) > 0$ en $D$."
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
            r"&\textbf{6. Deducción Formal del Rango:} \\[6pt]"
            r"&\text{Combinando la imagen de las dos ramas monótonas:} \\[4pt]"
            r"&\quad \operatorname{Im}_1 = f\left(\left[\frac{1}{2}, \frac{7}{8}\right]\right) = \left[\frac{25}{24}, \frac{109}{96}\right] \\[5pt]"
            r"&\quad \operatorname{Im}_2 = f\left(\left[\frac{7}{8}, \frac{3}{2}\right[\right) = \left]\frac{7}{8}, \frac{109}{96}\right] \\[6pt]"
            r"&\text{La imagen total es la unión de ambos intervalos:} \\[4pt]"
            r"&\quad \operatorname{Ran}(f) = \operatorname{Im}_1 \cup \operatorname{Im}_2 = \left]\frac{7}{8}, \frac{109}{96}\right] \\[6pt]"
            r"&\therefore \quad \mathbf{\operatorname{Ran}(f) = {\color{amgreen}\left]\frac{7}{8}, \frac{109}{96}\right]}} \approx \mathbf{{\color{amgreen}\left]0.875, 1.1354\right]}}"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{6. Conclusión Formal del Rango:}\\[6pt]"
            r"$\bullet$ La imagen cubre continuamente desde el ínfimo $7/8$ hasta el máximo $109/96$.\\[5pt]"
            r"$\bullet$ Extremo inferior abierto en $7/8$ porque $x = 3/2 \notin D$.\\[5pt]"
            r"$\bullet$ Extremo superior cerrado en $109/96$ alcanzado en el vértice $x_v = 7/8 \in D$.\\[5pt]"
            r"$\bullet$ Rango final unívoco: ${\color{amgreen}\operatorname{Ran}(f) = \left]\frac{7}{8}, \frac{109}{96}\right]}$."
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
            r"&\textbf{7. Puntos Notables y Tabla de Valores en } D: \\[6pt]"
            r"&\begin{array}{|c|c|c|c|c|c|c|} \hline "
            r"x & \mathbf{1/2} & 3/4 & \mathbf{7/8} & 1 & 5/4 & \mathbf{3/2} \\ \hline "
            r"f(x) & \mathbf{25/24} & 9/8 & \mathbf{{\color{amgreen}109/96}} & 9/8 & 25/24 & \mathbf{{\color{amred}7/8}} \\ \hline "
            r"\text{Rol} & \text{Cerrado } \bullet & \text{Sim.} & \mathbf{\text{Vértice } \bullet} & \text{Sim.} & \text{Sim.} & \text{Abierto } \circ \\ \hline "
            r"\end{array} \\[8pt]"
            r"&\textbf{Síntesis Institucional de Propiedades en } D: \\[5pt]"
            r"&\bullet \ \mathbf{\text{Vértice Interior: }} V\left(7/8, 109/96\right) \implies \text{Máximo Absoluto Global} \\[4pt]"
            r"&\bullet \ \mathbf{\text{Rango Final: }} \mathbf{{\color{amgreen}\operatorname{Ran}(f) = \left]7/8, 109/96\right]}} \approx \left]0.875, 1.135\right]"
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{7. Síntesis y Puntos Notables:}\\[6pt]"
            r"$\bullet$ La tabla refleja la simetría axial respecto a $x = 7/8$:\\[4pt]"
            r"\hspace*{0.8em}$f(3/4) = f(1) = 9/8 = 1.125$.\\[3pt]"
            r"\hspace*{0.8em}$f(1/2) = f(5/4) = 25/24 \approx 1.042$.\\[5pt]"
            r"$\bullet$ Al extenderse hasta $x = 3/2$, desciende más allá hasta $7/8 = 0.875$.\\[5pt]"
            r"$\bullet$ Puntos calibrados para el trazado cartesiano."
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
            r"$\bullet$ \textbf{Arco de Parábola:}\\[2pt]"
            r"\hspace*{0.8em}$f(x) = -\frac{2}{3}x^2 + \frac{7}{6}x + \frac{5}{8}$.\\[6pt]"
            r"$\bullet$ \textbf{Vértice Máximo:}\\[2pt]"
            r"\hspace*{0.8em}$V(0.875, 1.135)$ \textbf{Punto Cerrado}.\\[6pt]"
            r"$\bullet$ \textbf{Frontera Izquierda:}\\[2pt]"
            r"\hspace*{0.8em}$(0.5, 1.042)$ \textbf{Punto Cerrado} ($\bullet$).\\[6pt]"
            r"$\bullet$ \textbf{Frontera Derecha (Mín):}\\[2pt]"
            r"\hspace*{0.8em}$(1.5, 0.875)$ \textbf{Punto Abierto} ($\circ$).\\[6pt]"
            r"$\bullet$ \textbf{Rango Proyectado:}\\[2pt]"
            r"\hspace*{0.8em}$\left]\frac{7}{8}, \frac{109}{96}\right]$ en el eje vertical $Y$."
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
            x_range=[0.2, 1.8, 0.4],
            y_range=[0.7, 1.3, 0.1],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=13,
            labels_font_size=19
        )

        def f_val(x):
            return (-2.0 / 3.0) * (x**2) + (7.0 / 6.0) * x + (5.0 / 8.0)

        # Parábola completa referencial tenue
        curve_ref = axes.plot(
            f_val,
            x_range=[0.3, 1.7],
            color=THEME["statement_box"],
            stroke_width=1.5,
            stroke_opacity=0.45
        )

        # Arco de curva restringido en [0.5, 1.5]
        curve_dom = axes.plot(
            f_val,
            x_range=[0.5, 1.5],
            color=THEME["amarun_teal"],
            stroke_width=4.0
        )
        lbl_curve = MathTex(
            r"f(x) \text{ en } D",
            font_size=14.0,
            color=THEME["amarun_teal"]
        ).next_to(axes.c2p(1.15, 1.10), UP, buff=0.08)

        # Vértice interior V(7/8, 109/96)
        v_pt = axes.c2p(7.0 / 8.0, 109.0 / 96.0)
        dot_v = Dot(v_pt, radius=0.075, color=THEME["success"])
        lbl_v = MathTex(
            r"V\left(\frac{7}{8}, \frac{109}{96}\right)",
            font_size=13.0,
            color=THEME["success"]
        ).next_to(v_pt, UP, buff=0.10)

        # Extremo izquierdo cerrado (0.5, 25/24): punto sólido
        p_left = axes.c2p(0.5, 25.0 / 24.0)
        dot_left = Dot(p_left, radius=0.065, color=THEME["success"])
        lbl_left = MathTex(
            r"\left(\frac{1}{2}, \frac{25}{24}\right)",
            font_size=12.5,
            color=THEME["success"]
        ).next_to(p_left, DL, buff=0.08)

        # Extremo derecho abierto (1.5, 7/8): círculo hueco
        p_right = axes.c2p(1.5, 7.0 / 8.0)
        dot_right = Circle(
            radius=0.07,
            color=THEME["error"],
            stroke_width=2.5,
            fill_color=THEME["bg_color"],
            fill_opacity=1.0
        ).move_to(p_right)
        lbl_right = MathTex(
            r"\left(\frac{3}{2}, \frac{7}{8}\right)",
            font_size=12.5,
            color=THEME["error"]
        ).next_to(p_right, DR, buff=0.08)

        # Proyección del rango sobre el eje Y: ]7/8, 109/96]
        range_line = Line(
            axes.c2p(0.2, 7.0 / 8.0),
            axes.c2p(0.2, 109.0 / 96.0),
            color=THEME["success"],
            stroke_width=5.0
        )
        dot_r_open = Circle(
            radius=0.06,
            color=THEME["error"],
            stroke_width=2.2,
            fill_color=THEME["bg_color"],
            fill_opacity=1.0
        ).move_to(axes.c2p(0.2, 7.0 / 8.0))
        dot_r_closed = Dot(axes.c2p(0.2, 109.0 / 96.0), radius=0.065, color=THEME["success"])
        lbl_range = MathTex(
            r"\operatorname{Ran}(f) = \left]\frac{7}{8}, \frac{109}{96}\right]",
            font_size=12.5,
            color=THEME["success"]
        ).next_to(axes.c2p(0.2, 1.00), RIGHT, buff=0.10)

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

        # Trazado del arco restringido y proyección del rango
        self.play(
            Create(curve_dom), Write(lbl_curve),
            Create(range_line),
            FadeIn(dot_r_open), FadeIn(dot_r_closed), Write(lbl_range),
            run_time=2.2
        )

        # Marcado del vértice y extremos
        self.play(
            FadeIn(dot_v), Write(lbl_v),
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
            range_line, dot_r_open, dot_r_closed, lbl_range,
            dot_v, lbl_v,
            dot_left, lbl_left, dot_right, lbl_right
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
