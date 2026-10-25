"""
Ejercicio 5 - Tutorías y Preparación Quiz 4 (Jhoselyn)
Tema: Análisis Completo y Gráfica de Funciones:
      Función Racional Impar con Asíntota Oblicua: f(x) = (x^3 - 4x) / (x^2 - 1).
      Dominio, paridad impar, simetría central en el origen (0, 0), cortes coordenados,
      tabla de signos, asíntotas verticales x = ±1, asíntota oblicua y = x (con corte en (0, 0)),
      monotonía estrictamente creciente, rango R y trazado cartesiano de 3 ramas.

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica en 7 pasos con ecuaciones en LaTeX de gran legibilidad.
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
            desc_text="Analice completamente y grafique la función racional con asíntota oblicua:",
            math_tex=r"{\color{amteal}f(x)} = \frac{{\color{amteal}x^3 - 4x}}{{\color{amred}x^2 - 1}}",
            desc_font_size=18.5,
            math_font_size=30.0,
            box_pos=np.array([0.0, 2.65, 0.0]),
            read_time=3.5
        )

        # 3. Barra de Progreso Interactiva (7 pasos detallados)
        self.setup_progress_bar([
            "1/7: Dominio y Restricciones",
            "2/7: Paridad y Simetría Impar",
            "3/7: Cortes con los Ejes",
            "4/7: Tabla de Signos",
            "5/7: Asíntotas V. y Oblicua",
            "6/7: Monotonía y Rango",
            "7/7: Gráfica Cartesiana y Verificación"
        ], dot_spacing=0.92, label_font_size=14.5)

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
            r"$\bullet$ La función se fragmenta en 3 ramas continuas:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgreen}(-\infty, -1)}, \quad {\color{amgreen}(-1, 1)} \quad \text{y} \quad {\color{amgreen}(1, +\infty)}$.\\[2pt]"
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.1)

        # ==========================================================
        # PASO 2: Paridad y Simetría Impar (Central)
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Paridad y Simetría:} \\[5pt]"
            r"&\text{Evaluamos formalmente el signo de } f(-x): \\[4pt]"
            r"&f(-x) = \frac{(-x)^3 - 4(-x)}{(-x)^2 - 1} = \frac{-x^3 + 4x}{x^2 - 1} = -\frac{x^3 - 4x}{x^2 - 1} \\[6pt]"
            r"&\implies {\color{amteal}f(-x) = -f(x)} \implies \mathbf{\text{Función IMPAR}} \\[6pt]"
            r"&\implies \text{Presenta } \mathbf{\text{Simetría Central respecto al origen } (0, 0)} \\[5pt]"
            r"&\implies \text{Si } (x, y) \in f \implies (-x, -y) \in f \text{ (rotación de } 180^\circ)."
            r"\end{aligned}",
            font_size=21.5,
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

        self.morph_step(eq2, just2, box_color=THEME["highlight"], advance_to_step=1, wait_time=4.1)

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
            r"&\quad \mathbf{{\color{amorange}x_1 = -2}}, \quad \mathbf{{\color{amorange}x_2 = 0}}, \quad \mathbf{{\color{amorange}x_3 = 2}} \\[4pt]"
            r"&\quad \text{Puntos: } {\color{amorange}P_{x_1}(-2, 0)}, \quad {\color{amteal}P_0(0, 0)}, \quad {\color{amorange}P_{x_2}(2, 0)}."
            r"\end{aligned}",
            font_size=21.5,
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
            r"\hspace*{1.2em}${\color{amorange}x = -2}, \quad {\color{amorange}x = 0} \quad \text{y} \quad {\color{amorange}x = 2}$.\\[5pt]"
            r"$\bullet$ Puntos: ${\color{amorange}P_{x_1}(-2, 0)}$, ${\color{amteal}P_0(0, 0)}$ y ${\color{amorange}P_{x_2}(2, 0)}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=4.1)

        # ==========================================================
        # PASO 4: Factorización y Tabla de Signos
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Factorización y Tabla de Signos:} \\[4pt]"
            r"&{\color{amteal}f(x)} = \frac{x(x + 2)(x - 2)}{(x + 1)(x - 1)}, \quad \text{Ceros: } \{{\color{amorange}-2, -1, 0, 1, 2}\} \\[5pt]"
            r"&\bullet (-\infty, -2): \; \tfrac{(-)}{(-)} = {\color{amred}\mathbf{(-)}} < 0 \quad \bullet (-2, -1): \; \tfrac{(+)}{(+)} = {\color{amgreen}\mathbf{(+)}} > 0 \\[4pt]"
            r"&\bullet (-1, 0): \; \tfrac{(+)}{(-)} = {\color{amred}\mathbf{(-)}} < 0 \quad \bullet (0, 1): \; \tfrac{(-)}{(-)} = {\color{amgreen}\mathbf{(+)}} > 0 \\[4pt]"
            r"&\bullet (1, 2): \; \tfrac{(-)}{(+)} = {\color{amred}\mathbf{(-)}} < 0 \quad \bullet (2, +\infty): \; \tfrac{(+)}{(+)} = {\color{amgreen}\mathbf{(+)}} > 0 \\[5pt]"
            r"&\mathbf{\text{Positiva: } {\color{amgreen}(-2, -1) \cup (0, 1) \cup (2, +\infty)}} \\[4pt]"
            r"&\mathbf{\text{Negativa: } {\color{amred}(-\infty, -2) \cup (-1, 0) \cup (1, 2)}}."
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{4. Intervalos de Signo:}\\[6pt]"
            r"$\bullet$ Los 5 ceros particionan la recta en 6 intervalos.\\[4pt]"
            r"$\bullet$ Los factores lineales simples provocan alternancia de signos:\\[3pt]"
            r"\hspace*{1.2em}$(-), \quad (+), \quad (-), \quad (+), \quad (-), \quad (+)$.\\[5pt]"
            r"$\bullet$ Regiones positivas sobre el eje horizontal:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgreen}(-2, -1) \cup (0, 1) \cup (2, +\infty)}$.\\[5pt]"
            r"$\bullet$ Regiones negativas bajo el eje horizontal:\\[3pt]"
            r"\hspace*{1.2em}${\color{amred}(-\infty, -2) \cup (-1, 0) \cup (1, 2)}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=4.1)

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
            font_size=21.0,
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

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=4.1)

        # ==========================================================
        # PASO 6: Monotonía y Rango
        # ==========================================================
        eq6 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Monotonía y Rango de la Función:} \\[4pt]"
            r"&\bullet \textbf{Primera derivada formal } f'(x): \\[3pt]"
            r"&\quad f'(x) = \frac{(3x^2-4)(x^2-1) - (x^3-4x)(2x)}{(x^2-1)^2} = \mathbf{\frac{x^4 + x^2 + 4}{(x^2 - 1)^2}} \\[5pt]"
            r"&\quad \text{Como } x^4 + x^2 + 4 > 0 \implies \mathbf{{\color{amgreen}f'(x) > 0}} \quad \forall x \in \operatorname{Dom}(f) \\[4pt]"
            r"&\implies \mathbf{\text{Estrictamente Creciente}} \text{ en cada una de sus 3 ramas} \\[5pt]"
            r"&\implies \text{No presenta extremos locales } (f'(x) \neq 0) \\[4pt]"
            r"&\implies \mathbf{\operatorname{Ran}(f) = {\color{amgold}\mathbb{R}} = {\color{amgreen}(-\infty, +\infty)}}."
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{6. Monotonía y Rango:}\\[6pt]"
            r"$\bullet$ Derivada del cociente:\\[3pt]"
            r"\hspace*{1.2em}$f'(x) = \frac{x^4 + x^2 + 4}{(x^2 - 1)^2}$.\\[5pt]"
            r"$\bullet$ Numerador y denominador son siempre positivos:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgreen}f'(x) > 0}$ en todos los puntos de su dominio.\\[5pt]"
            r"$\bullet$ Cada una de las 3 ramas sube monótonamente hacia la derecha.\\[5pt]"
            r"$\bullet$ Al recorrer de $-\infty$ a $+\infty$, el recorrido cubre todo:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgold}\operatorname{Ran}(f) = \mathbb{R} = (-\infty, +\infty)}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq6, just6, box_color=THEME["highlight"], advance_to_step=5, wait_time=4.1)

        # ==========================================================
        # PASO 7: Gráfica Cartesiana y Verificación Visual
        # ==========================================================
        left_summary = MathTex(
            r"\begin{aligned}"
            r"&\textbf{7. Resumen Formal de Resultados:} \\[4pt]"
            r"&\bullet \mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R} \setminus \{-1, 1\}}} \\[4pt]"
            r"&\bullet \mathbf{\operatorname{Ran}(f) = {\color{amgold}\mathbb{R} = (-\infty, +\infty)}} \\[4pt]"
            r"&\bullet \mathbf{\text{Paridad: }} {\color{amteal}\text{Impar }} (f(-x) = -f(x)) \implies \text{Sim. Central } (0, 0) \\[4pt]"
            r"&\bullet \mathbf{\text{Asíntotas V.: }} {\color{amred}x = -1}, \quad {\color{amred}x = 1} \\[4pt]"
            r"&\bullet \mathbf{\text{Asíntota Oblicua: }} {\color{amgold}y = x} \quad (\text{corte en } (0, 0)) \\[4pt]"
            r"&\bullet \mathbf{\text{Cortes con Ejes: }} {\color{amorange}(-2, 0)}, \; {\color{amteal}(0, 0)}, \; {\color{amorange}(2, 0)} \\[4pt]"
            r"&\bullet \mathbf{\text{Monotonía: }} \text{Creciente en todo } \operatorname{Dom}(f) \quad {\color{amgreen}\blacksquare}"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        box7 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.18, corner_radius=0.1)

        # Gráfico cartesiano de la función racional con asíntota oblicua
        axes, axes_labels = self.setup_axes(
            x_range=[-4.5, 4.5, 1],
            y_range=[-4.5, 4.5, 1],
            x_length=4.8,
            y_length=3.4,
            center=[3.25, -0.65, 0],
            include_numbers=True,
            numbers_font_size=16,
            labels_font_size=19
        )
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
        lbl_av1 = MathTex(r"x = -1", font_size=14.0, color=THEME["poncho_red"]).next_to(axes.c2p(-1.0, -3.2), LEFT, buff=0.06)

        asymp_v2 = DashedLine(
            axes.c2p(1.0, -4.2), axes.c2p(1.0, 4.2),
            dash_length=0.08, color=THEME["poncho_red"], stroke_width=2.0
        )
        lbl_av2 = MathTex(r"x = 1", font_size=14.0, color=THEME["poncho_red"]).next_to(axes.c2p(1.0, 3.2), RIGHT, buff=0.06)

        # Asíntota oblicua discontinua (y = x)
        asymp_o = DashedLine(
            axes.c2p(-4.0, -4.0), axes.c2p(4.0, 4.0),
            dash_length=0.08, color=THEME["highlight"], stroke_width=1.8
        )
        lbl_ao = MathTex(r"y = x", font_size=14.0, color=THEME["highlight"]).next_to(axes.c2p(3.2, 3.2), DOWN + RIGHT, buff=0.06)

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
        curve_lbl = MathTex(r"y = f(x)", font_size=14.5, color=THEME["curve"]).move_to(axes.c2p(-3.0, 1.5))

        # Puntos notables: P_x1(-2, 0), P_0(0, 0), P_x2(2, 0)
        dot_0 = Dot(axes.c2p(0.0, 0.0), radius=0.07, color=THEME["highlight"])
        lbl_0 = MathTex(r"P_0(0, 0)", font_size=13.0, color=THEME["highlight"]).next_to(dot_0, UP + LEFT, buff=0.07)

        dot_x1 = Dot(axes.c2p(-2.0, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_x1 = MathTex(r"(-2, 0)", font_size=13.0, color=THEME["statement_text"]).next_to(dot_x1, UP + LEFT, buff=0.08)

        dot_x2 = Dot(axes.c2p(2.0, 0.0), radius=0.065, color=THEME["secondary"])
        lbl_x2 = MathTex(r"(2, 0)", font_size=13.0, color=THEME["statement_text"]).next_to(dot_x2, UP + RIGHT, buff=0.08)

        prog_anims = self.get_advance_progress_anims(6)

        self.play(
            FadeOut(self.active_math),
            FadeOut(self.active_just),
            FadeOut(self.active_box),
            FadeIn(left_summary),
            Create(box7),
            Create(axes),
            Write(axes_labels),
            Write(graph_title),
            *prog_anims,
            run_time=1.8
        )
        self.active_box = box7
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
