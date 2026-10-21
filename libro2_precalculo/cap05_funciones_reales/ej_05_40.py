"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.40 (Página 110 del libro / Página 130 del PDF)

Inecuaciones cuadráticas y racionales variadas:
1. 2x² + x - 1 > 0 ⟹ CS₁ = ]-∞, -1[ ∪ ]1/2, +∞[.
2. 2x² + x - 15 < 0, x ∈ [0, +∞[ ⟹ CS₂ = [0, 5/2[.
3. -x² + x + 7 ≥ 0 ⟹ CS₃ = [(1-√29)/2, (1+√29)/2].
4. x - 1 ≥ 3/(x+1), x ∈ ]-∞, 2[ ⟹ CS₄ = [-2, -1[.
5. x - 1/x ≥ 1 ⟹ CS₅ = [(1-√5)/2, 0[ ∪ [(1+√5)/2, +∞[.
6. 4(x-1) ≥ x(3x-4) ⟹ CS₆ = [2/3, 2].
7. -x² + 3/2 x - 1/2 < 0 ⟹ CS₇ = ]-∞, 1/2[ ∪ ]1, +∞[.
8. 4(x-1) ≥ x(3x-4), x ∈ ]-10, 10[ ⟹ CS₈ = [2/3, 2].
- Interpretación gráfica cartesiana: Inecuación 4 (recta y = x - 1 vs hipérbola y = 3/(x+1)).
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_40(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.40",
            topic="Inecuaciones Cuadráticas y Racionales Variadas"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Resuelve las 8 inecuaciones cuadráticas y racionales en sus dominios respectivos:",
            math_tex=r"1.\; 2x^2+x-1>0; \quad 2.\; 2x^2+x-15<0, \; x \ge 0; \quad 4.\; x-1 \ge \frac{3}{x+1}, \; x < 2; \quad 5.\; x-\frac{1}{x} \ge 1",
            desc_font_size=14,
            math_font_size=13,
            read_time=4.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Ítems 1 y 2 (Cuadráticas)",
            "2/6: Ítems 3 y 7 (Irracionales)",
            "3/6: Ítems 6 y 8 (Cuadráticas)",
            "4/6: Ítem 4 (Racional en ]-∞, 2[)",
            "5/6: Ítem 5 (Racional Áurea) y Resumen",
            "6/6: Gráfica de x - 1 ≥ 3/(x + 1)"
        ])

        # ==========================================================
        # PASO 1: Ítems 1 y 2 (Cuadráticas Factorizables)
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"\mathbf{1.} \quad &2x^2+x-1>0 \iff (2x-1)(x+1)>0 \\[4pt]"
            r"\implies &CS_1 = \; ]-\infty, -1[ \;\cup\; ]1/2, +\infty[ \\[6pt]"
            r"\mathbf{2.} \quad &2x^2+x-15<0 \iff (2x-5)(x+3)<0 \\[4pt]"
            r"\text{En } \mathbb{R}: \quad &x \in \; ]-3, 5/2[ \\[4pt]"
            r"\text{Con } x \in [0, +\infty[: \quad &CS_2 = [0, 5/2["
            r"\end{aligned}",
            font_size=19,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Ítems 1 y 2 (Cuadráticas):\n"
            "• Ítem 1: Factorizamos (2x - 1)(x + 1) > 0.\n"
            "  Positiva en el exterior: ]-∞, -1[ ∪ ]1/2, +∞[.\n"
            "• Ítem 2: Factorizamos (2x - 5)(x + 3) < 0.\n"
            "  Negativa en ]-3, 5/2[. Al intersecarsse con\n"
            "  el dominio propuesto [0, +∞[: CS₂ = [0, 5/2[."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Ítems 3 y 7 (Cuadráticas Irracionales)
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"\mathbf{3.} \quad &-x^2+x+7\ge 0 \iff x^2-x-7\le 0 \\[4pt]"
            r"\text{Raíces: } &x = \frac{1\pm\sqrt{29}}{2} \implies CS_3 = \left[\frac{1-\sqrt{29}}{2}, \frac{1+\sqrt{29}}{2}\right] \\[6pt]"
            r"\mathbf{7.} \quad &-x^2+\frac{3}{2}x-\frac{1}{2}<0 \iff 2x^2-3x+1>0 \\[4pt]"
            r"\iff &(2x-1)(x-1)>0 \implies CS_7 = \; ]-\infty, 1/2[ \;\cup\; ]1, +\infty["
            r"\end{aligned}",
            font_size=18,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Ítems 3 y 7 (Signo e irracionales):\n"
            "• Ítem 3: Multiplicamos por -1: x² - x - 7 ≤ 0.\n"
            "  Raíces irracionales: (1 ± √29)/2 ≈ -2.19, 3.19.\n"
            "  CS₃ = [(1 - √29)/2, (1 + √29)/2].\n"
            "• Ítem 7: Multiplicamos por -2: 2x² - 3x + 1 > 0.\n"
            "  Factorizamos: (2x - 1)(x - 1) > 0."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Ítems 6 y 8 (Cuadráticas con Dominios)
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"\mathbf{6.} \quad &4(x-1)\ge x(3x-4) \\[4pt]"
            r"\iff &4x-4 \ge 3x^2-4x \iff 3x^2-8x+4 \le 0 \\[4pt]"
            r"\iff &(3x-2)(x-2)\le 0 \implies CS_6 = [2/3, 2] \\[6pt]"
            r"\mathbf{8.} \quad &\text{Misma inecuación en } x \in \; ]-10, 10[: \\[4pt]"
            r"\text{Como } &[2/3, 2] \subset \; ]-10, 10[ \implies CS_8 = [2/3, 2]"
            r"\end{aligned}",
            font_size=19,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Ítems 6 y 8 (Desarrollo idéntico):\n"
            "Desarrollamos: 4x - 4 ≥ 3x² - 4x.\n"
            "Transponiendo: 3x² - 8x + 4 ≤ 0.\n"
            "Factorizamos: (3x - 2)(x - 2) ≤ 0 ⟹ [2/3, 2].\n"
            "• Ítem 6: en ℝ, CS₆ = [2/3, 2].\n"
            "• Ítem 8: al estar contenido en ]-10, 10[, CS₈ = [2/3, 2]."
        )

        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Ítem 4 (Inecuación Racional en ]-∞, 2[)
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"\mathbf{4.} \quad &x-1 \ge \frac{3}{x+1}, \quad \text{con } x \in \; ]-\infty, 2[ \\[4pt]"
            r"\iff &\frac{(x-1)(x+1)-3}{x+1} \ge 0 \iff \frac{x^2-4}{x+1} \ge 0 \\[4pt]"
            r"\iff &\frac{(x-2)(x+2)}{x+1} \ge 0, \quad \text{Ceros: } \{-2, -1, 2\} \\[4pt]"
            r"\text{En } \mathbb{R}: \quad &[-2, -1[ \;\cup\; [2, +\infty[ \\[4pt]"
            r"\therefore \quad &CS_4 = ([-2, -1[ \;\cup\; [2, +\infty[) \cap \; ]-\infty, 2[ = [-2, -1["
            r"\end{aligned}",
            font_size=18,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Ítem 4 (Racional acotada):\n"
            "Transponemos: (x - 1) - 3/(x + 1) ≥ 0.\n"
            "Común denominador: (x² - 4)/(x + 1) ≥ 0.\n"
            "Factorizamos: (x - 2)(x + 2)/(x + 1) ≥ 0.\n"
            "En ℝ es no-negativa en [-2, -1[ ∪ [2, +∞[.\n"
            "Intersecando con ]-∞, 2[: CS₄ = [-2, -1[."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=5.0)

        # ==========================================================
        # PASO 5: Ítem 5 (Racional Áurea) y Resumen
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"\mathbf{5.} \quad &x - \frac{1}{x} \ge 1 \iff \frac{x^2-x-1}{x} \ge 0 \\[4pt]"
            r"\text{Raíces: } &x = \frac{1\pm\sqrt{5}}{2}, \; x = 0 \implies CS_5 = \left[\frac{1-\sqrt{5}}{2}, 0\right[ \;\cup\; \left[\frac{1+\sqrt{5}}{2}, +\infty\right[ \\[6pt]"
            r"\text{\underline{Resumen:}} \quad &CS_1 = ]-\infty, -1[ \cup ]1/2, +\infty[; \quad CS_2 = [0, 5/2[ \\[3pt]"
            r"&CS_3 = \left[\frac{1-\sqrt{29}}{2}, \frac{1+\sqrt{29}}{2}\right]; \quad CS_4 = [-2, -1[ \\[3pt]"
            r"&CS_6 = CS_8 = [2/3, 2]; \quad CS_7 = ]-\infty, 1/2[ \cup ]1, +\infty["
            r"\end{aligned}",
            font_size=16,
            color=THEME["success"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Ítem 5 y consolidación global:\n"
            "• Ítem 5: x - 1/x ≥ 1 ⟺ (x² - x - 1)/x ≥ 0.\n"
            "  Las raíces involucran la razón áurea:\n"
            "  CS₅ = [(1 - √5)/2, 0[ ∪ [(1 + √5)/2, +∞[.\n"
            "Consolidamos la resolución exacta de los 8\n"
            "literales del Ejercicio 5.40 del libro."
        )

        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana (Ítem 4)
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen geométrico
        t_title = Text("Geometría de x - 1 ≥ 3/(x + 1):", font_size=15, color=THEME["header_color"], weight=BOLD)
        eq_curvas = MathTex(r"f(x) = x - 1, \quad g(x) = \frac{3}{x+1}", font_size=14, color=THEME["highlight"])
        t_desc1 = Text("• Asíntota vertical en x = -1.", font_size=12, color=THEME["statement_box"])
        t_desc2 = Text("• Intersecciones exactas en x = -2 y x = 2.", font_size=12, color=THEME["secondary"])
        t_desc3 = Text("• En ]-∞, 2[, la recta está por encima de g(x)", font_size=12, color=THEME["success"], weight=BOLD)
        t_desc4 = Text("  únicamente en el intervalo [-2, -1[.", font_size=12, color=THEME["success"])
        t_desc5 = Text("• En x = 2 se excluye por la cota estricta x < 2.", font_size=12, color=THEME["curve"])

        info_content = VGroup(t_title, eq_curvas, t_desc1, t_desc2, t_desc3, t_desc4, t_desc5).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        info_box = SurroundingRectangle(info_content, color=THEME["statement_box"], buff=0.2, stroke_width=1.5, corner_radius=0.08)
        info_grp = VGroup(info_box, info_content).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos
        axes, axes_labels = self.setup_axes(
            x_range=[-4.0, 3.5, 1],
            y_range=[-4.5, 3.5, 1],
            x_length=5.6,
            y_length=3.8,
            center=[2.8, -0.45, 0],
            include_numbers=True
        )

        # Recta f(x) = x - 1
        line_f = axes.plot(lambda x: x - 1, x_range=[-3.5, 3.0], color=THEME["highlight"], stroke_width=2.5)
        lbl_f = MathTex(r"x - 1", font_size=13, color=THEME["highlight"]).next_to(axes.c2p(2.8, 1.8), DR, buff=0.08)

        # Hipérbola g(x) = 3/(x + 1)
        hyp_left = axes.plot(lambda x: 3/(x + 1), x_range=[-3.8, -1.25], color=THEME["secondary"], stroke_width=2.2)
        hyp_right = axes.plot(lambda x: 3/(x + 1), x_range=[-0.75, 3.2], color=THEME["secondary"], stroke_width=2.2)
        lbl_g = MathTex(r"\frac{3}{x+1}", font_size=13, color=THEME["secondary"]).next_to(axes.c2p(2.5, 3/(2.5+1)), UR, buff=0.08)

        # Asíntota vertical en x = -1
        asymp = DashedLine(axes.c2p(-1.0, -4.2), axes.c2p(-1.0, 3.2), color=THEME["statement_box"], stroke_width=1.5)

        # Puntos de corte (-2, -3) y (2, 1)
        p1 = axes.c2p(-2.0, -3.0)
        p2 = axes.c2p(2.0, 1.0)
        dot1 = Dot(p1, radius=0.06, color=THEME["success"])
        dot2 = Dot(p2, radius=0.06, stroke_width=1.8, stroke_color=THEME["statement_box"], fill_color=THEME["bg_color"])

        lbl_p1 = MathTex(r"(-2, -3)", font_size=11, color=THEME["success"]).next_to(p1, DL, buff=0.08)
        lbl_p2 = MathTex(r"(2, 1)", font_size=11, color=THEME["statement_box"]).next_to(p2, UR, buff=0.08)

        # Intervalo solución sobre el eje X: [-2, -1[
        sol_seg = Line(axes.c2p(-2.0, 0), axes.c2p(-1.0, 0), color=THEME["success"], stroke_width=4.5)
        dot_x_closed = Dot(axes.c2p(-2.0, 0), radius=0.05, color=THEME["success"])
        dot_x_open = Dot(axes.c2p(-1.0, 0), radius=0.06, stroke_width=1.8, stroke_color=THEME["statement_box"], fill_color=THEME["bg_color"])

        lbl_cs_axis = MathTex(r"CS_4 = [-2, -1[", font_size=12, color=THEME["success"]).next_to(axes.c2p(-1.5, 0), DOWN, buff=0.18)

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

        # Trazado de recta, hipérbola y asíntota
        self.play(
            Create(line_f), Write(lbl_f),
            Create(hyp_left), Create(hyp_right), Write(lbl_g),
            Create(asymp),
            run_time=2.2
        )

        # Marcado de intersecciones y región solución en el eje X
        self.play(
            FadeIn(dot1), Write(lbl_p1),
            FadeIn(dot2), Write(lbl_p2),
            Create(sol_seg), FadeIn(dot_x_closed), FadeIn(dot_x_open),
            Write(lbl_cs_axis),
            run_time=1.6
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            line_f, lbl_f,
            hyp_left, hyp_right, lbl_g,
            asymp,
            dot1, dot2, lbl_p1, lbl_p2,
            sol_seg, dot_x_closed, dot_x_open,
            lbl_cs_axis
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
