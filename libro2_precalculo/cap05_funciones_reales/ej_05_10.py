"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.5: Invertibilidad de funciones
Ejercicio 5.10 (Página 62 del libro / Página 81 del PDF)

Demostración de la inyectividad de la función g(x) = 2x³ - 1:
- Definición de inyectividad: g(x₁) = g(x₂) ⟹ x₁ = x₂.
- Factorización por diferencia de cubos: (x₁ - x₂)(x₁² + x₁x₂ + x₂²) = 0.
- Análisis del factor cuadrático irreducible mediante completación de cuadrados.
- Conclusión formal de unicidad de preimagen.
- Interpretación gráfica en el plano cartesiano y prueba de la recta horizontal.
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_10(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.10",
            topic="Inyectividad de Funciones (Sección 5.5)"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 5.10: Sea g: ℝ → ℝ con g(x) = 2x³ - 1. Probar:",
            math_tex=r"\forall x_1, x_2 \in \mathbb{R} : g(x_1) = g(x_2) \implies x_1 = x_2 \quad [\text{g es inyectiva}]",
            desc_font_size=15,
            math_font_size=16,
            read_time=4.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Hipótesis g(x₁) = g(x₂)",
            "2/6: Cancelación y Reducción",
            "3/6: Factorización de Cubos",
            "4/6: Completación de Cuadrados",
            "5/6: Conclusión de Inyectividad",
            "6/6: Prueba Recta Horizontal"
        ])

        # ==========================================================
        # PASO 1: Hipótesis de Partida g(x₁) = g(x₂)
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"g(x_1) &= g(x_2) \\"
            r"2x_1^3 - 1 &= 2x_2^3 - 1"
            r"\end{aligned}",
            font_size=25,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Definición de inyectividad (5.40):\n"
            "Sean x₁, x₂ ∈ ℝ cualesquiera.\n"
            "Asumimos que comparten la misma imagen:\n"
            "g(x₁) = g(x₂).\n"
            "Sustituyendo la regla de correspondencia:\n"
            "2x₁³ - 1 = 2x₂³ - 1."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Cancelación de Constantes y Reducción
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"2x_1^3 &= 2x_2^3 \\"
            r"x_1^3 - x_2^3 &= 0"
            r"\end{aligned}",
            font_size=25,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Reducción algebraica:\n"
            "Sumamos 1 en ambos miembros:\n"
            "2x₁³ = 2x₂³.\n"
            "Dividimos entre 2 y transponemos:\n"
            "x₁³ - x₂³ = 0."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Factorización por Diferencia de Cubos
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"(x_1 - x_2)(x_1^2 + x_1 x_2 + x_2^2) &= 0 \\"
            r"\implies x_1 - x_2 = 0 \quad \lor \quad x_1^2 + x_1 x_2 + x_2^2 &= 0"
            r"\end{aligned}",
            font_size=22,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Diferencia de cubos:\n"
            "Aplicamos u³ - v³ = (u - v)(u² + uv + v²):\n"
            "(x₁ - x₂)(x₁² + x₁x₂ + x₂²) = 0.\n"
            "Por propiedad del producto nulo en ℝ:\n"
            "x₁ - x₂ = 0  ó  x₁² + x₁x₂ + x₂² = 0."
        )

        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=5.0)

        # ==========================================================
        # PASO 4: Completación de Cuadrados del Factor Cuadrático
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"x_1^2 + x_1 x_2 + x_2^2 &= \left(x_1 + \frac{x_2}{2}\right)^2 + \frac{3}{4}x_2^2 \ge 0 \\"
            r"= 0 &\iff x_1 = x_2 = 0"
            r"\end{aligned}",
            font_size=22,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Análisis cuadrático (Nota 65):\n"
            "Completamos cuadrados en el segundo factor:\n"
            "(x₁ + x₂/2)² + ¾x₂² ≥ 0.\n"
            "Una suma de cuadrados en ℝ solo es 0 si\n"
            "ambos términos son 0 (x₁ = x₂ = 0).\n"
            "Si (x₁, x₂) ≠ (0, 0), el factor es > 0."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=5.2)

        # ==========================================================
        # PASO 5: Conclusión Formal de Inyectividad
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"x_1 - x_2 &= 0 \implies x_1 = x_2 \\"
            r"\therefore \quad g &\text{ es inyectiva en } \mathbb{R}"
            r"\end{aligned}",
            font_size=24,
            color=THEME["success"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Conclusión formal:\n"
            "Dado que el segundo factor no anula\n"
            "soluciones distintas de x₁ = x₂ = 0,\n"
            "la única posibilidad es x₁ - x₂ = 0.\n"
            "Concluimos: x₁ = x₂ (∀ x₁, x₂ ∈ ℝ).\n"
            "Por tanto, g es inyectiva."
        )

        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.2)

        # ==========================================================
        # PASO 6: Interpretación Gráfica y Recta Horizontal
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Test de la recta horizontal
        t_title = Text("Test de la recta horizontal:", font_size=16, color=THEME["header_color"], weight=BOLD)
        eq_inv = MathTex(r"g(x) = 2x^3 - 1 \implies g^{-1}(y) = \sqrt[3]{\frac{y+1}{2}}", font_size=18, color=THEME["highlight"])
        t_desc1 = Text("• Toda recta horizontal y = y₀ corta al", font_size=13, color=THEME["statement_text"])
        t_desc2 = Text("  gráfico en un ÚNICO punto preimagen.", font_size=13, color=THEME["statement_text"])
        t_desc3 = Text("• Para y₀ = 1: 2x³ - 1 = 1 ⟹ x³ = 1 ⟹ x = 1.", font_size=13, color=THEME["success"])
        t_desc4 = Text("• Monotonía estrictamente creciente en ℝ.", font_size=13, color=THEME["curve"])

        info_content = VGroup(t_title, eq_inv, t_desc1, t_desc2, t_desc3, t_desc4).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        info_box = SurroundingRectangle(info_content, color=THEME["statement_box"], buff=0.2, stroke_width=1.5, corner_radius=0.08)
        info_grp = VGroup(info_box, info_content).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos y curva cúbica
        axes, axes_labels = self.setup_axes(
            x_range=[-1.8, 1.8, 1],
            y_range=[-3.5, 3.5, 1],
            x_length=5.6,
            y_length=3.8,
            center=[2.8, -0.45, 0],
            include_numbers=True
        )

        # Curva cúbica: g(x) = 2x³ - 1
        curve_g = axes.plot(
            lambda x: 2 * (x**3) - 1,
            x_range=[-1.08, 1.28],
            color=THEME["curve"],
            stroke_width=3.2
        )
        lbl_curve = MathTex(r"g(x) = 2x^3 - 1", font_size=15, color=THEME["curve"]).next_to(axes.c2p(1.28, 3.2), UL, buff=0.08)

        # Punto de corte con eje Y: (0, -1)
        p_corte_y = Dot(axes.c2p(0, -1), radius=0.06, color=THEME["secondary"])
        lbl_corte_y = MathTex(r"(0, -1)", font_size=13, color=THEME["secondary"]).next_to(p_corte_y, RIGHT, buff=0.12)

        # Recta horizontal de prueba y = 1
        y_test = 1.0
        line_test = DashedLine(axes.c2p(-1.6, y_test), axes.c2p(1.6, y_test), color=THEME["statement_box"], stroke_width=2.0)
        lbl_line_test = MathTex(r"y_0 = 1", font_size=13, color=THEME["statement_box"]).next_to(axes.c2p(-1.6, y_test), UP, buff=0.06)

        # Punto único de intersección: (1, 1)
        p_inter = Dot(axes.c2p(1.0, 1.0), radius=0.07, color=THEME["success"])
        lbl_inter = MathTex(r"(1, 1) \text{ [preimagen única]}", font_size=13, color=THEME["success"]).next_to(p_inter, UL, buff=0.12)

        # Línea de proyección vertical hacia x = 1
        proj_x = DashedLine(axes.c2p(1.0, 1.0), axes.c2p(1.0, 0), color=THEME["axes"], stroke_width=1.5)

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

        # Trazado de la curva y el punto característico (0, -1)
        self.play(
            Create(curve_g), Write(lbl_curve),
            FadeIn(p_corte_y), Write(lbl_corte_y),
            run_time=1.6
        )

        # Aplicación del test de la recta horizontal
        self.play(
            Create(line_test), Write(lbl_line_test),
            run_time=1.2
        )
        self.play(
            FadeIn(p_inter), Write(lbl_inter),
            Create(proj_x),
            run_time=1.4
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_g, lbl_curve,
            p_corte_y, lbl_corte_y,
            line_test, lbl_line_test,
            p_inter, lbl_inter,
            proj_x
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
