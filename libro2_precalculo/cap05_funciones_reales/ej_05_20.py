r"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.20 (Página 108 del libro / Página 127 del PDF)

Tema: Inecuación Racional y Determinación del Conjunto Solución:
      Determinar si A = ]-4, +∞[ es el conjunto solución de:
      (x + 5)/(x + 4) ≥ (x - 6)/(x + 4),  x ∈ ℝ.

Estructura de la Demostración (6 Pasos):
      1. Restricción del Máximo Dominio (RMD): x + 4 ≠ 0 ⟹ x ≠ -4, Universo U = ℝ \ {-4}.
      2. Trasposición rigurosa a un miembro: (x+5)/(x+4) - (x-6)/(x+4) ≥ 0 (sin multiplicar por variable).
      3. Reducción de fracciones homogéneas: [ (x+5) - (x-6) ] / (x+4) = 11 / (x+4) ≥ 0.
      4. Criterio de signos: numerador constante 11 > 0 ⟹ denominador x + 4 > 0 ⟹ x > -4.
      5. Conjunto solución y veredicto: CS = ]-4, +∞[ = A ⟹ VERDADERO.
      6. Interpretación geométrica cartesiana: curvas f(x) y g(x), asíntota vertical x = -4,
         comparación f(x) ≥ g(x) y rayo solución ]-4, +∞[ en el eje X.

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica en 6 pasos con tipografía LaTeX HD generosa y legible.
"""

from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
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


class Ejercicio05_20(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.20",
            topic="Inecuación Racional y Conjunto Solución",
            font_size=18.0
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 5.20: Determina si A = ]-4, +∞[ es el conjunto solución de la inecuación:",
            math_tex=r"{\color{amgold}\frac{x+5}{x+4} \ge \frac{x-6}{x+4}}, \quad x \in \mathbb{R} \quad \implies \quad {\color{amteal}A = \; ]-4, +\infty[}",
            desc_font_size=20.0,
            math_font_size=25.0,
            arrange_direction=DOWN,
            buff=0.18,
            box_pos=np.array([0.0, 2.45, 0.0]),
            read_time=4.2
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Restricción de Dominio (RMD)",
            "2/6: Trasposición a un Miembro",
            "3/6: Reducción de Numeradores",
            "4/6: Criterio de Signos",
            "5/6: Conjunto Solución y Veredicto",
            "6/6: Gráfica y Región Solución"
        ], dot_spacing=0.96, label_font_size=14.5)

        # ==========================================================
        # PASO 1: Restricción del Máximo Dominio (RMD)
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Restricción del Dominio (RMD):} \\[7pt]"
            r"&\text{Para que las fracciones existan en } \mathbb{R}: \\[6pt]"
            r"&\quad x + 4 \neq 0 \iff \mathbf{{\color{amred}x \neq -4}} \\[8pt]"
            r"&\text{Definimos el Universo admisible } U: \\[6pt]"
            r"&\quad \mathbf{{\color{amgold}U = \mathbb{R} \setminus \{-4\} = \; ]-\infty, -4[ \;\cup\; ]-4, +\infty[}}"
            r"\end{aligned}",
            font_size=24.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Condición de Existencia:}\\[6pt]"
            r"$\bullet$ El denominador común $x + 4$ aparece en\\ "
            r"\hspace*{1.2em}ambos lados de la inecuación.\\[6pt]"
            r"$\bullet$ La división para cero no está definida en $\mathbb{R}$:\\ "
            r"\hspace*{1.2em}exigimos $x + 4 \neq 0 \iff {\color{amred}x \neq -4}$.\\[6pt]"
            r"$\bullet$ El conjunto universo de búsqueda es:\\ "
            r"\hspace*{1.2em}${\color{amgold}U = \mathbb{R} \setminus \{-4\} = ]-\infty, -4[ \cup ]-4, +\infty[}$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Trasposición a un Solo Miembro
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Trasposición a un Miembro:} \\[7pt]"
            r"&\text{Restamos el miembro derecho } (\forall x \in U): \\[6pt]"
            r"&\quad \mathbf{{\color{amteal}\frac{x+5}{x+4} - \frac{x-6}{x+4} \ge 0}} \\[9pt]"
            r"&\text{\textbf{¡Regla crítica de inecuaciones!}} \\[6pt]"
            r"&\quad \text{No multiplicar por } (x+4) \text{ pues su} \\[4pt]"
            r"&\quad \text{signo cambia según } x > -4 \text{ o } x < -4."
            r"\end{aligned}",
            font_size=24.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Trasposición Rigurosa:}\\[6pt]"
            r"$\bullet$ Restamos la fracción derecha para comparar\\ "
            r"\hspace*{1.2em}la expresión directamente contra cero.\\[6pt]"
            r"$\bullet$ \textbf{Principio de preservación de orden}:\\ "
            r"\hspace*{1.2em}nunca multiplicar por incógnitas sin conocer\\ "
            r"\hspace*{1.2em}su signo, pues si $x+4 < 0$ el sentido\\ "
            r"\hspace*{1.2em}de la desigualdad se invertiría."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Reducción de Fracciones Homogéneas
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Reducción de Fracciones Homogéneas:} \\[7pt]"
            r"&\text{Al tener igual denominador común } (x+4): \\[6pt]"
            r"&\quad \frac{(x + 5) - (x - 6)}{x + 4} \ge 0 \\[8pt]"
            r"&\quad \frac{x + 5 - x + 6}{x + 4} \ge 0 \\[8pt]"
            r"&\therefore \quad \mathbf{{\color{amorange}\frac{11}{x + 4} \ge 0}}"
            r"\end{aligned}",
            font_size=24.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{3. Simplificación de Numeradores:}\\[6pt]"
            r"$\bullet$ Restamos algebraicamente los numeradores:\\[4pt]"
            r"\hspace*{1.2em}$(x + 5) - (x - 6) = x - x + 5 + 6 = 11$.\\[6pt]"
            r"$\bullet$ Las variables $x$ se cancelan en el numerador.\\[6pt]"
            r"$\bullet$ Obtenemos la inecuación irreducible:\\ "
            r"\hspace*{1.2em}${\color{amorange}\frac{11}{x + 4} \ge 0}$."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Criterio de Signos de la Fracción
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Criterio de Signos:} \\[7pt]"
            r"&\frac{11}{x + 4} \ge 0 \quad \land \quad \mathbf{{\color{amgold}11 > 0 \quad (\text{Constante positiva})}} \\[8pt]"
            r"&\text{Regla de los signos para el cociente } \frac{(+)}{(+)} = (+): \\[6pt]"
            r"&\quad \frac{11}{x+4} > 0 \iff x + 4 > 0 \\[8pt]"
            r"&\therefore \quad \mathbf{{\color{amteal}x > -4 \quad (\text{con } x \neq -4)}}"
            r"\end{aligned}",
            font_size=24.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Análisis de Signos:}\\[6pt]"
            r"$\bullet$ El numerador es la constante estrictamente\\ "
            r"\hspace*{1.2em}positiva $11 > 0$ (nunca se anula).\\[6pt]"
            r"$\bullet$ Un cociente es $\ge 0$ con numerador positivo\\ "
            r"\hspace*{1.2em}si y solo si su denominador es positivo:\\[4pt]"
            r"\hspace*{1.2em}$x + 4 > 0 \iff {\color{amteal}x > -4}$.\\[6pt]"
            r"$\bullet$ El caso de igualdad a cero no es alcanzable."
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=5.0)

        # ==========================================================
        # PASO 5: Conjunto Solución y Veredicto
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Conjunto Solución y Veredicto:} \\[7pt]"
            r"&CS = \{x \in U : x > -4\} = \mathbf{{\color{amgreen}]-4, +\infty[}} \\[8pt]"
            r"&\text{Comparando con el conjunto propuesto } A: \\[6pt]"
            r"&\quad A = \; ]-4, +\infty[ \implies \mathbf{{\color{amgreen}CS = A}} \\[9pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}\text{La afirmación es VERDADERA}}} \quad \blacksquare"
            r"\end{aligned}",
            font_size=24.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Conclusión y Veredicto:}\\[6pt]"
            r"$\bullet$ Intersecamos la condición $x > -4$ con el\\ "
            r"\hspace*{1.2em}universo admisible $U = \mathbb{R} \setminus \{-4\}$:\\[4pt]"
            r"\hspace*{1.2em}${\color{amgreen}CS = \; ]-4, +\infty[}$.\\[6pt]"
            r"$\bullet$ El conjunto solución calculado coincide\\ "
            r"\hspace*{1.2em}idénticamente con el conjunto propuesto $A$.\\[6pt]"
            r"$\bullet$ \textbf{Veredicto}: ${\color{amgreen}\text{VERDADERO}}$. $\blacksquare$"
            r"\end{minipage}",
            font_size=22.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen geométrico
        t_card = Tex(
            r"\begin{minipage}{5.8cm}\raggedright "
            r"\textbf{{\color{amteal}Comportamiento Gráfico:}}\\[6pt]"
            r"$\bullet$ \textbf{Hipérbolas racionales:}\\[2pt]"
            r"\hspace*{0.8em}$f(x) = \frac{x+5}{x+4} = 1 + \frac{1}{x+4}$.\\[2pt]"
            r"\hspace*{0.8em}$g(x) = \frac{x-6}{x+4} = 1 - \frac{10}{x+4}$.\\[6pt]"
            r"$\bullet$ \textbf{Asíntota vertical común:}\\[2pt]"
            r"\hspace*{0.8em}$x = -4$ (discontinuidad esencial).\\[6pt]"
            r"$\bullet$ \textbf{Comparación de ramas:}\\[2pt]"
            r"\hspace*{0.8em}Para $x > -4$: $f(x) > g(x)$ (válida).\\[2pt]"
            r"\hspace*{0.8em}Para $x < -4$: $f(x) < g(x)$ (falsa).\\[6pt]"
            r"$\bullet$ \textbf{Rayo solución en eje X:}\\[2pt]"
            r"\hspace*{0.8em}$]-4, +\infty[$ con punto abierto en $-4$."
            r"\end{minipage}",
            font_size=18.5,
            color=WHITE
        )
        info_box = SurroundingRectangle(
            t_card,
            color=THEME["statement_box"],
            buff=0.22,
            stroke_width=1.8,
            corner_radius=0.1
        )
        info_grp = VGroup(info_box, t_card).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos
        axes, axes_labels = self.setup_axes(
            x_range=[-8.0, 4.0, 2],
            y_range=[-4.0, 5.0, 2],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=15,
            labels_font_size=21
        )

        # Asíntota vertical en x = -4
        p_asymp_top = axes.c2p(-4.0, 4.8)
        p_asymp_bot = axes.c2p(-4.0, -3.8)
        asymp_line = DashedLine(
            p_asymp_bot,
            p_asymp_top,
            color=THEME["statement_box"],
            stroke_width=2.2
        )
        lbl_asymp = MathTex(
            r"x = -4",
            font_size=16.5,
            color=THEME["statement_box"]
        ).next_to(axes.c2p(-4.0, 4.5), RIGHT, buff=0.10)

        # Curva f(x) = (x+5)/(x+4)
        curve_f_left = axes.plot(
            lambda x: (x + 5.0) / (x + 4.0),
            x_range=[-7.8, -4.3],
            color=THEME["highlight"],
            stroke_width=2.8
        )
        curve_f_right = axes.plot(
            lambda x: (x + 5.0) / (x + 4.0),
            x_range=[-3.7, 3.8],
            color=THEME["highlight"],
            stroke_width=3.2
        )
        lbl_f_tag = MathTex(
            r"f(x) = \frac{x+5}{x+4}",
            font_size=16.5,
            color=THEME["highlight"]
        ).next_to(axes.c2p(1.5, (1.5 + 5) / (1.5 + 4)), UP, buff=0.10)

        # Curva g(x) = (x-6)/(x+4)
        curve_g_left = axes.plot(
            lambda x: (x - 6.0) / (x + 4.0),
            x_range=[-7.8, -4.3],
            color=THEME["secondary"],
            stroke_width=2.4
        )
        curve_g_right = axes.plot(
            lambda x: (x - 6.0) / (x + 4.0),
            x_range=[-3.7, 3.8],
            color=THEME["secondary"],
            stroke_width=2.4
        )
        lbl_g_tag = MathTex(
            r"g(x) = \frac{x-6}{x+4}",
            font_size=16.5,
            color=THEME["secondary"]
        ).next_to(axes.c2p(1.5, (1.5 - 6) / (1.5 + 4)), DR, buff=0.10)

        # Resaltado del intervalo solución en el eje X: ]-4, +∞[
        sol_ray = Line(
            axes.c2p(-4.0, 0),
            axes.c2p(3.8, 0),
            color=THEME["success"],
            stroke_width=5.0
        )
        open_dot = Dot(
            axes.c2p(-4.0, 0),
            radius=0.08,
            stroke_width=2.2,
            stroke_color=THEME["success"],
            fill_color=THEME["bg_color"]
        )
        lbl_sol = MathTex(
            r"CS = \; ]-4, +\infty[",
            font_size=16.5,
            color=THEME["success"]
        ).next_to(axes.c2p(0.0, 0), UP, buff=0.16)

        # Transición hacia el paso 6
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

        # Trazado de la asíntota vertical
        self.play(
            Create(asymp_line),
            Write(lbl_asymp),
            run_time=1.2
        )

        # Trazado de las curvas f(x) y g(x)
        self.play(
            Create(curve_f_left), Create(curve_f_right), Write(lbl_f_tag),
            Create(curve_g_left), Create(curve_g_right), Write(lbl_g_tag),
            run_time=2.2
        )

        # Resaltado del conjunto solución en el eje X
        self.play(
            Create(sol_ray),
            FadeIn(open_dot),
            Write(lbl_sol),
            run_time=1.4
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            asymp_line, lbl_asymp,
            curve_f_left, curve_f_right, lbl_f_tag,
            curve_g_left, curve_g_right, lbl_g_tag,
            sol_ray, open_dot, lbl_sol
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
