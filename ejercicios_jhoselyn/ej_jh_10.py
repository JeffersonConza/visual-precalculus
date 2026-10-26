"""
Ejercicio 10 - Tutorías y Preparación Quiz 4 (Jhoselyn)
Tema: Comparación de Operadores de Transformación de Funciones:
      Sea una función cualquiera f. Compare las transformaciones:
      g(x) = -2f(x - 3) + 4    vs    h(x) = f(-2(x - 3)) + 4.
      Describa las transformaciones de cada una.

Contenido Pedagógico en 8 Pasos:
      1. Planteamiento de funciones y principio fundamental (exterior vs interior).
      2. Análisis deductivo de operadores exteriores en g(x).
      3. Secuencia canónica completa de transformaciones de g(x).
      4. Análisis deductivo de operadores interiores en h(x) (reciprocidad).
      5. Secuencia canónica completa de transformaciones de h(x).
      6. Matriz comparativa directa (coincidencias y discrepancias).
      7. Rastreo numérico de coordenadas con función prototipo f(x) = sqrt(x).
      8. Gráfica cartesiana comparativa dual (g vs h) y resumen formal.

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación en 8 pasos con tipografía HD garantizada (>= 21.0 pt).
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
\definecolor{amgold}{HTML}{F6B840}
\definecolor{amteal}{HTML}{5CE1E6}
\definecolor{amred}{HTML}{E53E3E}
\definecolor{amgreen}{HTML}{48BB78}
\definecolor{amorange}{HTML}{DB5A38}
""")
config.tex_template = AMARUN_TEX_TEMPLATE


