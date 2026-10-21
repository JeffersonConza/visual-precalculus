"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.22 (Página 108 del libro / Página 127 del PDF)

Ecuaciones con valor absoluto: Determinar si A es el conjunto solución:
1. |x+3| - |2x-5| = 7,  x ∈ ℝ,  A = ∅  (VERDADERO, CS = ∅).
2. |x| + |x-5| = 6,  x ∈ ℝ,  A = {-1/2, 11/2}  (VERDADERO, CS = {-1/2, 11/2}).
3. |2|x| - 2| = -1,  x ∈ ℝ,  A = {-1/2, 1/2}  (FALSO, |u| ≥ 0 ⟹ CS = ∅ ≠ A).
4. |x² - 9| = 2x + 6,  x ∈ ℝ,  A = {-3, 1, 5}  (VERDADERO, CS = {-3, 1, 5}).
- Interpretación gráfica cartesiana: Intersección de f(x) = |x² - 9| y g(x) = 2x + 6 en (-3, 0), (1, 8) y (5, 16).
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_22(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.22",
            topic="Ecuaciones con Valor Absoluto"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Determina si el conjunto propuesto A es el conjunto solución de cada ecuación:",
            math_tex=r"1.\; |x+3|-|2x-5|=7;\; 2.\; |x|+|x-5|=6;\; 3.\; |2|x|-2|=-1;\; 4.\; |x^2-9|=2x+6",
            desc_font_size=14,
            math_font_size=14,
            read_time=4.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Ecuación 1 (Zonas Críticas)",
            "2/6: Ecuación 2 (Partición en ℝ)",
            "3/6: Ecuación 3 (No Negatividad)",
            "4/6: Ecuación 4 (Condición y Casos)",
            "5/6: Ecuación 4 (Veredicto Global)",
            "6/6: Gráfica de |x²-9| = 2x+6"
        ])

        # ==========================================================
        # PASO 1: Ecuación 1: |x+3| - |2x-5| = 7
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"\mathbf{1.} \quad &|x+3| - |2x-5| = 7, \quad \text{Puntos críticos: } x \in \{-3, 5/2\} \\[4pt]"
            r"x < -3 &: -(x+3) - (-(2x-5)) = 7 \implies x - 8 = 7 \implies x = 15 \;\; (\text{Incompatible}) \\[4pt]"
            r"-3 \le x < 5/2 &: (x+3) - (-(2x-5)) = 7 \implies 3x - 2 = 7 \implies x = 3 \;\; (\text{Fuera de rango}) \\[4pt]"
            r"x \ge 5/2 &: (x+3) - (2x-5) = 7 \implies -x + 8 = 7 \implies x = 1 \;\; (\text{Fuera de rango}) \\[4pt]"
            r"\therefore \quad &CS_1 = \emptyset = A \implies \mathbf{\text{VERDADERO}}"
            r"\end{aligned}",
            font_size=18,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Ecuación 1 (Zonas críticas):\n"
            "Los ceros de los valores absolutos son -3 y 5/2.\n"
            "Analizamos los 3 intervalos en la recta real:\n"
            "• x < -3 produce x = 15 (no pertenece al intervalo).\n"
            "• [-3, 5/2[ produce x = 3 (fuera del intervalo).\n"
            "• x ≥ 5/2 produce x = 1 (fuera del intervalo).\n"
            "Ninguna rama tiene solución: CS = ∅ = A (Verdadero)."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Ecuación 2: |x| + |x-5| = 6
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"\mathbf{2.} \quad &|x| + |x-5| = 6, \quad \text{Puntos críticos: } x \in \{0, 5\} \\[4pt]"
            r"x < 0 &: -x - (x-5) = 6 \implies -2x = 1 \implies x = -1/2 \;\; (\text{Válido}) \\[4pt]"
            r"0 \le x < 5 &: x - (x-5) = 6 \implies 5 = 6 \;\; (\text{Sin solución}) \\[4pt]"
            r"x \ge 5 &: x + (x-5) = 6 \implies 2x = 11 \implies x = 11/2 \;\; (\text{Válido}) \\[4pt]"
            r"\therefore \quad &CS_2 = \{-1/2, 11/2\} = A \implies \mathbf{\text{VERDADERO}}"
            r"\end{aligned}",
            font_size=18,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Ecuación 2 (Partición en ℝ):\n"
            "Puntos críticos en x = 0 y x = 5:\n"
            "• Si x < 0: -2x + 5 = 6 ⟹ x = -1/2 < 0 (válido).\n"
            "• Si 0 ≤ x < 5: 5 = 6 (imposible).\n"
            "• Si x ≥ 5: 2x - 5 = 6 ⟹ x = 11/2 ≥ 5 (válido).\n"
            "Conjunto solución: CS = {-1/2, 11/2} = A (Verdadero)."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Ecuación 3: |2|x| - 2| = -1
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"\mathbf{3.} \quad &|2|x| - 2| = -1, \quad \text{con } A = \{-1/2, 1/2\} \\[6pt]"
            r"\text{Propiedad: } &\forall u \in \mathbb{R}, \quad |u| \ge 0 \\[6pt]"
            r"|2|x| - 2| \ge 0 &> -1 \quad \implies \text{Ecuación incompatible} \\[6pt]"
            r"\therefore \quad CS_3 &= \emptyset \neq \{-1/2, 1/2\} \implies \mathbf{\text{FALSO}}"
            r"\end{aligned}",
            font_size=21,
            color=THEME["statement_box"]
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Ecuación 3 (No negatividad):\n"
            "Por axioma del valor absoluto, |u| ≥ 0 para todo u ∈ ℝ.\n"
            "Una expresión con valor absoluto exterior nunca puede\n"
            "ser estrictamente negativa: |2|x| - 2| ≥ 0 > -1.\n"
            "El conjunto solución real es vacío: CS = ∅.\n"
            "Como A = {-1/2, 1/2} ≠ ∅, la afirmación es FALSA."
        )

        self.morph_step(eq3, just3, box_color=THEME["statement_box"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Ecuación 4: |x² - 9| = 2x + 6 (Condición y Casos)
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"\mathbf{4.} \quad &|x^2 - 9| = 2x + 6 \\[4pt]"
            r"\text{Condición: } &2x + 6 \ge 0 \iff x \ge -3 \\[6pt]"
            r"\text{Caso (+): } &x^2 - 9 = 2x + 6 \implies x^2 - 2x - 15 = 0 \\[3pt]"
            r"&(x - 5)(x + 3) = 0 \implies x = 5 \;\lor\; x = -3 \\[6pt]"
            r"\text{Caso (-): } &x^2 - 9 = -(2x + 6) \implies x^2 + 2x - 3 = 0 \\[3pt]"
            r"&(x + 3)(x - 1) = 0 \implies x = -3 \;\lor\; x = 1"
            r"\end{aligned}",
            font_size=19,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Ecuación 4 (Desglose):\n"
            "Para |u| = v debe cumplirse v ≥ 0 ⟹ 2x + 6 ≥ 0 ⟹ x ≥ -3.\n"
            "Bifurcamos en dos casos:\n"
            "• x² - 9 = 2x + 6 ⟹ (x - 5)(x + 3) = 0 ⟹ x = 5, -3.\n"
            "• x² - 9 = -(2x + 6) ⟹ (x + 3)(x - 1) = 0 ⟹ x = 1, -3.\n"
            "Todos los candidatos cumplen la condición x ≥ -3."
        )

        self.morph_step(eq4, just4, box_color=THEME["curve"], advance_to_step=3, wait_time=5.0)

        # ==========================================================
        # PASO 5: Ecuación 4: Veredicto Global
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"CS_4 &= \{-3, 1, 5\} = A \implies \mathbf{\text{VERDADERO}} \\[8pt]"
            r"\text{\underline{Resumen de Veredictos del Ejercicio 5.22:}} & \\[6pt]"
            r"\mathbf{1.} \; |x+3|-|2x-5|=7, \; A = \emptyset &\implies \mathbf{\text{VERDADERO}} \\[3pt]"
            r"\mathbf{2.} \; |x|+|x-5|=6, \; A = \{-1/2, 11/2\} &\implies \mathbf{\text{VERDADERO}} \\[3pt]"
            r"\mathbf{3.} \; |2|x|-2|=-1, \; A = \{-1/2, 1/2\} &\implies \mathbf{\text{FALSO}} \\[3pt]"
            r"\mathbf{4.} \; |x^2-9|=2x+6, \; A = \{-3, 1, 5\} &\implies \mathbf{\text{VERDADERO}}"
            r"\end{aligned}",
            font_size=18,
            color=THEME["success"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Veredicto unificado:\n"
            "La ecuación 4 tiene exactamente las soluciones {-3, 1, 5},\n"
            "lo que coincide exactamente con el conjunto A propuesto.\n"
            "Consolidamos la evaluación de los 4 literales:\n"
            "• Ítem 1: VERDADERO (CS = ∅)\n"
            "• Ítem 2: VERDADERO (CS = {-1/2, 11/2})\n"
            "• Ítem 3: FALSO (CS = ∅ ≠ A)\n"
            "• Ítem 4: VERDADERO (CS = {-3, 1, 5})"
        )

        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana (Ecuación 4)
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen geométrico
        t_title = Text("Resolución gráfica de |x²-9| = 2x+6:", font_size=15, color=THEME["header_color"], weight=BOLD)
        eq_curva = MathTex(r"f(x) = |x^2 - 9|, \quad g(x) = 2x + 6", font_size=14, color=THEME["highlight"])
        t_desc1 = Text("• f(x) refleja las ordenadas negativas en [-3, 3].", font_size=12, color=THEME["curve"])
        t_desc2 = Text("• g(x) es una recta con pendiente 2 y corte (0, 6).", font_size=12, color=THEME["statement_text"])
        t_desc3 = Text("• 3 Puntos de intersección exactos:", font_size=12, color=THEME["success"], weight=BOLD)
        t_desc4 = Text("  P₁(-3, 0),   P₂(1, 8),   P₃(5, 16).", font_size=12, color=THEME["success"])
        t_desc5 = Text("• Veredicto: CS = {-3, 1, 5} confirmado.", font_size=12, color=THEME["secondary"])

        info_content = VGroup(t_title, eq_curva, t_desc1, t_desc2, t_desc3, t_desc4, t_desc5).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        info_box = SurroundingRectangle(info_content, color=THEME["statement_box"], buff=0.2, stroke_width=1.5, corner_radius=0.08)
        info_grp = VGroup(info_box, info_content).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos
        axes, axes_labels = self.setup_axes(
            x_range=[-4.5, 6.0, 2],
            y_range=[-2.0, 18.0, 4],
            x_length=5.6,
            y_length=3.8,
            center=[2.8, -0.45, 0],
            include_numbers=True
        )

        # Curva f(x) = |x² - 9|
        curve_f = axes.plot(lambda x: np.abs(x**2 - 9), x_range=[-4.2, 5.2], color=THEME["curve"], stroke_width=2.8)
        lbl_f = MathTex(r"|x^2-9|", font_size=13, color=THEME["curve"]).next_to(axes.c2p(-3.8, 6.0), LEFT, buff=0.08)

        # Recta g(x) = 2x + 6
        line_g = axes.plot(lambda x: 2*x + 6, x_range=[-3.5, 5.5], color=THEME["highlight"], stroke_width=2.2)
        lbl_g = MathTex(r"2x+6", font_size=13, color=THEME["highlight"]).next_to(axes.c2p(4.5, 15.0), LEFT, buff=0.08)

        # Puntos de intersección
        p1 = axes.c2p(-3.0, 0.0)
        p2 = axes.c2p(1.0, 8.0)
        p3 = axes.c2p(5.0, 16.0)

        dot1 = Dot(p1, radius=0.06, color=THEME["success"])
        dot2 = Dot(p2, radius=0.06, color=THEME["success"])
        dot3 = Dot(p3, radius=0.06, color=THEME["success"])

        lbl_p1 = MathTex(r"(-3, 0)", font_size=11, color=THEME["success"]).next_to(p1, DOWN, buff=0.08)
        lbl_p2 = MathTex(r"(1, 8)", font_size=11, color=THEME["success"]).next_to(p2, RIGHT, buff=0.08)
        lbl_p3 = MathTex(r"(5, 16)", font_size=11, color=THEME["success"]).next_to(p3, DR, buff=0.08)

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
            Create(curve_f), Write(lbl_f),
            Create(line_g), Write(lbl_g),
            run_time=2.0
        )

        # Marcado de las tres intersecciones
        self.play(
            FadeIn(dot1), Write(lbl_p1),
            FadeIn(dot2), Write(lbl_p2),
            FadeIn(dot3), Write(lbl_p3),
            run_time=1.6
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_f, lbl_f,
            line_g, lbl_g,
            dot1, dot2, dot3,
            lbl_p1, lbl_p2, lbl_p3
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
