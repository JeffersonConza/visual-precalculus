"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.26 (Página 108 del libro / Página 127 del PDF)

Inecuación con valor absoluto anidado:
- Enunciado: Resuelve la inecuación:
  |3|x| - 1| ≤ 5,  x ∈ ℝ.
- Paso 1: Acotación exterior: |u| ≤ c ⟺ -c ≤ u ≤ c ⟹ -5 ≤ 3|x| - 1 ≤ 5.
- Paso 2: Despeje del valor absoluto: -4 ≤ 3|x| ≤ 6 ⟹ -4/3 ≤ |x| ≤ 2.
- Paso 3: Conjunción lógica: (|x| ≥ -4/3) ∧ (|x| ≤ 2).
- Paso 4: Análisis de ramas: |x| ≥ -4/3 es universal (S₁ = ℝ); |x| ≤ 2 ⟹ -2 ≤ x ≤ 2 (S₂ = [-2, 2]).
- Paso 5: Intersección y conclusión: CS = S₁ ∩ S₂ = [-2, 2].
- Paso 6: Interpretación gráfica cartesiana: Curva f(x) = |3|x| - 1|, recta y = 5,
  intersecciones en (±2, 5) y región sombreada [-2, 2] en el eje X.
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_26(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.26",
            topic="Inecuación con Valor Absoluto Anidado"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Resuelve la inecuación con valor absoluto en el conjunto de los números reales:",
            math_tex=r"|3|x| - 1| \le 5, \quad x \in \mathbb{R}",
            desc_font_size=15,
            math_font_size=16,
            read_time=4.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Acotación Exterior",
            "2/6: Despeje de |x|",
            "3/6: Conjunción de Condiciones",
            "4/6: Análisis de Ramas",
            "5/6: Conjunto Solución (CS)",
            "6/6: Gráfica de |3|x|-1| ≤ 5"
        ])

        # ==========================================================
        # PASO 1: Acotación Exterior del Valor Absoluto
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"\text{Propiedad: } &\forall u \in \mathbb{R}, \; c > 0: \quad |u| \le c \iff -c \le u \le c \\[6pt]"
            r"\text{Con } u = 3|x| - 1 & \text{ y } c = 5: \\[6pt]"
            r"-5 &\le 3|x| - 1 \le 5"
            r"\end{aligned}",
            font_size=22,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Acotación exterior:\n"
            "Aplicamos el teorema fundamental de acotación:\n"
            "|u| ≤ c equivale a que u esté acotado entre -c y c.\n"
            "Tomamos como argumento interior u = 3|x| - 1.\n"
            "La inecuación se transforma en la doble desigualdad:\n"
            "-5 ≤ 3|x| - 1 ≤ 5."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Despeje del Valor Absoluto Interior
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"-5 + 1 &\le 3|x| \le 5 + 1 \\[6pt]"
            r"-4 &\le 3|x| \le 6 \\[6pt]"
            r"\text{Dividiendo entre } 3 > 0 &: \\[4pt]"
            r"-\frac{4}{3} &\le |x| \le 2"
            r"\end{aligned}",
            font_size=23,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Despeje de |x|:\n"
            "Sumamos 1 en todos los miembros para aislar 3|x|:\n"
            "-4 ≤ 3|x| ≤ 6.\n"
            "Dividimos entre 3 (como 3 > 0, el sentido\n"
            "de las desigualdades se preserva estrictamente):\n"
            "-4/3 ≤ |x| ≤ 2."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Conjunción de Condiciones
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"-\frac{4}{3} \le |x| \le 2 &\iff \left(|x| \ge -\frac{4}{3}\right) \;\land\; (|x| \le 2) \\[8pt]"
            r"\text{Se desglosa en la } &\text{intersección de dos exigencias: } \\[6pt]"
            r"S_1 &= \{x \in \mathbb{R} : |x| \ge -4/3\} \\[4pt]"
            r"S_2 &= \{x \in \mathbb{R} : |x| \le 2\}"
            r"\end{aligned}",
            font_size=21,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Conjunción de condiciones:\n"
            "Toda doble desigualdad es una conjunción lógica (∧):\n"
            "Se debe cumplir simultáneamente que |x| ≥ -4/3\n"
            "y que |x| ≤ 2.\n"
            "Analizaremos cada condición por separado\n"
            "para luego intersecarlas."
        )

        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Análisis de Ramas
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"\mathbf{Rama \; 1:} \quad &|x| \ge -\frac{4}{3} \\[4pt]"
            r"\text{Como } |x| \ge 0 &> -\frac{4}{3} \quad \forall x \in \mathbb{R} \implies S_1 = \mathbb{R} \quad (\text{Trivial}) \\[8pt]"
            r"\mathbf{Rama \; 2:} \quad &|x| \le 2 \\[4pt]"
            r"\iff -2 &\le x \le 2 \implies S_2 = [-2, 2]"
            r"\end{aligned}",
            font_size=21,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Análisis deductivo de ramas:\n"
            "• En la Rama 1: por axioma, |x| ≥ 0 para todo x ∈ ℝ.\n"
            "  Como 0 > -4/3, |x| ≥ -4/3 siempre se cumple (S₁ = ℝ).\n"
            "• En la Rama 2: |x| ≤ 2 equivale al intervalo\n"
            "  acotado cerrado [-2, 2] (S₂ = [-2, 2])."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=5.0)

        # ==========================================================
        # PASO 5: Conjunto Solución (CS)
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"CS &= S_1 \;\cap\; S_2 \\[8pt]"
            r"&= \mathbb{R} \;\cap\; [-2, 2] \\[8pt]"
            r"\therefore \quad CS &= [-2, 2] = \{x \in \mathbb{R} : -2 \le x \le 2\}"
            r"\end{aligned}",
            font_size=23,
            color=THEME["success"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Conjunto solución final:\n"
            "Al intersecarsse la condición universal ℝ con el\n"
            "intervalo acotado [-2, 2], obtenemos:\n"
            "CS = ℝ ∩ [-2, 2] = [-2, 2].\n"
            "Cualquier número real entre -2 y 2 satisface la\n"
            "inecuación original de manera exacta."
        )

        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen geométrico
        t_title = Text("Geometría de |3|x| - 1| ≤ 5:", font_size=15, color=THEME["header_color"], weight=BOLD)
        eq_curva = MathTex(r"f(x) = |3|x| - 1|, \quad g(x) = 5", font_size=15, color=THEME["highlight"])
        t_desc1 = Text("• f(x) es una función par (simétrica respecto al eje Y).", font_size=12, color=THEME["statement_text"])
        t_desc2 = Text("• Vértice central en (0, 1) y valles en (±1/3, 0).", font_size=12, color=THEME["curve"])
        t_desc3 = Text("• Intersecciones con la recta horizontal y = 5:", font_size=12, color=THEME["secondary"])
        t_desc4 = Text("  P₁(-2, 5)   y   P₂(2, 5).", font_size=12, color=THEME["secondary"])
        t_desc5 = Text("• Región donde f(x) ≤ 5 (curva por debajo de la recta):", font_size=12, color=THEME["success"], weight=BOLD)
        t_desc6 = Text("  Intervalo continuo sobre el eje X: [-2, 2].", font_size=12, color=THEME["success"])

        info_content = VGroup(t_title, eq_curva, t_desc1, t_desc2, t_desc3, t_desc4, t_desc5, t_desc6).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        info_box = SurroundingRectangle(info_content, color=THEME["statement_box"], buff=0.2, stroke_width=1.5, corner_radius=0.08)
        info_grp = VGroup(info_box, info_content).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos
        axes, axes_labels = self.setup_axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-1.0, 7.0, 1],
            x_length=5.6,
            y_length=3.8,
            center=[2.8, -0.45, 0],
            include_numbers=True
        )

        # Curva f(x) = |3|x| - 1|
        curve_f = axes.plot(lambda x: np.abs(3*np.abs(x) - 1), x_range=[-2.4, 2.4], color=THEME["highlight"], stroke_width=2.8)
        lbl_f = MathTex(r"|3|x|-1|", font_size=13, color=THEME["highlight"]).next_to(axes.c2p(0, 1.0), UP, buff=0.08)

        # Recta horizontal y = 5
        line_g = axes.plot(lambda x: 5.0, x_range=[-3.2, 3.2], color=THEME["secondary"], stroke_width=2.0)
        lbl_g = MathTex(r"y = 5", font_size=13, color=THEME["secondary"]).next_to(axes.c2p(2.6, 5.0), UP, buff=0.08)

        # Puntos de corte (-2, 5) y (2, 5)
        p1 = axes.c2p(-2.0, 5.0)
        p2 = axes.c2p(2.0, 5.0)
        dot1 = Dot(p1, radius=0.06, color=THEME["success"])
        dot2 = Dot(p2, radius=0.06, color=THEME["success"])
        lbl_p1 = MathTex(r"(-2, 5)", font_size=11, color=THEME["success"]).next_to(p1, UL, buff=0.08)
        lbl_p2 = MathTex(r"(2, 5)", font_size=11, color=THEME["success"]).next_to(p2, UR, buff=0.08)

        # Segmento solución en el eje X: [-2, 2]
        sol_segment = Line(axes.c2p(-2.0, 0), axes.c2p(2.0, 0), color=THEME["success"], stroke_width=5.0)
        dot_sol_l = Dot(axes.c2p(-2.0, 0), radius=0.06, color=THEME["success"])
        dot_sol_r = Dot(axes.c2p(2.0, 0), radius=0.06, color=THEME["success"])
        lbl_cs = MathTex(r"CS = [-2, 2]", font_size=12, color=THEME["success"]).next_to(axes.c2p(0, 0), DOWN, buff=0.18)

        # Líneas guía discontinuas desde los puntos de corte al eje X
        proj_l = DashedLine(p1, axes.c2p(-2.0, 0), color=THEME["statement_box"], stroke_width=1.5)
        proj_r = DashedLine(p2, axes.c2p(2.0, 0), color=THEME["statement_box"], stroke_width=1.5)

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

        # Trazado de la curva y la recta horizontal
        self.play(
            Create(curve_f), Write(lbl_f),
            Create(line_g), Write(lbl_g),
            run_time=2.0
        )

        # Marcado de intersecciones y proyección
        self.play(
            FadeIn(dot1), Write(lbl_p1),
            FadeIn(dot2), Write(lbl_p2),
            Create(proj_l), Create(proj_r),
            run_time=1.4
        )

        # Resaltado del intervalo solución [-2, 2] en el eje X
        self.play(
            Create(sol_segment),
            FadeIn(dot_sol_l), FadeIn(dot_sol_r),
            Write(lbl_cs),
            run_time=1.4
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_f, lbl_f,
            line_g, lbl_g,
            dot1, dot2, lbl_p1, lbl_p2,
            proj_l, proj_r,
            sol_segment, dot_sol_l, dot_sol_r, lbl_cs
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
