"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.36 (Página 110 del libro / Página 129 del PDF)

Inecuaciones cuadráticas y fraccionarias con valor absoluto:
1. x² - 3x + 2 > 0,  A = ℝ \ [1, 2]  (VERDADERO).
2. 1 - x - 2x² ≥ 0,  A = [-1, 1/2]  (VERDADERO).
3. 4x² - 9x < 0,  A = ]0, 9/4[  (VERDADERO).
4. (|x+1| - |x-3|) / (x - 1) ≥ 2,  A = [-1, 3] \ {1}  (VERDADERO).
- Interpretación gráfica cartesiana: Función a trozos f(x) = (|x+1|-|x-3|)/(x-1) y recta y = 2.
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_36(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.36",
            topic="Inecuaciones Cuadráticas y Fraccionarias"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Determina si el conjunto propuesto A es el conjunto solución de cada inecuación:",
            math_tex=r"1.\; x^2-3x+2>0;\; 2.\; 1-x-2x^2\ge 0;\; 3.\; 4x^2-9x<0;\; 4.\; \frac{|x+1|-|x-3|}{x-1}\ge 2",
            desc_font_size=14,
            math_font_size=14,
            read_time=4.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Inecuación 1 (Complemento)",
            "2/6: Inecuación 2 (Inversión de Signo)",
            "3/6: Inecuación 3 (Factor Común)",
            "4/6: Inecuación 4 (Zonas Críticas)",
            "5/6: Inecuación 4 (Veredicto Global)",
            "6/6: Gráfica de (|x+1|-|x-3|)/(x-1) ≥ 2"
        ])

        # ==========================================================
        # PASO 1: Inecuación 1: x² - 3x + 2 > 0
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"\mathbf{1.} \quad &x^2 - 3x + 2 > 0 \\[4pt]"
            r"\iff &(x - 1)(x - 2) > 0 \\[4pt]"
            r"\text{Raíces: } &x = 1, \; x = 2 \implies x \in \; ]-\infty, 1[ \;\cup\; ]2, +\infty[ \\[6pt]"
            r"\therefore \quad &CS_1 = \mathbb{R} \setminus [1, 2] = A \implies \mathbf{\text{VERDADERO}}"
            r"\end{aligned}",
            font_size=20,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Inecuación cuadrática 1:\n"
            "Factorizamos el trinomio: (x - 1)(x - 2) > 0.\n"
            "La parábola se abre hacia arriba y es positiva\n"
            "estrictamente fuera del intervalo de sus raíces:\n"
            "]-∞, 1[ ∪ ]2, +∞[ = ℝ \\ [1, 2].\n"
            "Coincide con A propuesto ⟹ VERDADERO."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Inecuación 2: 1 - x - 2x² ≥ 0
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"\mathbf{2.} \quad &1 - x - 2x^2 \ge 0 \\[4pt]"
            r"\text{Multiplicando } &\text{por } -1 \text{ (se invierte el orden):} \\[4pt]"
            r"&2x^2 + x - 1 \le 0 \iff (2x - 1)(x + 1) \le 0 \\[6pt]"
            r"\text{Raíces: } &x = -1, \; x = 1/2 \implies x \in [-1, 1/2] \\[6pt]"
            r"\therefore \quad &CS_2 = [-1, 1/2] = A \implies \mathbf{\text{VERDADERO}}"
            r"\end{aligned}",
            font_size=19,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Inecuación cuadrática 2:\n"
            "Multiplicamos por -1 para positivizar x²:\n"
            "2x² + x - 1 ≤ 0.\n"
            "Factorizamos: (2x - 1)(x + 1) ≤ 0.\n"
            "Es no-positiva en el intervalo cerrado de raíces:\n"
            "CS = [-1, 1/2] = A propuesto ⟹ VERDADERO."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Inecuación 3: 4x² - 9x < 0
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"\mathbf{3.} \quad &4x^2 - 9x < 0 \\[4pt]"
            r"\iff &x(4x - 9) < 0 \\[4pt]"
            r"\text{Raíces: } &x = 0, \; x = 9/4 \implies x \in \; ]0, 9/4[ \\[6pt]"
            r"\therefore \quad &CS_3 = \; ]0, 9/4[ = A \implies \mathbf{\text{VERDADERO}}"
            r"\end{aligned}",
            font_size=20,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Inecuación cuadrática 3:\n"
            "Extraemos el factor común x: x(4x - 9) < 0.\n"
            "Las raíces reales son x = 0 y x = 9/4.\n"
            "El producto de factores con signos opuestos ocurre\n"
            "en el interior del intervalo: ]0, 9/4[.\n"
            "Coincide con A propuesto ⟹ VERDADERO."
        )

        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Inecuación 4: Zonas Críticas
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"\mathbf{4.} \quad &\frac{|x+1| - |x-3|}{x - 1} \ge 2, \quad \text{RMD: } x \neq 1 \\[6pt]"
            r"\text{Ceros: } &x = -1, \; x = 1, \; x = 3 \\[6pt]"
            r"\text{En } [-1, 3] \setminus \{1\}: \quad &|x+1| = x+1, \quad |x-3| = -(x-3) \\[4pt]"
            r"|x+1| - |x-3| &= (x+1) - (-x+3) = 2(x - 1)"
            r"\end{aligned}",
            font_size=19,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Inecuación fraccionaria 4:\n"
            "Restricción por división entre cero: x ≠ 1.\n"
            "Puntos críticos del valor absoluto: x = -1 y x = 3.\n"
            "En la zona central [-1, 3] \\ {1}:\n"
            "x + 1 ≥ 0  y  x - 3 ≤ 0.\n"
            "El numerador se reduce a: 2(x - 1)."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=4.8)

        # ==========================================================
        # PASO 5: Inecuación 4: Veredicto Global
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"\text{En } [-1, 3] \setminus \{1\}: \quad &\frac{2(x-1)}{x-1} = 2 \ge 2 \quad (\mathbf{\text{Identidad } \forall x}) \\[4pt]"
            r"\text{En } x < -1 \lor x > 3: \quad &\text{No hay soluciones adicionales} \\[6pt]"
            r"\therefore \quad CS_4 &= [-1, 3] \setminus \{1\} = A \implies \mathbf{\text{VERDADERO}} \\[8pt]"
            r"\text{\underline{Resumen:}} \quad &\mathbf{1: V}, \quad \mathbf{2: V}, \quad \mathbf{3: V}, \quad \mathbf{4: V}"
            r"\end{aligned}",
            font_size=18,
            color=THEME["success"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Veredicto consolidado:\n"
            "Al cancelar (x - 1) ≠ 0 obtenemos 2 ≥ 2, identidad\n"
            "que se cumple para todo punto de [-1, 3] \\ {1}.\n"
            "Fuera de este intervalo la desigualdad no se cumple.\n"
            "Por ende: CS₄ = [-1, 3] \\ {1} = A (Verdadero).\n"
            "Los 4 literales del ejercicio son VERDADEROS."
        )

        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana (Inecuación 4)
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen geométrico
        t_title = Text("Geometría de la Fracción:", font_size=15, color=THEME["header_color"], weight=BOLD)
        eq_curva = MathTex(r"f(x) = \frac{|x+1|-|x-3|}{x-1}, \quad g(x) = 2", font_size=13, color=THEME["highlight"])
        t_desc1 = Text("• f(x) = 2 constante en [-1, 3] \\ {1}.", font_size=12, color=THEME["success"])
        t_desc2 = Text("• Discontinuidad evitable (punto abierto) en (1, 2).", font_size=12, color=THEME["statement_box"])
        t_desc3 = Text("• Para x < -1: f(x) = -4/(x-1) < 2.", font_size=12, color=THEME["curve"])
        t_desc4 = Text("• Para x > 3: f(x) = 4/(x-1) < 2.", font_size=12, color=THEME["curve"])
        t_desc5 = Text("• f(x) ≥ 2 se cumple exactamente en:", font_size=12, color=THEME["secondary"], weight=BOLD)
        t_desc6 = Text("  [-1, 3] \\ {1}  (región verde con salto en 1).", font_size=12, color=THEME["secondary"])

        info_content = VGroup(t_title, eq_curva, t_desc1, t_desc2, t_desc3, t_desc4, t_desc5, t_desc6).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        info_box = SurroundingRectangle(info_content, color=THEME["statement_box"], buff=0.2, stroke_width=1.5, corner_radius=0.08)
        info_grp = VGroup(info_box, info_content).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos
        axes, axes_labels = self.setup_axes(
            x_range=[-3.0, 5.0, 1],
            y_range=[-1.0, 4.0, 1],
            x_length=5.6,
            y_length=3.8,
            center=[2.8, -0.45, 0],
            include_numbers=True
        )

        def f_rat(x):
            return (np.abs(x + 1) - np.abs(x - 3)) / (x - 1)

        # Ramas de f(x)
        c_left = axes.plot(f_rat, x_range=[-2.8, -1.0], color=THEME["highlight"], stroke_width=2.5)
        c_mid_1 = axes.plot(f_rat, x_range=[-1.0, 0.95], color=THEME["success"], stroke_width=3.2)
        c_mid_2 = axes.plot(f_rat, x_range=[1.05, 3.0], color=THEME["success"], stroke_width=3.2)
        c_right = axes.plot(f_rat, x_range=[3.0, 4.8], color=THEME["highlight"], stroke_width=2.5)

        # Recta horizontal y = 2
        line_2 = axes.plot(lambda x: 2.0, x_range=[-2.8, 4.8], color=THEME["secondary"], stroke_width=1.5)
        lbl_2 = MathTex(r"y = 2", font_size=12, color=THEME["secondary"]).next_to(axes.c2p(4.5, 2.0), UP, buff=0.06)

        # Puntos notables: extremos en (-1, 2) y (3, 2), y abierto en (1, 2)
        p_l = axes.c2p(-1.0, 2.0)
        p_r = axes.c2p(3.0, 2.0)
        p_open = axes.c2p(1.0, 2.0)

        dot_l = Dot(p_l, radius=0.06, color=THEME["success"])
        dot_r = Dot(p_r, radius=0.06, color=THEME["success"])
        dot_open = Dot(p_open, radius=0.07, stroke_width=2.0, stroke_color=THEME["statement_box"], fill_color=THEME["bg_color"])

        lbl_open = MathTex(r"(1, 2)", font_size=11, color=THEME["statement_box"]).next_to(p_open, UP, buff=0.1)

        # Segmento solución sobre el eje X
        seg_x1 = Line(axes.c2p(-1.0, 0), axes.c2p(0.93, 0), color=THEME["success"], stroke_width=4.5)
        seg_x2 = Line(axes.c2p(1.07, 0), axes.c2p(3.0, 0), color=THEME["success"], stroke_width=4.5)
        dot_x_l = Dot(axes.c2p(-1.0, 0), radius=0.05, color=THEME["success"])
        dot_x_r = Dot(axes.c2p(3.0, 0), radius=0.05, color=THEME["success"])
        dot_x_open = Dot(axes.c2p(1.0, 0), radius=0.06, stroke_width=1.8, stroke_color=THEME["statement_box"], fill_color=THEME["bg_color"])

        lbl_cs_axis = MathTex(r"CS_4 = [-1, 3] \setminus \{1\}", font_size=11, color=THEME["success"]).next_to(axes.c2p(1.0, 0), DOWN, buff=0.18)

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

        # Trazado de las curvas y la recta y = 2
        self.play(
            Create(line_2), Write(lbl_2),
            Create(c_left), Create(c_mid_1), Create(c_mid_2), Create(c_right),
            run_time=2.2
        )

        # Marcado de puntos y conjunto solución en el eje X
        self.play(
            FadeIn(dot_l), FadeIn(dot_r), FadeIn(dot_open), Write(lbl_open),
            Create(seg_x1), Create(seg_x2),
            FadeIn(dot_x_l), FadeIn(dot_x_r), FadeIn(dot_x_open),
            Write(lbl_cs_axis),
            run_time=1.6
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            line_2, lbl_2,
            c_left, c_mid_1, c_mid_2, c_right,
            dot_l, dot_r, dot_open, lbl_open,
            seg_x1, seg_x2,
            dot_x_l, dot_x_r, dot_x_open,
            lbl_cs_axis
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
