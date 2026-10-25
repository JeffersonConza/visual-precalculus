"""
Ejercicio 6 - Tutorías y Preparación Quiz 4 (Jhoselyn)
Tema: Análisis Completo y Gráfica de Funciones:
      Función Racional Par con Extremos Locales: f(x) = (x^2 - 9) / (x^2 - 1).
      Dominio, paridad par, simetría axial bilateral eje Y, cortes coordenados,
      tabla de signos por factores, asíntotas verticales x = ±1, asíntota horizontal y = 1,
      monotonía, mínimo local en M(0, 9), rango (-∞, 1) U [9, +∞),
      cuadro resumen de puntos críticos/notables y trazado cartesiano de 3 ramas.

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica en 8 pasos con ecuaciones en LaTeX de gran legibilidad.
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


class EjercicioJh_06(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Jhoselyn",
            exercise="Ejercicio 6",
            topic="Función Racional y Extremos Locales",
            font_size=16.5
        )

        # 2. Enunciado institucional permanente con fórmula prominente (y = 2.65)
        self.setup_statement(
            desc_text="Analice completamente y grafique la función racional par:",
            math_tex=r"{\color{amteal}f(x)} = \frac{{\color{amteal}x^2 - 9}}{{\color{amred}x^2 - 1}}",
            desc_font_size=18.5,
            math_font_size=30.0,
            box_pos=np.array([0.0, 2.65, 0.0]),
            read_time=3.5
        )

        # 3. Barra de Progreso Interactiva (8 pasos detallados)
        self.setup_progress_bar([
            "1/8: Dominio y Restricciones",
            "2/8: Paridad y Simetría",
            "3/8: Cortes con los Ejes",
            "4/8: Tabla de Signos",
            "5/8: Asíntotas V. y H.",
            "6/8: Monotonía y Extremos",
            "7/8: Cuadro de Puntos Notables",
            "8/8: Gráfica Cartesiana y Verificación"
        ], dot_spacing=0.82, label_font_size=14.0)

        # ==========================================================
        # PASO 1 (C2): Dominio y Restricciones del Denominador
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Dominio y Restricciones:} \\[5pt]"
            r"&\text{Al ser una función racional, el denominador no se anula:} \\[4pt]"
            r"&x^2 - 1 \neq 0 \iff (x - 1)(x + 1) \neq 0 \implies x \neq \pm 1 \\[6pt]"
            r"&\mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R} \setminus \{-1, 1\}}} \\[5pt]"
            r"&\mathbf{\operatorname{Dom}(f) = {\color{amgreen}(-\infty, -1) \cup (-1, 1) \cup (1, +\infty)}} \\[6pt]"
            r"&\implies \text{El plano queda dividido en } \mathbf{3 \text{ ramas continuas}}."
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{1. Dominio y Restricciones:}\\[6pt]"
            r"$\bullet$ Toda fracción exige denominador no nulo:\\[3pt]"
            r"\hspace*{1.2em}$x^2 - 1 \neq 0 \implies x \neq -1 \quad \text{y} \quad x \neq 1$.\\[5pt]"
            r"$\bullet$ El dominio excluye ambos puntos:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgold}\operatorname{Dom}(f) = \mathbb{R} \setminus \{-1, 1\}}$.\\[5pt]"
            r"$\bullet$ La gráfica presenta 3 ramas continuas:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgreen}(-\infty, -1)}, \quad {\color{amgreen}(-1, 1)} \quad \text{y} \quad {\color{amgreen}(1, +\infty)}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=3.2)

        # ==========================================================
        # PASO 2: Paridad y Simetría Axial
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Paridad y Simetría:} \\[5pt]"
            r"&\text{Evaluamos formalmente el valor de } f(-x): \\[4pt]"
            r"&f(-x) = \frac{(-x)^2 - 9}{(-x)^2 - 1} = \frac{x^2 - 9}{x^2 - 1} = f(x) \\[6pt]"
            r"&\implies \mathbf{{\color{amteal}f(-x) = f(x)}} \implies \mathbf{\text{Función PAR}} \\[6pt]"
            r"&\implies \text{Presenta } \mathbf{\text{Simetría Axial respecto al eje vertical }} Y \\[5pt]"
            r"&\implies \text{Si } (x, y) \in f \implies (-x, y) \in f \text{ (reflejo especular)}."
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{2. Paridad y Simetría:}\\[6pt]"
            r"$\bullet$ Al sustituir $-x$, todos los exponentes son pares:\\[3pt]"
            r"\hspace*{1.2em}$(-x)^2 = x^2 \implies f(-x) = f(x)$.\\[5pt]"
            r"$\bullet$ Concluimos formalmente: ${\color{amteal}f \text{ es una función PAR}}$.\\[5pt]"
            r"$\bullet$ Presenta simetría axial bilateral respecto al eje $Y$.\\[5pt]"
            r"$\bullet$ La rama en $x < -1$ es el reflejo exacto de la rama en $x > 1$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq2, just2, box_color=THEME["highlight"], advance_to_step=1, wait_time=3.2)

        # ==========================================================
        # PASO 3: Intersecciones con los Ejes Coordenados
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Intersecciones con los Ejes Coordenados:} \\[5pt]"
            r"&\bullet \textbf{Intercepto vertical } (x = 0): \\[3pt]"
            r"&\quad f(0) = \frac{0^2 - 9}{0^2 - 1} = \frac{-9}{-1} = 9 \implies \mathbf{{\color{amteal}P_y = (0, 9)}} \\[6pt]"
            r"&\bullet \textbf{Interceptos horizontales } (f(x) = 0): \\[3pt]"
            r"&\quad \frac{x^2 - 9}{x^2 - 1} = 0 \iff x^2 - 9 = 0 \iff (x - 3)(x + 3) = 0 \\[5pt]"
            r"&\quad \mathbf{{\color{amorange}x_1 = -3}}, \quad \mathbf{{\color{amorange}x_2 = 3}} \\[4pt]"
            r"&\quad \text{Puntos: } {\color{amorange}P_{x_1}(-3, 0)} \quad \text{y} \quad {\color{amorange}P_{x_2}(3, 0)}."
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{3. Cortes Coordenados:}\\[6pt]"
            r"$\bullet$ Corte con el eje vertical $Y$ ($x = 0$):\\[3pt]"
            r"\hspace*{1.2em}$f(0) = \frac{-9}{-1} = 9 \implies {\color{amteal}P_y(0, 9)}$.\\[5pt]"
            r"$\bullet$ Cortes con el eje horizontal $X$ ($f(x) = 0$):\\[3pt]"
            r"\hspace*{1.2em}Se anula cuando el numerador es cero: $x^2 - 9 = 0$.\\[5pt]"
            r"$\bullet$ Dos raíces simétricas en el plano:\\[3pt]"
            r"\hspace*{1.2em}${\color{amorange}x = -3} \quad \text{y} \quad {\color{amorange}x = 3}$.\\[5pt]"
            r"$\bullet$ Puntos: ${\color{amorange}P_{x_1}(-3, 0)}$ y ${\color{amorange}P_{x_2}(3, 0)}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=3.2)

        # ==========================================================
        # PASO 4: Factorización y Tabla de Signos
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Factorización y Tabla de Signos:} \\[4pt]"
            r"&{\color{amteal}f(x)} = \frac{(x + 3)(x - 3)}{(x + 1)(x - 1)}, \quad \text{Ceros/Polos: } \{{\color{amorange}-3, -1, 1, 3}\} \\[5pt]"
            r"&\bullet (-\infty, -3): \; \tfrac{(-)(-)}{(-)(-)} = {\color{amgreen}\mathbf{(+)}} > 0 \quad \bullet (-3, -1): \; \tfrac{(+)(-)}{(-)(-)} = {\color{amred}\mathbf{(-)}} < 0 \\[4pt]"
            r"&\bullet (-1, 1): \; \tfrac{(+)(-)}{(+)(-)} = {\color{amgreen}\mathbf{(+)}} > 0 \quad \bullet (1, 3): \; \tfrac{(+)(-)}{(+)(+)} = {\color{amred}\mathbf{(-)}} < 0 \\[4pt]"
            r"&\bullet (3, +\infty): \; \tfrac{(+)(+)}{(+)(+)} = {\color{amgreen}\mathbf{(+)}} > 0 \\[5pt]"
            r"&\mathbf{\text{Positiva: } {\color{amgreen}(-\infty, -3) \cup (-1, 1) \cup (3, +\infty)}} \\[4pt]"
            r"&\mathbf{\text{Negativa: } {\color{amred}(-3, -1) \cup (1, 3)}}."
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{4. Intervalos de Signo:}\\[6pt]"
            r"$\bullet$ Los 4 valores clave particionan la recta en 5 intervalos.\\[4pt]"
            r"$\bullet$ Signo en cada región evaluando los factores:\\[3pt]"
            r"\hspace*{1.2em}$(+), \quad (-), \quad (+), \quad (-), \quad (+)$.\\[5pt]"
            r"$\bullet$ Regiones sobre el eje horizontal ($f > 0$):\\[3pt]"
            r"\hspace*{1.2em}${\color{amgreen}(-\infty, -3) \cup (-1, 1) \cup (3, +\infty)}$.\\[5pt]"
            r"$\bullet$ Regiones bajo el eje horizontal ($f < 0$):\\[3pt]"
            r"\hspace*{1.2em}${\color{amred}(-3, -1) \cup (1, 3)}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=3.2)

        # ==========================================================
        # PASO 5: Asíntotas Verticales y Horizontal
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Asíntotas Verticales y Horizontal:} \\[4pt]"
            r"&\bullet \textbf{Asíntotas Verticales (A.V.): } \mathbf{{\color{amred}x = -1}} \quad \text{y} \quad \mathbf{{\color{amred}x = 1}} \\[3pt]"
            r"&\quad \lim_{x \to 1^-} f(x) = +\infty, \quad \lim_{x \to 1^+} f(x) = -\infty \\[4pt]"
            r"&\quad \lim_{x \to -1^+} f(x) = +\infty, \quad \lim_{x \to -1^-} f(x) = -\infty \\[5pt]"
            r"&\bullet \textbf{Asíntota Horizontal (A.H.): } \text{Grado}(N) = \text{Grado}(D) = 2 \\[3pt]"
            r"&\quad \lim_{x \to \pm\infty} \frac{x^2 - 9}{x^2 - 1} = \frac{1}{1} \implies \mathbf{{\color{amgold}y = 1}} \\[4pt]"
            r"&\bullet \textbf{Cruce con A.H.: } \frac{x^2 - 9}{x^2 - 1} = 1 \implies -9 = -1 \text{ (Falso, no corta)}."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{5. Asíntotas del Sistema:}\\[6pt]"
            r"$\bullet$ Asíntotas Verticales en los polos irreducibles:\\[3pt]"
            r"\hspace*{1.2em}${\color{amred}x = -1} \quad \text{y} \quad {\color{amred}x = 1}$.\\[5pt]"
            r"$\bullet$ La rama central diverge a $+\infty$ por ambos lados.\\[5pt]"
            r"$\bullet$ Grados iguales en numerador y denominador:\\[3pt]"
            r"\hspace*{1.2em}Cociente de coeficientes principales: ${\color{amgold}y = 1}$.\\[5pt]"
            r"$\bullet$ La curva jamás cruza su asíntota horizontal $y = 1$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=3.2)

        # ==========================================================
        # PASO 6: Monotonía, Extremos Locales y Rango
        # ==========================================================
        eq6 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Monotonía, Extremos Locales y Rango:} \\[4pt]"
            r"&\bullet \textbf{Primera derivada formal } f'(x): \\[3pt]"
            r"&\quad f'(x) = \frac{2x(x^2 - 1) - (x^2 - 9)(2x)}{(x^2 - 1)^2} = \mathbf{\frac{16x}{(x^2 - 1)^2}} \\[5pt]"
            r"&\bullet \textbf{Punto Crítico } (f'(x) = 0): 16x = 0 \implies \mathbf{{\color{amteal}x = 0}} \\[4pt]"
            r"&\quad \bullet x < 0 \; (x \neq -1): {\color{amred}f'(x) < 0} \implies \text{Estrictamente Decreciente} \\[3pt]"
            r"&\quad \bullet x > 0 \; (x \neq 1): {\color{amgreen}f'(x) > 0} \implies \text{Estrictamente Creciente} \\[4pt]"
            r"&\implies \mathbf{\text{Mínimo Local en } {\color{amteal}M(0, 9)}} \text{ (vértice de rama central)} \\[5pt]"
            r"&\implies \mathbf{\operatorname{Ran}(f) = {\color{amgold}(-\infty, 1) \cup [9, +\infty)}}."
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{6. Monotonía y Rango:}\\[6pt]"
            r"$\bullet$ Derivada del cociente:\\[3pt]"
            r"\hspace*{1.2em}$f'(x) = \frac{16x}{(x^2 - 1)^2}$.\\[5pt]"
            r"$\bullet$ Como el denominador al cuadrado es positivo, el signo de $f'$ es el signo de $x$.\\[5pt]"
            r"$\bullet$ En $x = 0$, $f'$ cambia de $-$ a $+$:\\[3pt]"
            r"\hspace*{1.2em}${\color{amteal}M(0, 9)}$ es un ${\color{amteal}\textbf{Mínimo Local}}$.\\[5pt]"
            r"$\bullet$ Rango con franja prohibida en $[1, 9)$:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgold}\operatorname{Ran}(f) = (-\infty, 1) \cup [9, +\infty)}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq6, just6, box_color=THEME["highlight"], advance_to_step=5, wait_time=3.2)

        # ==========================================================
        # PASO 7: Cuadro de Puntos Críticos y Notables
        # ==========================================================
        eq7 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{7. Cuadro de Puntos Críticos y Notables:} \\[5pt]"
            r"&\begin{array}{|c|c|c|l|}"
            r"\hline"
            r"\mathbf{x} & \mathbf{f(x)} & \mathbf{\text{Signo } f'} & \mathbf{\text{Rol y Comportamiento Gráfico}} \\ \hline"
            r"-3 & 0 & f' < 0 & \text{Corte eje } X_1(-3, 0) \text{ (decrece hacia } -\infty) \\"
            r"-1 & \pm\infty & \nexists & \text{Asíntota Vertical } x = -1 \text{ (polo lateral)} \\"
            r"0 & 9 & f' = 0 & \mathbf{\text{Mínimo Local }} {\color{amteal}M(0, 9)} \text{ (vértice central)} \\"
            r"1 & \pm\infty & \nexists & \text{Asíntota Vertical } x = 1 \text{ (polo lateral)} \\"
            r"3 & 0 & f' > 0 & \text{Corte eje } X_2(3, 0) \text{ (crece hacia } 1) \\ \hline"
            r"\end{array} \\[6pt]"
            r"&\bullet \text{Rama izquierda } (-\infty, -1): \text{Decrece de } 1 \text{ pasando por } (-3, 0) \text{ a } -\infty. \\[3pt]"
            r"&\bullet \text{Rama central } (-1, 1): \text{Forma de U con mínimo en } (0, 9), \text{ sube a } +\infty. \\[3pt]"
            r"&\bullet \text{Rama derecha } (1, +\infty): \text{Sube de } -\infty \text{ pasando por } (3, 0) \text{ hacia } 1."
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{7. Síntesis Pre-Graficación:}\\[6pt]"
            r"$\bullet$ La tabla consolida en orden de izquierda a derecha todos los puntos clave.\\[5pt]"
            r"$\bullet$ Muestra la transición de signos de $f'(x)$ y los polos de discontinuidad.\\[5pt]"
            r"$\bullet$ Confirma la simetría par respecto al eje $Y$ entre los puntos $\pm 3$ y $\pm 1$.\\[5pt]"
            r"$\bullet$ Proporciona las coordenadas exactas para el trazado cartesiano riguroso."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq7, just7, box_color=THEME["highlight"], advance_to_step=6, wait_time=3.6)

        # ==========================================================
        # PASO 8: Gráfica Cartesiana y Verificación Visual
        # ==========================================================
        left_summary = MathTex(
            r"\begin{aligned}"
            r"&\textbf{8. Resumen Formal de Resultados:} \\[4pt]"
            r"&\bullet \mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R} \setminus \{-1, 1\}}} \\[4pt]"
            r"&\bullet \mathbf{\operatorname{Ran}(f) = {\color{amgold}(-\infty, 1) \cup [9, +\infty)}} \\[4pt]"
            r"&\bullet \mathbf{\text{Paridad: }} {\color{amteal}\text{Par }} (f(-x) = f(x)) \implies \text{Sim. Axial eje } Y \\[4pt]"
            r"&\bullet \mathbf{\text{Asíntotas V.: }} {\color{amred}x = -1}, \quad {\color{amred}x = 1} \\[4pt]"
            r"&\bullet \mathbf{\text{Asíntota Horizontal: }} {\color{amgold}y = 1} \quad (\text{no la corta}) \\[4pt]"
            r"&\bullet \mathbf{\text{Mínimo Local: }} {\color{amteal}M(0, 9)} \text{ (vértice central)} \\[4pt]"
            r"&\bullet \mathbf{\text{Cortes con Ejes: }} {\color{amorange}(-3, 0)}, \; {\color{amorange}(3, 0)}, \; {\color{amteal}(0, 9)} \\[4pt]"
            r"&\bullet \mathbf{\text{Monotonía: }} \text{Decrece en } (-\infty, 0) \setminus \{-1\}, \\[2pt]"
            r"&\quad \text{Crece en } (0, +\infty) \setminus \{1\} \quad {\color{amgreen}\blacksquare}"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        box8 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.18, corner_radius=0.1)

        # Gráfico cartesiano de la función racional con mínimo local
        axes = Axes(
            x_range=[-4.6, 4.6, 2],
            y_range=[-4.0, 13.0, 4],
            x_length=5.1,
            y_length=3.6,
            tips=True,
            axis_config={
                "color": THEME["axes"],
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 14,
                "tip_width": 0.12,
                "tip_height": 0.12,
            }
        ).move_to([3.25, -0.65, 0])
        axes_labels = axes.get_axis_labels(
            x_label=MathTex("x", font_size=18, color=THEME["statement_text"]),
            y_label=MathTex("y", font_size=18, color=THEME["statement_text"])
        )

        graph_title = Tex(
            r"Gráfica de ${\color{amteal}f(x)} = \frac{{\color{amteal}x^2 - 9}}{{\color{amred}x^2 - 1}}$",
            font_size=21.5,
            color=WHITE
        ).move_to([3.25, 1.70, 0])

        # Asíntotas verticales discontinuas (x = -1 y x = 1)
        asymp_v1 = DashedLine(
            axes.c2p(-1.0, -3.8), axes.c2p(-1.0, 12.5),
            dash_length=0.08, color=THEME["poncho_red"], stroke_width=2.0
        )
        lbl_av1 = MathTex(r"x = -1", font_size=13.5, color=THEME["poncho_red"]).next_to(axes.c2p(-1.0, -3.0), LEFT, buff=0.06)

        asymp_v2 = DashedLine(
            axes.c2p(1.0, -3.8), axes.c2p(1.0, 12.5),
            dash_length=0.08, color=THEME["poncho_red"], stroke_width=2.0
        )
        lbl_av2 = MathTex(r"x = 1", font_size=13.5, color=THEME["poncho_red"]).next_to(axes.c2p(1.0, -3.0), RIGHT, buff=0.06)

        # Asíntota horizontal discontinua (y = 1)
        asymp_h = DashedLine(
            axes.c2p(-4.5, 1.0), axes.c2p(4.5, 1.0),
            dash_length=0.08, color=THEME["highlight"], stroke_width=1.8
        )
        lbl_ah = MathTex(r"y = 1", font_size=13.5, color=THEME["highlight"]).next_to(axes.c2p(4.0, 1.0), UP, buff=0.07)

        # 3 Ramas continuas
        branch_left = axes.plot(
            lambda x: (x**2 - 9) / (x**2 - 1),
            x_range=[-4.5, -1.60],
            color=THEME["curve"],
            stroke_width=2.5
        )
        branch_center = axes.plot(
            lambda x: (x**2 - 9) / (x**2 - 1),
            x_range=[-0.52, 0.52],
            color=THEME["curve"],
            stroke_width=2.5
        )
        branch_right = axes.plot(
            lambda x: (x**2 - 9) / (x**2 - 1),
            x_range=[1.60, 4.5],
            color=THEME["curve"],
            stroke_width=2.5
        )
        curve_branches = VGroup(branch_left, branch_center, branch_right)
        curve_lbl = MathTex(r"y = f(x)", font_size=14.0, color=THEME["curve"]).move_to(axes.c2p(-2.8, 2.5))

        # Puntos notables: M(0, 9), P_x1(-3, 0), P_x2(3, 0)
        dot_m = Dot(axes.c2p(0.0, 9.0), radius=0.07, color=THEME["highlight"])
        lbl_m = MathTex(r"M(0, 9)", font_size=12.0, color=THEME["highlight"]).next_to(dot_m, RIGHT, buff=0.06)

        dot_x1 = Dot(axes.c2p(-3.0, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_x1 = MathTex(r"(-3, 0)", font_size=13.0, color=THEME["statement_text"]).next_to(dot_x1, DOWN, buff=0.10)

        dot_x2 = Dot(axes.c2p(3.0, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_x2 = MathTex(r"(3, 0)", font_size=13.0, color=THEME["statement_text"]).next_to(dot_x2, DOWN, buff=0.10)

        prog_anims = self.get_advance_progress_anims(7)

        self.play(
            FadeOut(self.active_math),
            FadeOut(self.active_just),
            FadeOut(self.active_box),
            FadeIn(left_summary),
            Create(box8),
            Create(axes),
            Write(axes_labels),
            Write(graph_title),
            *prog_anims,
            run_time=1.8
        )
        self.active_box = box8
        self.active_math = left_summary
        self.active_just = None

        self.play(
            Create(asymp_v1),
            Write(lbl_av1),
            Create(asymp_v2),
            Write(lbl_av2),
            Create(asymp_h),
            Write(lbl_ah),
            Create(curve_branches),
            Write(curve_lbl),
            FadeIn(dot_m),
            Write(lbl_m),
            FadeIn(dot_x1),
            Write(lbl_x1),
            FadeIn(dot_x2),
            Write(lbl_x2),
            run_time=2.4
        )
        self.wait(8.0)

        # Cierre institucional
        graph_group = VGroup(
            axes, axes_labels, graph_title,
            asymp_v1, lbl_av1, asymp_v2, lbl_av2,
            asymp_h, lbl_ah,
            curve_branches, curve_lbl,
            dot_m, lbl_m,
            dot_x1, lbl_x1,
            dot_x2, lbl_x2
        )
        self.play(
            FadeOut(graph_group),
            FadeOut(self.active_math),
            FadeOut(self.active_box),
            run_time=1.4
        )
        self.wait(1.0)
