"""
Ejercicio 9 - Tutorías y Preparación Quiz 4 (Jhoselyn)
Tema: Transformaciones de Funciones Cuadráticas y Forma Canónica:
      A partir de f(x) = x^2, determine todas las transformaciones necesarias para obtener
      g(x) = -3/2 (2x + 4)^2 + 5.
      Exprese además en la forma a(x - h)^2 + k y determine su vértice.

Contenido Pedagógico en 8 Pasos:
      1. Identificación de la función elemental base f(x) = x^2 y objetivo.
      2. Factorización interna obligatoria del argumento: 2x + 4 = 2(x + 2).
      3. Obtención de la forma canónica estándar g(x) = -6(x + 2)^2 + 5.
      4. Determinación analítica del vértice V(-2, 5), apertura y concavidad.
      5. Desglose secuencial de las 4 transformaciones elementales paso a paso.
      6. Interpretación alternativa directa según operadores de la guía oficial.
      7. Cuadro de transformación de pares ordenados (puntos de control).
      8. Representación gráfica cartesiana comparativa dual (f vs g) y resumen formal.

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica en 8 pasos con tipografía HD garantizada (>= 21 pt).
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


class EjercicioJh_09(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Jhoselyn",
            exercise="Ejercicio 9",
            topic="Transformaciones de Funciones Cuadráticas",
            font_size=17.0
        )

        # ==========================================================
        # 2. Enunciado Permanente en Recuadro Rojo Poncho (y = 2.65)
        # ==========================================================
        self.setup_statement(
            desc_text="A partir de f(x) = x², determine las transformaciones de:",
            math_tex=r"{\color{amteal}g(x) = -\frac{3}{2}(2x + 4)^2 + 5}",
            desc_font_size=18.5,
            math_font_size=28.0,
            box_pos=np.array([0.0, 2.65, 0.0]),
            read_time=3.8
        )

        # ==========================================================
        # 3. Barra de Progreso Interactiva (8 pasos detallados)
        # ==========================================================
        self.setup_progress_bar([
            "1/8: Función Base y Objetivo",
            "2/8: Factorización Interna",
            "3/8: Forma Canónica a(x-h)²+k",
            "4/8: Vértice y Concavidad",
            "5/8: Secuencia de Transformaciones",
            "6/8: Interpretación Directa",
            "7/8: Tabla de Puntos Clave",
            "8/8: Gráfica Dual y Resumen"
        ], dot_spacing=0.82, label_font_size=14.5)

        # ==========================================================
        # PASO 1: Función Elemental Base y Planteamiento
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Función Base y Expresión Dada:} \\[4pt]"
            r"&\text{Partimos de la parábola estándar elemental:} \\[4pt]"
            r"&\qquad {\color{amgold}f(x) = x^2}, \qquad V_{\text{base}}(0, 0) \\[5pt]"
            r"&\text{Queremos obtener mediante transformaciones:} \\[4pt]"
            r"&\qquad {\color{amteal}g(x) = -\frac{3}{2}(2x + 4)^2 + 5} \\[5pt]"
            r"&\bullet \text{Objetivo: Expresar en forma canónica } a(x - h)^2 + k, \\[3pt]"
            r"&\quad \text{hallar su vértice } V(h, k) \text{ y describir cada cambio.}"
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{1. Identificación del Problema:}\\[6pt]"
            r"$\bullet$ La función base es la parábola canónica $f(x) = x^2$, con vértice en el origen $(0, 0)$.\\[5pt]"
            r"$\bullet$ La función $g(x)$ presenta múltiples modificaciones combinadas (argumento y exteriores).\\[5pt]"
            r"$\bullet$ Para identificar con precisión las traslaciones y dilataciones, es indispensable llevarla a la forma canónica estándar:\\[3pt]"
            r"\hspace*{1.2em}$g(x) = a(x - h)^2 + k$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=3.2)

        # ==========================================================
        # PASO 2: Factorización Interna del Argumento
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Factorización Interna del Argumento:} \\[4pt]"
            r"&\text{Para aislar la traslación horizontal, factorizamos } 2: \\[4pt]"
            r"&\qquad 2x + 4 = {\color{amgold}2(x + 2)} \\[5pt]"
            r"&\text{Elevamos al cuadrado aplicando leyes de exponentes:} \\[4pt]"
            r"&\qquad (2x + 4)^2 = [{\color{amgold}2(x + 2)}]^2 = 2^2 \cdot (x + 2)^2 \\[4pt]"
            r"&\qquad \mathbf{(2x + 4)^2 = {\color{amteal}4(x + 2)^2}} \\[5pt]"
            r"&\implies \text{El factor } 4 \text{ saldrá a multiplicar al coeficiente exterior.}"
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{2. Regla Clave de Factorización:}\\[6pt]"
            r"$\bullet$ \textbf{¡Error muy común en exámenes!}\\[3pt]"
            r"\hspace*{1.2em}No confundir el $+4$ con una traslación de $4$ unidades. El coeficiente de $x$ debe ser $1$.\\[5pt]"
            r"$\bullet$ Al factorizar el $2$ dentro del binomio:\\[3pt]"
            r"\hspace*{1.2em}$2x + 4 = 2(x + 2)$.\\[5pt]"
            r"$\bullet$ Al elevar al cuadrado, se distribuye la potencia:\\[3pt]"
            r"\hspace*{1.2em}$[2(x + 2)]^2 = 4(x + 2)^2$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq2, just2, box_color=THEME["highlight"], advance_to_step=1, wait_time=3.2)

        # ==========================================================
        # PASO 3: Obtención de la Forma Canónica Estándar
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Obtención de la Forma Canónica Estándar:} \\[4pt]"
            r"&\text{Sustituimos el término cuadrático factorizado:} \\[4pt]"
            r"&g(x) = -\frac{3}{2} \cdot \left[{\color{amteal}4(x + 2)^2}\right] + 5 \\[5pt]"
            r"&\text{Multiplicamos los coeficientes numéricos:} \\[4pt]"
            r"&-\frac{3}{2} \cdot 4 = -\frac{12}{2} = {\color{amred}-6} \\[5pt]"
            r"&\mathbf{{\color{amgreen}g(x) = -6(x + 2)^2 + 5}} \quad \equiv \quad a(x - h)^2 + k \\[5pt]"
            r"&\implies \mathbf{a = -6, \quad h = -2, \quad k = 5}"
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{3. Forma Estándar $a(x-h)^2 + k$:}\\[6pt]"
            r"$\bullet$ La constante $-\frac{3}{2}$ se multiplica por $4$:\\[3pt]"
            r"\hspace*{1.2em}$-\frac{3}{2} \times 4 = -6$.\\[5pt]"
            r"$\bullet$ La función toma su forma canónica final:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgreen}g(x) = -6(x + 2)^2 + 5}$.\\[5pt]"
            r"$\bullet$ Identificación inmediata de parámetros:\\[3pt]"
            r"\hspace*{1.2em}$a = -6, \quad h = -2, \quad k = 5$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=3.2)

        # ==========================================================
        # PASO 4: Vértice, Eje de Simetría y Apertura
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Determinación del Vértice y Propiedades:} \\[4pt]"
            r"&\bullet \mathbf{\text{Vértice: }} V(h, k) = \mathbf{{\color{amgold}(-2, 5)}} \\[4pt]"
            r"&\bullet \mathbf{\text{Eje de Simetría: }} \text{Recta vertical } {\color{amgold}x = -2} \\[5pt]"
            r"&\bullet \mathbf{\text{Sentido de Apertura:}} \\[3pt]"
            r"&\quad \text{Como } {\color{amred}a = -6 < 0} \implies \text{La parábola abre hacia abajo.} \\[5pt]"
            r"&\bullet \mathbf{\text{Naturaleza del Extremo: }} V(-2, 5) \text{ es un } \mathbf{\text{MÁXIMO absoluto.}} \\[4pt]"
            r"&\bullet \mathbf{\operatorname{Ran}(g) = (-\infty, 5]} \quad (\text{conjunto imagen})"
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{4. Geometría de la Parábola:}\\[6pt]"
            r"$\bullet$ El vértice $(h, k)$ se extrae directamente de la forma canónica: $V = (-2, 5)$.\\[5pt]"
            r"$\bullet$ El signo negativo ($a = -6$) invierte la concavidad: abre hacia abajo.\\[5pt]"
            r"$\bullet$ El vértice es el punto más alto de la trayectoria (máximo absoluto en $y = 5$).\\[5pt]"
            r"$\bullet$ El rango está acotado superiormente por $5$: $\operatorname{Ran}(g) = (-\infty, 5]$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=3.2)

        # ==========================================================
        # PASO 5: Secuencia Canónica de Transformaciones
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Cadena de Transformaciones (desde } f(x) = x^2\textbf{):} \\[4pt]"
            r"&\mathbf{1.} \; f_1(x) = f(x + 2) = (x + 2)^2 \\[3pt]"
            r"&\quad \implies \text{\textbf{Traslación horizontal}} \text{ de } {\color{amgold}2 \text{ u a la izquierda.}} \\[4pt]"
            r"&\mathbf{2.} \; f_2(x) = 6 f_1(x) = 6(x + 2)^2 \\[3pt]"
            r"&\quad \implies \text{\textbf{Dilatación vertical}} \text{ de factor } {\color{amgold}6} \text{ (estiramiento).} \\[4pt]"
            r"&\mathbf{3.} \; f_3(x) = -f_2(x) = -6(x + 2)^2 \\[3pt]"
            r"&\quad \implies \text{\textbf{Reflexión respecto al eje }} {\color{amred}X} \text{ (invierte ramas).} \\[4pt]"
            r"&\mathbf{4.} \; g(x) = f_3(x) + 5 = -6(x + 2)^2 + 5 \\[3pt]"
            r"&\quad \implies \text{\textbf{Traslación vertical}} \text{ de } {\color{amgreen}5 \text{ u hacia arriba.}}"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{5. Secuencia Paso a Paso:}\\[6pt]"
            r"$\bullet$ Partiendo de la forma canónica $g(x) = -6(x+2)^2 + 5$, aplicamos el orden estándar de operaciones:\\[4pt]"
            r"1. Argumento $x+2$: desplaza $2$ unidades a la izquierda.\\[3pt]"
            r"2. Factor $6$: estira verticalmente la curva por un factor de $6$.\\[3pt]"
            r"3. Signo $-$: refleja toda la parábola sobre el eje horizontal $X$.\\[3pt]"
            r"4. Término $+5$: sube la gráfica $5$ unidades completas."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=3.4)

        # ==========================================================
        # PASO 6: Interpretación Directa según la Guía Oficial
        # ==========================================================
        eq6 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Interpretación según Expresión Original:} \\[4pt]"
            r"&\text{En } g(x) = -{\color{amred}\frac{3}{2}}({\color{amteal}2}(x + {\color{amgold}2}))^2 + {\color{amgreen}5}, \text{ la guía indica:} \\[4pt]"
            r"&\bullet \text{\textbf{2 unidades a la izquierda}} \quad (x \to x + 2) \\[4pt]"
            r"&\bullet \text{\textbf{Compresión horizontal}} \text{ de factor } {\color{amteal}\frac{1}{2}} \quad (x \to 2x) \\[4pt]"
            r"&\bullet \text{\textbf{Dilatación vertical}} \text{ de factor } {\color{amred}\frac{3}{2}} \\[4pt]"
            r"&\bullet \text{\textbf{Reflexión respecto al eje }} {\color{amred}X} \quad (\text{signo exterior } -) \\[4pt]"
            r"&\bullet \text{\textbf{5 unidades hacia arriba}} \quad (y \to y + 5) \\[5pt]"
            r"&\implies \text{\textbf{Equivalencia: }} \left(\frac{1}{2}\right)^{-2} \cdot \frac{3}{2} = 4 \cdot \frac{3}{2} = \mathbf{6} \quad \checkmark"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{6. Ambas Descripciones son Válidas:}\\[6pt]"
            r"$\bullet$ La guía oficial de clase presenta la lectura directa de los operadores originales:\\[3pt]"
            r"\hspace*{1.2em}Compresión horizontal de factor $\frac{1}{2}$ combinada con dilatación vertical de $\frac{3}{2}$.\\[5pt]"
            r"$\bullet$ Debido a la propiedad cuadrática $(2x)^2 = 4x^2$, comprimir horizontalmente por $\frac{1}{2}$ equivale exactamente a multiplicar verticalmente por $4$.\\[5pt]"
            r"$\bullet$ Por ello: $4 \times \frac{3}{2} = 6$. Ambas vías son $100\%$ rigurosas."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq6, just6, box_color=THEME["highlight"], advance_to_step=5, wait_time=3.4)

        # ==========================================================
        # PASO 7: Tabla de Transformación de Puntos Clave
        # ==========================================================
        eq7 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{7. Cuadro de Transformación de Puntos Clave:} \\[5pt]"
            r"&\begin{array}{c|c|c|c}"
            r"\textbf{Etapa de Transformación} & \text{Vértice } O(0, 0) & P_1(1, 1) & P_2(-1, 1) \\ \hline "
            r"f(x) = x^2 & (0, 0) & (1, 1) & (-1, 1) \\ "
            r"\text{Izquierda } 2\text{ u } (x \to x - 2) & (-2, 0) & (-1, 1) & (-3, 1) \\ "
            r"\text{Escala } -6 \quad (y \to -6y) & (-2, 0) & (-1, -6) & (-3, -6) \\ "
            r"\text{Arriba } 5\text{ u } (y \to y + 5) & \mathbf{V(-2, 5)} & \mathbf{P_1'(-1, -1)} & \mathbf{P_2'(-3, -1)}"
            r"\end{array} \\[6pt]"
            r"&\bullet \mathbf{\text{Simetría Parábola: }} P_1' \text{ y } P_2' \text{ equidistan del eje } x = -2. \\[4pt]"
            r"&\bullet \mathbf{\text{Puntos de Control: }} \text{Garantizan el trazado exacto de las ramas.}"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{7. Rastreo Numérico de Coordenadas:}\\[6pt]"
            r"$\bullet$ El rastreo de puntos notables es la técnica más sólida para no errar en el examen:\\[3pt]"
            r"\hspace*{1.2em}$(x, y) \longrightarrow (x - 2, \; -6y + 5)$.\\[5pt]"
            r"$\bullet$ Vértice base $(0, 0) \longrightarrow (-2, 5)$.\\[4pt]"
            r"$\bullet$ Puntos simétricos a $1$ unidad:\\[3pt]"
            r"\hspace*{1.2em}$(1, 1) \longrightarrow (-1, -1)$.\\[3pt]"
            r"\hspace*{1.2em}$(-1, 1) \longrightarrow (-3, -1)$.\\[5pt]"
            r"$\bullet$ Confirma que las ramas caen velozmente."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq7, just7, box_color=THEME["highlight"], advance_to_step=6, wait_time=3.6)

        # ==========================================================
        # PASO 8: Gráfica Cartesiana Comparativa y Resumen Formal
        # ==========================================================
        left_summary = MathTex(
            r"\begin{aligned}"
            r"&\textbf{8. Resumen Formal de Resultados:} \\[4pt]"
            r"&\bullet \mathbf{\text{Función Base: }} {\color{amgold}f(x) = x^2}, \quad V_{\text{base}}(0, 0) \\[4pt]"
            r"&\bullet \mathbf{\text{Forma Canónica: }} {\color{amgreen}g(x) = -6(x + 2)^2 + 5} \\[4pt]"
            r"&\bullet \mathbf{\text{Parámetros: }} a = -6, \quad h = -2, \quad k = 5 \\[4pt]"
            r"&\bullet \mathbf{\text{Vértice: }} \mathbf{V(h, k) = {\color{amgold}(-2, 5)}} \quad (\text{Máximo}) \\[4pt]"
            r"&\bullet \mathbf{\text{Eje de Simetría: }} {\color{amgold}x = -2} \\[4pt]"
            r"&\bullet \mathbf{\text{Apertura: }} a < 0 \implies \text{Cóncava hacia abajo} \\[4pt]"
            r"&\bullet \mathbf{\operatorname{Ran}(g) = (-\infty, 5]} \\[4pt]"
            r"&\bullet \mathbf{\text{Puntos Clave: }} (-1, -1) \quad \text{y} \quad (-3, -1) \quad {\color{amgreen}\blacksquare}"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.60, 0])

        box8 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.16, corner_radius=0.1)

        # Gráfico cartesiano
        axes = Axes(
            x_range=[-4.0, 2.0, 1],
            y_range=[-2.0, 6.0, 2],
            x_length=4.8,
            y_length=4.0,
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
                "numbers_to_include": [-4, -3, 1, 2],
            },
            y_axis_config={
                "numbers_to_include": [-2, 2, 4, 6],
            }
        ).move_to([3.3, -0.65, 0])

        x_lbl = MathTex("x", font_size=19, color=THEME["statement_text"]).next_to(axes.x_axis.get_end(), RIGHT, buff=0.10)
        y_lbl = MathTex("y", font_size=19, color=THEME["statement_text"]).next_to(axes.y_axis.get_end(), LEFT, buff=0.12)
        axes_labels = VGroup(x_lbl, y_lbl)

        # Curva base f(x) = x^2
        curve_f = axes.plot(
            lambda x: x**2,
            x_range=[-2.1, 2.1],
            color=THEME["highlight"],
            stroke_width=2.2
        )
        lbl_f = MathTex(r"f(x) = x^2", font_size=15.0, color=THEME["highlight"]).move_to(axes.c2p(1.4, 3.4))

        # Eje de simetría x = -2 (sube desde abajo hasta el vértice)
        sym_line = DashedLine(
            axes.c2p(-2.0, -1.9), axes.c2p(-2.0, 5.0),
            dash_length=0.08, color=THEME["highlight"], stroke_width=1.5
        )
        lbl_sym = MathTex(r"x = -2", font_size=13.0, color=THEME["highlight"]).next_to(axes.c2p(-2.0, -1.9), DOWN, buff=0.08)

        # Curva transformada g(x) = -6(x + 2)^2 + 5
        curve_g = axes.plot(
            lambda x: -6*(x + 2)**2 + 5,
            x_range=[-3.05, -0.95],
            color=THEME["curve"],
            stroke_width=2.8
        )
        lbl_g = MathTex(r"g(x)", font_size=15.0, color=THEME["curve"]).move_to(axes.c2p(-0.6, 2.0))

        # Vértice V(-2, 5)
        dot_v = Dot(axes.c2p(-2.0, 5.0), radius=0.07, color=THEME["highlight"])
        lbl_v = MathTex(r"V(-2, 5)", font_size=13.5, color=THEME["highlight"]).next_to(dot_v, UP, buff=0.10)

        # Puntos de control P1(-1, -1) y P2(-3, -1)
        dot_p1 = Dot(axes.c2p(-1.0, -1.0), radius=0.06, color=THEME["success"])
        lbl_p1 = MathTex(r"(-1, -1)", font_size=12.5, color=THEME["success"]).next_to(dot_p1, RIGHT, buff=0.08)

        dot_p2 = Dot(axes.c2p(-3.0, -1.0), radius=0.06, color=THEME["success"])
        lbl_p2 = MathTex(r"(-3, -1)", font_size=12.5, color=THEME["success"]).next_to(dot_p2, LEFT, buff=0.08)

        # Vértice base (0, 0)
        dot_origin = Dot(axes.c2p(0.0, 0.0), radius=0.055, color=THEME["statement_text"])

        prog_anims = self.get_advance_progress_anims(7)

        self.play(
            FadeOut(self.active_math),
            FadeOut(self.active_just),
            FadeOut(self.active_box),
            FadeIn(left_summary),
            Create(box8),
            Create(axes),
            Write(axes_labels),
            *prog_anims,
            run_time=1.8
        )
        self.active_box = box8
        self.active_math = left_summary
        self.active_just = None

        self.play(
            Create(curve_f),
            Write(lbl_f),
            FadeIn(dot_origin),
            Create(sym_line),
            Write(lbl_sym),
            Create(curve_g),
            Write(lbl_g),
            FadeIn(dot_v),
            Write(lbl_v),
            FadeIn(dot_p1),
            Write(lbl_p1),
            FadeIn(dot_p2),
            Write(lbl_p2),
            run_time=2.4
        )
        self.wait(8.0)

        # Cierre institucional
        graph_group = VGroup(
            axes, axes_labels,
            curve_f, lbl_f, dot_origin,
            sym_line, lbl_sym,
            curve_g, lbl_g,
            dot_v, lbl_v,
            dot_p1, lbl_p1,
            dot_p2, lbl_p2
        )
        self.play(
            FadeOut(graph_group),
            FadeOut(self.active_math),
            FadeOut(self.active_box),
            run_time=1.4
        )
        self.wait(1.0)
