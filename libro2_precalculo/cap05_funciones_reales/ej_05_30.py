"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.30 (Página 109 del libro / Página 128 del PDF)

Inecuaciones con radicales (Método del Ejemplo 5.40):
- Enunciado: Resuelve las inecuaciones:
  (I1): √(x² - 5x + 4) ≥ x - 3,  x ∈ ℝ
  (I2): √(x² + 9x + 18) ≥ √(2x) √(3x - 2),  x ∈ ℝ
- Paso 1: (I1) RMD y análisis de casos: x ∈ ]-∞, 1] ∪ [4, +∞[.
- Paso 2: (I1) Caso A (x < 3) ⟹ ]-∞, 1]; Caso B (x ≥ 3) ⟹ x ≥ 5. CS₁ = ]-∞, 1] ∪ [5, +∞[.
- Paso 3: (I2) RMD común: D = [2/3, +∞[.
- Paso 4: (I2) Cuadrado de miembros: x² + 9x + 18 ≥ 6x² - 4x ⟹ 5x² - 13x - 18 ≤ 0.
- Paso 5: (I2) Factorización: (5x - 18)(x + 1) ≤ 0 ⟹ CS₂ = [2/3, 18/5].
- Paso 6: Interpretación gráfica cartesiana de (I1): Curva f(x) = √(x²-5x+4), recta g(x) = x - 3,
  corte en (5, 2) e intervalos solución ]-∞, 1] ∪ [5, +∞[.
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_30(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.30",
            topic="Inecuaciones con Radicales (Ejemplo 5.40)"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Resuelve las inecuaciones con radicales en ℝ aplicando el método del Ejemplo 5.40:",
            math_tex=r"(I_1): \sqrt{x^2 - 5x + 4} \ge x - 3 \quad \text{y} \quad (I_2): \sqrt{x^2 + 9x + 18} \ge \sqrt{2x}\,\sqrt{3x - 2}",
            desc_font_size=14,
            math_font_size=15,
            read_time=4.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: (I₁) RMD y Casos de Signo",
            "2/6: (I₁) Resolución y CS₁",
            "3/6: (I₂) Dominio Múltiple RMD",
            "4/6: (I₂) Elevación al Cuadrado",
            "5/6: (I₂) Factorización y CS₂",
            "6/6: Gráfica Cartesiana de (I₁)"
        ])

        # ==========================================================
        # PASO 1: (I₁) RMD y Casos de Signo
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"\mathbf{(I_1):} \quad &\sqrt{x^2 - 5x + 4} \ge x - 3 \\[4pt]"
            r"\text{RMD: } &x^2 - 5x + 4 \ge 0 \iff (x - 1)(x - 4) \ge 0 \\[4pt]"
            r"\implies &U_1 = \; ]-\infty, 1] \;\cup\; [4, +\infty[ \\[6pt]"
            r"\text{Partición: } &\text{Caso A: } x - 3 < 0 \quad \lor \quad \text{Caso B: } x - 3 \ge 0"
            r"\end{aligned}",
            font_size=20,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. (I₁) Dominio y análisis de signo:\n"
            "El radicando debe ser no-negativo (RMD):\n"
            "(x - 1)(x - 4) ≥ 0 ⟹ U₁ = ]-∞, 1] ∪ [4, +∞[.\n"
            "Particionamos según el signo del segundo miembro:\n"
            "• Caso A: x - 3 < 0 (segundo miembro negativo).\n"
            "• Caso B: x - 3 ≥ 0 (ambos miembros no-negativos)."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: (I₁) Resolución y CS₁
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"\text{Caso A } (x < 3): \quad &\sqrt{\dots} \ge 0 > x - 3 \implies S_A = \; ]-\infty, 1] \\[6pt]"
            r"\text{Caso B } (x \ge 3): \quad &x \in [4, +\infty[ \implies x^2 - 5x + 4 \ge (x - 3)^2 \\[4pt]"
            r"&x^2 - 5x + 4 \ge x^2 - 6x + 9 \implies x \ge 5 \\[4pt]"
            r"\implies &S_B = [5, +\infty[ \\[6pt]"
            r"\therefore \quad CS_1 &= S_A \;\cup\; S_B = \; ]-\infty, 1] \;\cup\; [5, +\infty["
            r"\end{aligned}",
            font_size=19,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. (I₁) Resolución completa:\n"
            "• En Caso A (x < 3): un radical no-negativo siempre\n"
            "  supera a un número negativo en U₁ ⟹ S_A = ]-∞, 1].\n"
            "• En Caso B (x ≥ 3): elevamos al cuadrado en [4, +∞[:\n"
            "  -5x + 4 ≥ -6x + 9 ⟹ x ≥ 5 ⟹ S_B = [5, +∞[.\n"
            "Unión: CS₁ = ]-∞, 1] ∪ [5, +∞[."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: (I₂) Dominio Múltiple RMD
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"\mathbf{(I_2):} \quad &\sqrt{x^2 + 9x + 18} \ge \sqrt{2x}\,\sqrt{3x - 2} \\[6pt]"
            r"\text{RMD: } &x^2 + 9x + 18 \ge 0 \iff (x + 3)(x + 6) \ge 0 \\[4pt]"
            r"\implies &x \in \; ]-\infty, -6] \;\cup\; [-3, +\infty[ \\[4pt]"
            r"\text{Además: } &2x \ge 0 \implies x \ge 0 \quad \land \quad 3x - 2 \ge 0 \implies x \ge 2/3 \\[6pt]"
            r"\therefore \quad D &= [2/3, +\infty["
            r"\end{aligned}",
            font_size=19,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. (I₂) Dominio múltiple:\n"
            "Exigimos que los tres radicandos sean no-negativos:\n"
            "• (x + 3)(x + 6) ≥ 0 ⟹ x ≤ -6 ó x ≥ -3.\n"
            "• 2x ≥ 0 ⟹ x ≥ 0.\n"
            "• 3x - 2 ≥ 0 ⟹ x ≥ 2/3.\n"
            "Intersección común de existencia: D = [2/3, +∞[."
        )

        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: (I₂) Elevación al Cuadrado
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"\text{En } D = [2/3, +\infty[, \quad &\text{ambos lados son no-negativos:} \\[6pt]"
            r"\left(\sqrt{x^2 + 9x + 18}\right)^2 &\ge \left(\sqrt{2x}\,\sqrt{3x - 2}\right)^2 \\[6pt]"
            r"x^2 + 9x + 18 &\ge 2x(3x - 2) = 6x^2 - 4x \\[6pt]"
            r"0 &\ge 5x^2 - 13x - 18 \iff 5x^2 - 13x - 18 \le 0"
            r"\end{aligned}",
            font_size=20,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. (I₂) Elevación al cuadrado:\n"
            "Como t ↦ t² es estrictamente creciente en [0, +∞[,\n"
            "elevamos al cuadrado preservando la desigualdad:\n"
            "x² + 9x + 18 ≥ 2x(3x - 2) = 6x² - 4x.\n"
            "Trasponiendo términos al miembro derecho:\n"
            "5x² - 13x - 18 ≤ 0."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=4.8)

        # ==========================================================
        # PASO 5: (I₂) Factorización y CS₂
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"5x^2 - 13x - 18 \le 0 &\iff (5x - 18)(x + 1) \le 0 \\[6pt]"
            r"\text{Raíces: } x = -1 \;&,\; x = 18/5 \implies x \in [-1, 18/5] \\[6pt]"
            r"\text{Intersecando con } &D = [2/3, +\infty[: \\[4pt]"
            r"\therefore \quad CS_2 &= [2/3, 18/5] = [2/3, 3.6]"
            r"\end{aligned}",
            font_size=21,
            color=THEME["success"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. (I₂) Factorización y solución:\n"
            "Discriminante Δ = (-13)² - 4(5)(-18) = 529 = 23².\n"
            "Factorizamos: (5x - 18)(x + 1) ≤ 0 ⟹ x ∈ [-1, 18/5].\n"
            "Intersecamos con el dominio real D = [2/3, +∞[:\n"
            "CS₂ = [2/3, 18/5] = [2/3, 3.6]."
        )

        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana de (I₁)
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen de soluciones
        t_title = Text("Geometría y Veredictos Finales:", font_size=15, color=THEME["header_color"], weight=BOLD)
        eq_sol1 = MathTex(r"CS_1 = \; ]-\infty, 1] \;\cup\; [5, +\infty[", font_size=15, color=THEME["highlight"])
        eq_sol2 = MathTex(r"CS_2 = [2/3, 18/5]", font_size=15, color=THEME["curve"])
        t_desc1 = Text("• Curva f(x) = √(x² - 5x + 4) no existe en ]1, 4[.", font_size=12, color=THEME["statement_text"])
        t_desc2 = Text("• Recta g(x) = x - 3 con corte en (0, -3).", font_size=12, color=THEME["statement_text"])
        t_desc3 = Text("• Punto de contacto exacto: P(5, 2)  [√(4) = 2].", font_size=12, color=THEME["secondary"])
        t_desc4 = Text("• f(x) ≥ g(x) en ]-∞, 1] y [5, +∞[ (zonas verdes).", font_size=12, color=THEME["success"], weight=BOLD)

        info_content = VGroup(t_title, eq_sol1, eq_sol2, t_desc1, t_desc2, t_desc3, t_desc4).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        info_box = SurroundingRectangle(info_content, color=THEME["statement_box"], buff=0.2, stroke_width=1.5, corner_radius=0.08)
        info_grp = VGroup(info_box, info_content).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos
        axes, axes_labels = self.setup_axes(
            x_range=[-2.0, 7.0, 1],
            y_range=[-3.5, 4.5, 1],
            x_length=5.6,
            y_length=3.8,
            center=[2.8, -0.45, 0],
            include_numbers=True
        )

        # Curva f(x) = √(x² - 5x + 4)
        curve_f_left = axes.plot(lambda x: np.sqrt(x**2 - 5*x + 4), x_range=[-1.8, 1.0], color=THEME["highlight"], stroke_width=2.8)
        curve_f_right = axes.plot(lambda x: np.sqrt(x**2 - 5*x + 4), x_range=[4.0, 6.8], color=THEME["highlight"], stroke_width=2.8)
        lbl_f = MathTex(r"\sqrt{x^2-5x+4}", font_size=12, color=THEME["highlight"]).next_to(axes.c2p(4.2, 2.8), UR, buff=0.08)

        # Recta g(x) = x - 3
        line_g = axes.plot(lambda x: x - 3, x_range=[-0.5, 6.8], color=THEME["secondary"], stroke_width=2.0)
        lbl_g = MathTex(r"x - 3", font_size=12, color=THEME["secondary"]).next_to(axes.c2p(6.2, 3.2), DR, buff=0.08)

        # Punto de corte P(5, 2)
        p_corte = axes.c2p(5.0, 2.0)
        dot_corte = Dot(p_corte, radius=0.06, color=THEME["success"])
        lbl_corte = MathTex(r"(5, 2)", font_size=11, color=THEME["success"]).next_to(p_corte, UL, buff=0.08)

        # Intervalos solución en el eje X: ]-∞, 1] y [5, +∞[
        ray_left = Line(axes.c2p(-1.8, 0), axes.c2p(1.0, 0), color=THEME["success"], stroke_width=4.5)
        dot_1 = Dot(axes.c2p(1.0, 0), radius=0.06, color=THEME["success"])
        ray_right = Line(axes.c2p(5.0, 0), axes.c2p(6.8, 0), color=THEME["success"], stroke_width=4.5)
        dot_5 = Dot(axes.c2p(5.0, 0), radius=0.06, color=THEME["success"])

        lbl_cs_x = MathTex(r"CS_1", font_size=12, color=THEME["success"]).next_to(axes.c2p(5.8, 0), UP, buff=0.1)

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

        # Trazado de las curvas f(x) y g(x)
        self.play(
            Create(curve_f_left), Create(curve_f_right), Write(lbl_f),
            Create(line_g), Write(lbl_g),
            run_time=2.2
        )

        # Marcado de intersección y regiones solución
        self.play(
            FadeIn(dot_corte), Write(lbl_corte),
            Create(ray_left), FadeIn(dot_1),
            Create(ray_right), FadeIn(dot_5),
            Write(lbl_cs_x),
            run_time=1.6
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_f_left, curve_f_right, lbl_f,
            line_g, lbl_g,
            dot_corte, lbl_corte,
            ray_left, dot_1, ray_right, dot_5, lbl_cs_x
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
