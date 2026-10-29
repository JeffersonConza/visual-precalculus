r"""
Precálculo Universitario · Tutorías Annelisse / Editorial Amarun
Capítulo: Funciones Reales y Gráficas
Ejercicio 2.a: Análisis Formal y Gráfica de Función Cuadrática
               f(x) = 5x² + 2x + 1

Propiedades solicitadas (100% Precálculo Universitario - Sin Derivadas):
  1. Positividad y negatividad (análisis de signos por discriminante y forma canónica)
  2. Cortes con los ejes coordenados (eje X por resolvente y eje Y con punto simétrico)
  3. Simetría y paridad (f(-x) vs f(x) y eje de simetría axial x = -b/(2a))
  4. Monotonía formal por desigualdades (estrictamente decreciente y creciente a cada lado del vértice)
  + Vértice, concavidad, rango y trazado cartesiano de alta precisión.

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica en 8 pasos con tipografía HD generosa y legible.
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


class EjercicioAnn_02(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Annelisse",
            exercise="Ejercicio 2.a",
            topic="Análisis Formal y Gráfica de Parábola",
            font_size=17.0
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 2.a: Analice formalmente (signos, cortes, simetría y monotonía) y grafique:",
            math_tex=r"{\color{amteal}f(x) = 5x^2 + 2x + 1}, \quad x \in \mathbb{R}",
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
            "1/8: Concavidad y Vértice",
            "2/8: Cortes con los Ejes",
            "3/8: Simetría y Paridad",
            "4/8: Signos y Positividad",
            "5/8: Monotonía por Inecuaciones",
            "6/8: Dominio y Rango",
            "7/8: Síntesis de Propiedades",
            "8/8: Trazado Cartesiano"
        ], dot_spacing=0.82, label_font_size=14.0)

        # ==========================================================
        # PASO 1: Concavidad y Forma Canónica del Vértice
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Concavidad y Forma Canónica del Vértice:} \\[5pt]"
            r"&\text{Para } f(x) = 5x^2 + 2x + 1 \implies a = 5, \; b = 2, \; c = 1: \\[4pt]"
            r"&\bullet \ \text{Como } a = 5 > 0, \text{ la parábola es } \mathbf{{\color{amgreen}\text{cóncava hacia arriba } (\cup)}}. \\[5pt]"
            r"&\textbf{Completación Canónica de Cuadrados (Precálculo):} \\[4pt]"
            r"&\quad f(x) = 5\left(x^2 + \frac{2}{5}x\right) + 1 = 5\left(x + \frac{1}{5}\right)^2 - \frac{1}{5} + 1 \\[5pt]"
            r"&\quad \mathbf{f(x) = 5(x + 0.2)^2 + 0.8} \quad \left(a(x - h)^2 + k\right) \\[6pt]"
            r"&\therefore \quad \text{Vértice Mínimo Absoluto: } \mathbf{{\color{amgold}V(-0.2, \; 0.8)}} \quad (V(-1/5, \; 4/5))"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Parábola y Vértice:}\\[6pt]"
            r"$\bullet$ El coeficiente $a = 5 > 0$ determina que la curva abre hacia arriba ($\cup$).\\[5pt]"
            r"$\bullet$ Por completación de cuadrados se obtiene la forma canónica:\\"
            r"\hspace*{1.0em}$f(x) = 5(x + 0.2)^2 + 0.8$.\\[5pt]"
            r"$\bullet$ Como $(x + 0.2)^2 \ge 0$, el valor mínimo absoluto ocurre exactamente cuando el cuadrado se anula ($x = -0.2$).\\[5pt]"
            r"$\bullet$ Vértice extremo: ${\color{amgold}V(-0.2, \; 0.8)}$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=3.6)

        # ==========================================================
        # PASO 2: Cortes con los Ejes Coordenados
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Cortes con los Ejes Coordenados:} \\[5pt]"
            r"&\bullet \ \textbf{Corte con el Eje } Y \; (x = 0): \\[3pt]"
            r"&\quad f(0) = 5(0)^2 + 2(0) + 1 = 1 \implies \mathbf{{\color{amteal}P_y(0, \; 1)}} \\[5pt]"
            r"&\bullet \ \textbf{Punto Simétrico Reflejo } (x = -0.4): \\[3pt]"
            r"&\quad f(-0.4) = 5(-0.4)^2 + 2(-0.4) + 1 = 1 \implies \mathbf{{\color{amteal}P_{\text{sym}}(-0.4, \; 1)}} \\[5pt]"
            r"&\bullet \ \textbf{Cortes con el Eje } X \; (y = 0): \\[3pt]"
            r"&\quad 5x^2 + 2x + 1 = 0 \implies \Delta = b^2 - 4ac \\[4pt]"
            r"&\quad \Delta = 2^2 - 4(5)(1) = 4 - 20 = \mathbf{{\color{amred}-16 < 0}} \\[6pt]"
            r"&\therefore \quad \text{Sin ceros reales: } \mathbf{{\color{amred}\text{Cortes } X = \emptyset}} \quad (\text{No corta al eje } X)"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Intersecciones con los Ejes:}\\[6pt]"
            r"$\bullet$ El corte con el eje $Y$ se halla evaluando en $x = 0$: $P_y(0, 1)$.\\[5pt]"
            r"$\bullet$ Por simetría axial respecto a $x = -0.2$, existe el punto homólogo $P_{\text{sym}}(-0.4, 1)$.\\[5pt]"
            r"$\bullet$ El discriminante $\Delta = -16 < 0$ demuestra analíticamente que no existen raíces reales.\\[5pt]"
            r"$\bullet$ La parábola flota enteramente por encima del eje horizontal ($y \ge 0.8 > 0$)."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=3.6)

        # ==========================================================
        # PASO 3: Simetría y Paridad Funcional
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Simetría y Paridad Funcional:} \\[5pt]"
            r"&\bullet \ \textbf{Evaluación de Paridad General } f(-x): \\[3pt]"
            r"&\quad f(-x) = 5(-x)^2 + 2(-x) + 1 = 5x^2 - 2x + 1 \\[4pt]"
            r"&\quad \text{Como } 5x^2 - 2x + 1 \ne \pm(5x^2 + 2x + 1): \\[3pt]"
            r"&\quad \implies \mathbf{f(-x) \ne f(x)} \quad \text{y} \quad \mathbf{f(-x) \ne -f(x)} \\[4pt]"
            r"&\quad \therefore \ \mathbf{{\color{amorange}\text{No es función par ni impar}}} \quad (\text{Sin simetría con } Y \text{ ni con } (0,0)) \\[6pt]"
            r"&\bullet \ \textbf{Eje de Simetría Axial de la Parábola:} \\[3pt]"
            r"&\quad \text{Recta vertical canónica: } \mathbf{{\color{amgreen}x = h = -0.2}} \\[4pt]"
            r"&\quad \text{Demostración: } \forall u \in \mathbb{R}: \; \mathbf{f(-0.2 + u) = f(-0.2 - u) = 5u^2 + 0.8}"
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{3. Simetría y Paridad:}\\[6pt]"
            r"$\bullet$ El término lineal $2x$ destruye la paridad global respecto a los ejes principales.\\[5pt]"
            r"$\bullet$ La función no es ni par ni impar.\\[5pt]"
            r"$\bullet$ No obstante, posee simetría axial respecto a su propio eje vertical:\\"
            r"\hspace*{1.0em}${\color{amgreen}x = -0.2}$.\\[5pt]"
            r"$\bullet$ Puntos equidistantes al eje comparten la misma altura: $f(-0.2 \pm u) = 5u^2 + 0.8$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq3, just3, box_color=THEME["statement_box"], advance_to_step=2, wait_time=3.6)

        # ==========================================================
        # PASO 4: Positividad y Negatividad (Signos)
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Positividad y Negatividad } (C^+, \; C^-): \\[5pt]"
            r"&\bullet \ \textbf{Teorema del Signo del Trinomio Cuadrático:} \\[3pt]"
            r"&\quad \text{Dado } f(x) = ax^2 + bx + c \text{ con } \Delta < 0: \\[3pt]"
            r"&\quad \operatorname{signo}(f(x)) = \operatorname{signo}(a) \quad \forall x \in \mathbb{R} \\[4pt]"
            r"&\quad \text{Como } a = 5 > 0 \text{ y } \Delta = -16 < 0 \implies \mathbf{{\color{amgreen}f(x) > 0, \quad \forall x \in \mathbb{R}}} \\[5pt]"
            r"&\bullet \ \textbf{Demostración Canónica Directa (Precálculo):} \\[3pt]"
            r"&\quad f(x) = 5(x + 0.2)^2 + 0.8 \ge 0.8 > 0, \quad \forall x \in \mathbb{R} \\[6pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}\text{Positividad: } C^+ = \mathbb{R} = (-\infty, \; +\infty)}} \\[4pt]"
            r"&\quad \quad \mathbf{{\color{amred}\text{Negatividad: } C^- = \emptyset}}, \quad \mathbf{{\color{amgold}\text{Ceros: } C^0 = \emptyset}}"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Signos de la Función:}\\[6pt]"
            r"$\bullet$ Al ser $\Delta < 0$, la parábola no cruza el eje $X$.\\[5pt]"
            r"$\bullet$ Por la forma canónica $5(x+0.2)^2 + 0.8$, todo término es suma de un cuadrado no negativo y un número estrictamente positivo ($0.8 > 0$).\\[5pt]"
            r"$\bullet$ La función es estrictamente positiva en todos los reales:\\[3pt]"
            r"\hspace*{1.0em}$C^+ = \mathbb{R}$ y $C^- = \emptyset$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq4, just4, box_color=THEME["success"], advance_to_step=3, wait_time=3.6)

        # ==========================================================
        # PASO 5: Monotonía por Inecuaciones (100% Precálculo - Sin Derivadas)
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Monotonía Formal por Inecuaciones (Precálculo):} \\[5pt]"
            r"&\text{El eje de simetría } x = -0.2 \text{ define los dos intervalos monótonos:} \\[5pt]"
            r"&\bullet \ \textbf{Rama Izquierda } (-\infty, \; -0.2]: \text{ Sean } x_1 < x_2 \le -0.2: \\[3pt]"
            r"&\quad x_1 + 0.2 < x_2 + 0.2 \le 0 \implies (x_1 + 0.2)^2 > (x_2 + 0.2)^2 \\[4pt]"
            r"&\quad \implies 5(x_1 + 0.2)^2 + 0.8 > 5(x_2 + 0.2)^2 + 0.8 \iff \mathbf{f(x_1) > f(x_2)} \\[4pt]"
            r"&\quad \therefore \ \mathbf{{\color{amorange}\text{Estrictamente Decreciente en: } \left(-\infty, \; -0.2\right]}} \\[6pt]"
            r"&\bullet \ \textbf{Rama Derecha } [-0.2, \; +\infty): \text{ Sean } -0.2 \le x_1 < x_2: \\[3pt]"
            r"&\quad 0 \le x_1 + 0.2 < x_2 + 0.2 \implies (x_1 + 0.2)^2 < (x_2 + 0.2)^2 \\[4pt]"
            r"&\quad \implies 5(x_1 + 0.2)^2 + 0.8 < 5(x_2 + 0.2)^2 + 0.8 \iff \mathbf{f(x_1) < f(x_2)} \\[4pt]"
            r"&\quad \therefore \ \mathbf{{\color{amgreen}\text{Estrictamente Creciente en: } \left[-0.2, \; +\infty\right)}}"
            r"\end{aligned}",
            font_size=19.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Monotonía sin Derivadas:}\\[6pt]"
            r"$\bullet$ En Precálculo, la monotonía se prueba mediante la definición formal de desigualdades.\\[5pt]"
            r"$\bullet$ Al elevar números negativos al cuadrado, la desigualdad se invierte ($u < v \le 0 \implies u^2 > v^2$), lo que demuestra que la función decrece antes del vértice.\\[5pt]"
            r"$\bullet$ Al elevar números positivos, el orden se preserva, demostrando que crece después del vértice.\\[5pt]"
            r"$\bullet$ Demostración $100\%$ algebraica."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq5, just5, box_color=THEME["error"], advance_to_step=4, wait_time=3.6)

        # ==========================================================
        # PASO 6: Dominio, Rango y Extremo Absoluto
        # ==========================================================
        eq6 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Dominio, Rango y Extremo Global:} \\[5pt]"
            r"&\bullet \ \textbf{Dominio Natural:} \\[3pt]"
            r"&\quad \text{Por ser un polinomio cuadrático entero: } \mathbf{{\color{amgold}\operatorname{Dom}(f) = \mathbb{R}}} \\[5pt]"
            r"&\bullet \ \textbf{Deducción Formal del Rango por Inecuaciones:} \\[3pt]"
            r"&\quad \forall x \in \mathbb{R}: \quad (x + 0.2)^2 \ge 0 \implies 5(x + 0.2)^2 \ge 0 \\[4pt]"
            r"&\quad \implies 5(x + 0.2)^2 + 0.8 \ge 0.8 \iff \mathbf{{\color{amgreen}f(x) \ge 0.8}} \\[5pt]"
            r"&\quad \text{Despeje de existencia en } \mathbb{R}: \; (x + 0.2)^2 = \frac{y - 0.8}{5} \ge 0 \iff y \ge 0.8 \\[6pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}\operatorname{Ran}(f) = [0.8, \; +\infty) = \left[\frac{4}{5}, \; +\infty\right)}} \\[4pt]"
            r"&\quad \quad \text{Mínimo Absoluto Global: } \mathbf{m = 0.8} \text{ en } V(-0.2, \; 0.8)"
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{6. Recorrido o Rango:}\\[6pt]"
            r"$\bullet$ El dominio de cualquier función polinómica cuadrática es todo $\mathbb{R}$.\\[5pt]"
            r"$\bullet$ La cota inferior estricta es el valor del vértice $y = 0.8$, alcanzable en $x = -0.2$.\\[5pt]"
            r"$\bullet$ Al despejar $x$, la condición de existencia de la raíz real exige $y \ge 0.8$.\\[5pt]"
            r"$\bullet$ Rango final: ${\color{amgreen}\operatorname{Ran}(f) = [0.8, \; +\infty)}$.\\[5pt]"
            r"$\bullet$ La parábola no tiene máximo global."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq6, just6, box_color=THEME["statement_box"], advance_to_step=5, wait_time=3.6)

        # ==========================================================
        # PASO 7: Tabla de Valores y Síntesis Formal
        # ==========================================================
        eq7 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{7. Tabla de Valores Simétricos y Síntesis Formal:} \\[5pt]"
            r"&\begin{array}{|c|c|c|c|c|c|} \hline "
            r"x & -0.9 & \mathbf{-0.4} & \mathbf{-0.2} & \mathbf{0.0} & 0.5 \\ \hline "
            r"f(x) & 3.25 & \mathbf{{\color{amteal}1.0}} & \mathbf{{\color{amgold}0.8}} & \mathbf{{\color{amteal}1.0}} & 3.25 \\ \hline "
            r"\text{Rol} & \text{Control} & \mathbf{P_{\text{sym}}} & \mathbf{\text{Vértice } V} & \mathbf{P_y} & \text{Control} \\ \hline "
            r"\end{array} \\[6pt]"
            r"&\textbf{Resumen de las Propiedades Pedidas:} \\[4pt]"
            r"&\bullet \ \textbf{Positividad / Negatividad:} \; C^+ = \mathbb{R}, \quad C^- = \emptyset, \quad C^0 = \emptyset \\"
            r"&\bullet \ \textbf{Cortes con Ejes:} \; \text{Eje } Y \text{ en } (0, 1); \quad \text{Eje } X \text{ sin corte } (\emptyset) \\"
            r"&\bullet \ \textbf{Simetría:} \; \text{Eje axial } x = -0.2 \quad (\text{Ni par ni impar}) \\"
            r"&\bullet \ \textbf{Monotonía:} \; \text{Decrece en } (-\infty, -0.2], \quad \text{Crece en } [-0.2, +\infty)"
            r"\end{aligned}",
            font_size=18.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{7. Síntesis Deductiva:}\\[6pt]"
            r"$\bullet$ La tabla de valores ilustra la perfecta simetría axial respecto a $x = -0.2$.\\[5pt]"
            r"$\bullet$ Se responden con exactitud las cuatro preguntas del enunciado oficial.\\[5pt]"
            r"$\bullet$ Los puntos $(-0.9, 3.25)$, $(-0.4, 1)$, $(-0.2, 0.8)$, $(0, 1)$ y $(0.5, 3.25)$ permiten un trazado geométrico exacto.\\[5pt]"
            r"$\bullet$ Paso final: construcción cartesiana."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq7, just7, box_color=THEME["highlight"], advance_to_step=6, wait_time=3.6)

        # ==========================================================
        # PASO 8: Trazado Cartesiano de Precisión
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(7)

        # Panel izquierdo: Resumen geométrico
        t_card = Tex(
            r"\begin{minipage}{5.8cm}\raggedright "
            r"\textbf{{\color{amteal}Verificación Cartesiana:}}\\[6pt]"
            r"$\bullet$ \textbf{Parábola Cóncava } ($\cup$):\\[2pt]"
            r"\hspace*{0.8em}$f(x) = 5(x + 0.2)^2 + 0.8$.\\[5pt]"
            r"$\bullet$ \textbf{Vértice Mínimo:}\\[2pt]"
            r"\hspace*{0.8em}$V(-0.2, \; 0.8)$ \textbf{Punto Global} ($\bullet$).\\[5pt]"
            r"$\bullet$ \textbf{Eje de Simetría:}\\[2pt]"
            r"\hspace*{0.8em}Recta vertical $x = -0.2$.\\[5pt]"
            r"$\bullet$ \textbf{Corte } $Y$ \textbf{y Simétrico:}\\[2pt]"
            r"\hspace*{0.8em}$P_y(0, 1)$ y $P_{\text{sym}}(-0.4, 1)$.\\[5pt]"
            r"$\bullet$ \textbf{Rango Proyectado:}\\[2pt]"
            r"\hspace*{0.8em}$[0.8, \; +\infty)$ sobre el eje $Y$."
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
            x_range=[-1.6, 1.4, 0.5],
            y_range=[-0.5, 4.0, 1.0],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=12,
            labels_font_size=19
        )

        # Eje de simetría vertical x = -0.2
        sym_line = DashedLine(
            start=axes.c2p(-0.2, 0.8),
            end=axes.c2p(-0.2, 3.8),
            color=THEME["highlight"],
            dash_length=0.08,
            stroke_width=2.0
        )
        sym_lbl = MathTex(
            r"x = -0.2",
            font_size=11.5,
            color=THEME["highlight"]
        ).next_to(axes.c2p(-0.2, 3.8), UP, buff=0.06)

        # Curva de la parábola f(x) = 5x^2 + 2x + 1
        curve_f = axes.plot(
            lambda x: 5.0 * x**2 + 2.0 * x + 1.0,
            x_range=[-0.96, 0.56, 0.02],
            color=THEME["amarun_teal"],
            stroke_width=4.0
        )
        lbl_f = MathTex(
            r"f(x) = 5x^2 + 2x + 1",
            font_size=13.0,
            color=THEME["amarun_teal"]
        ).next_to(axes.c2p(0.55, 3.3), UR, buff=0.06)

        # Vértice V(-0.2, 0.8)
        p_v = axes.c2p(-0.2, 0.8)
        dot_v = Dot(p_v, radius=0.075, color=THEME["highlight"])
        lbl_v = MathTex(
            r"V(-0.2, 0.8)",
            font_size=11.5,
            color=THEME["highlight"]
        ).next_to(p_v, DOWN, buff=0.08)

        # Corte Y (0, 1) y Punto Simétrico (-0.4, 1)
        p_y = axes.c2p(0.0, 1.0)
        dot_y = Dot(p_y, radius=0.065, color=THEME["secondary"])
        lbl_y = MathTex(
            r"P_y(0, 1)",
            font_size=11.0,
            color=THEME["secondary"]
        ).next_to(p_y, RIGHT, buff=0.08)

        p_sym = axes.c2p(-0.4, 1.0)
        dot_sym = Dot(p_sym, radius=0.065, color=THEME["secondary"])
        lbl_sym = MathTex(
            r"P_{\text{sym}}(-0.4, 1)",
            font_size=11.0,
            color=THEME["secondary"]
        ).next_to(p_sym, LEFT, buff=0.08)

        # Puntos de control (0.5, 3.25) y (-0.9, 3.25)
        dot_p1 = Dot(axes.c2p(0.5, 3.25), radius=0.055, color=THEME["amarun_teal"])
        dot_p2 = Dot(axes.c2p(-0.9, 3.25), radius=0.055, color=THEME["amarun_teal"])

        # Proyección del rango sobre el eje vertical [0.8, 3.8]
        range_line = Line(
            axes.c2p(-1.6, 0.8),
            axes.c2p(-1.6, 3.8),
            color=THEME["success"],
            stroke_width=5.0
        )
        dot_r_bottom = Dot(axes.c2p(-1.6, 0.8), radius=0.065, color=THEME["success"])
        lbl_range = MathTex(
            r"\operatorname{Ran}=[0.8, +\infty)",
            font_size=11.5,
            color=THEME["success"]
        ).next_to(axes.c2p(-1.6, 2.3), RIGHT, buff=0.10)

        # Transición hacia el paso 8
        self.play(
            FadeOut(self.active_box),
            FadeOut(self.active_math, shift=DOWN * 0.2),
            FadeOut(self.active_just, shift=DOWN * 0.2),
            FadeIn(info_grp, shift=DOWN * 0.2),
            Create(axes),
            Write(axes_labels),
            *prog_anims,
            run_time=1.8
        )
        self.active_box = None
        self.active_math = None
        self.active_just = None

        # Trazado de la parábola y eje de simetría
        self.play(
            Create(curve_f), Write(lbl_f),
            Create(sym_line), Write(sym_lbl),
            run_time=2.2
        )

        # Puntos notables y proyección del rango
        self.play(
            FadeIn(dot_v), Write(lbl_v),
            FadeIn(dot_y), Write(lbl_y),
            FadeIn(dot_sym), Write(lbl_sym),
            FadeIn(dot_p1), FadeIn(dot_p2),
            Create(range_line), FadeIn(dot_r_bottom), Write(lbl_range),
            run_time=1.8
        )
        self.wait(4.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            sym_line, sym_lbl, curve_f, lbl_f,
            dot_v, lbl_v, dot_y, lbl_y, dot_sym, lbl_sym,
            dot_p1, dot_p2,
            range_line, dot_r_bottom, lbl_range
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
