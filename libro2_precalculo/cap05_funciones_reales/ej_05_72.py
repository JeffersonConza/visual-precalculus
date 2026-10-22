"""
Ejercicio 5.72 - Precálculo 2 (Colección Yachay Tech / Editorial Amarun)
Capítulo 5: Funciones Reales
Tema: Interpolación Cuadrática de Lagrange y Sistema de Vandermonde:
      Construcción de la función cuadrática P(x) que pasa por tres puntos
      dados (a₁, b₁), (a₂, b₂) y (a₃, b₃) con a₁ < a₂ < a₃.

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


class Ejercicio05_72(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.72",
            topic="Interpolación Cuadrática y Polinomio de Lagrange"
        )

        # 2. Enunciado institucional permanente (y = 2.5)
        self.setup_statement(
            desc_text="Sean b₁, b₂, b₃ ∈ ℝ y a₁, a₂, a₃ ∈ ℝ con a₁ < a₂ < a₃:",
            math_tex=r"\text{Encontrar la función cuadrática } P(x) \text{ que pasa por } (a_1, b_1), \; (a_2, b_2) \text{ y } (a_3, b_3).",
            desc_font_size=13,
            math_font_size=12,
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (6 pasos)
        self.setup_progress_bar([
            "1/6: Planteamiento y Sistema Lineal",
            "2/6: Determinante de Vandermonde y Unicidad",
            "3/6: Base Polinomial de Lagrange",
            "4/6: Fórmula Explícita de Lagrange",
            "5/6: Coeficientes Estándar (A, B, C)",
            "6/6: Esquema Gráfico y Síntesis"
        ])

        # ==========================================================
        # PASO 1: Planteamiento y Sistema Lineal
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Planteamiento del Modelo Cuadrático:} \\[4pt]"
            r"&\text{Buscamos } P(x) = A x^2 + B x + C \quad (A, B, C \in \mathbb{R}) \text{ tal que:} \\[4pt]"
            r"&P(a_1) = b_1, \quad P(a_2) = b_2, \quad P(a_3) = b_3 \\[5pt]"
            r"&\text{Esto genera un sistema lineal } 3 \times 3 \text{ en forma matricial:} \\[3pt]"
            r"&\begin{pmatrix} a_1^2 & a_1 & 1 \\ a_2^2 & a_2 & 1 \\ a_3^2 & a_3 & 1 \end{pmatrix}"
            r"\begin{pmatrix} A \\ B \\ C \end{pmatrix} = \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix} \\[5pt]"
            r"&\text{Condición de orden dada: } \mathbf{a_1 < a_2 < a_3} \quad (\text{Nodos estrictamente distintos})"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Planteamiento Lineal:\n"
            "• Toda función cuadrática tiene la forma Ax² + Bx + C.\n"
            "• Evaluar en los 3 puntos da 3 ecuaciones lineales.\n"
            "• La matriz del sistema es la matriz de Vandermonde 3×3.\n"
            "• La hipótesis a₁ < a₂ < a₃ garantiza que las abscisas\n"
            "  son distintas dos a dos."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Determinante de Vandermonde y Unicidad
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Determinante de Vandermonde y Unicidad:} \\[4pt]"
            r"&\det(V) = \begin{vmatrix} a_1^2 & a_1 & 1 \\ a_2^2 & a_2 & 1 \\ a_3^2 & a_3 & 1 \end{vmatrix} "
            r"= (a_2 - a_1)(a_3 - a_1)(a_3 - a_2) \\[5pt]"
            r"&\text{Como } a_1 < a_2 < a_3 \implies \begin{cases} a_2 - a_1 > 0 \\ a_3 - a_1 > 0 \\ a_3 - a_2 > 0 \end{cases} \implies \mathbf{\det(V) > 0} \\[5pt]"
            r"&\text{Al ser } \det(V) \neq 0, \text{ la matriz } V \text{ es estrictamente invertible.} \\[4pt]"
            r"&\implies \textbf{Existe una ÚNICA función polinomial } P(x) \text{ de grado } \le 2"
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Determinante de Vandermonde:\n"
            "• El determinante se factoriza como producto\n"
            "  de las diferencias de las abscisas (aⱼ - aᵢ).\n"
            "• Al ser a₁ < a₂ < a₃, cada diferencia es positiva.\n"
            "• det(V) > 0 asegura que el sistema es compatible\n"
            "  determinado: la solución (A, B, C) es única."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=5.0)

        # ==========================================================
        # PASO 3: Base Polinomial de Lagrange
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Base Constructiva de Lagrange:} \\[4pt]"
            r"&\text{Definimos tres polinomios cuadráticos cardinales } L_1, L_2, L_3: \\[4pt]"
            r"&L_1(x) = \frac{(x - a_2)(x - a_3)}{(a_1 - a_2)(a_1 - a_3)} \implies L_1(a_1) = 1, \; L_1(a_2) = L_1(a_3) = 0 \\[5pt]"
            r"&L_2(x) = \frac{(x - a_1)(x - a_3)}{(a_2 - a_1)(a_2 - a_3)} \implies L_2(a_2) = 1, \; L_2(a_1) = L_2(a_3) = 0 \\[5pt]"
            r"&L_3(x) = \frac{(x - a_1)(x - a_2)}{(a_3 - a_1)(a_3 - a_2)} \implies L_3(a_3) = 1, \; L_3(a_1) = L_3(a_2) = 0 \\[5pt]"
            r"&\text{Propiedad de delta de Kronecker: } \mathbf{L_i(a_j) = \delta_{ij}}"
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Polinomios de Lagrange:\n"
            "• Cada polinomio Lᵢ(x) se diseña para valer 1\n"
            "  en su propio nodo x = aᵢ, y anularse en los otros dos.\n"
            "• Los denominadores no se anulan pues a₁ < a₂ < a₃.\n"
            "• Constituyen una base del espacio vectorial\n"
            "  de polinomios de grado a lo más 2."
        )

        self.morph_step(eq3, just3, box_color=THEME["success"], advance_to_step=2, wait_time=5.0)

        # ==========================================================
        # PASO 4: Fórmula Explícita de Lagrange
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Fórmula Explícita del Polinomio Interpolador:} \\[4pt]"
            r"&P(x) = b_1 L_1(x) + b_2 L_2(x) + b_3 L_3(x) \\[5pt]"
            r"&\mathbf{P(x) = b_1 \frac{(x - a_2)(x - a_3)}{(a_1 - a_2)(a_1 - a_3)} + b_2 \frac{(x - a_1)(x - a_3)}{(a_2 - a_1)(a_2 - a_3)} + b_3 \frac{(x - a_1)(x - a_2)}{(a_3 - a_1)(a_3 - a_2)}} \\[6pt]"
            r"&\textbf{Verificación Exacta en los Nodos:} \\[3pt]"
            r"&\bullet\; P(a_1) = b_1(1) + b_2(0) + b_3(0) = \mathbf{b_1} \\[3pt]"
            r"&\bullet\; P(a_2) = b_1(0) + b_2(1) + b_3(0) = \mathbf{b_2} \\[3pt]"
            r"&\bullet\; P(a_3) = b_1(0) + b_2(0) + b_3(1) = \mathbf{b_3}"
            r"\end{aligned}",
            font_size=13,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Polinomio Interpolador de Lagrange:\n"
            "• P(x) es la combinación lineal ponderada por bᵢ.\n"
            "• En x = a₁, L₁ vale 1 y los demás 0, dando b₁.\n"
            "• Análogamente para a₂ y a₃.\n"
            "• P(x) interpola los 3 puntos de forma exacta\n"
            "  y explícita sin necesidad de invertir matrices."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=5.2)

        # ==========================================================
        # PASO 5: Coeficientes Estándar (A, B, C)
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Coeficientes en Forma Estándar } A x^2 + B x + C: \\[4pt]"
            r"&A = \frac{b_1}{(a_1-a_2)(a_1-a_3)} + \frac{b_2}{(a_2-a_1)(a_2-a_3)} + \frac{b_3}{(a_3-a_1)(a_3-a_2)} \\[5pt]"
            r"&B = -\left[ \frac{b_1(a_2+a_3)}{(a_1-a_2)(a_1-a_3)} + \frac{b_2(a_1+a_3)}{(a_2-a_1)(a_2-a_3)} + \frac{b_3(a_1+a_2)}{(a_3-a_1)(a_3-a_2)} \right] \\[5pt]"
            r"&C = \frac{b_1 a_2 a_3}{(a_1-a_2)(a_1-a_3)} + \frac{b_2 a_1 a_3}{(a_2-a_1)(a_2-a_3)} + \frac{b_3 a_1 a_2}{(a_3-a_1)(a_3-a_2)} \\[6pt]"
            r"&\bullet\; \text{Si } A \neq 0 \implies \textbf{Parábola cuadrática genuina} \\[3pt]"
            r"&\bullet\; \text{Si } A = 0 \iff \text{Puntos colineales } (\textbf{Recta afín})"
            r"\end{aligned}",
            font_size=13,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Coeficientes Canónicos:\n"
            "• Expandiendo los productos (x-aⱼ)(x-aₖ) y sumando,\n"
            "  se obtienen los coeficientes estándar A, B y C.\n"
            "• A representa la concavidad de la parábola.\n"
            "• Si los 3 puntos están alineados, A = 0 y la\n"
            "  función degenera en una recta afín de grado 1.\n"
            "• Si no son colineales, A ≠ 0 y es una parábola."
        )

        self.morph_step(eq5, just5, box_color=THEME["curve"], advance_to_step=4, wait_time=5.2)

        # ==========================================================
        # PASO 6: Síntesis Analítica y Esquema Gráfico
        # ==========================================================
        # Panel izquierdo: Cuadro Síntesis
        t_title = Text("Síntesis de Interpolación (Ej. 5.72)", font_size=13, color=THEME["header_color"], weight=BOLD)
        t_prop1 = MathTex(r"\det(V) = (a_2-a_1)(a_3-a_1)(a_3-a_2) > 0", font_size=11, color=THEME["highlight"])
        t_prop2 = MathTex(r"P(x) = \sum_{i=1}^3 b_i \prod_{j \neq i} \frac{x - a_j}{a_i - a_j}", font_size=12, color=THEME["success"])
        t_prop3 = Text("• Unicidad garantizada por Vandermonde", font_size=10, color=WHITE)
        t_prop4 = Text("• P(aᵢ) = bᵢ para i = 1, 2, 3", font_size=10, color=THEME["secondary"])
        t_prop5 = Text("• Grado ≤ 2 (Parábola si A ≠ 0, Recta si A = 0)", font_size=10, color=THEME["curve"])

        table_grp = VGroup(t_title, t_prop1, t_prop2, t_prop3, t_prop4, t_prop5).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        table_box = SurroundingRectangle(table_grp, color=THEME["statement_box"], buff=0.18, stroke_width=1.5, corner_radius=0.08)
        left_summary = VGroup(table_box, table_grp).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos para ilustrar la parábola que pasa por 3 puntos
        axes, axes_labels = self.setup_axes(
            x_range=[-1.0, 5.0, 1],
            y_range=[-1.0, 5.0, 1],
            x_length=4.8,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True
        )
        graph_title = Text("Interpolación: Parábola por 3 Nodos", font_size=12, color=WHITE).next_to(axes, UP, buff=0.15)

        # Ejemplo gráfico concreto de interpolación:
        # Nodos: (a₁, b₁) = (0, 3), (a₂, b₂) = (2, 1), (a₃, b₃) = (4, 3)
        # Parábola simétrica: P(x) = 0.5(x - 2)² + 1 = 0.5 x² - 2x + 3
        parabola = axes.plot(lambda x: 0.5 * (x - 2.0)**2 + 1.0, x_range=[-0.5, 4.5], color=THEME["curve"], stroke_width=2.6)

        # Puntos interpolados
        dot1 = Dot(axes.c2p(0, 3), color=THEME["highlight"], radius=0.07)
        lbl1 = MathTex(r"(a_1, b_1)", font_size=10, color=THEME["highlight"]).next_to(dot1, LEFT, buff=0.08)

        dot2 = Dot(axes.c2p(2, 1), color=THEME["secondary"], radius=0.07)
        lbl2 = MathTex(r"(a_2, b_2)", font_size=10, color=THEME["secondary"]).next_to(dot2, DOWN, buff=0.08)

        dot3 = Dot(axes.c2p(4, 3), color=THEME["success"], radius=0.07)
        lbl3 = MathTex(r"(a_3, b_3)", font_size=10, color=THEME["success"]).next_to(dot3, RIGHT, buff=0.08)

        leg_p = MathTex(r"P(x) = A x^2 + B x + C", font_size=11, color=THEME["curve"]).move_to(axes.c2p(2.0, 4.2))

        prog_anims = self.get_advance_progress_anims(5)

        self.play(
            FadeOut(self.active_math),
            FadeOut(self.active_just),
            FadeOut(self.active_box),
            FadeIn(left_summary),
            Create(axes),
            Write(axes_labels),
            Write(graph_title),
            *prog_anims,
            run_time=1.8
        )
        self.active_box = None
        self.active_math = None
        self.active_just = None

        self.play(
            FadeIn(dot1),
            Write(lbl1),
            FadeIn(dot2),
            Write(lbl2),
            FadeIn(dot3),
            Write(lbl3),
            run_time=1.4
        )
        self.play(
            Create(parabola),
            Write(leg_p),
            run_time=1.6
        )
        self.wait(6.0)

        # Cierre suave
        extra_mobs = [
            left_summary, axes, axes_labels, graph_title,
            dot1, lbl1, dot2, lbl2, dot3, lbl3, parabola, leg_p
        ]
        self.finish_exercise(extra_mobjects=extra_mobs)
        self.wait(0.5)