class EjercicioJh_10(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Jhoselyn",
            exercise="Ejercicio 10",
            topic="Comparación de Operadores",
            font_size=15.5
        )

        # ==========================================================
        # 2. Enunciado Permanente en Recuadro Rojo Poncho (y = 2.65)
        # ==========================================================
        self.setup_statement(
            desc_text="Dada una función f, determine y compare las transformaciones de:",
            math_tex=r"{\color{amred}g(x) = -2f(x - 3) + 4} \quad \text{vs} \quad {\color{amteal}h(x) = f(-2(x - 3)) + 4}",
            desc_font_size=18.5,
            math_font_size=26.5,
            box_pos=np.array([0.0, 2.65, 0.0]),
            read_time=3.8
        )

        # ==========================================================
        # 3. Barra de Progreso Interactiva (8 pasos detallados)
        # ==========================================================
        self.setup_progress_bar([
            "1/8: Principio Exterior vs Interior",
            "2/8: Operadores Exteriores en g(x)",
            "3/8: Desglose Completo de g(x)",
            "4/8: Operadores Interiores en h(x)",
            "5/8: Desglose Completo de h(x)",
            "6/8: Matriz Comparativa",
            "7/8: Mapeo de Coordenadas",
            "8/8: Gráfica Dual y Resumen"
        ], dot_spacing=0.82, label_font_size=14.5)

        # ==========================================================
        # PASO 1: Planteamiento y Principio Fundamental
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Principio Fundamental de Transformación:} \\[4pt]"
            r"&\text{Analizamos dos formas con los mismos coeficientes } {\color{amred}-2}, {\color{amgold}3}, {\color{amgreen}4}: \\[5pt]"
            r"&\mathbf{g(x) = {\color{amred}-2} f(x - {\color{amgold}3}) + {\color{amgreen}4}} \quad \longleftarrow \text{\textbf{Operador Exterior}} \\[4pt]"
            r"&\mathbf{h(x) = f({\color{amred}-2}(x - {\color{amgold}3})) + {\color{amgreen}4}} \quad \longleftarrow \text{\textbf{Operador Interior}} \\[6pt]"
            r"&\bullet \text{\textbf{Regla Exterior: }} \text{Afecta a la salida } y \text{ (vertical, sentido directo).} \\[4pt]"
            r"&\bullet \text{\textbf{Regla Interior: }} \text{Afecta a la entrada } x \text{ (horizontal, sentido recíproco).}"
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{1. ¿Por qué es Pregunta Fija de Examen?}\\[6pt]"
            r"$\bullet$ Ambas expresiones usan exactamente los mismos números ($-2$, $3$ y $4$), pero su ubicación altera radicalmente el resultado geométrico.\\[5pt]"
            r"$\bullet$ \textbf{Afuera de $f$:} Las operaciones modifican la altura $y$. Lo que ves es lo que obtienes.\\[5pt]"
            r"$\bullet$ \textbf{Adentro de $f$:} Las operaciones modifican el dominio $x$, actuando de forma contraintuitiva (recíproca)."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=3.3)

        # ==========================================================
        # PASO 2: Operaciones Exteriores en g(x)
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Análisis de Operaciones en } g(x): \\[4pt]"
            r"&g(x) = {\color{amred}-2} f(x - 3) + {\color{amgreen}4} \\[5pt]"
            r"&\bullet \text{\textbf{Dilatación Vertical:}} \\[3pt]"
            r"&\quad \text{Factor exterior } |{-2}| = {\color{amred}2 > 1} \implies \text{Estiramiento vertical } \times 2 \\[5pt]"
            r"&\bullet \text{\textbf{Reflexión respecto al eje }} {\color{amred}X}\textbf{:} \\[3pt]"
            r"&\quad \text{Signo exterior } - \implies \text{Invierte verticalmente } (y \to -y) \\[5pt]"
            r"&\bullet \text{\textbf{Traslación Vertical:}} \\[3pt]"
            r"&\quad \text{Constante } {\color{amgreen}+4} \implies \text{Desplaza } 4 \text{ unidades hacia arriba}"
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{2. Efecto de los Operadores Externos:}\\[6pt]"
            r"$\bullet$ El número $-2$ multiplica directamente a $f(x-3)$:\\[3pt]"
            r"\hspace*{1.2em}La gráfica duplica su altura respecto al eje $X$ y luego se invierte boca abajo.\\[5pt]"
            r"$\bullet$ El término $+4$ se suma al final de toda la evaluación:\\[3pt]"
            r"\hspace*{1.2em}Eleva verticalmente todos los puntos $4$ unidades completas.\\[5pt]"
            r"$\bullet$ El argumento $x-3$ desplaza a la derecha."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq2, just2, box_color=THEME["highlight"], advance_to_step=1, wait_time=3.3)

        # ==========================================================
        # PASO 3: Desglose Completo de g(x) (Respuesta Guía 2.5)
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Secuencia Canónica de } g(x) = -2f(x - 3) + 4: \\[4pt]"
            r"&\mathbf{1.} \; f_1(x) = f(x - 3) \implies \text{\textbf{3 unidades a la derecha}} \\[4pt]"
            r"&\mathbf{2.} \; f_2(x) = 2f(x - 3) \implies \text{\textbf{Dilatación vertical de factor 2}} \\[4pt]"
            r"&\mathbf{3.} \; f_3(x) = -2f(x - 3) \implies \text{\textbf{Reflexión respecto al eje }} \mathbf{X} \\[4pt]"
            r"&\mathbf{4.} \; g(x) = -2f(x - 3) + 4 \implies \text{\textbf{4 unidades hacia arriba}} \\[6pt]"
            r"&\implies \mathbf{\text{Mapeo de Coordenadas: }} (x, y) \longrightarrow \mathbf{(x + 3, \; -2y + 4)}"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{3. Respuesta Formal para el Examen:}\\[6pt]"
            r"$\bullet$ Para $g(x) = -2f(x-3) + 4$, la Guía Oficial exige redactar la lista ordenada de 4 pasos:\\[3pt]"
            r"1. $3$ unidades a la derecha ($x \to x + 3$).\\[2pt]"
            r"2. Dilatación vertical de factor $2$.\\[2pt]"
            r"3. Reflexión respecto al eje $X$.\\[2pt]"
            r"4. $4$ unidades hacia arriba ($y \to y + 4$).\\[5pt]"
            r"$\bullet$ La regla de mapeo $(x+3, -2y+4)$ servirá para graficar."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=3.3)

        # ==========================================================
        # PASO 4: Operaciones Interiores en h(x)
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Análisis de Operaciones Interiores en } h(x): \\[4pt]"
            r"&h(x) = f({\color{amteal}-2}(x - {\color{amgold}3})) + {\color{amgreen}4} \\[5pt]"
            r"&\bullet \text{\textbf{Compresión Horizontal:}} \\[3pt]"
            r"&\quad \text{Factor interior } |{-2}| = {\color{amteal}2 > 1} \implies \text{Factor de escala } \mathbf{\frac{1}{2}} \quad \left(x \to \frac{x}{2}\right) \\[5pt]"
            r"&\bullet \text{\textbf{Reflexión respecto al eje }} {\color{amteal}Y}\textbf{:} \\[3pt]"
            r"&\quad \text{Signo interior } - \implies \text{Invierte horizontalmente } (x \to -x) \\[5pt]"
            r"&\bullet \text{\textbf{Traslación Horizontal:}} \\[3pt]"
            r"&\quad \text{Término factorizado } (x - 3) = 0 \implies \mathbf{3 \text{ unidades a la derecha}}"
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{4. Regla Recíproca de Factores Internos:}\\[6pt]"
            r"$\bullet$ \textbf{¡Error Crítico de Examen!}\\[3pt]"
            r"\hspace*{1.2em}Multiplicar por $2$ adentro no dilata; \textbf{comprime} la curva a la mitad de ancho.\\[5pt]"
            r"$\bullet$ El signo negativo interior cambia el sentido horizontal:\\[3pt]"
            r"\hspace*{1.2em}Refleja respecto al eje vertical $Y$ (izquierda $\leftrightarrow$ derecha).\\[5pt]"
            r"$\bullet$ El $-2$ ya está factorizado: la traslación es $+3$ u a la derecha."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=3.3)

        # ==========================================================
        # PASO 5: Desglose Completo de h(x) (Respuesta Guía 2.5)
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Secuencia Canónica de } h(x) = f(-2(x - 3)) + 4: \\[4pt]"
            r"&\mathbf{1.} \; h_1(x) = f(x - 3) \implies \text{\textbf{3 unidades a la derecha}} \\[4pt]"
            r"&\mathbf{2.} \; h_2(x) = f(2(x - 3)) \implies \text{\textbf{Compresión horiz. factor }} \mathbf{\frac{1}{2}} \\[4pt]"
            r"&\mathbf{3.} \; h_3(x) = f(-2(x - 3)) \implies \text{\textbf{Reflexión respecto al eje }} \mathbf{Y} \\[4pt]"
            r"&\mathbf{4.} \; h(x) = h_3(x) + 4 \implies \text{\textbf{4 unidades hacia arriba}} \\[6pt]"
            r"&\implies \mathbf{\text{Mapeo de Coordenadas: }} (x, y) \longrightarrow \mathbf{\left(-\frac{x}{2} + 3, \; y + 4\right)}"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{5. Respuesta Formal para } $h(x)$:\\[6pt]"
            r"$\bullet$ Para $h(x) = f(-2(x-3)) + 4$, la Guía Oficial indica:\\[3pt]"
            r"1. $3$ unidades a la derecha ($x \to x + 3$).\\[2pt]"
            r"2. Compresión horizontal de factor $\frac{1}{2}$.\\[2pt]"
            r"3. Reflexión respecto al eje $Y$.\\[2pt]"
            r"4. $4$ unidades hacia arriba ($y \to y + 4$).\\[5pt]"
            r"$\bullet$ Nota que la traslación vertical $+4$ es idéntica en ambas funciones."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=3.3)

        # ==========================================================
        # PASO 6: Matriz Comparativa Directa
        # ==========================================================
        eq6 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Matriz Comparativa Frente a Frente:} \\[5pt]"
            r"&\begin{array}{c|c|c}"
            r"\textbf{Propiedad} & \mathbf{g(x) = -2f(x - 3) + 4} & \mathbf{h(x) = f(-2(x - 3)) + 4} \\ \hline "
            r"\text{Traslación } X & 3\text{ u a la derecha} & 3\text{ u a la derecha} \\ "
            r"\text{Factor Escala} & \text{\textbf{Dilatación vert. factor 2}} & \text{\textbf{Compresión horiz. factor }} \mathbf{\frac{1}{2}} \\ "
            r"\text{Reflexión} & \text{\textbf{Eje }} \mathbf{X} \text{ (vertical)} & \text{\textbf{Eje }} \mathbf{Y} \text{ (horizontal)} \\ "
            r"\text{Traslación } Y & 4\text{ u hacia arriba} & 4\text{ u hacia arriba}"
            r"\end{array} \\[6pt]"
            r"&\bullet \mathbf{\text{Clave Nemotécnica: }} \text{Factor exterior } \to Y; \quad \text{Factor interior } \to X."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{6. Resumen Teórico de Alto Impacto:}\\[6pt]"
            r"$\bullet$ \textbf{Semejanzas:}\\[3pt]"
            r"\hspace*{1.2em}Ambas funciones se desplazan $3$ unidades a la derecha y suben $4$ unidades.\\[5pt]"
            r"$\bullet$ \textbf{Diferencias Cruciales:}\\[3pt]"
            r"\hspace*{1.2em}En $g(x)$, el $-2$ actúa sobre las amplitudes verticales ($Y$).\\[3pt]"
            r"\hspace*{1.2em}En $h(x)$, el $-2$ actúa sobre el ancho y sentido horizontal ($X$)."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq6, just6, box_color=THEME["highlight"], advance_to_step=5, wait_time=3.2)

        # ==========================================================
        # PASO 7: Mapeo de Puntos con Prototipo f(x) = sqrt(x)
        # ==========================================================
        eq7 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{7. Rastreo Coordenado con } f(x) = \sqrt{x}: \\[5pt]"
            r"&\begin{array}{c|c|c}"
            r"\textbf{Punto en } f & \text{Transformado en } g(x) & \text{Transformado en } h(x) \\ \hline "
            r"\mathbf{O(0, 0)} & (0+3, -2(0)+4) = \mathbf{(3, 4)} & (-0/2+3, 0+4) = \mathbf{(3, 4)} \\ "
            r"\mathbf{A(1, 1)} & (1+3, -2(1)+4) = \mathbf{(4, 2)} & (-1/2+3, 1+4) = \mathbf{(2.5, 5)} \\ "
            r"\mathbf{B(4, 2)} & (4+3, -2(2)+4) = \mathbf{(7, 0)} & (-4/2+3, 2+4) = \mathbf{(1, 6)}"
            r"\end{array} \\[6pt]"
            r"&\bullet \mathbf{\text{Punto Ancla Común: }} (3, 4) \text{ es el origen transformado.} \\[4pt]"
            r"&\bullet \mathbf{\operatorname{Dom}(g) = [3, +\infty)}, \quad \mathbf{\operatorname{Dom}(h) = (-\infty, 3]}."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{7. Visualización con Función Prototipo:}\\[6pt]"
            r"$\bullet$ Para evidenciar la reflexión en $Y$, usamos $f(x) = \sqrt{x}$ (función no simétrica orientada a la derecha):\\[4pt]"
            r"$\bullet$ En $g(x)$: Al reflejarse en $X$, las ramas apuntan hacia abajo-derecha ($y \le 4, x \le 3$).\\[4pt]"
            r"$\bullet$ En $h(x)$: Al reflejarse en $Y$, las ramas apuntan hacia arriba-izquierda ($y \ge 4, x \le 3$).\\[4pt]"
            r"$\bullet$ ¡Ambas curvas nacen en el mismo ancla $(3, 4)$!"
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq7, just7, box_color=THEME["highlight"], advance_to_step=6, wait_time=3.2)

        # ==========================================================
        # PASO 8: Gráfica Cartesiana Comparativa Dual y Resumen
        # ==========================================================
        # Panel Izquierdo: Resumen Formal Esmeralda
        left_summary = MathTex(
            r"\begin{aligned}"
            r"&\textbf{8. Síntesis Formal de Transformaciones:} \\[6pt]"
            r"&\bullet \mathbf{\text{Punto Ancla Compartido: }} \mathbf{(3, 4)} \\[5pt]"
            r"&\bullet \mathbf{g(x) = -2f(x - 3) + 4:} \\[3pt]"
            r"&\quad \text{Derecha 3, Dilatación vert. } \times 2, \text{ Reflexión } {\color{amred}X}, \text{ Sube 4.} \\[3pt]"
            r"&\quad \text{Curva proyectada hacia } \mathbf{\text{abajo-derecha.}} \\[5pt]"
            r"&\bullet \mathbf{h(x) = f(-2(x - 3)) + 4:} \\[3pt]"
            r"&\quad \text{Derecha 3, Compresión horiz. } \times \frac{1}{2}, \text{ Reflexión } {\color{amteal}Y}, \text{ Sube 4.} \\[3pt]"
            r"&\quad \text{Curva proyectada hacia } \mathbf{\text{arriba-izquierda.}} \\[5pt]"
            r"&\bullet \mathbf{\text{Conclusión: }} \text{El orden y posición de operadores} \\[2pt]"
            r"&\quad \text{determinan el cuadrante de desarrollo.} \quad \blacksquare"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.65, 0])

        box8 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.16, corner_radius=0.12)

        # Panel Derecho: Gráfico Cartesiano
        axes = Axes(
            x_range=[-0.5, 7.5, 1],
            y_range=[-0.5, 7.0, 1],
            x_length=4.8,
            y_length=4.2,
            tips=True,
            axis_config={
                "color": THEME["axes"],
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 16,
                "tip_width": 0.12,
                "tip_height": 0.12,
            },
            x_axis_config={
                "numbers_to_include": [1, 3, 5],
            },
            y_axis_config={
                "numbers_to_include": [2, 4, 6],
            }
        ).move_to([3.3, -0.65, 0])

        x_lbl = axes.get_x_axis_label("x", edge=RIGHT, direction=RIGHT).scale(0.85)
        y_lbl = axes.get_y_axis_label("y", edge=UP, direction=UP).scale(0.85)

        # Curva prototipo base f(x) = sqrt(x)
        curve_f = axes.plot(
            lambda x: np.sqrt(x),
            x_range=[0.0, 4.5],
            color=THEME["highlight"],
            stroke_width=2.5
        )
        lbl_f = MathTex(r"f(x) = \sqrt{x}", font_size=17.0, color=THEME["highlight"]).next_to(
            axes.c2p(2.2, 1.48), UP, buff=0.08
        )

        # Curva g(x) = -2*sqrt(x - 3) + 4  (x in [3.0, 7.0])
        curve_g = axes.plot(
            lambda x: -2.0 * np.sqrt(x - 3.0) + 4.0,
            x_range=[3.0, 7.0],
            color=THEME["error"],
            stroke_width=3.2
        )
        lbl_g = MathTex(r"g(x)", font_size=18.0, color=THEME["error"]).next_to(
            axes.c2p(5.8, 0.8), UR, buff=0.08
        )

        # Curva h(x) = sqrt(-2*(x - 3)) + 4  (x in [0.5, 3.0])
        curve_h = axes.plot(
            lambda x: np.sqrt(-2.0 * (x - 3.0)) + 4.0,
            x_range=[0.5, 3.0],
            color=THEME["curve"],
            stroke_width=3.2
        )
        lbl_h = MathTex(r"h(x)", font_size=18.0, color=THEME["curve"]).next_to(
            axes.c2p(1.8, 5.2), DL, buff=0.1
        )

        # Punto Ancla Común (3, 4)
        dot_anchor = Dot(axes.c2p(3, 4), color=THEME["highlight"], radius=0.08)
        lbl_anchor = MathTex(r"(3, 4)", font_size=18.0, color=THEME["highlight"]).next_to(
            dot_anchor, UR, buff=0.08
        )

        # Puntos de Control en g: (4, 2) y (7, 0)
        dot_g1 = Dot(axes.c2p(4, 2), color=THEME["error"], radius=0.06)
        dot_g2 = Dot(axes.c2p(7, 0), color=THEME["error"], radius=0.06)
        lbl_g2 = MathTex(r"(7, 0)", font_size=15.0, color=THEME["error"]).next_to(
            dot_g2, UR, buff=0.08
        )

        # Puntos de Control en h: (2.5, 5) y (1, 6)
        dot_h1 = Dot(axes.c2p(2.5, 5), color=THEME["curve"], radius=0.06)
        dot_h2 = Dot(axes.c2p(1, 6), color=THEME["curve"], radius=0.06)
        lbl_h2 = MathTex(r"(1, 6)", font_size=15.0, color=THEME["curve"]).next_to(
            dot_h2, UP, buff=0.08
        )

        prog_anims = self.get_advance_progress_anims(7)

        # Animación secuencial Paso 8
        self.play(
            FadeOut(self.active_math),
            FadeOut(self.active_just),
            FadeOut(self.active_box),
            FadeIn(left_summary),
            Create(box8),
            Create(axes),
            Write(x_lbl),
            Write(y_lbl),
            *prog_anims,
            run_time=2.0
        )
        self.active_box = box8
        self.active_math = left_summary
        self.active_just = None

        self.play(
            Create(curve_f),
            Write(lbl_f),
            run_time=1.4
        )
        self.play(
            FadeIn(dot_anchor),
            Write(lbl_anchor),
            Create(curve_g),
            Write(lbl_g),
            FadeIn(dot_g1),
            FadeIn(dot_g2),
            Write(lbl_g2),
            run_time=2.2
        )
        self.play(
            Create(curve_h),
            Write(lbl_h),
            FadeIn(dot_h1),
            FadeIn(dot_h2),
            Write(lbl_h2),
            run_time=2.0
        )

        # Pausa de asimilación completa
        self.wait(4.5)

        # Cierre institucional
        graph_group = VGroup(
            axes, x_lbl, y_lbl,
            curve_f, lbl_f,
            curve_g, lbl_g, dot_anchor, lbl_anchor,
            dot_g1, dot_g2, lbl_g2,
            curve_h, lbl_h,
            dot_h1, dot_h2, lbl_h2
        )
        self.play(
            FadeOut(graph_group),
            FadeOut(self.active_math),
            FadeOut(self.active_box),
            run_time=1.4
        )
        self.wait(1.0)
