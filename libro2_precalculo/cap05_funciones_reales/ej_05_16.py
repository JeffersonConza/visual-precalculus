"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.7: Monotonía y funciones a trozos
Ejercicio 5.16 (Página 75 del libro / Página 94 del PDF)

Demostración de monotonía estricta e inyectividad (Teorema 5.19):
- Función: f: ℝ → ℝ dada por f(x) = x³ + 1.
- Tasa de variación media: α = [f(x₂) - f(x₁)] / (x₂ - x₁).
- Factorización por diferencia de cubos y completación de cuadrados: α = (x₁ + x₂/2)² + 3/4 x₂² > 0.
- Monotonía estricta: α > 0 ⟹ f es estrictamente creciente en ℝ.
- Inyectividad (Teorema 5.19): f estrictamente creciente ⟹ f es inyectiva.
- Interpretación gráfica cartesiana: curva f(x) = x³ + 1, recta secante y test de la recta horizontal.
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_16(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.16",
            topic="Monotonía e Inyectividad (Teorema 5.19)"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Prueba que la función real f es estrictamente creciente y, por tanto, inyectiva:",
            math_tex=r"f: \mathbb{R} \to \mathbb{R}, \quad f(x) = x^3 + 1 \implies f \text{ es estrictamente creciente } (\nearrow\nearrow) \text{ e inyectiva}",
            desc_font_size=15,
            math_font_size=15,
            read_time=4.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Hipótesis y Tasa de Variación",
            "2/6: Factorización de Cubos",
            "3/6: Positividad Estricta de α",
            "4/6: Monotonía Estricta",
            "5/6: Prueba de Inyectividad",
            "6/6: Gráfica y Recta Horizontal"
        ])

        # ==========================================================
        # PASO 1: Hipótesis de Orden y Planteamiento de la Tasa
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"\text{Sean } x_1, x_2 &\in \mathbb{R} \quad \text{con } x_1 < x_2 \implies x_2 - x_1 > 0 \\[6pt]"
            r"\alpha &= \frac{f(x_2) - f(x_1)}{x_2 - x_1} \quad (\text{Tasa de variación media})"
            r"\end{aligned}",
            font_size=23,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Hipótesis y tasa de variación:\n"
            "Tomamos dos puntos arbitrarios con x₁ < x₂.\n"
            "Por los axiomas de orden en ℝ: x₂ - x₁ > 0.\n"
            "Planteamos la tasa de variación media α\n"
            "(pendiente de la recta secante entre x₁ y x₂)\n"
            "según el criterio de la Sección 5.7.2."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Factorización por Diferencia de Cubos
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"\alpha &= \frac{(x_2^3 + 1) - (x_1^3 + 1)}{x_2 - x_1} = \frac{x_2^3 - x_1^3}{x_2 - x_1} \\[6pt]"
            r"&= \frac{(x_2 - x_1)(x_1^2 + x_1 x_2 + x_2^2)}{x_2 - x_1} \\[6pt]"
            r"&= x_1^2 + x_1 x_2 + x_2^2 \quad (x_2 - x_1 \neq 0)"
            r"\end{aligned}",
            font_size=21,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Factorización algebraica:\n"
            "Evaluamos las imágenes f(x₂) y f(x₁).\n"
            "Las constantes se anulan: (+1 - 1 = 0).\n"
            "Factorizamos la diferencia de cubos:\n"
            "a³ - b³ = (a - b)(a² + ab + b²).\n"
            "Al ser x₂ - x₁ > 0, simplificamos el factor común."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Positividad Estricta de la Tasa α
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"\alpha &= \left(x_1 + \frac{x_2}{2}\right)^2 + \frac{3}{4}x_2^2 \ge 0 \\[6pt]"
            r"\alpha = 0 &\iff x_2 = 0 \;\land\; x_1 + \frac{x_2}{2} = 0 \iff x_1 = x_2 = 0 \\[6pt]"
            r"\text{Pero } &x_1 < x_2 \implies x_1 \neq x_2 \quad (\text{No pueden ser ambos } 0) \\[6pt]"
            r"\therefore \quad &\alpha > 0 \quad \forall x_1 < x_2"
            r"\end{aligned}",
            font_size=20,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Positividad estricta de α:\n"
            "Completamos el cuadrado respecto a x₁:\n"
            "(x₁ + x₂/2)² + (3/4)x₂² es suma de cuadrados.\n"
            "Para anularse se requeriría x₂ = 0 y x₁ = 0,\n"
            "lo que contradice la hipótesis estricta x₁ < x₂.\n"
            "Por tanto, la tasa es estrictamente positiva: α > 0."
        )

        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=5.0)

        # ==========================================================
        # PASO 4: Conclusión de Monotonía Estricta
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"\alpha = \frac{f(x_2) - f(x_1)}{x_2 - x_1} > 0 \quad &\land \quad x_2 - x_1 > 0 \\[6pt]"
            r"\implies f(x_2) - f(x_1) &> 0 \iff f(x_1) < f(x_2) \\[6pt]"
            r"\therefore \quad f \text{ es estrictamente } &\text{creciente } (\nearrow\nearrow) \text{ en } \mathbb{R}"
            r"\end{aligned}",
            font_size=21,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Conclusión de monotonía:\n"
            "Como el denominador x₂ - x₁ es positivo,\n"
            "el numerador conserva el signo estricto de α:\n"
            "f(x₂) - f(x₁) > 0 ⟺ f(x₁) < f(x₂).\n"
            "Por el criterio de monotonía (Sec. 5.7.2),\n"
            "f preserva el orden estricto en todo ℝ."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=4.8)

        # ==========================================================
        # PASO 5: Prueba de Inyectividad (Teorema 5.19)
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"\text{Teorema 5.19: } &\text{Sean } a, b \in \mathbb{R} \text{ con } a \neq b: \\[6pt]"
            r"a < b &\implies f(a) < f(b) \implies f(a) \neq f(b) \\[6pt]"
            r"a > b &\implies f(a) > f(b) \implies f(a) \neq f(b) \\[6pt]"
            r"\therefore \quad a \neq b &\implies f(a) \neq f(b) \iff f \text{ es inyectiva}"
            r"\end{aligned}",
            font_size=21,
            color=THEME["success"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Teorema 5.19 (Inyectividad):\n"
            "Por la ley de tricotomía en ℝ, si a ≠ b:\n"
            "o bien a < b (luego f(a) < f(b)),\n"
            "o bien a > b (luego f(a) > f(b)).\n"
            "En ambos casos: f(a) ≠ f(b).\n"
            "Toda función estrictamente creciente es inyectiva."
        )

        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana y Test Horizontal
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen geométrico
        t_title = Text("Propiedades geométricas:", font_size=16, color=THEME["header_color"], weight=BOLD)
        eq_curva = MathTex(r"f(x) = x^3 + 1", font_size=17, color=THEME["highlight"])
        t_desc1 = Text("• Raíz real única: x = -1,  f(-1) = 0.", font_size=13, color=THEME["statement_text"])
        t_desc2 = Text("• Intersección con el eje Y: (0, 1).", font_size=13, color=THEME["statement_text"])
        t_desc3 = Text("• Recta secante con pendiente α > 0.", font_size=13, color=THEME["curve"])
        t_desc4 = Text("• Test de la recta horizontal:", font_size=13, color=THEME["success"], weight=BOLD)
        t_desc5 = Text("  Cada recta y = c corta a la curva en", font_size=12, color=THEME["success"])
        t_desc6 = Text("  un único punto x = ∛(c - 1)  (inyectividad).", font_size=12, color=THEME["success"])

        info_content = VGroup(t_title, eq_curva, t_desc1, t_desc2, t_desc3, t_desc4, t_desc5, t_desc6).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        info_box = SurroundingRectangle(info_content, color=THEME["statement_box"], buff=0.2, stroke_width=1.5, corner_radius=0.08)
        info_grp = VGroup(info_box, info_content).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos
        axes, axes_labels = self.setup_axes(
            x_range=[-2.2, 2.2, 1],
            y_range=[-3.0, 4.0, 1],
            x_length=5.6,
            y_length=3.8,
            center=[2.8, -0.45, 0],
            include_numbers=True
        )

        # Curva cúbica f(x) = x³ + 1
        curve_f = axes.plot(lambda x: x**3 + 1, x_range=[-1.55, 1.42], color=THEME["highlight"], stroke_width=3.2)
        lbl_f = MathTex(r"f(x) = x^3 + 1", font_size=14, color=THEME["highlight"]).next_to(axes.c2p(1.3, 3.2), LEFT, buff=0.1)

        # Puntos notables: corte en Y (0,1) y raíz (-1,0)
        p_corte_y = axes.c2p(0.0, 1.0)
        dot_corte_y = Dot(p_corte_y, radius=0.06, color=THEME["secondary"])
        lbl_corte_y = MathTex(r"(0, 1)", font_size=12, color=THEME["secondary"]).next_to(p_corte_y, DR, buff=0.08)

        p_raiz = axes.c2p(-1.0, 0.0)
        dot_raiz = Dot(p_raiz, radius=0.06, color=THEME["secondary"])
        lbl_raiz = MathTex(r"(-1, 0)", font_size=12, color=THEME["secondary"]).next_to(p_raiz, DL, buff=0.08)

        # Recta secante entre x₁ = -0.5 (y = 0.875) y x₂ = 1.0 (y = 2.0)
        x1_val, x2_val = -0.6, 1.0
        y1_val, y2_val = x1_val**3 + 1, x2_val**3 + 1
        p_sec1 = axes.c2p(x1_val, y1_val)
        p_sec2 = axes.c2p(x2_val, y2_val)

        dot_sec1 = Dot(p_sec1, radius=0.05, color=THEME["curve"])
        dot_sec2 = Dot(p_sec2, radius=0.05, color=THEME["curve"])
        secant_line = Line(axes.c2p(-1.1, (-1.1 - x1_val)*((y2_val-y1_val)/(x2_val-x1_val)) + y1_val),
                           axes.c2p(1.3, (1.3 - x1_val)*((y2_val-y1_val)/(x2_val-x1_val)) + y1_val),
                           color=THEME["curve"], stroke_width=1.8)
        lbl_sec = MathTex(r"\text{Secante } (\alpha > 0)", font_size=12, color=THEME["curve"]).next_to(p_sec1, UP, buff=0.1)

        # Recta horizontal ilustrativa para el test de inyectividad: y = 2
        p_test_int = axes.c2p(1.0, 2.0)
        horiz_line = DashedLine(axes.c2p(-2.0, 2.0), axes.c2p(2.0, 2.0), color=THEME["success"], stroke_width=1.6)
        dot_test = Dot(p_test_int, radius=0.06, color=THEME["success"])
        lbl_test = MathTex(r"y = 2 \implies x = 1", font_size=12, color=THEME["success"]).next_to(p_test_int, UP, buff=0.08)

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

        # Trazado de la curva y puntos notables
        self.play(
            Create(curve_f), Write(lbl_f),
            FadeIn(dot_corte_y), Write(lbl_corte_y),
            FadeIn(dot_raiz), Write(lbl_raiz),
            run_time=1.8
        )

        # Trazado de la secante demostrando α > 0
        self.play(
            Create(secant_line),
            FadeIn(dot_sec1), FadeIn(dot_sec2),
            Write(lbl_sec),
            run_time=1.4
        )

        # Test de la recta horizontal demostrando inyectividad
        self.play(
            Create(horiz_line),
            FadeIn(dot_test),
            Write(lbl_test),
            run_time=1.4
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_f, lbl_f,
            dot_corte_y, lbl_corte_y,
            dot_raiz, lbl_raiz,
            secant_line, dot_sec1, dot_sec2, lbl_sec,
            horiz_line, dot_test, lbl_test
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
