"""
Ejercicio 5.74 - Precálculo 2 (Colección Yachay Tech / Editorial Amarun)
Capítulo 5: Funciones Reales
Tema: Ecuaciones Trascendentes Compuestas y Reducción Polinomial de Grado 6:
      2 f⁶(x) + 5 f⁵(x) - 13 f⁴(x) - 5 f³(x) - 7 f²(x) - 10 f(x) + 8 = 0,
      para f(x) = ln(5x+4), f(x) = log₂(5-4x), f(x) = 5^{x+1}, f(x) = √(x²+x-2).

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica y rigurosa en 6 pasos.
"""

from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME


class Ejercicio05_74(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.74",
            topic="Ecuaciones Trascendentes y Reducción Polinomial"
        )

        # 2. Enunciado institucional permanente (y = 2.5)
        self.setup_statement(
            desc_text="Resolver la ecuación polinómica compuesta en f(x) para 4 modelos funcionales:",
            math_tex=r"2f^6(x) + 5f^5(x) - 13f^4(x) - 5f^3(x) - 7f^2(x) - 10f(x) + 8 = 0, \quad x \in \mathbb{R}.",
            desc_font_size=13,
            math_font_size=12,
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (6 pasos)
        self.setup_progress_bar([
            "1/6: Cambio de Variable y Factorización",
            "2/6: Caso 1: f(x) = ln(5x + 4)",
            "3/6: Caso 2: f(x) = log₂(5 - 4x)",
            "4/6: Caso 3: f(x) = 5^{x + 1}",
            "5/6: Caso 4: f(x) = √(x² + x - 2)",
            "6/6: Esquema Gráfico y Síntesis"
        ])

        # ==========================================================
        # PASO 1: Cambio de Variable y Factorización Polinomial
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Cambio de Variable y Factorización en } \mathbb{R}: \\[4pt]"
            r"&\text{Sea } u = f(x). \text{ La ecuación } (E) \text{ se expresa como:} \\[4pt]"
            r"&P(u) = 2u^6 + 5u^5 - 13u^4 - 5u^3 - 7u^2 - 10u + 8 = 0 \\[5pt]"
            r"&\text{Factorizando mediante la regla de Ruffini y raíces racionales:} \\[4pt]"
            r"&(2u - 1)(u + 1)(u - 2)(u + 4)(u^2 + 1) = 0 \\[5pt]"
            r"&\text{Puesto que } u^2 + 1 \ge 1 > 0 \quad \forall u \in \mathbb{R}, \text{ no aporta raíces reales.} \\[4pt]"
            r"&\implies \mathbf{u \in \left\{ -4, \; -1, \; \frac{1}{2}, \; 2 \right\}} \quad (\text{Valores admisibles para } f(x))"
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Reducción Algebraica:\n"
            "• Hacemos u = f(x) para desacoplar el grado 6.\n"
            "• Por Ruffini y Teorema de Raíces Racionales:\n"
            "  divisores de 8 entre divisores de 2.\n"
            "• Se obtienen 4 raíces racionales y el factor\n"
            "  irreducible cuadrático (u² + 1 > 0).\n"
            "• Las preimágenes dependerán del rango de f."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=6.2)

        # ==========================================================
        # PASO 2: Caso 1: f(x) = ln(5x + 4)
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Caso 1: } f(x) = \ln(5x + 4) \\[4pt]"
            r"&\operatorname{Dom}(f) = \{x \in \mathbb{R} : 5x+4 > 0\} = \left] -\frac{4}{5}, +\infty \right[, \quad \operatorname{Rg}(f) = \mathbb{R} \\[5pt]"
            r"&\text{Dado que } \operatorname{Rg}(f) = \mathbb{R}, \text{ los 4 valores de } u \text{ son plenamente alcanzables:} \\[4pt]"
            r"&\ln(5x+4) = u \iff 5x+4 = e^u \iff x = \frac{e^u - 4}{5} > -\frac{4}{5} \\[5pt]"
            r"&\bullet \; u = -4 \implies x_1 = \frac{e^{-4}-4}{5} \quad \bullet \; u = -1 \implies x_2 = \frac{e^{-1}-4}{5} \\[4pt]"
            r"&\bullet \; u = \frac{1}{2} \implies x_3 = \frac{\sqrt{e}-4}{5} \quad \bullet \; u = 2 \implies x_4 = \frac{e^2-4}{5} \\[5pt]"
            r"&\implies \mathbf{CS_1 = \left\{ \frac{e^{-4}-4}{5}, \; \frac{e^{-1}-4}{5}, \; \frac{\sqrt{e}-4}{5}, \; \frac{e^2-4}{5} \right\}}"
            r"\end{aligned}",
            font_size=13.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Caso Logaritmo Neperiano:\n"
            "• Dominio de definición: 5x + 4 > 0 ⇒ x > -4/5.\n"
            "• La biyección ln: ]0, +∞[ → ℝ asegura que\n"
            "  toda recta horizontal u ∈ ℝ interseca a la curva.\n"
            "• Como eᵘ > 0, x = (eᵘ - 4)/5 > -4/5 siempre.\n"
            "• Obtenemos exactamente 4 soluciones reales."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=6.2)

        # ==========================================================
        # PASO 3: Caso 2: f(x) = log₂(5 - 4x)
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Caso 2: } f(x) = \log_2(5 - 4x) \\[4pt]"
            r"&\operatorname{Dom}(f) = \{x \in \mathbb{R} : 5-4x > 0\} = \left] -\infty, \frac{5}{4} \right[, \quad \operatorname{Rg}(f) = \mathbb{R} \\[5pt]"
            r"&\text{Despejando con la función exponencial base 2:} \\[4pt]"
            r"&\log_2(5-4x) = u \iff 5-4x = 2^u \iff x = \frac{5 - 2^u}{4} < \frac{5}{4} \\[5pt]"
            r"&\bullet \; u = -4 \implies x_1 = \frac{5 - 1/16}{4} = \frac{79}{64} \\[4pt]"
            r"&\bullet \; u = -1 \implies x_2 = \frac{5 - 1/2}{4} = \frac{9}{8} \\[4pt]"
            r"&\bullet \; u = \frac{1}{2} \implies x_3 = \frac{5 - \sqrt{2}}{4} \quad \bullet \; u = 2 \implies x_4 = \frac{5-4}{4} = \frac{1}{4} \\[5pt]"
            r"&\implies \mathbf{CS_2 = \left\{ \frac{1}{4}, \; \frac{5-\sqrt{2}}{4}, \; \frac{9}{8}, \; \frac{79}{64} \right\}}"
            r"\end{aligned}",
            font_size=13.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Caso Logaritmo Base 2:\n"
            "• Condición de existencia: 5 - 4x > 0 ⇒ x < 5/4.\n"
            "• Al aplicar la función inversa 2ᵘ:\n"
            "  4x = 5 - 2ᵘ ⇒ x = (5 - 2ᵘ)/4.\n"
            "• Al ser 2ᵘ > 0, x < 5/4 para todo u real.\n"
            "• Las cuatro raíces pertenecen a Dom(f)."
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=6.2)

        # ==========================================================
        # PASO 4: Caso 3: f(x) = 5^{x + 1}
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Caso 3: } f(x) = 5^{x + 1} \\[4pt]"
            r"&\operatorname{Dom}(f) = \mathbb{R}, \qquad \mathbf{\operatorname{Rg}(f) = \left] 0, +\infty \right[} \\[5pt]"
            r"&\text{Criba de valores admisibles según el rango:} \\[4pt]"
            r"&\bullet \; u = -4 < 0 \text{ y } u = -1 < 0 \implies \mathbf{\text{Sin solución en } \mathbb{R}} \quad (5^{x+1} > 0) \\[5pt]"
            r"&\text{Resolviendo únicamente para los valores estrictamente positivos:} \\[4pt]"
            r"&\bullet \; 5^{x+1} = \frac{1}{2} \iff x+1 = \log_5(2^{-1}) \iff x_1 = -1 - \log_5(2) \\[4pt]"
            r"&\bullet \; 5^{x+1} = 2 \iff x+1 = \log_5(2) \iff x_2 = -1 + \log_5(2) \\[5pt]"
            r"&\implies \mathbf{CS_3 = \left\{ -1 - \log_5(2), \; -1 + \log_5(2) \right\}}"
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Caso Exponencial Base 5:\n"
            "• La exponencial real toma solo valores positivos.\n"
            "• Por tanto, las ramas u = -4 y u = -1 son\n"
            "  incompatibles (raíces extrañas descartadas).\n"
            "• Se aplican logaritmos en base 5 a u = 1/2 y u = 2.\n"
            "• El conjunto solución consta de 2 valores reales."
        )

        self.morph_step(eq4, just4, box_color=THEME["success"], advance_to_step=3, wait_time=6.2)

        # ==========================================================
        # PASO 5: Caso 4: f(x) = √(x² + x - 2)
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Caso 4: } f(x) = \sqrt{x^2 + x - 2} \\[4pt]"
            r"&\operatorname{Dom}(f) = \{x : (x+2)(x-1) \ge 0\} = \left] -\infty, -2 \right] \cup \left[ 1, +\infty \right[, \; \operatorname{Rg}(f) = [0, +\infty[ \\[4pt]"
            r"&\text{Descartamos } u = -4 < 0 \text{ y } u = -1 < 0 \text{ (el radical aritmético es } \ge 0\text{):} \\[4pt]"
            r"&\bullet \; \sqrt{x^2+x-2} = \frac{1}{2} \implies x^2+x-2 = \frac{1}{4} \iff 4x^2+4x-9 = 0 \\[3pt]"
            r"&\quad \implies x = \frac{-4 \pm \sqrt{160}}{8} = \mathbf{\frac{-1 \pm \sqrt{10}}{2}} \quad (\in \operatorname{Dom}(f)) \\[4pt]"
            r"&\bullet \; \sqrt{x^2+x-2} = 2 \implies x^2+x-2 = 4 \iff (x+3)(x-2) = 0 \\[3pt]"
            r"&\quad \implies \mathbf{x = -3} \quad \text{ó} \quad \mathbf{x = 2} \quad (\in \operatorname{Dom}(f)) \\[4pt]"
            r"&\implies \mathbf{CS_4 = \left\{ -3, \; \frac{-1-\sqrt{10}}{2}, \; \frac{-1+\sqrt{10}}{2}, \; 2 \right\}}"
            r"\end{aligned}",
            font_size=13,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Caso Radical Cuadrático:\n"
            "• El radicando debe ser no negativo: x ∉ ]-2, 1[.\n"
            "• El radical aritmético principal es ≥ 0,\n"
            "  descartando de nuevo u = -4 y u = -1.\n"
            "• Elevando al cuadrado: 4x² + 4x - 9 = 0 y x² + x - 6 = 0.\n"
            "• Las 4 raíces cuadráticas caen dentro de Dom(f)."
        )

        self.morph_step(eq5, just5, box_color=THEME["secondary"], advance_to_step=4, wait_time=6.2)

        # ==========================================================
        # PASO 6: Esquema Gráfico y Síntesis
        # ==========================================================
        left_summary = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Resumen de Conjuntos Solución:} \\[4pt]"
            r"&\mathbf{CS_1} = \left\{ \frac{e^{-4}-4}{5}, \; \frac{e^{-1}-4}{5}, \; \frac{\sqrt{e}-4}{5}, \; \frac{e^2-4}{5} \right\} \\[4pt]"
            r"&\mathbf{CS_2} = \left\{ \frac{1}{4}, \; \frac{5-\sqrt{2}}{4}, \; \frac{9}{8}, \; \frac{79}{64} \right\} \\[4pt]"
            r"&\mathbf{CS_3} = \left\{ -1 - \log_5(2), \; -1 + \log_5(2) \right\} \\[4pt]"
            r"&\mathbf{CS_4} = \left\{ -3, \; \frac{-1-\sqrt{10}}{2}, \; \frac{-1+\sqrt{10}}{2}, \; 2 \right\} \\[5pt]"
            r"&\text{Gráfica: Exponencial } y = 5^{x+1} \text{ y cortes } u."
            r"\end{aligned}",
            font_size=13,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        box6 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.18, corner_radius=0.1)

        # Construcción del sistema cartesiano institucional
        axes, axes_labels = self.setup_axes(
            x_range=[-2.5, 0.5, 0.5],
            y_range=[-1.5, 3.5, 1],
            x_length=3.6,
            y_length=3.0,
            center=[3.0, -0.45, 0],
            include_numbers=True
        )
        graph_title = Text("Caso 3: y = 5^{x+1} y niveles u", font_size=12, color=WHITE).next_to(axes, UP, buff=0.15)

        # Curva exponencial y = 5^{x+1}
        exp_curve = axes.plot(
            lambda x: 5**(x + 1),
            x_range=[-2.3, 0.05],
            color=THEME["curve"],
            stroke_width=2.5
        )
        curve_lbl = MathTex(r"y = 5^{x+1}", font_size=11, color=THEME["curve"]).move_to(
            axes.c2p(-0.6, 3.1)
        )

        # Niveles u = 2 (válido) y u = 0.5 (válido)
        line_u2 = axes.plot(lambda x: 2.0, x_range=[-2.3, 0.4], color=THEME["highlight"], stroke_width=1.5)
        lbl_u2 = MathTex(r"u = 2", font_size=10, color=THEME["highlight"]).move_to(axes.c2p(0.2, 2.25))

        line_u05 = axes.plot(lambda x: 0.5, x_range=[-2.3, 0.4], color=THEME["secondary"], stroke_width=1.5)
        lbl_u05 = MathTex(r"u = 1/2", font_size=10, color=THEME["secondary"]).move_to(axes.c2p(0.2, 0.75))

        # Nivel u = -1 (descartado, línea discontinua)
        line_uneg = DashedVMobject(
            axes.plot(lambda x: -1.0, x_range=[-2.3, 0.4], color=THEME["statement_box"], stroke_width=1.5),
            num_dashes=16
        )
        lbl_uneg = MathTex(r"u = -1 \text{ (sin sol.)}", font_size=9.5, color=THEME["statement_box"]).move_to(
            axes.c2p(-0.7, -1.25)
        )

        # Puntos de intersección
        x1_val = -1.0 - np.log(2.0)/np.log(5.0)  # ≈ -1.4307
        x2_val = -1.0 + np.log(2.0)/np.log(5.0)  # ≈ -0.5693
        dot1 = Dot(axes.c2p(x1_val, 0.5), radius=0.06, color=THEME["secondary"])
        dot2 = Dot(axes.c2p(x2_val, 2.0), radius=0.06, color=THEME["highlight"])

        prog_anims = self.get_advance_progress_anims(5)

        self.play(
            FadeOut(self.active_math),
            FadeOut(self.active_just),
            FadeOut(self.active_box),
            FadeIn(left_summary),
            Create(box6),
            Create(axes),
            Write(axes_labels),
            Write(graph_title),
            *prog_anims,
            run_time=1.8
        )
        self.active_box = box6
        self.active_math = left_summary
        self.active_just = None

        self.play(
            Create(exp_curve),
            Write(curve_lbl),
            Create(line_u2),
            Write(lbl_u2),
            Create(line_u05),
            Write(lbl_u05),
            Create(line_uneg),
            Write(lbl_uneg),
            FadeIn(dot1),
            FadeIn(dot2),
            run_time=2.2
        )
        self.wait(5.0)

        # Despedida y cierre institucional
        graph_group = VGroup(
            axes, axes_labels, graph_title, exp_curve, curve_lbl,
            line_u2, lbl_u2, line_u05, lbl_u05,
            line_uneg, lbl_uneg, dot1, dot2
        )
        self.play(
            FadeOut(graph_group),
            FadeOut(self.active_math),
            FadeOut(self.active_box),
            run_time=1.4
        )
        self.wait(1.0)
