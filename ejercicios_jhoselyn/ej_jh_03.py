"""
Ejercicio 3 - Tutorías y Preparación Quiz 4 (Jhoselyn)
Tema: Análisis Completo y Gráfica de Funciones:
      Polinomio Bicuadrático: f(x) = 1/4 x^4 - 3/2 x^2 + 5/4.
      Dominio, paridad par, simetría axial bilateral respecto al eje Y,
      cortes coordenados, factorización canónica, tabla horizontal de signos por factores,
      extremos locales y absolutos, monotonía, rango, cuadro horizontal de variación (estilo Vista.webp)
      y trazado cartesiano en forma de W.

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


class EjercicioJh_03(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Jhoselyn",
            exercise="Ejercicio 3",
            topic="Análisis y Gráfica de Polinomio Bicuadrático",
            font_size=16.5
        )

        # 2. Enunciado institucional permanente con fórmula prominente (y = 2.65)
        self.setup_statement(
            desc_text="Analice completamente y grafique la función polinómica bicuadrática:",
            math_tex=r"{\color{amteal}f(x)} = {\color{amteal}\frac{1}{4}}x^4 - {\color{amred}\frac{3}{2}}x^2 + {\color{amgold}\frac{5}{4}}",
            desc_font_size=19.0,
            math_font_size=30.0,
            box_pos=np.array([0.0, 2.65, 0.0]),
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (8 pasos unificados)
        self.setup_progress_bar([
            "1/8: Dominio y Paridad",
            "2/8: Cortes Coordenados",
            "3/8: Factorización Canónica",
            "4/8: Tabla de Signos",
            "5/8: Extremos Notables",
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
            r"&\text{Al ser } {\color{amteal}f(x)} \text{ una función polinómica de grado 4:} \\[5pt]"
            r"&\mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R}} = {\color{amgreen}(-\infty, +\infty)}} \\[8pt]"
            r"&\textbf{Evaluación formal de paridad } f(-x): \\[5pt]"
            r"&f(-x) = \frac{1}{4}(-x)^4 - \frac{3}{2}(-x)^2 + \frac{5}{4} = \frac{1}{4}x^4 - \frac{3}{2}x^2 + \frac{5}{4} = f(x) \\[7pt]"
            r"&\implies {\color{amteal}f(-x) = f(x)} \implies \mathbf{\text{Función PAR}} \\[6pt]"
            r"&\implies \text{Presenta } \mathbf{\text{Simetría Axial respecto al eje vertical } {\color{amteal}Y}}."
            r"\end{aligned}",
            font_size=21.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{1. Dominio y Paridad:}\\[6pt]"
            r"$\bullet$ Toda función polinómica tiene ${\color{amgold}\operatorname{Dom}(f) = \mathbb{R}}$.\\[5pt]"
            r"$\bullet$ Evaluamos $f(-x)$ sustituyendo $-x$ en cada potencia:\\[3pt]"
            r"\hspace*{1.2em}$(-x)^4 = x^4, \quad (-x)^2 = x^2 \implies f(-x) = f(x)$.\\[5pt]"
            r"$\bullet$ Concluimos formalmente: ${\color{amteal}f \text{ es función PAR}}$.\\[5pt]"
            r"$\bullet$ Simetría bilateral: la mitad izquierda es el reflejo especular\\[2pt]"
            r"\hspace*{1.2em}exacto de la mitad derecha respecto al eje $Y$."
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
            r"&\quad f(0) = \frac{1}{4}(0)^4 - \frac{3}{2}(0)^2 + \frac{5}{4} = \mathbf{{\color{amteal}\frac{5}{4} = 1.25}} \implies \mathbf{{\color{amteal}P_y(0, 1.25)}} \\[6pt]"
            r"&\bullet \textbf{Interceptos horizontales } (f(x) = 0): \\[3pt]"
            r"&\quad \frac{1}{4}x^4 - \frac{3}{2}x^2 + \frac{5}{4} = 0 \quad (\times 4) \iff x^4 - 6x^2 + 5 = 0 \\[5pt]"
            r"&\quad (x^2 - 1)(x^2 - 5) = 0 \implies x^2 = 1 \quad \lor \quad x^2 = 5 \\[5pt]"
            r"&\quad \mathbf{{\color{amorange}x = \pm 1}}, \qquad \mathbf{{\color{amorange}x = \pm\sqrt{5} \approx \pm 2.236}} \\[5pt]"
            r"&\quad \text{Puntos: } {\color{amorange}P_{x_1}(-\sqrt{5}, 0)}, \; {\color{amorange}P_{x_2}(-1, 0)}, \; {\color{amorange}P_{x_3}(1, 0)}, \; {\color{amorange}P_{x_4}(\sqrt{5}, 0)}."
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{2. Cortes Coordenados:}\\[6pt]"
            r"$\bullet$ Eje $y$: Evaluamos $x = 0 \implies {\color{amteal}P_y\left(0, \frac{5}{4}\right) = (0, 1.25)}$.\\[5pt]"
            r"$\bullet$ Eje $x$: Resolvemos la ecuación bicuadrática $f(x) = 0$.\\[5pt]"
            r"$\bullet$ Factorización en binomios cuadráticos: $(x^2 - 1)(x^2 - 5) = 0$.\\[5pt]"
            r"$\bullet$ Cuatro raíces reales simétricas por paridad:\\[2pt]"
            r"\hspace*{1.2em}${\color{amorange}x = \pm 1} \quad \text{y} \quad {\color{amorange}x = \pm\sqrt{5} \approx \pm 2.24}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq2, just2, box_color=THEME["highlight"], advance_to_step=1, wait_time=3.2)

        # ==========================================================
        # PASO 3: Factorización Canónica de la Bicuadrática
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Factorización Canónica en Factores Lineales:} \\[6pt]"
            r"&{\color{amteal}f(x)} = \frac{1}{4}(x^2 - 1)(x^2 - 5) \\[6pt]"
            r"&\text{Descomponiendo cada diferencia de cuadrados } (u^2 - c): \\[5pt]"
            r"&\mathbf{{\color{amteal}f(x) = \frac{1}{4} \left(x + \sqrt{5}\right)(x + 1)(x - 1)\left(x - \sqrt{5}\right)}} \\[7pt]"
            r"&\bullet \mathbf{\text{Multiplicidad: }} \text{Las 4 raíces son simples (multiplicidad 1)}. \\[4pt]"
            r"&\bullet \mathbf{\text{Comportamiento: }} \text{La curva atraviesa limpiamente el eje } X \\[3pt]"
            r"&\quad \text{en cada punto de corte } \{-\sqrt{5}, -1, 1, \sqrt{5}\}."
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{3. Factorización Canónica:}\\[6pt]"
            r"$\bullet$ Expresión canónica en 4 factores lineales reales de grado 1.\\[5pt]"
            r"$\bullet$ Constante de escala positiva: $k = \frac{1}{4} > 0$.\\[5pt]"
            r"$\bullet$ Al ser raíces de orden impar, no existe rebote tangencial:\\[2pt]"
            r"\hspace*{1.2em}la curva cruza de una región de signo a otra.\\[5pt]"
            r"$\bullet$ Estructura base para el cuadro de signos por factores."
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
            r"&{\color{amteal}f(x)} = \frac{1}{4}\left(x + \sqrt{5}\right)(x + 1)(x - 1)\left(x - \sqrt{5}\right) \\[5pt]"
            r"&\begin{array}{c|c|c|c|c|c}"
            r"\text{Factor} & (-\infty, -\sqrt{5}) & (-\sqrt{5}, -1) & (-1, 1) & (1, \sqrt{5}) & (\sqrt{5}, +\infty) \\ \hline "
            r"x + \sqrt{5} & - & + & + & + & + \\ \hline "
            r"x + 1 & - & - & + & + & + \\ \hline "
            r"x - 1 & - & - & - & + & + \\ \hline "
            r"x - \sqrt{5} & - & - & - & - & + \\ \hline "
            r"f(x) & {\color{amgreen}\mathbf{+}} & {\color{amred}\mathbf{-}} & {\color{amgreen}\mathbf{+}} & {\color{amred}\mathbf{-}} & {\color{amgreen}\mathbf{+}}"
            r"\end{array} \\[6pt]"
            r"&\bullet \mathbf{\text{Positiva en: }} {\color{amgreen}\left(-\infty, -\sqrt{5}\right) \cup (-1, 1) \cup \left(\sqrt{5}, +\infty\right)} \quad (f(x) > 0). \\[3pt]"
            r"&\bullet \mathbf{\text{Negativa en: }} {\color{amred}\left(-\sqrt{5}, -1\right) \cup \left(1, \sqrt{5}\right)} \quad (f(x) < 0)."
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{4. Tabla de Signos (Guía Pág. 10):}\\[6pt]"
            r"$\bullet$ Tabla horizontal idéntica a la guía de estudio para Quiz 4.\\[5pt]"
            r"$\bullet$ 5 intervalos delimitados por las 4 raíces simétricas.\\[5pt]"
            r"$\bullet$ Regla de los signos por producto de factores en cada columna.\\[5pt]"
            r"$\bullet$ Alternancia de signos ($+, -, +, -, +$) característica de bicuadráticas."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=3.2)

        # ==========================================================
        # PASO 5: Extremos Locales y Absolutos
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Puntos Críticos y Extremos Absolutos:} \\[5pt]"
            r"&\text{Datos oficiales proporcionados en el enunciado de examen:} \\[5pt]"
            r"&\bullet \mathbf{\text{Máximo Local en el eje } Y: } \\[3pt]"
            r"&\quad f(0) = \frac{5}{4} \implies \mathbf{{\color{amgold}M\left(0, \frac{5}{4}\right) = (0, 1.25)}} \quad (\text{Cúspide central}) \\[6pt]"
            r"&\bullet \mathbf{\text{Mínimos Absolutos en } x = \pm\sqrt{3} \approx \pm 1.732: } \\[3pt]"
            r"&\quad f(\pm\sqrt{3}) = \frac{1}{4}(9) - \frac{3}{2}(3) + \frac{5}{4} = \frac{9 - 18 + 5}{4} = \mathbf{{\color{amteal}-1}} \\[5pt]"
            r"&\quad \mathbf{{\color{amteal}m_1\left(-\sqrt{3}, -1\right)}}, \qquad \mathbf{{\color{amteal}m_2\left(\sqrt{3}, -1\right)}} \\[5pt]"
            r"&\bullet \mathbf{\text{Simetría Par: }} f(-\sqrt{3}) = f(\sqrt{3}) = -1 \text{ (ambos pozos a nivel } -1)."
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{5. Extremos Notables:}\\[6pt]"
            r"$\bullet$ Datos oficiales del enunciado de Quiz 4.\\[5pt]"
            r"$\bullet$ Máximo local en la cresta central ${\color{amgold}M(0, 1.25)}$.\\[5pt]"
            r"$\bullet$ Mínimos absolutos en los dos valles idénticos:\\[2pt]"
            r"\hspace*{1.2em}${\color{amteal}m_1(-\sqrt{3}, -1)}$ y ${\color{amteal}m_2(\sqrt{3}, -1)}$.\\[5pt]"
            r"$\bullet$ La cota inferior global de toda la función es $y = -1$."
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
            r"&\bullet \textbf{Monotonía (Silueta en ``W''):} \\[4pt]"
            r"&\quad \mathbf{{\color{amred}f \text{ es decreciente en } \left(-\infty, -\sqrt{3}\right] \cup \left[0, \sqrt{3}\right]}} \\[5pt]"
            r"&\quad \mathbf{{\color{amgreen}f \text{ es creciente en } \left[-\sqrt{3}, 0\right] \cup \left[\sqrt{3}, +\infty\right)}} \\[7pt]"
            r"&\bullet \textbf{Rango (Recorrido de la Función):} \\[4pt]"
            r"&\quad \text{Valor mínimo absoluto alcanzado: } y_{\min} = -1 \\[4pt]"
            r"&\quad \lim_{x \to \pm\infty} f(x) = +\infty \\[4pt]"
            r"&\quad \mathbf{\operatorname{Ran}(f) = {\color{amgold}[-1, +\infty)}}."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{6. Monotonía y Rango:}\\[6pt]"
            r"$\bullet$ Decreciente en $(-\infty, -\sqrt{3}]$ y en $[0, \sqrt{3}]$ (${\color{amred}\searrow}$).\\[5pt]"
            r"$\bullet$ Creciente en $[-\sqrt{3}, 0]$ y en $[\sqrt{3}, +\infty)$ (${\color{amgreen}\nearrow}$).\\[5pt]"
            r"$\bullet$ Las ramas laterales se disparan al infinito: $\lim_{x \to \pm\infty} f(x) = +\infty$.\\[5pt]"
            r"$\bullet$ Recorrido vertical cerrado inferiormente: ${\color{amgold}\operatorname{Ran}(f) = [-1, +\infty)}$."
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
            r"&\begin{array}{c|c|c|c|c}"
            r"x & (-\infty, -\sqrt{3}) & (-\sqrt{3}, 0) & (0, \sqrt{3}) & (\sqrt{3}, +\infty) \\ \hline "
            r"\text{Tendencia} & {\color{amred}\mathbf{\text{Baja }(-)}} & {\color{amgreen}\mathbf{\text{Sube }(+)}} & {\color{amred}\mathbf{\text{Baja }(-)}} & {\color{amgreen}\mathbf{\text{Sube }(+)}} \\ \hline "
            r"f(x) & \searrow & \nearrow & \searrow & \nearrow"
            r"\end{array} \\[8pt]"
            r"&\bullet \mathbf{\text{Mínimos Absolutos: }} x = \pm\sqrt{3} \implies {\color{amteal}m_{1,2}(\pm\sqrt{3}, -1)} \text{ (Fondo de valles)}. \\[3pt]"
            r"&\bullet \mathbf{\text{Máximo Local: }} x = 0 \implies {\color{amgold}M(0, 1.25)} \text{ (Cúspide en eje } Y). \\[3pt]"
            r"&\bullet \mathbf{\text{Cortes } X: } P_{x_{1,4}}(\pm\sqrt{5}, 0) \text{ en ramas exteriores, } P_{x_{2,3}}(\pm 1, 0) \text{ en valles}."
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{7. Síntesis Horizontal:}\\[6pt]"
            r"$\bullet$ Cuadro horizontal consolidado según el modelo de referencia.\\[5pt]"
            r"$\bullet$ Flechas confirman la ondulación completa en forma de ``W'':\\[2pt]"
            r"\hspace*{1.2em}$\searrow \text{ hacia } m_1 \nearrow \text{ hacia } M \searrow \text{ hacia } m_2 \nearrow$.\\[5pt]"
            r"$\bullet$ Confirma la perfecta simetría par respecto al eje vertical $Y$.\\[5pt]"
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
            r"&\bullet \mathbf{\operatorname{Dom}(f) = {\color{amgold}\mathbb{R}}}, \quad \mathbf{\operatorname{Ran}(f) = {\color{amgold}[-1, +\infty)}} \\[5pt]"
            r"&\bullet \mathbf{\text{Paridad: }} {\color{amteal}\text{Par }} (f(-x) = f(x)) \implies \text{Simetría axial eje } {\color{amteal}Y} \\[5pt]"
            r"&\bullet \mathbf{\text{Máx. Local: }} {\color{amgold}M(0, 1.25)}, \quad \mathbf{\text{Mín. Abs: }} {\color{amteal}m_{1,2}\left(\pm\sqrt{3}, -1\right)} \\[5pt]"
            r"&\bullet \mathbf{\text{Cortes } X: } {\color{amorange}\pm 1, \; \pm\sqrt{5}} \quad (\sqrt{5} \approx 2.24) \\[5pt]"
            r"&\bullet \mathbf{\text{Corte } Y: } {\color{amorange}(0, 1.25)} \\[5pt]"
            r"&\bullet \mathbf{\text{Monotonía: }} \text{Silueta simétrica en ``W''} \quad {\color{amgreen}\blacksquare}"
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        box8 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.18, corner_radius=0.1)

        # Gráfico cartesiano de la función bicuadrática en W
        axes, axes_labels = self.setup_axes(
            x_range=[-3.2, 3.2, 1],
            y_range=[-1.8, 2.5, 1],
            x_length=4.5,
            y_length=3.3,
            center=[3.15, -0.75, 0],
            include_numbers=True,
            numbers_font_size=17,
            labels_font_size=20
        )
        graph_title = Tex(
            r"Gráfica de ${\color{amteal}f(x)} = {\color{amteal}\frac{1}{4}}x^4 - {\color{amred}\frac{3}{2}}x^2 + {\color{amgold}\frac{5}{4}}$",
            font_size=21.0,
            color=WHITE
        ).move_to([3.15, 1.65, 0])

        # Curva bicuadrática continua
        biquad = axes.plot(
            lambda x: 0.25 * x**4 - 1.5 * x**2 + 1.25,
            x_range=[-2.55, 2.55],
            color=THEME["curve"],
            stroke_width=2.5
        )
        biquad_lbl = MathTex(r"y = f(x)", font_size=15.0, color=THEME["curve"]).move_to(axes.c2p(2.4, 2.0))

        # Máximo local central M(0, 1.25)
        dot_max = Dot(axes.c2p(0.0, 1.25), radius=0.08, color=THEME["highlight"])
        lbl_max = MathTex(r"M(0, 1.25)", font_size=13.5, color=THEME["highlight"]).next_to(dot_max, UP, buff=0.10)

        # Mínimos absolutos m1(-sqrt(3), -1) y m2(sqrt(3), -1)
        dot_m1 = Dot(axes.c2p(-np.sqrt(3), -1.0), radius=0.08, color=THEME["secondary"])
        lbl_m1 = MathTex(r"m_1(-\sqrt{3}, -1)", font_size=12.5, color=THEME["secondary"]).next_to(dot_m1, DOWN, buff=0.10)

        dot_m2 = Dot(axes.c2p(np.sqrt(3), -1.0), radius=0.08, color=THEME["secondary"])
        lbl_m2 = MathTex(r"m_2(\sqrt{3}, -1)", font_size=12.5, color=THEME["secondary"]).next_to(dot_m2, DOWN, buff=0.10)

        # Cortes interiores en eje x: (-1, 0) y (1, 0)
        dot_x2 = Dot(axes.c2p(-1.0, 0.0), radius=0.065, color=THEME["statement_box"])
        lbl_x2 = MathTex(r"-1", font_size=13.0, color=THEME["statement_text"]).next_to(dot_x2, UP + LEFT, buff=0.06)

        dot_x3 = Dot(axes.c2p(1.0, 0.0), radius=0.065, color=THEME["statement_box"])
        lbl_x3 = MathTex(r"1", font_size=13.0, color=THEME["statement_text"]).next_to(dot_x3, UP + RIGHT, buff=0.06)

        # Cortes exteriores en eje x: (-sqrt(5), 0) y (sqrt(5), 0)
        dot_x1 = Dot(axes.c2p(-np.sqrt(5), 0.0), radius=0.065, color=THEME["secondary"])
        lbl_x1 = MathTex(r"-\sqrt{5}", font_size=12.5, color=THEME["statement_text"]).next_to(dot_x1, UP + LEFT, buff=0.08)

        dot_x4 = Dot(axes.c2p(np.sqrt(5), 0.0), radius=0.065, color=THEME["secondary"])
        lbl_x4 = MathTex(r"\sqrt{5}", font_size=12.5, color=THEME["statement_text"]).next_to(dot_x4, UP + RIGHT, buff=0.08)

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
            Create(biquad),
            Write(biquad_lbl),
            FadeIn(dot_max),
            Write(lbl_max),
            FadeIn(dot_m1),
            Write(lbl_m1),
            FadeIn(dot_m2),
            Write(lbl_m2),
            FadeIn(dot_x2),
            Write(lbl_x2),
            FadeIn(dot_x3),
            Write(lbl_x3),
            FadeIn(dot_x1),
            Write(lbl_x1),
            FadeIn(dot_x4),
            Write(lbl_x4),
            run_time=2.2
        )
        self.wait(8.5)

        # Cierre institucional
        graph_group = VGroup(
            axes, axes_labels, graph_title,
            biquad, biquad_lbl,
            dot_max, lbl_max,
            dot_m1, lbl_m1,
            dot_m2, lbl_m2,
            dot_x1, lbl_x1,
            dot_x2, lbl_x2,
            dot_x3, lbl_x3,
            dot_x4, lbl_x4
        )
        self.play(
            FadeOut(graph_group),
            FadeOut(self.active_math),
            FadeOut(self.active_box),
            run_time=1.4
        )
        self.wait(1.0)
