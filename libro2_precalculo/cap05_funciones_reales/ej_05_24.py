"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.24 (Página 108 del libro / Página 127 del PDF)

Inecuación con valor absoluto anidado:
- Enunciado: Determina si A ⊆ ℝ es el conjunto solución de:
  ||x| - 5| ≥ 3,  x ∈ ℝ,  A = ]-∞, -8] ∪ [-2, 2] ∪ [8, +∞[.
- Paso 1: Desdoblamiento exterior: |u| ≥ 3 ⟺ u ≤ -3 ∨ u ≥ 3.
- Paso 2: Rama 1: |x| - 5 ≤ -3 ⟹ |x| ≤ 2 ⟹ x ∈ [-2, 2].
- Paso 3: Rama 2: |x| - 5 ≥ 3 ⟹ |x| ≥ 8 ⟹ x ∈ ]-∞, -8] ∪ [8, +∞[.
- Paso 4: Unión lógica: CS = CS₁ ∪ CS₂ = ]-∞, -8] ∪ [-2, 2] ∪ [8, +∞[.
- Paso 5: Veredicto: CS = A (VERDADERO).
- Paso 6: Interpretación gráfica cartesiana: Curva en forma de 'W' f(x) = ||x| - 5|,
  recta y = 3, y los 3 intervalos solución proyectados sobre el eje X.
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_24(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.24",
            topic="Inecuación con Valor Absoluto Anidado"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Determina si el conjunto propuesto A es el conjunto solución de la inecuación:",
            math_tex=r"||x| - 5| \ge 3, \quad x \in \mathbb{R}, \quad A = \; ]-\infty, -8] \;\cup\; [-2, 2] \;\cup\; [8, +\infty[",
            desc_font_size=15,
            math_font_size=15,
            read_time=4.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Desdoblamiento Exterior",
            "2/6: Rama Interior (|x| ≤ 2)",
            "3/6: Rama Exterior (|x| ≥ 8)",
            "4/6: Unión de Intervalos",
            "5/6: Veredicto Final (CS = A)",
            "6/6: Gráfica de ||x|-5| ≥ 3"
        ])

        # ==========================================================
        # PASO 1: Desdoblamiento del Valor Absoluto Exterior
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"\text{Propiedad: } &\forall u \in \mathbb{R}, \; c > 0: \quad |u| \ge c \iff u \le -c \;\lor\; u \ge c \\[6pt]"
            r"\text{Con } u = |x| - 5 & \text{ y } c = 3: \\[6pt]"
            r"|x| - 5 &\le -3 \quad \lor \quad |x| - 5 \ge 3"
            r"\end{aligned}",
            font_size=22,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Desdoblamiento exterior:\n"
            "Aplicamos la propiedad fundamental de inecuaciones:\n"
            "|u| ≥ c equivale a que u esté fuera de ]-c, c[.\n"
            "Tomamos el argumento interior u = |x| - 5.\n"
            "Se obtienen dos ramas disyuntivas (conectivo ∨):\n"
            "|x| - 5 ≤ -3   ó   |x| - 5 ≥ 3."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Rama Interior (|x| - 5 ≤ -3)
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"|x| - 5 &\le -3 \iff |x| \le 5 - 3 \\[6pt]"
            r"|x| &\le 2 \\[6pt]"
            r"\iff -2 &\le x \le 2 \\[6pt]"
            r"\therefore \quad CS_1 &= [-2, 2]"
            r"\end{aligned}",
            font_size=23,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Rama 1 (|x| ≤ 2):\n"
            "Sumamos 5 a ambos lados: |x| ≤ 2.\n"
            "Por propiedad de acotación en valor absoluto:\n"
            "|x| ≤ d ⟺ -d ≤ x ≤ d.\n"
            "Esto genera el intervalo cerrado central:\n"
            "CS₁ = [-2, 2]."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Rama Exterior (|x| - 5 ≥ 3)
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"|x| - 5 &\ge 3 \iff |x| \ge 3 + 5 \\[6pt]"
            r"|x| &\ge 8 \\[6pt]"
            r"\iff x &\le -8 \quad \lor \quad x \ge 8 \\[6pt]"
            r"\therefore \quad CS_2 &= \; ]-\infty, -8] \;\cup\; [8, +\infty["
            r"\end{aligned}",
            font_size=22,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Rama 2 (|x| ≥ 8):\n"
            "Sumamos 5 a ambos miembros: |x| ≥ 8.\n"
            "Nuevamente, por la propiedad exterior:\n"
            "|x| ≥ 8 ⟺ x ≤ -8 ó x ≥ 8.\n"
            "Esto genera los dos rayos infinitos laterales:\n"
            "CS₂ = ]-∞, -8] ∪ [8, +∞[."
        )

        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Unión de las Ramas (Conjunto Solución)
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"CS &= CS_1 \;\cup\; CS_2 \\[8pt]"
            r"&= [-2, 2] \;\cup\; \left( ]-\infty, -8] \;\cup\; [8, +\infty[ \right) \\[8pt]"
            r"&= \; ]-\infty, -8] \;\cup\; [-2, 2] \;\cup\; [8, +\infty["
            r"\end{aligned}",
            font_size=22,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Unión de soluciones:\n"
            "Dado que las condiciones están unidas por el\n"
            "conectivo lógico de disyunción (∨),\n"
            "el conjunto solución total es la unión de ambos:\n"
            "CS = CS₁ ∪ CS₂.\n"
            "Ordenando en la recta real de izquierda a derecha."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=4.8)

        # ==========================================================
        # PASO 5: Veredicto Final (CS = A)
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"CS &= \; ]-\infty, -8] \;\cup\; [-2, 2] \;\cup\; [8, +\infty[ \\[6pt]"
            r"A &= \; ]-\infty, -8] \;\cup\; [-2, 2] \;\cup\; [8, +\infty[ \\[8pt]"
            r"\therefore \quad CS &= A \quad \implies \quad \mathbf{\text{VERDADERO}}"
            r"\end{aligned}",
            font_size=22,
            color=THEME["success"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Veredicto formal:\n"
            "Contrastamos el conjunto solución deducido rigurosamente\n"
            "con el conjunto candidato A propuesto en el enunciado:\n"
            "Coinciden exactamente en todos sus intervalos y bordes.\n"
            "Conclusión: Sí, A es el conjunto solución (VERDADERO)."
        )

        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen geométrico
        t_title = Text("Geometría de ||x| - 5| ≥ 3:", font_size=15, color=THEME["header_color"], weight=BOLD)
        eq_curva = MathTex(r"f(x) = ||x| - 5|, \quad g(x) = 3", font_size=15, color=THEME["highlight"])
        t_desc1 = Text("• f(x) es una función par (simétrica respecto al eje Y).", font_size=12, color=THEME["statement_text"])
        t_desc2 = Text("• Vértice superior en (0, 5) y valles en (±5, 0).", font_size=12, color=THEME["curve"])
        t_desc3 = Text("• Puntos de corte con la recta y = 3:", font_size=12, color=THEME["secondary"])
        t_desc4 = Text("  x ∈ {-8, -2, 2, 8}.", font_size=12, color=THEME["secondary"])
        t_desc5 = Text("• Intervalos donde f(x) ≥ 3 (curva sobre la recta):", font_size=12, color=THEME["success"], weight=BOLD)
        t_desc6 = Text("  ]-∞, -8] ∪ [-2, 2] ∪ [8, +∞[ (tres regiones verdes).", font_size=12, color=THEME["success"])

        info_content = VGroup(t_title, eq_curva, t_desc1, t_desc2, t_desc3, t_desc4, t_desc5, t_desc6).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        info_box = SurroundingRectangle(info_content, color=THEME["statement_box"], buff=0.2, stroke_width=1.5, corner_radius=0.08)
        info_grp = VGroup(info_box, info_content).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos
        axes, axes_labels = self.setup_axes(
            x_range=[-10.0, 10.0, 2],
            y_range=[-1.0, 7.0, 2],
            x_length=5.6,
            y_length=3.8,
            center=[2.8, -0.45, 0],
            include_numbers=True
        )

        # Curva en W: f(x) = ||x| - 5|
        curve_f = axes.plot(lambda x: np.abs(np.abs(x) - 5), x_range=[-9.8, 9.8], color=THEME["highlight"], stroke_width=2.8)
        lbl_f = MathTex(r"||x|-5|", font_size=13, color=THEME["highlight"]).next_to(axes.c2p(0, 5.0), UP, buff=0.08)

        # Recta horizontal y = 3
        horiz_line = axes.plot(lambda x: 3.0, x_range=[-9.8, 9.8], color=THEME["secondary"], stroke_width=2.0)
        lbl_horiz = MathTex(r"y = 3", font_size=13, color=THEME["secondary"]).next_to(axes.c2p(7.0, 3.0), UP, buff=0.08)

        # 4 Puntos de intersección
        pts_inter = [-8.0, -2.0, 2.0, 8.0]
        dots_inter = VGroup(*[Dot(axes.c2p(x, 3.0), radius=0.06, color=THEME["success"]) for x in pts_inter])

        # Resaltado de los 3 intervalos solución sobre el eje X
        ray_left = Line(axes.c2p(-9.8, 0), axes.c2p(-8.0, 0), color=THEME["success"], stroke_width=4.5)
        seg_mid = Line(axes.c2p(-2.0, 0), axes.c2p(2.0, 0), color=THEME["success"], stroke_width=4.5)
        ray_right = Line(axes.c2p(8.0, 0), axes.c2p(9.8, 0), color=THEME["success"], stroke_width=4.5)

        dot_b1 = Dot(axes.c2p(-8.0, 0), radius=0.06, color=THEME["success"])
        dot_b2 = Dot(axes.c2p(-2.0, 0), radius=0.06, color=THEME["success"])
        dot_b3 = Dot(axes.c2p(2.0, 0), radius=0.06, color=THEME["success"])
        dot_b4 = Dot(axes.c2p(8.0, 0), radius=0.06, color=THEME["success"])

        lbl_sol = MathTex(r"CS = ]-\infty, -8] \cup [-2, 2] \cup [8, +\infty[", font_size=11, color=THEME["success"]).next_to(axes.c2p(0, 0), DOWN, buff=0.18)

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
            Create(horiz_line), Write(lbl_horiz),
            run_time=2.0
        )

        # Marcado de intersecciones y regiones solución
        self.play(
            FadeIn(dots_inter),
            Create(ray_left), Create(seg_mid), Create(ray_right),
            FadeIn(dot_b1), FadeIn(dot_b2), FadeIn(dot_b3), FadeIn(dot_b4),
            Write(lbl_sol),
            run_time=1.8
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_f, lbl_f,
            horiz_line, lbl_horiz,
            dots_inter,
            ray_left, seg_mid, ray_right,
            dot_b1, dot_b2, dot_b3, dot_b4,
            lbl_sol
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
