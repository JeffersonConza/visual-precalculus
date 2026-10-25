"""
Ejercicio 2 - Tutorías y Preparación Quiz 4 (Jhoselyn)
Tema: Análisis Completo y Gráfica de Funciones:
      Polinomio Cúbico Impar: f(x) = 1/2 x^3 - 3/2 x.
      Dominio, paridad, simetría central respecto al origen,
      cortes coordenados, factorización canónica, tabla horizontal de signos por factores,
      extremos locales, monotonía, rango, cuadro horizontal de variación (estilo Vista.webp)
      y trazado cartesiano riguroso.

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica en 8 pasos con ecuaciones legibles HD.
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


class EjercicioJh_02(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Jhoselyn",
            exercise="Ejercicio 2",
            topic="Análisis y Gráfica de Función Cúbica Impar",
            font_size=17.0
        )

        # 2. Enunciado institucional permanente con fórmula prominente (y = 2.65)
        self.setup_statement(
            desc_text="Analice completamente y grafique la función polinómica cúbica:",
            math_tex=r"{\color{amteal}f(x)} = {\color{amteal}\frac{1}{2}}x^3 - {\color{amred}\frac{3}{2}}x",
            desc_font_size=19.0,
            math_font_size=31.0,
            box_pos=np.array([0.0, 2.65, 0.0]),
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (8 pasos unificados)
        self.setup_progress_bar([
            "1/8: Dominio y Paridad",
            "2/8: Cortes Coordenados",
            "3/8: Factorización Canónica",
            "4/8: Tabla de Signos",
            "5/8: Extremos Locales",
            "6/8: Monotonía y Rango",
            "7/8: Cuadro de Variación",
            "8/8: Gráfica Cartesiana y Verificación"
        ], dot_spacing=0.82, label_font_size=14.0)

        # ==========================================================
        # PASO 1: Dominio y Simetría de Paridad
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Dominio y Simetría de Paridad:} \\[6pt]"
            r"&\text{Al ser } {\color{amteal}f(x)} \text{ una función polinómica de grado 3:} \\[5pt]"
            r"&\mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R}} = {\color{amgreen}(-\infty, +\infty)}} \\[8pt]"
            r"&\textbf{Evaluación formal de paridad } f(-x): \\[5pt]"
            r"&f(-x) = \frac{1}{2}(-x)^3 - \frac{3}{2}(-x) = -\frac{1}{2}x^3 + \frac{3}{2}x = -f(x) \\[7pt]"
            r"&\implies {\color{amteal}f(-x) = -f(x)} \implies \mathbf{\text{Función IMPAR}} \\[6pt]"
            r"&\implies \text{Presenta } \mathbf{\text{Simetría Central respecto al origen } {\color{amteal}O(0, 0)}}."
            r"\end{aligned}",
            font_size=22.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{1. Dominio y Paridad:}\\[6pt]"
            r"$\bullet$ Toda función polinómica tiene ${\color{amgold}\operatorname{Dom}(f) = \mathbb{R}}$.\\[5pt]"
            r"$\bullet$ Evaluamos $f(-x)$ sustituyendo $-x$ en cada término:\\[3pt]"
            r"\hspace*{1.2em}$f(-x) = -\frac{1}{2}x^3 + \frac{3}{2}x = -f(x)$.\\[5pt]"
            r"$\bullet$ Concluimos formalmente: ${\color{amteal}f \text{ es función IMPAR}}$.\\[5pt]"
            r"$\bullet$ Presenta simetría central respecto al origen ${\color{amteal}(0, 0)}$:\\[2pt]"
            r"\hspace*{1.2em}rotación de $180^\circ$ preserva la gráfica."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=3.2)

        # ==========================================================
        # PASO 2: Cortes con los Ejes Coordenados
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Intersecciones con los Ejes Coordenados:} \\[5pt]"
            r"&\bullet \textbf{Intercepto vertical } (x = 0): \\[3pt]"
            r"&\quad f(0) = \frac{1}{2}(0)^3 - \frac{3}{2}(0) = 0 \implies \mathbf{{\color{amteal}P_0 = (0, 0)}} \\[6pt]"
            r"&\bullet \textbf{Interceptos horizontales } (f(x) = 0): \\[3pt]"
            r"&\quad \frac{1}{2}x^3 - \frac{3}{2}x = 0 \iff \frac{1}{2}x(x^2 - 3) = 0 \\[5pt]"
            r"&\quad x = 0 \quad \lor \quad x^2 - 3 = 0 \implies x = \pm\sqrt{3} \approx \pm 1.732 \\[6pt]"
            r"&\quad \mathbf{{\color{amorange}x_1 = -\sqrt{3}}}, \qquad \mathbf{{\color{amorange}x_2 = 0}}, \qquad \mathbf{{\color{amorange}x_3 = \sqrt{3}}} \\[5pt]"
            r"&\quad \text{Puntos: } {\color{amorange}P_{x_1}(-\sqrt{3}, 0)}, \; {\color{amorange}P_0(0, 0)}, \; {\color{amorange}P_{x_2}(\sqrt{3}, 0)}."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{2. Cortes Coordenados:}\\[6pt]"
            r"$\bullet$ Eje $y$: Evaluamos $x = 0 \implies {\color{amteal}P_0(0, 0)}$ (pasa por el origen).\\[5pt]"
            r"$\bullet$ Eje $x$: Igualamos a cero y extraemos factor común:\\[3pt]"
            r"\hspace*{1.2em}$\frac{1}{2}x(x^2 - 3) = 0$.\\[5pt]"
            r"$\bullet$ Obtenemos 3 raíces reales: $x = 0$ y $x = \pm\sqrt{3} \approx \pm 1.73$.\\[5pt]"
            r"$\bullet$ La simetría impar confirma que las raíces equidistan del origen."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq2, just2, box_color=THEME["highlight"], advance_to_step=1, wait_time=3.2)

        # ==========================================================
        # PASO 3: Factorización Canónica de la Cúbica
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Factorización Canónica en Factores Lineales:} \\[6pt]"
            r"&{\color{amteal}f(x)} = \frac{1}{2}x^3 - \frac{3}{2}x = \frac{1}{2}x(x^2 - 3) \\[6pt]"
            r"&\text{Por diferencia de cuadrados } a^2 - b^2 = (a-b)(a+b): \\[5pt]"
            r"&\mathbf{{\color{amteal}f(x) = \frac{1}{2} x \left(x + \sqrt{3}\right)\left(x - \sqrt{3}\right)}} \\[7pt]"
            r"&\bullet \mathbf{\text{Multiplicidad: }} \text{Las 3 raíces son simples (multiplicidad 1)}. \\[4pt]"
            r"&\bullet \mathbf{\text{Comportamiento: }} \text{La curva cruza transversalmente el eje } X \\[3pt]"
            r"&\quad \text{en cada punto de corte } \{-\sqrt{3}, 0, \sqrt{3}\}."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{3. Factorización Canónica:}\\[6pt]"
            r"$\bullet$ Descomposición completa en tres factores lineales reales.\\[5pt]"
            r"$\bullet$ Constante de escala positiva: $k = \frac{1}{2} > 0$.\\[5pt]"
            r"$\bullet$ Como todas las raíces tienen exponente impar (1),\\[2pt]"
            r"\hspace*{1.2em}la gráfica atraviesa el eje $X$ sin rebotar.\\[5pt]"
            r"$\bullet$ Base fundamental para la tabla de variación de signos."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=3.2)

        # ==========================================================
        # PASO 4: Tabla Horizontal de Signos por Factores
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Tabla Horizontal de Signos por Factores:} \\[4pt]"
            r"&{\color{amteal}f(x)} = \frac{1}{2} x \left(x + \sqrt{3}\right)\left(x - \sqrt{3}\right) \\[5pt]"
            r"&\begin{array}{c|c|c|c|c}"
            r"\text{Factor} & (-\infty, -\sqrt{3}) & (-\sqrt{3}, 0) & (0, \sqrt{3}) & (\sqrt{3}, +\infty) \\ \hline "
            r"x + \sqrt{3} & - & + & + & + \\ \hline "
            r"x & - & - & + & + \\ \hline "
            r"x - \sqrt{3} & - & - & - & + \\ \hline "
            r"1/2 & + & + & + & + \\ \hline "
            r"f(x) & {\color{amred}\mathbf{-}} & {\color{amgreen}\mathbf{+}} & {\color{amred}\mathbf{-}} & {\color{amgreen}\mathbf{+}}"
            r"\end{array} \\[6pt]"
            r"&\bullet \mathbf{\text{Positiva en: }} {\color{amgreen}\left(-\sqrt{3}, 0\right) \cup \left(\sqrt{3}, +\infty\right)} \quad (f(x) > 0). \\[3pt]"
            r"&\bullet \mathbf{\text{Negativa en: }} {\color{amred}\left(-\infty, -\sqrt{3}\right) \cup \left(0, \sqrt{3}\right)} \quad (f(x) < 0)."
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{4. Tabla de Signos (Guía Pág. 8):}\\[6pt]"
            r"$\bullet$ Tabla horizontal idéntica a la guía de preparación para Quiz 4.\\[5pt]"
            r"$\bullet$ 4 intervalos delimitados por las raíces $\{-\sqrt{3}, 0, \sqrt{3}\}$.\\[5pt]"
            r"$\bullet$ Regla de los signos por columnas determina el signo global.\\[5pt]"
            r"$\bullet$ Alternancia de signos ($-, +, -, +$) característica de cúbicas."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=3.2)

        # ==========================================================
        # PASO 5: Puntos Notables y Extremos Locales
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Extremos Locales y Puntos Notables:} \\[6pt]"
            r"&\text{Datos oficiales proporcionados en el enunciado de examen:} \\[5pt]"
            r"&\bullet \mathbf{\text{Máximo Local en: }} {\color{amgold}M(-1, 1)} \\[4pt]"
            r"&\quad f(-1) = \frac{1}{2}(-1)^3 - \frac{3}{2}(-1) = -\frac{1}{2} + \frac{3}{2} = \mathbf{{\color{amgold}1}} \\[6pt]"
            r"&\bullet \mathbf{\text{Mínimo Local en: }} {\color{amteal}m(1, -1)} \\[4pt]"
            r"&\quad f(1) = \frac{1}{2}(1)^3 - \frac{3}{2}(1) = \frac{1}{2} - \frac{3}{2} = \mathbf{{\color{amteal}-1}} \\[6pt]"
            r"&\bullet \mathbf{\text{Punto de Inflexión y Simetría: }} {\color{amorange}I(0, 0)} \\[3pt]"
            r"&\quad \text{Centro geométrico entre el máximo y el mínimo local}."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{5. Extremos y Simetría:}\\[6pt]"
            r"$\bullet$ Enunciado oficial de Quiz 4 entrega los puntos extremos.\\[5pt]"
            r"$\bullet$ La simetría impar valida que $f(1) = -f(-1) = -1$.\\[5pt]"
            r"$\bullet$ El origen ${\color{amorange}(0, 0)}$ es el punto medio exacto de los extremos:\\[3pt]"
            r"\hspace*{1.2em}$\frac{M(-1, 1) + m(1, -1)}{2} = (0, 0)$.\\[5pt]"
            r"$\bullet$ Punto de inflexión donde la curva cambia de concavidad."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=3.2)

        # ==========================================================
        # PASO 6: Intervalos de Monotonía y Rango
        # ==========================================================
        eq6 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Intervalos de Monotonía y Rango:} \\[6pt]"
            r"&\bullet \textbf{Monotonía (Crecimiento / Decrecimiento):} \\[4pt]"
            r"&\quad \mathbf{{\color{amgreen}f \text{ es creciente en } (-\infty, -1] \cup [1, +\infty)}} \\[5pt]"
            r"&\quad \mathbf{{\color{amred}f \text{ es decreciente en } [-1, 1]}} \\[7pt]"
            r"&\bullet \textbf{Comportamiento en los Extremos Infinitos:} \\[4pt]"
            r"&\quad \lim_{x \to -\infty} f(x) = -\infty, \qquad \lim_{x \to +\infty} f(x) = +\infty \\[5pt]"
            r"&\bullet \mathbf{\text{Rango: }} \mathbf{\operatorname{Ran}(f) = {\color{amgold}\mathbb{R} = (-\infty, +\infty)}}."
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{6. Monotonía y Rango:}\\[6pt]"
            r"$\bullet$ La función asciende monótonamente en $(-\infty, -1]$ hasta el máximo.\\[5pt]"
            r"$\bullet$ Desciende en $[-1, 1]$ atravesando el origen hasta el mínimo.\\[5pt]"
            r"$\bullet$ Vuelve a ascender monótonamente hacia $+\infty$ en $[1, +\infty)$.\\[5pt]"
            r"$\bullet$ Al no tener asíntotas horizontales, su rango cubre todo ${\color{amgold}\mathbb{R}}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq6, just6, box_color=THEME["highlight"], advance_to_step=5, wait_time=3.2)

        # ==========================================================
        # PASO 7: Cuadro Horizontal de Variación y Puntos Notables
        # ==========================================================
        eq7 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{7. Cuadro de Variación y Puntos Notables:} \\[6pt]"
            r"&\begin{array}{c|c|c|c}"
            r"x & (-\infty, -1) & (-1, 1) & (1, +\infty) \\ \hline "
            r"\text{Pendiente / Comportamiento} & {\color{amgreen}\mathbf{\text{Creciente }(+)}} & {\color{amred}\mathbf{\text{Decreciente }(-)}} & {\color{amgreen}\mathbf{\text{Creciente }(+)}} \\ \hline "
            r"f(x) & \nearrow & \searrow & \nearrow"
            r"\end{array} \\[8pt]"
            r"&\bullet \mathbf{\text{Máximo Local: }} x = -1 \implies {\color{amgold}M(-1, 1)} \text{ (Cúspide izquierda)}. \\[3pt]"
            r"&\bullet \mathbf{\text{Mínimo Local: }} x = 1 \implies {\color{amteal}m(1, -1)} \text{ (Valle derecho)}. \\[3pt]"
            r"&\bullet \mathbf{\text{Inflexión: }} {\color{amorange}I(0, 0)} \text{ centro de simetría impar y corte coordenado}. \\[3pt]"
            r"&\bullet \mathbf{\text{Cortes } X: } P_{x_1}(-\sqrt{3}, 0) \text{ en tramo inicial, } P_{x_2}(\sqrt{3}, 0) \text{ en tramo final}."
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{7. Síntesis Horizontal:}\\[6pt]"
            r"$\bullet$ Cuadro horizontal consolidado según el modelo de referencia.\\[5pt]"
            r"$\bullet$ Flechas confirman el ascenso ($\nearrow$) hacia ${\color{amgold}M(-1, 1)}$,\\[2pt]"
            r"\hspace*{1.2em}descenso ($\searrow$) hacia ${\color{amteal}m(1, -1)}$ y nuevo ascenso ($\nearrow$).\\[5pt]"
            r"$\bullet$ Muestra la alternancia clásica de la silueta en ``S''.\\[5pt]"
            r"$\bullet$ Puntos de anclaje para el trazado cartesiano continuo."
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
            r"&\textbf{8. Resumen Formal de Resultados:} \\[5pt]"
            r"&\bullet \mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R}}}, \quad \mathbf{\operatorname{Ran}(f) = {\color{amgold}\mathbb{R}}} \\[5pt]"
            r"&\bullet \mathbf{\text{Paridad: }} {\color{amteal}\text{Impar }} (f(-x) = -f(x)) \implies \text{Simetría } {\color{amorange}O(0, 0)} \\[5pt]"
            r"&\bullet \mathbf{\text{Máx. Local: }} {\color{amgold}M(-1, 1)}, \quad \mathbf{\text{Mín. Local: }} {\color{amteal}m(1, -1)} \\[5pt]"
            r"&\bullet \mathbf{\text{Cortes } X: } {\color{amorange}(-\sqrt{3}, 0), \; (0, 0), \; (\sqrt{3}, 0)} \quad (\sqrt{3} \approx 1.73) \\[5pt]"
            r"&\bullet \mathbf{\text{Creciente: }} {\color{amgreen}(-\infty, -1] \cup [1, +\infty)} \\[5pt]"
            r"&\bullet \mathbf{\text{Decreciente: }} {\color{amred}[-1, 1]} \quad {\color{amgreen}\blacksquare}"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        box8 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.18, corner_radius=0.1)

        # Gráfico cartesiano de la función cúbica
        axes, axes_labels = self.setup_axes(
            x_range=[-3.0, 3.0, 1],
            y_range=[-3.0, 3.0, 1],
            x_length=4.5,
            y_length=3.3,
            center=[3.15, -0.75, 0],
            include_numbers=True,
            numbers_font_size=17,
            labels_font_size=20
        )
        graph_title = Tex(
            r"Gráfica de ${\color{amteal}f(x)} = {\color{amteal}\frac{1}{2}}x^3 - {\color{amred}\frac{3}{2}}x$",
            font_size=21.5,
            color=WHITE
        ).move_to([3.15, 1.65, 0])

        # Curva cúbica continua
        cubic = axes.plot(
            lambda x: 0.5 * x**3 - 1.5 * x,
            x_range=[-2.4, 2.4],
            color=THEME["curve"],
            stroke_width=2.5
        )
        cubic_lbl = MathTex(r"y = f(x)", font_size=15.0, color=THEME["curve"]).move_to(axes.c2p(2.2, 2.2))

        # Extremos locales: M(-1, 1) y m(1, -1)
        dot_max = Dot(axes.c2p(-1.0, 1.0), radius=0.08, color=THEME["highlight"])
        lbl_max = MathTex(r"M(-1, 1)", font_size=14.5, color=THEME["highlight"]).next_to(dot_max, UP, buff=0.10)

        dot_min = Dot(axes.c2p(1.0, -1.0), radius=0.08, color=THEME["secondary"])
        lbl_min = MathTex(r"m(1, -1)", font_size=14.5, color=THEME["secondary"]).next_to(dot_min, DOWN, buff=0.10)

        # Origen e Inflexión: (0, 0)
        dot_p0 = Dot(axes.c2p(0.0, 0.0), radius=0.07, color=THEME["statement_box"])
        lbl_p0 = MathTex(r"O(0, 0)", font_size=13.5, color=WHITE).next_to(dot_p0, UP + RIGHT, buff=0.08)

        # Cortes en eje x: (-sqrt(3), 0) y (sqrt(3), 0)
        dot_x1 = Dot(axes.c2p(-np.sqrt(3), 0.0), radius=0.07, color=THEME["secondary"])
        lbl_x1 = MathTex(r"(-\sqrt{3}, 0)", font_size=13.0, color=THEME["statement_text"]).next_to(dot_x1, UP + LEFT, buff=0.08)

        dot_x2 = Dot(axes.c2p(np.sqrt(3), 0.0), radius=0.07, color=THEME["secondary"])
        lbl_x2 = MathTex(r"(\sqrt{3}, 0)", font_size=13.0, color=THEME["statement_text"]).next_to(dot_x2, UP + RIGHT, buff=0.08)

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
            Create(cubic),
            Write(cubic_lbl),
            FadeIn(dot_max),
            Write(lbl_max),
            FadeIn(dot_min),
            Write(lbl_min),
            FadeIn(dot_p0),
            Write(lbl_p0),
            FadeIn(dot_x1),
            Write(lbl_x1),
            FadeIn(dot_x2),
            Write(lbl_x2),
            run_time=2.2
        )
        self.wait(8.5)

        # Cierre institucional
        graph_group = VGroup(
            axes, axes_labels, graph_title,
            cubic, cubic_lbl,
            dot_max, lbl_max,
            dot_min, lbl_min,
            dot_p0, lbl_p0,
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
