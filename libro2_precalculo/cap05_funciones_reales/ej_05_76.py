"""
Ejercicio 5.76 - Precálculo 2 (Colección Yachay Tech / Editorial Amarun)
Capítulo 5: Funciones Reales
Tema: Sistemas de Ecuaciones Cuadráticas Homogéneas y No Lineales:
      E₁: 3x² + xy - 2y² = 0,
      E₂: 2x² - 3xy + y² = -1,  para (x, y) ∈ ℝ².

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


class Ejercicio05_76(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.76",
            topic="Sistemas No Lineales y Factorización Homogénea"
        )

        # 2. Enunciado institucional permanente (y = 2.5)
        self.setup_statement(
            desc_text="Resolver el sistema cuadrático en el plano real (x, y) ∈ ℝ²:",
            math_tex=r"(S): \begin{cases} 3x^2 + xy - 2y^2 = 0 \\ 2x^2 - 3xy + y^2 = -1 \end{cases}",
            desc_font_size=13,
            math_font_size=12,
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (6 pasos)
        self.setup_progress_bar([
            "1/6: Planteamiento del Sistema No Lineal",
            "2/6: Factorización de la Ecuación Homogénea",
            "3/6: Análisis de la Rama 1: y = -x",
            "4/6: Análisis de la Rama 2: y = 3x/2",
            "5/6: Determinación del Conjunto Solución",
            "6/6: Esquema Gráfico y Síntesis"
        ])

        # ==========================================================
        # PASO 1: Planteamiento del Sistema No Lineal
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Planteamiento e Identificación Estructural:} \\[4pt]"
            r"&\text{Consideramos el sistema } (S) \text{ en } \mathbb{R}^2: \\[4pt]"
            r"&(E_1): \quad 3x^2 + xy - 2y^2 = 0 \quad (\text{Ecuación cuadrática homogénea}) \\[4pt]"
            r"&(E_2): \quad 2x^2 - 3xy + y^2 = -1 \quad (\text{Forma cónica cuadrática}) \\[5pt]"
            r"&\text{Estrategia de resolución rigurosa:} \\[3pt]"
            r"&\bullet \text{ Como } (E_1) \text{ es homogénea de grado 2, se descompone en} \\[2pt]"
            r"&\quad \text{el producto de dos factores lineales (rectas por el origen).} \\[4pt]"
            r"&\bullet \text{ Cada recta linealiza la relación } y = m x \text{ sobre } (E_2)."
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Estructura Homogénea:\n"
            "• La ecuación (E₁) no tiene término independiente:\n"
            "  todos sus monomios son de grado 2.\n"
            "• Esto garantiza que representa un par de rectas\n"
            "  secantes que se cruzan en el origen (0, 0).\n"
            "• Factorizar (E₁) divide el sistema en dos\n"
            "  ramas univariadas completamente resolubles."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=6.2)

        # ==========================================================
        # PASO 2: Factorización de la Ecuación Homogénea
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Factorización de } (E_1): 3x^2 + xy - 2y^2 = 0: \\[4pt]"
            r"&\text{Descomponiendo el término central } xy = 3xy - 2xy: \\[4pt]"
            r"&3x^2 + 3xy - 2xy - 2y^2 = 0 \\[4pt]"
            r"&3x(x + y) - 2y(x + y) = 0 \iff (3x - 2y)(x + y) = 0 \\[5pt]"
            r"&\text{Por la propiedad del producto nulo en } \mathbb{R}: \\[4pt]"
            r"&\mathbf{\text{Rama 1: }} x + y = 0 \implies \mathbf{y = -x} \\[4pt]"
            r"&\mathbf{\text{Rama 2: }} 3x - 2y = 0 \implies \mathbf{y = \frac{3}{2}x}"
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Descomposición en Rectas:\n"
            "• El aspa simple o factorización por agrupación:\n"
            "  3x² + xy - 2y² = (3x - 2y)(x + y).\n"
            "• Un producto es cero sii al menos uno de sus\n"
            "  factores se anula en ℝ.\n"
            "• Obtenemos dos rectas en el plano: y = -x y\n"
            "  y = (3/2)x, a intersecar con (E₂)."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=6.2)

        # ==========================================================
        # PASO 3: Análisis de la Rama 1: y = -x
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Sustitución de la Rama 1: } y = -x \text{ en } (E_2): \\[4pt]"
            r"&2x^2 - 3x(-x) + (-x)^2 = -1 \\[5pt]"
            r"&2x^2 + 3x^2 + x^2 = -1 \iff 6x^2 = -1 \\[5pt]"
            r"&\implies x^2 = -\frac{1}{6} \\[5pt]"
            r"&\text{Puesto que } \forall x \in \mathbb{R}, \; x^2 \ge 0 \implies 6x^2 \ge 0 > -1, \\[4pt]"
            r"&\text{la ecuación no admite soluciones reales.} \\[5pt]"
            r"&\implies \mathbf{CS_{\text{Rama 1}} = \emptyset}"
            r"\end{aligned}",
            font_size=14.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Incompatibilidad Rama 1:\n"
            "• Reemplazando y = -x en 2x² - 3xy + y² = -1:\n"
            "  el miembro izquierdo suma 6x² ≥ 0.\n"
            "• El miembro derecho es -1 < 0.\n"
            "• En el cuerpo ℝ, ningún cuadrado es negativo.\n"
            "• Por ende, la recta y = -x no interseca a la\n"
            "  curva (E₂): su conjunto solución es vacío."
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=6.2)

        # ==========================================================
        # PASO 4: Análisis de la Rama 2: y = 3x/2
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Sustitución de la Rama 2: } y = \frac{3}{2}x \text{ en } (E_2): \\[4pt]"
            r"&2x^2 - 3x\left(\frac{3}{2}x\right) + \left(\frac{3}{2}x\right)^2 = -1 \\[5pt]"
            r"&2x^2 - \frac{9}{2}x^2 + \frac{9}{4}x^2 = -1 \\[5pt]"
            r"&\left( \frac{8 - 18 + 9}{4} \right) x^2 = -1 \iff -\frac{1}{4}x^2 = -1 \\[5pt]"
            r"&\implies x^2 = 4 \iff \mathbf{x = 2 \quad \text{ó} \quad x = -2}"
            r"\end{aligned}",
            font_size=14.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Solución Rama 2:\n"
            "• Sustituimos y = (3/2)x en (E₂).\n"
            "• Reduciendo fracciones con denominador común 4:\n"
            "  (8 - 18 + 9)/4 = -1/4.\n"
            "• Multiplicando por -4 se obtiene x² = 4.\n"
            "• La ecuación cuadrática pura produce\n"
            "  exactamente dos valores reales: x = ±2."
        )

        self.morph_step(eq4, just4, box_color=THEME["success"], advance_to_step=3, wait_time=6.2)

        # ==========================================================
        # PASO 5: Determinación del Conjunto Solución
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Cálculo de Ordenadas y Verificación:} \\[4pt]"
            r"&\text{Utilizamos la relación lineal } y = \frac{3}{2}x: \\[4pt]"
            r"&\bullet \text{ Para } x = 2 \implies y = \frac{3}{2}(2) = 3 \implies \mathbf{P_1 = (2, 3)} \\[4pt]"
            r"&\bullet \text{ Para } x = -2 \implies y = \frac{3}{2}(-2) = -3 \implies \mathbf{P_2 = (-2, -3)} \\[5pt]"
            r"&\textbf{Verificación rigurosa en el sistema } (S): \\[3pt]"
            r"&(E_1): 3(4) + (2)(3) - 2(9) = 12 + 6 - 18 = 0 \quad \checkmark \\[3pt]"
            r"&(E_2): 2(4) - 3(6) + 9 = 8 - 18 + 9 = -1 \quad \checkmark \\[5pt]"
            r"&\implies \mathbf{CS = \{(2, 3), \; (-2, -3)\}}"
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Pares Solución y Validación:\n"
            "• Evaluamos las dos abscisas en y = 3x/2,\n"
            "  obteniendo las ordenadas 3 y -3.\n"
            "• Ambos pares ordenados satisfacen estrictamente\n"
            "  las dos ecuaciones simultáneas del sistema.\n"
            "• El conjunto solución consta exactamente de los\n"
            "  dos pares simétricos CS = {(2,3), (-2,-3)}."
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=6.2)

        # ==========================================================
        # PASO 6: Esquema Gráfico y Síntesis
        # ==========================================================
        left_summary = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Síntesis y Conclusión:} \\[4pt]"
            r"&\text{Ecuación homogénea } (E_1): \\[3pt]"
            r"&(3x - 2y)(x + y) = 0 \iff y = \frac{3}{2}x \; \lor \; y = -x \\[5pt]"
            r"&\text{Cónica } (E_2): 2x^2 - 3xy + y^2 = -1 \\[4pt]"
            r"&\bullet \text{ Rama } y = -x: \quad 6x^2 = -1 \implies \emptyset \\[4pt]"
            r"&\bullet \text{ Rama } y = \frac{3}{2}x: \quad x^2 = 4 \implies x = \pm 2 \\[5pt]"
            r"&\mathbf{CS = \left\{ (2, 3), \; (-2, -3) \right\}}"
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        box6 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.18, corner_radius=0.1)

        # Sistema coordenado institucional
        axes, axes_labels = self.setup_axes(
            x_range=[-4.0, 4.0, 1],
            y_range=[-4.5, 4.5, 1],
            x_length=3.6,
            y_length=3.2,
            center=[3.0, -0.45, 0],
            include_numbers=True
        )
        graph_title = Text("Intersección en el Plano Real", font_size=12, color=WHITE).next_to(axes, UP, buff=0.15)

        # Recta solución y = 1.5x
        line_sol = axes.plot(lambda x: 1.5 * x, x_range=[-2.6, 2.6], color=THEME["secondary"], stroke_width=2.2)
        lbl_sol = MathTex(r"y = \frac{3}{2}x", font_size=10, color=THEME["secondary"]).move_to(axes.c2p(2.2, 4.0))

        # Recta descartada y = -x
        line_disc = DashedVMobject(
            axes.plot(lambda x: -x, x_range=[-2.8, 2.8], color=THEME["statement_box"], stroke_width=1.8),
            num_dashes=18
        )
        lbl_disc = MathTex(r"y = -x", font_size=10, color=THEME["statement_box"]).move_to(axes.c2p(-2.4, 3.0))

        # Ramas de la hipérbola: y = (3x ± √(x²-4))/2 con |x| ≥ 2
        hyp_r_sup = axes.plot(lambda x: 0.5 * (3*x + np.sqrt(x**2 - 4.0)), x_range=[2.001, 3.6], color=THEME["curve"], stroke_width=2.2)
        hyp_r_inf = axes.plot(lambda x: 0.5 * (3*x - np.sqrt(x**2 - 4.0)), x_range=[2.001, 3.6], color=THEME["curve"], stroke_width=2.2)
        hyp_l_sup = axes.plot(lambda x: 0.5 * (3*x + np.sqrt(x**2 - 4.0)), x_range=[-3.6, -2.001], color=THEME["curve"], stroke_width=2.2)
        hyp_l_inf = axes.plot(lambda x: 0.5 * (3*x - np.sqrt(x**2 - 4.0)), x_range=[-3.6, -2.001], color=THEME["curve"], stroke_width=2.2)

        # Puntos de intersección
        dot1 = Dot(axes.c2p(2, 3), radius=0.07, color=THEME["highlight"])
        lbl_p1 = MathTex(r"(2, 3)", font_size=10, color=THEME["highlight"]).next_to(dot1, RIGHT, buff=0.08)

        dot2 = Dot(axes.c2p(-2, -3), radius=0.07, color=THEME["highlight"])
        lbl_p2 = MathTex(r"(-2, -3)", font_size=10, color=THEME["highlight"]).next_to(dot2, LEFT, buff=0.08)

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
            Create(line_sol),
            Write(lbl_sol),
            Create(line_disc),
            Write(lbl_disc),
            Create(hyp_r_sup),
            Create(hyp_r_inf),
            Create(hyp_l_sup),
            Create(hyp_l_inf),
            FadeIn(dot1),
            Write(lbl_p1),
            FadeIn(dot2),
            Write(lbl_p2),
            run_time=2.2
        )
        self.wait(5.0)

        # Despedida y cierre institucional
        graph_group = VGroup(
            axes, axes_labels, graph_title,
            line_sol, lbl_sol, line_disc, lbl_disc,
            hyp_r_sup, hyp_r_inf, hyp_l_sup, hyp_l_inf,
            dot1, lbl_p1, dot2, lbl_p2
        )
        self.play(
            FadeOut(graph_group),
            FadeOut(self.active_math),
            FadeOut(self.active_box),
            run_time=1.4
        )
        self.wait(1.0)
