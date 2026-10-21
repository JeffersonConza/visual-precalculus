"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.20 (Página 108 del libro / Página 127 del PDF)

Inecuación racional:
- Enunciado: Determina si A = ]-4, ∞[ es el conjunto solución de:
  (x + 5)/(x + 4) ≥ (x - 6)/(x + 4),  x ∈ ℝ.
- RMD: Denominador x + 4 ≠ 0 ⟹ x ≠ -4.
- Trasposición y resta de fracciones homogéneas: [ (x+5) - (x-6) ] / (x+4) ≥ 0 ⟹ 11 / (x+4) ≥ 0.
- Análisis de signos: Numerador 11 > 0 constante ⟹ x + 4 > 0 ⟹ x > -4.
- Veredicto: CS = ]-4, +∞[ = A (Verdadero).
- Interpretación gráfica: Asíntota vertical en x = -4, comparación f(x) vs g(x) e intervalo sombreado.
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_20(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.20",
            topic="Inecuación Racional y Conjunto Solución"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Determina si A = ]-4, +∞[ es el conjunto solución de la inecuación racional:",
            math_tex=r"\frac{x+5}{x+4} \ge \frac{x-6}{x+4}, \quad x \in \mathbb{R}",
            desc_font_size=15,
            math_font_size=16,
            read_time=4.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Restricción de Dominio (RMD)",
            "2/6: Trasposición a un Miembro",
            "3/6: Reducción de Numeradores",
            "4/6: Criterio de Signos",
            "5/6: Conjunto Solución y Veredicto",
            "6/6: Gráfica y Región Solución"
        ])

        # ==========================================================
        # PASO 1: Restricción del Dominio (RMD)
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"\text{RMD: } &\text{La división para cero no está definida en } \mathbb{R}: \\[6pt]"
            r"x + 4 \neq 0 &\iff x \neq -4 \\[6pt]"
            r"\therefore \quad U &= \mathbb{R} \setminus \{-4\} = ]-\infty, -4[ \;\cup\; ]-4, +\infty["
            r"\end{aligned}",
            font_size=22,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Regla del Máximo Dominio:\n"
            "El denominador x + 4 aparece en ambos miembros.\n"
            "Para que las expresiones tengan sentido real,\n"
            "debemos exigir x + 4 ≠ 0 ⟺ x ≠ -4.\n"
            "El universo de resolución es U = ℝ \\ {-4}."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Trasposición a un Solo Miembro
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"\frac{x+5}{x+4} - \frac{x-6}{x+4} &\ge 0 \quad (\forall x \in U) \\[8pt]"
            r"\text{¡Cuidado! } &\text{No multiplicar por } (x+4) \\[4pt]"
            r"&\text{porque su signo depende de } x."
            r"\end{aligned}",
            font_size=22,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Trasposición algebraica:\n"
            "Restamos el miembro derecho a ambos lados.\n"
            "Principio riguroso: nunca se multiplica por\n"
            "una variable cuyo signo se desconoce,\n"
            "ya que si x+4 < 0 la desigualdad se invertiría."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Reducción al Mismo Denominador
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"\frac{(x+5) - (x-6)}{x+4} &\ge 0 \\[6pt]"
            r"\frac{x + 5 - x + 6}{x+4} &\ge 0 \\[6pt]"
            r"\frac{11}{x+4} &\ge 0"
            r"\end{aligned}",
            font_size=23,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Reducción de numeradores:\n"
            "Como las fracciones tienen denominador común,\n"
            "restamos directamente los numeradores:\n"
            "(x + 5) - (x - 6) = x - x + 5 + 6 = 11.\n"
            "La inecuación se simplifica a: 11 / (x + 4) ≥ 0."
        )

        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Criterio de Signos de la Fracción
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"\frac{11}{x+4} \ge 0 \quad &\land \quad 11 > 0 \quad (\text{Constante positiva}) \\[6pt]"
            r"\frac{+}{+} = + \quad &\implies \quad x + 4 > 0 \\[6pt]"
            r"x + 4 > 0 \quad &\iff \quad x > -4 \quad (x \neq -4)"
            r"\end{aligned}",
            font_size=22,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Análisis de signos:\n"
            "El numerador es la constante positiva 11 > 0.\n"
            "Una fracción es ≥ 0 ssi numerador y denominador\n"
            "tienen el mismo signo (y numerador ≠ 0).\n"
            "Por tanto, se requiere estrictamente x + 4 > 0,\n"
            "lo que equivale a x > -4."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=5.0)

        # ==========================================================
        # PASO 5: Conjunto Solución y Veredicto
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"CS &= \{x \in U : x > -4\} = \; ]-4, +\infty[ \\[6pt]"
            r"\text{Dado: } A &= \; ]-4, +\infty[ \\[6pt]"
            r"\therefore \quad CS &= A \quad \implies \quad \mathbf{\text{VERDADERO}}"
            r"\end{aligned}",
            font_size=23,
            color=THEME["success"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Veredicto final:\n"
            "Intersecando x > -4 con el dominio U = ℝ \\ {-4},\n"
            "obtenemos el intervalo solución CS = ]-4, +∞[.\n"
            "Comparando con el conjunto propuesto A:\n"
            "CS coincide exactamente con A.\n"
            "Conclusión: Sí, A es el conjunto solución."
        )

        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen geométrico
        t_title = Text("Análisis comparativo de curvas:", font_size=15, color=THEME["header_color"], weight=BOLD)
        eq_f = MathTex(r"f(x) = \frac{x+5}{x+4} = 1 + \frac{1}{x+4}", font_size=14, color=THEME["highlight"])
        eq_g = MathTex(r"g(x) = \frac{x-6}{x+4} = 1 - \frac{10}{x+4}", font_size=14, color=THEME["secondary"])
        t_desc1 = Text("• Asíntota vertical común en x = -4.", font_size=12, color=THEME["statement_text"])
        t_desc2 = Text("• Para x > -4: f(x) ≥ g(x)  (Curva f por encima).", font_size=12, color=THEME["success"])
        t_desc3 = Text("• Para x < -4: f(x) < g(x)  (Desigualdad falsa).", font_size=12, color=THEME["statement_box"])
        t_desc4 = Text("• Intervalo solución sobre el eje X:", font_size=12, color=THEME["success"], weight=BOLD)
        t_desc5 = Text("  ]-4, +∞[ con punto abierto en x = -4.", font_size=12, color=THEME["success"])

        info_content = VGroup(t_title, eq_f, eq_g, t_desc1, t_desc2, t_desc3, t_desc4, t_desc5).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        info_box = SurroundingRectangle(info_content, color=THEME["statement_box"], buff=0.2, stroke_width=1.5, corner_radius=0.08)
        info_grp = VGroup(info_box, info_content).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos
        axes, axes_labels = self.setup_axes(
            x_range=[-8.0, 4.0, 2],
            y_range=[-4.0, 5.0, 2],
            x_length=5.6,
            y_length=3.8,
            center=[2.8, -0.45, 0],
            include_numbers=True
        )

        # Asíntota vertical en x = -4
        p_asymp_top = axes.c2p(-4.0, 4.8)
        p_asymp_bot = axes.c2p(-4.0, -3.8)
        asymp_line = DashedLine(p_asymp_bot, p_asymp_top, color=THEME["statement_box"], stroke_width=2.0)
        lbl_asymp = MathTex(r"x = -4", font_size=12, color=THEME["statement_box"]).next_to(p_asymp_top, RIGHT, buff=0.08)

        # Curva f(x) = (x+5)/(x+4)
        curve_f_left = axes.plot(lambda x: (x+5)/(x+4), x_range=[-7.8, -4.3], color=THEME["highlight"], stroke_width=2.4)
        curve_f_right = axes.plot(lambda x: (x+5)/(x+4), x_range=[-3.7, 3.8], color=THEME["highlight"], stroke_width=2.8)
        lbl_f_tag = MathTex(r"f(x)", font_size=13, color=THEME["highlight"]).next_to(axes.c2p(2.5, (2.5+5)/(2.5+4)), UR, buff=0.08)

        # Curva g(x) = (x-6)/(x+4)
        curve_g_left = axes.plot(lambda x: (x-6)/(x+4), x_range=[-7.8, -4.3], color=THEME["secondary"], stroke_width=2.0)
        curve_g_right = axes.plot(lambda x: (x-6)/(x+4), x_range=[-3.7, 3.8], color=THEME["secondary"], stroke_width=2.0)
        lbl_g_tag = MathTex(r"g(x)", font_size=13, color=THEME["secondary"]).next_to(axes.c2p(2.5, (2.5-6)/(2.5+4)), DR, buff=0.08)

        # Resaltado del intervalo solución en el eje X: ]-4, +∞[
        sol_ray = Line(axes.c2p(-4.0, 0), axes.c2p(3.8, 0), color=THEME["success"], stroke_width=5.0)
        open_dot = Dot(axes.c2p(-4.0, 0), radius=0.08, stroke_width=2.0, stroke_color=THEME["success"], fill_color=THEME["bg_color"])
        lbl_sol = MathTex(r"CS = ]-4, +\infty[", font_size=13, color=THEME["success"]).next_to(axes.c2p(0, 0), UP, buff=0.15)

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

        # Trazado de la asíntota vertical
        self.play(
            Create(asymp_line),
            Write(lbl_asymp),
            run_time=1.2
        )

        # Trazado de las curvas f(x) y g(x)
        self.play(
            Create(curve_f_left), Create(curve_f_right), Write(lbl_f_tag),
            Create(curve_g_left), Create(curve_g_right), Write(lbl_g_tag),
            run_time=2.2
        )

        # Resaltado del conjunto solución en el eje X
        self.play(
            Create(sol_ray),
            FadeIn(open_dot),
            Write(lbl_sol),
            run_time=1.4
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            asymp_line, lbl_asymp,
            curve_f_left, curve_f_right, lbl_f_tag,
            curve_g_left, curve_g_right, lbl_g_tag,
            sol_ray, open_dot, lbl_sol
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
