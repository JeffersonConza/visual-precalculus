"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.4: Paridad y valor absoluto
Ejercicio 5.4 (Página 46 del libro / Página 65 del PDF)

Demostración de las propiedades de paridad del Teorema 5.4:
- Punto 2: Par × Impar es Impar, y Par / Impar es Impar.
- Punto 3: Par + Par es Par.
- Punto 4: Impar + Impar es Impar.
- Interpretación geométrica de simetría par (eje Y) e impar (origen).
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_04(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.4",
            topic="Paridad de Funciones (Teorema 5.4)"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Teorema 5.4: Sean f par y g impar (dominio simétrico I). Probar:",
            math_tex=r"f \cdot g, \; f/g \text{ (impares)}; \quad f_1+f_2 \text{ (par)}; \quad g_1+g_2 \text{ (impar)}",
            desc_font_size=16,
            math_font_size=18,
            read_time=4.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Definición de Paridad",
            "2/6: Producto Par × Impar",
            "3/6: Cociente Par / Impar",
            "4/6: Suma de Pares",
            "5/6: Suma de Impares",
            "6/6: Simetría Geométrica"
        ])

        # ==========================================================
        # PASO 1: Definición de Paridad
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"f \text{ es par} &\iff \forall x \in I : f(-x) = f(x) \\"
            r"g \text{ es impar} &\iff \forall x \in I : g(-x) = -g(x)"
            r"\end{aligned}",
            font_size=24,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Definiciones fundamentales:\n"
            "Un dominio I es simétrico si x ∈ I ⇒ -x ∈ I.\n"
            "• Función par: el signo del argumento no altera la imagen.\n"
            "• Función impar: el signo negativo sale de la función."
        )
        self.morph_step(eq1, just1, box_color=THEME["secondary"], wait_time=5.0)

        # ==========================================================
        # PASO 2: Producto de Par e Impar
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"(f \cdot g)(-x) &= f(-x) \cdot g(-x) \\"
            r"&= [f(x)] \cdot [-g(x)] \\"
            r"&= -[f(x) \cdot g(x)] \\"
            r"&= -(f \cdot g)(x) \implies f \cdot g \text{ es impar}"
            r"\end{aligned}",
            font_size=23,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Producto Par × Impar:\n"
            "Evaluamos (f·g) en -x.\n"
            "Aplicamos la paridad de f y la imparidad de g.\n"
            "Por regla de signos (+)(-) = -,\n"
            "el signo negativo factoriza globalmente."
        )
        self.morph_step(eq2, just2, box_color=THEME["highlight"], advance_to_step=1, wait_time=5.8)

        # ==========================================================
        # PASO 3: Cociente de Par e Impar
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"\left(\frac{f}{g}\right)(-x) &= \frac{f(-x)}{g(-x)} \\"
            r"&= \frac{f(x)}{-g(x)} = -\frac{f(x)}{g(x)} \\"
            r"&= -\left(\frac{f}{g}\right)(x) \implies \frac{f}{g} \text{ es impar}"
            r"\end{aligned}",
            font_size=23,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Cociente Par / Impar:\n"
            "Definido para todo x tal que g(x) ≠ 0.\n"
            "El numerador preserva el valor f(x)\n"
            "y el denominador aporta el signo -.\n"
            "Por tanto, f/g es impar."
        )
        self.morph_step(eq3, just3, box_color=THEME["secondary"], advance_to_step=2, wait_time=5.8)

        # ==========================================================
        # PASO 4: Suma de Funciones Pares
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"(f_1 + f_2)(-x) &= f_1(-x) + f_2(-x) \\"
            r"&= f_1(x) + f_2(x) \\"
            r"&= (f_1 + f_2)(x) \implies f_1 + f_2 \text{ es par}"
            r"\end{aligned}",
            font_size=23,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Suma de funciones pares:\n"
            "Sean f₁ y f₂ ambas pares.\n"
            "Evaluamos la suma en -x.\n"
            "Como f₁(-x) = f₁(x) y f₂(-x) = f₂(x),\n"
            "la suma conserva la paridad."
        )
        self.morph_step(eq4, just4, box_color=THEME["curve"], advance_to_step=3, wait_time=5.5)

        # ==========================================================
        # PASO 5: Suma de Funciones Impares
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"(g_1 + g_2)(-x) &= g_1(-x) + g_2(-x) \\"
            r"&= [-g_1(x)] + [-g_2(x)] \\"
            r"&= -[g_1(x) + g_2(x)] \\"
            r"&= -(g_1 + g_2)(x) \implies g_1 + g_2 \text{ es impar}"
            r"\end{aligned}",
            font_size=23,
            color=THEME["success"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Suma de funciones impares:\n"
            "Sean g₁ y g₂ ambas impares.\n"
            "Evaluamos la suma en -x.\n"
            "Factorizamos el signo negativo común.\n"
            "Conclusión: g₁ + g₂ es impar."
        )
        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.5)

        # ==========================================================
        # PASO 6: Interpretación Geométrica (Simetrías Comparadas)
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Resumen teórico a la izquierda
        info_title = Text("6. Simetría Geométrica", font_size=18, color=THEME["header_color"], weight=BOLD).move_to([-3.4, 1.2, 0])
        info_pts = VGroup(
            MathTex(r"\bullet \quad \text{Función Par: Simetría axial (Eje } Y\text{)}", font_size=18, color=THEME["highlight"]),
            MathTex(r"\quad \quad f(-x) = f(x) \implies \text{Reflexión horizontal}", font_size=16, color=WHITE),
            MathTex(r"\bullet \quad \text{Función Impar: Simetría central (Origen)}", font_size=18, color=THEME["curve"]),
            MathTex(r"\quad \quad g(-x) = -g(x) \implies \text{Rotación de } 180^\circ", font_size=16, color=WHITE),
            MathTex(r"\bullet \quad \text{Teorema 5.4 completamente verificado } \blacksquare", font_size=18, color=THEME["success"])
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(info_title, DOWN, buff=0.30)
        info_grp = VGroup(info_title, info_pts)

        # Plano cartesiano en el panel derecho
        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.2, 2.2, 1],
            x_length=5.6,
            y_length=3.8,
            tips=True,
            axis_config={
                "color": THEME["axes"],
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 13,
            }
        ).move_to([2.7, -0.45, 0])

        axes_labels = axes.get_axis_labels(
            x_label=MathTex("x", font_size=18, color=THEME["statement_text"]),
            y_label=MathTex("y", font_size=18, color=THEME["statement_text"])
        )

        # Curva Par: y = x^2 - 1 (color highlight)
        curve_par = axes.plot(lambda x: x**2 - 1, x_range=[-1.7, 1.7], color=THEME["highlight"], stroke_width=3)
        lbl_par = MathTex(r"f(x) \text{ [Par]}", font_size=15, color=THEME["highlight"]).next_to(axes.c2p(1.7, 1.89), RIGHT, buff=0.1)

        # Curva Impar: y = 0.5 * x^3 (color curve)
        curve_impar = axes.plot(lambda x: 0.5 * (x**3), x_range=[-1.6, 1.6], color=THEME["curve"], stroke_width=3)
        lbl_impar = MathTex(r"g(x) \text{ [Impar]}", font_size=15, color=THEME["curve"]).next_to(axes.c2p(-1.6, -2.05), UP + LEFT, buff=0.1)

        # Puntos simétricos para la función par: (1.2, f(1.2)) y (-1.2, f(1.2))
        x_val = 1.2
        y_par = x_val**2 - 1
        dot_p1 = Dot(axes.c2p(x_val, y_par), radius=0.06, color=THEME["highlight"])
        dot_p2 = Dot(axes.c2p(-x_val, y_par), radius=0.06, color=THEME["highlight"])
        sym_line_par = DashedLine(dot_p2.get_center(), dot_p1.get_center(), color=THEME["highlight"], stroke_width=1.5)

        # Puntos simétricos para la función impar: (1.3, g(1.3)) y (-1.3, -g(1.3))
        x_imp = 1.3
        y_imp = 0.5 * (x_imp**3)
        dot_i1 = Dot(axes.c2p(x_imp, y_imp), radius=0.06, color=THEME["curve"])
        dot_i2 = Dot(axes.c2p(-x_imp, -y_imp), radius=0.06, color=THEME["curve"])
        sym_line_imp = DashedLine(dot_i2.get_center(), dot_i1.get_center(), color=THEME["curve"], stroke_width=1.5)

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

        # Trazado de las curvas par e impar
        self.play(
            Create(curve_par), Write(lbl_par),
            Create(curve_impar), Write(lbl_impar),
            run_time=2.0
        )

        # Resaltado de las líneas de simetría axial y central
        self.play(
            Create(sym_line_par), FadeIn(dot_p1), FadeIn(dot_p2),
            Create(sym_line_imp), FadeIn(dot_i1), FadeIn(dot_i2),
            run_time=1.5
        )
        self.wait(7.0)

        # ==========================================================
        # Cierre suave
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_par, lbl_par, curve_impar, lbl_impar,
            sym_line_par, dot_p1, dot_p2,
            sym_line_imp, dot_i1, dot_i2
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
