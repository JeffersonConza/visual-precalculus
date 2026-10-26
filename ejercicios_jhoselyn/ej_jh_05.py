"""
Ejercicio 5 - Tutorías y Preparación Quiz 4 (Jhoselyn)
Tema: Análisis Completo y Gráfica de Funciones:
      Función Racional Impar con Asíntota Oblicua: f(x) = (x^3 - 4x) / (x^2 - 1).
      Dominio, paridad impar, simetría central en (0, 0), cortes coordenados,
      tabla horizontal de signos (6 columnas), asíntotas verticales x = ±1,
      asíntota oblicua y = x (con corte en (0, 0)), monotonía estrictamente creciente,
      rango R, cuadro horizontal de variación (Vista.webp) y trazado cartesiano de 3 ramas.

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica en 8 pasos con ecuaciones en LaTeX de gran legibilidad.
        Enfoque 100% Precálculo Universitario (sin derivadas).
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


class EjercicioJh_05(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Jhoselyn",
            exercise="Ejercicio 5",
            topic="Función Racional con Asíntota Oblicua",
            font_size=16.5
        )

        # 2. Enunciado institucional permanente con fórmula prominente (y = 2.65)
        self.setup_statement(
            desc_text="Analice y grafique la función racional:",
            math_tex=r"{\color{amteal}f(x)} = \frac{{\color{amteal}x^3 - 4x}}{{\color{amred}x^2 - 1}} \quad \text{\footnotesize (Creciente en su dominio)}",
            desc_font_size=18.0,
            math_font_size=26.0,
            box_pos=np.array([0.0, 2.65, 0.0]),
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (8 pasos detallados)
        self.setup_progress_bar([
            "1/8: Dominio y Ramas",
            "2/8: Paridad y Simetría Impar",
            "3/8: Cortes Coordenados",
            "4/8: Tabla de Signos",
            "5/8: Asíntotas V. y Oblicua",
            "6/8: Monotonía y Rango",
            "7/8: Cuadro de Variación",
            "8/8: Gráfica Cartesiana"
        ], dot_spacing=0.82, label_font_size=14.0)

        # ==========================================================
        # PASO 1: Dominio y Restricciones del Denominador
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Dominio y Restricciones:} \\[5pt]"
            r"&\text{Al ser una función racional, el denominador no se anula:} \\[4pt]"
            r"&x^2 - 1 \neq 0 \iff (x - 1)(x + 1) \neq 0 \implies x \neq \pm 1 \\[6pt]"
            r"&\mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R} \setminus \{-1, 1\}}} \\[5pt]"
            r"&\mathbf{\operatorname{Dom}(f) = {\color{amgreen}(-\infty, -1) \cup (-1, 1) \cup (1, +\infty)}} \\[6pt]"
            r"&\implies \text{El plano queda dividido en } \mathbf{3 \text{ ramas continuas}} \text{ disjuntas.}"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{1. Dominio y Restricciones:}\\[6pt]"
            r"$\bullet$ Toda fracción exige denominador no nulo:\\[3pt]"
            r"\hspace*{1.2em}$x^2 - 1 \neq 0 \implies x \neq -1 \quad \text{y} \quad x \neq 1$.\\[5pt]"
            r"$\bullet$ El dominio excluye ambos polos:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgold}\operatorname{Dom}(f) = \mathbb{R} \setminus \{-1, 1\}}$.\\[5pt]"
            r"$\bullet$ La función se fragmenta en 3 ramas continuas:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgreen}(-\infty, -1)}, \quad {\color{amgreen}(-1, 1)} \quad \text{y} \quad {\color{amgreen}(1, +\infty)}$.\\[5pt]"
            r"$\bullet$ Base fundamental para la ubicación de asíntotas verticales."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=3.2)

        # ==========================================================
        # PASO 2: Paridad y Simetría Impar (Central)
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Paridad y Simetría Impar:} \\[5pt]"
            r"&\text{Evaluamos formalmente el signo de } f(-x): \\[4pt]"
            r"&f(-x) = \frac{(-x)^3 - 4(-x)}{(-x)^2 - 1} = \frac{-x^3 + 4x}{x^2 - 1} = -\frac{x^3 - 4x}{x^2 - 1} \\[6pt]"
            r"&\implies \mathbf{{\color{amteal}f(-x) = -f(x)}} \implies \mathbf{f \text{ es una Función IMPAR}} \\[6pt]"
            r"&\implies \mathbf{\text{Presenta Simetría Central respecto al origen } (0, 0)} \\[5pt]"
            r"&\implies \text{Si } (x, y) \in f \implies (-x, -y) \in f \text{ (rotación de } 180^\circ)."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{2. Paridad y Simetría:}\\[6pt]"
            r"$\bullet$ Evaluamos $f(-x)$ sustituyendo $-x$ en el cociente:\\[3pt]"
            r"\hspace*{1.2em}$f(-x) = \frac{-x^3 + 4x}{x^2 - 1} = -\frac{x^3 - 4x}{x^2 - 1} = -f(x)$.\\[5pt]"
            r"$\bullet$ Concluimos formalmente: ${\color{amteal}f \text{ es IMPAR}}$.\\[5pt]"
            r"$\bullet$ Presenta simetría central respecto al origen ${\color{amteal}(0, 0)}$.\\[5pt]"
            r"$\bullet$ La rama en $x > 1$ es idéntica a la rama en $x < -1$ tras rotar $180^\circ$."
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
            r"&\quad f(0) = \frac{0^3 - 4(0)}{0^2 - 1} = \frac{0}{-1} = 0 \implies \mathbf{{\color{amteal}P_0 = (0, 0)}} \\[6pt]"
            r"&\bullet \textbf{Interceptos horizontales } (f(x) = 0): \\[3pt]"
            r"&\quad \frac{x^3 - 4x}{x^2 - 1} = 0 \iff x(x^2 - 4) = x(x-2)(x+2) = 0 \\[5pt]"
            r"&\quad \mathbf{{\color{amorange}x_1 = -2}}, \quad \mathbf{{\color{amteal}x_2 = 0}}, \quad \mathbf{{\color{amorange}x_3 = 2}} \\[4pt]"
            r"&\quad \text{Puntos: } {\color{amorange}P_{x_1}(-2, 0)}, \quad {\color{amteal}P_0(0, 0)}, \quad {\color{amorange}P_{x_2}(2, 0)}."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{3. Cortes Coordenados:}\\[6pt]"
            r"$\bullet$ Corte con el eje $y$ ($x = 0$):\\[3pt]"
            r"\hspace*{1.2em}$f(0) = 0 \implies {\color{amteal}P_0(0, 0)}$ (pasa por el origen).\\[5pt]"
            r"$\bullet$ Cortes con el eje $x$ ($f(x) = 0$):\\[3pt]"
            r"\hspace*{1.2em}Se anula cuando el numerador es cero: $x(x^2 - 4) = 0$.\\[5pt]"
            r"$\bullet$ Tres raíces reales simétricas:\\[3pt]"
            r"\hspace*{1.2em}${\color{amorange}x = -2}, \quad {\color{amteal}x = 0} \quad \text{y} \quad {\color{amorange}x = 2}$.\\[5pt]"
            r"$\bullet$ Puntos: ${\color{amorange}P_{x_1}(-2, 0)}$, ${\color{amteal}P_0(0, 0)}$ y ${\color{amorange}P_{x_2}(2, 0)}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=3.2)

        # ==========================================================
        # PASO 4: Factorización Canónica y Tabla Horizontal de Signos
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Tabla Horizontal de Signos por Factores:} \\[4pt]"
            r"&{\color{amteal}f(x)} = \frac{x(x + 2)(x - 2)}{(x + 1)(x - 1)} \\[4pt]"
            r"&\begin{array}{c|c|c|c|c|c|c}"
            r"\text{Factor} & (-\infty, -2) & (-2, -1) & (-1, 0) & (0, 1) & (1, 2) & (2, +\infty) \\ \hline "
            r"x + 2 & - & + & + & + & + & + \\ \hline "
            r"x + 1 & - & - & + & + & + & + \\ \hline "
            r"x     & - & - & - & + & + & + \\ \hline "
            r"x - 1 & - & - & - & - & + & + \\ \hline "
            r"x - 2 & - & - & - & - & - & + \\ \hline "
            r"f(x) & {\color{amred}-} & {\color{amgreen}+} & {\color{amred}-} & {\color{amgreen}+} & {\color{amred}-} & {\color{amgreen}+}"
            r"\end{array} \\[6pt]"
            r"&\bullet \text{Positiva en: } {\color{amgreen}(-2, -1) \cup (0, 1) \cup (2, +\infty)} \quad (f(x) > 0). \\[3pt]"
            r"&\bullet \text{Negativa en: } {\color{amred}(-\infty, -2) \cup (-1, 0) \cup (1, 2)} \quad (f(x) < 0)."
            r"\end{aligned}",
            font_size=17.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{4. Tabla de Signos (Guía Pág. 14):}\\[6pt]"
            r"$\bullet$ Tabla horizontal idéntica a la guía de estudio para Quiz 4.\\[5pt]"
            r"$\bullet$ 6 intervalos delimitados por 3 ceros ($\pm 2, 0$) y 2 polos ($\pm 1$).\\[5pt]"
            r"$\bullet$ Regla de los signos por producto y cociente en cada columna.\\[5pt]"
            r"$\bullet$ Alternancia perfecta $(-, +, -, +, -, +)$ define las zonas arriba y abajo del eje $X$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=3.2)

        # ==========================================================
        # PASO 5: Asíntotas Verticales y Asíntota Oblicua
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Asíntotas Verticales y Oblicua:} \\[4pt]"
            r"&\bullet \textbf{Asíntotas Verticales (A.V.): } \mathbf{{\color{amred}x = -1}} \quad \text{y} \quad \mathbf{{\color{amred}x = 1}} \\[3pt]"
            r"&\quad \lim_{x \to 1^+} f(x) = -\infty, \quad \lim_{x \to 1^-} f(x) = +\infty \\[5pt]"
            r"&\bullet \textbf{Asíntota Oblicua (A.O.): } \text{Grado}(N) = \text{Grado}(D) + 1 \\[3pt]"
            r"&\quad \frac{x^3 - 4x}{x^2 - 1} = x - \frac{3x}{x^2 - 1} \implies \mathbf{{\color{amgold}y = x}} \\[4pt]"
            r"&\bullet \textbf{Corte con A.O.: } -\frac{3x}{x^2 - 1} = 0 \implies \mathbf{{\color{amteal}x = 0 \; (P_0(0, 0))}}."
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{5. Asíntotas del Sistema:}\\[6pt]"
            r"$\bullet$ Asíntotas Verticales en los polos irreducibles:\\[3pt]"
            r"\hspace*{1.2em}${\color{amred}x = -1} \quad \text{y} \quad {\color{amred}x = 1}$.\\[5pt]"
            r"$\bullet$ Grado del numerador excede en 1 al denominador:\\[3pt]"
            r"\hspace*{1.2em}División polinómica: $f(x) = x - \frac{3x}{x^2 - 1}$.\\[5pt]"
            r"$\bullet$ La parte lineal define la Asíntota Oblicua: ${\color{amgold}y = x}$.\\[5pt]"
            r"$\bullet$ Cruce con su asíntota: la curva corta a $y = x$ en ${\color{amteal}(0, 0)}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=3.2)

        # ==========================================================
        # PASO 6: Monotonía y Rango (100% Precálculo)
        # ==========================================================
        eq6 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Monotonía y Rango de la Función:} \\[4pt]"
            r"&\text{Datos oficiales proporcionados en el enunciado de examen:} \\[4pt]"
            r"&\bullet \textbf{Monotonía por Ramas Continuas:} \\[3pt]"
            r"&\quad \bullet \text{Estrictamente Creciente en } {\color{amgreen}(-\infty, -1)} \\[3pt]"
            r"&\quad \bullet \text{Estrictamente Creciente en } {\color{amgreen}(-1, 1)} \\[3pt]"
            r"&\quad \bullet \text{Estrictamente Creciente en } {\color{amgreen}(1, +\infty)} \\[5pt]"
            r"&\implies \text{No presenta máximos ni mínimos locales.} \\[4pt]"
            r"&\implies \text{La rama central } (-1, 1) \text{ recorre todo } (-\infty, +\infty): \\[4pt]"
            r"&\implies \mathbf{\operatorname{Ran}(f) = {\color{amgold}\mathbb{R}} = {\color{amgreen}(-\infty, +\infty)}}."
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{6. Monotonía y Rango:}\\[6pt]"
            r"$\bullet$ Propiedad dada en el enunciado de examen:\\[3pt]"
            r"\hspace*{1.2em}$f$ es estrictamente creciente en cada intervalo.\\[5pt]"
            r"$\bullet$ Cada una de las 3 ramas sube monótonamente hacia la derecha.\\[5pt]"
            r"$\bullet$ Sin extremos relativos (crecimiento sostenido sin inversión).\\[5pt]"
            r"$\bullet$ La rama central abarca todo el eje vertical:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgold}\operatorname{Ran}(f) = \mathbb{R} = (-\infty, +\infty)}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq6, just6, box_color=THEME["highlight"], advance_to_step=5, wait_time=3.2)

        # ==========================================================
        # PASO 7: Cuadro Horizontal de Variación y Puntos Notables (Vista.webp)
        # ==========================================================
        eq7 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{7. Cuadro de Variación y Puntos Notables:} \\[6pt]"
            r"&\begin{array}{c|c|c|c}"
            r"x & (-\infty, -1) & (-1, 1) & (1, +\infty) \\ \hline "
            r"\text{Tendencia} & {\color{amgreen}\text{Sube }(+)} & {\color{amgreen}\text{Sube }(+)} & {\color{amgreen}\text{Sube }(+)} \\ \hline "
            r"f(x) & \nearrow & \nearrow & \nearrow "
            r"\end{array} \\[8pt]"
            r"&\bullet \text{Monotonía: Creciente en cada una de sus 3 ramas (sin extremos)}. \\[3pt]"
            r"&\bullet \text{Asíntotas V.: } x = -1 \text{ y } x = 1 \text{ con divergencia } \pm\infty. \\[3pt]"
            r"&\bullet \text{Asíntota Oblicua: } y = x, \text{ con cruce central en el origen } P_0(0, 0). \\[3pt]"
            r"&\bullet \text{Cortes } \mathbf{X}: P_{x_1}(-2, 0), \; P_0(0, 0) \text{ y } P_{x_2}(2, 0)."
            r"\end{aligned}",
            font_size=18.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{7. Síntesis Horizontal:}\\[6pt]"
            r"$\bullet$ Cuadro horizontal consolidado según el modelo de referencia.\\[5pt]"
            r"$\bullet$ Flechas ($\nearrow$) confirman crecimiento monótono estricto continuo.\\[5pt]"
            r"$\bullet$ Destaca el origen ${\color{amteal}(0, 0)}$ como centro simétrico y cruce de A.O.\\[5pt]"
            r"$\bullet$ Define la dirección de las 3 ramas hacia sus asíntotas."
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
            r"&\bullet \mathbf{\operatorname{Ran}(f) = {\color{amgold}\mathbb{R} = (-\infty, +\infty)}} \\[4pt]"
            r"&\bullet \mathbf{\text{Paridad: }} {\color{amteal}\text{Impar }} (f(-x) = -f(x)) \implies \text{Sim. Central } (0, 0) \\[4pt]"
            r"&\bullet \mathbf{\text{Asíntotas V.: }} {\color{amred}x = -1}, \quad {\color{amred}x = 1} \\[4pt]"
            r"&\bullet \mathbf{\text{Asíntota Oblicua: }} {\color{amgold}y = x} \quad (\text{corte en } (0, 0)) \\[4pt]"
            r"&\bullet \mathbf{\text{Cortes con Ejes: }} {\color{amorange}(-2, 0)}, \; {\color{amteal}(0, 0)}, \; {\color{amorange}(2, 0)} \\[4pt]"
            r"&\bullet \mathbf{\text{Monotonía: }} \text{Creciente en todo } \operatorname{Dom}(f) \quad {\color{amgreen}\blacksquare}"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        box8 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.18, corner_radius=0.1)

        # Gráfico cartesiano de la función racional con asíntota oblicua
        axes = Axes(
            x_range=[-4.5, 4.5, 1],
            y_range=[-4.5, 4.5, 1],
            x_length=4.8,
            y_length=3.4,
            axis_config={"font_size": 16},
            x_axis_config={"numbers_to_include": [-4, -3, -2, -1, 1, 2, 3, 4], "font_size": 16},
            y_axis_config={"numbers_to_include": [-4, -3, -2, -1, 1, 2, 3, 4], "font_size": 16}
        ).move_to([3.25, -0.65, 0])
        axes_labels = axes.get_axis_labels(x_label=MathTex(r"x", font_size=19), y_label=MathTex(r"y", font_size=19))

        graph_title = Tex(
            r"Gráfica de ${\color{amteal}f(x)} = \frac{{\color{amteal}x^3 - 4x}}{{\color{amred}x^2 - 1}}$",
            font_size=21.5,
            color=WHITE
        ).move_to([3.25, 1.70, 0])

        # Asíntotas verticales discontinuas (x = -1 y x = 1)
        asymp_v1 = DashedLine(
            axes.c2p(-1.0, -4.2), axes.c2p(-1.0, 4.2),
            dash_length=0.08, color=THEME["poncho_red"], stroke_width=2.0
        )
        lbl_av1 = MathTex(r"x = -1", font_size=13.0, color=THEME["poncho_red"]).next_to(axes.c2p(-1.0, -3.2), LEFT, buff=0.06)

        asymp_v2 = DashedLine(
            axes.c2p(1.0, -4.2), axes.c2p(1.0, 4.2),
            dash_length=0.08, color=THEME["poncho_red"], stroke_width=2.0
        )
        lbl_av2 = MathTex(r"x = 1", font_size=13.0, color=THEME["poncho_red"]).next_to(axes.c2p(1.0, 3.2), RIGHT, buff=0.06)

        # Asíntota oblicua discontinua (y = x)
        asymp_o = DashedLine(
            axes.c2p(-4.0, -4.0), axes.c2p(4.0, 4.0),
            dash_length=0.08, color=THEME["highlight"], stroke_width=1.8
        )
        lbl_ao = MathTex(r"y = x", font_size=13.5, color=THEME["highlight"]).next_to(axes.c2p(3.2, 3.2), DOWN + RIGHT, buff=0.06)

        # 3 Ramas continuas crecientes
        branch_left = axes.plot(
            lambda x: (x**3 - 4*x) / (x**2 - 1),
            x_range=[-4.2, -1.25],
            color=THEME["curve"],
            stroke_width=2.5
        )
        branch_center = axes.plot(
            lambda x: (x**3 - 4*x) / (x**2 - 1),
            x_range=[-0.70, 0.70],
            color=THEME["curve"],
            stroke_width=2.5
        )
        branch_right = axes.plot(
            lambda x: (x**3 - 4*x) / (x**2 - 1),
            x_range=[1.25, 4.2],
            color=THEME["curve"],
            stroke_width=2.5
        )
        curve_branches = VGroup(branch_left, branch_center, branch_right)
        curve_lbl = MathTex(r"y = f(x)", font_size=14.0, color=THEME["curve"]).move_to(axes.c2p(-3.0, 1.5))

        # Puntos notables: P_x1(-2, 0), P_0(0, 0), P_x2(2, 0)
        dot_0 = Dot(axes.c2p(0.0, 0.0), radius=0.07, color=THEME["highlight"])
        lbl_0 = MathTex(r"P_0(0, 0)", font_size=12.0, color=THEME["highlight"]).next_to(dot_0, DOWN + 0.8*RIGHT, buff=0.10)

        dot_x1 = Dot(axes.c2p(-2.0, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_x1 = MathTex(r"(-2, 0)", font_size=12.0, color=THEME["statement_text"]).next_to(dot_x1, UP + LEFT, buff=0.08)

        dot_x2 = Dot(axes.c2p(2.0, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_x2 = MathTex(r"(2, 0)", font_size=12.0, color=THEME["statement_text"]).next_to(dot_x2, UP + RIGHT, buff=0.08)

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
            Create(asymp_o),
            Write(lbl_ao),
            Create(curve_branches),
            Write(curve_lbl),
            FadeIn(dot_0),
            Write(lbl_0),
            FadeIn(dot_x1),
            Write(lbl_x1),
            FadeIn(dot_x2),
            Write(lbl_x2),
            run_time=2.4
        )
        self.wait(8.5)

        # Cierre institucional
        graph_group = VGroup(
            axes, axes_labels, graph_title,
            asymp_v1, lbl_av1, asymp_v2, lbl_av2,
            asymp_o, lbl_ao,
            curve_branches, curve_lbl,
            dot_0, lbl_0,
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
