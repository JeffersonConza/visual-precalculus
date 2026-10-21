"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.7: Monotonía y funciones a trozos
Ejercicio 5.14 (Página 74 del libro / Página 93 del PDF)

Demostración del Teorema 5.18 (Propiedades de monotonía de la suma de funciones):
- Punto 1: f, g crecientes (o decrecientes) ⟹ f + g es creciente (o decreciente).
- Punto 2: f creciente y g estrictamente creciente ⟹ f + g es estrictamente creciente.
- Punto 3: f decreciente y g estrictamente decreciente ⟹ f + g es estrictamente decreciente.
- Criterio de la tasa de variación media: aditividad α_{f+g} = α_f + α_g.
- Interpretación gráfica cartesiana: superposición de curvas y pendientes secantes.
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_14(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.14",
            topic="Monotonía de la Suma (Teorema 5.18)"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Teorema 5.18: Sean f, g con dominio común I. Probar:",
            math_tex=r"f, g \nearrow \implies f+g \nearrow; \quad f \nearrow, g \nearrow\nearrow \implies f+g \nearrow\nearrow; \quad f \searrow, g \searrow\searrow \implies f+g \searrow\searrow",
            desc_font_size=15,
            math_font_size=15,
            read_time=4.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Definición de Monotonía",
            "2/6: Suma de Crecientes (Pto 1)",
            "3/6: Creciente + Estricta (Pto 2)",
            "4/6: Decreciente + Estricta (Pto 3)",
            "5/6: Tasa de Variación Aditiva",
            "6/6: Gráfica e Interpretación"
        ])

        # ==========================================================
        # PASO 1: Definición Formal de Monotonía
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"\forall x_1, x_2 \in I, \; x_1 < x_2 &: \\"
            r"f \text{ es creciente } (\nearrow) &\iff f(x_1) \le f(x_2) \\"
            r"g \text{ es estrict. creciente } (\nearrow\nearrow) &\iff g(x_1) < g(x_2)"
            r"\end{aligned}",
            font_size=23,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Definiciones fundamentales:\n"
            "Sean x₁, x₂ ∈ I cualesquiera con x₁ < x₂.\n"
            "• f es creciente si conserva el orden débil:\n"
            "  f(x₁) ≤ f(x₂).\n"
            "• g es estrictamente creciente si preserva\n"
            "  el orden estricto: g(x₁) < g(x₂)."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Punto 1 — Suma de Funciones Crecientes
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"f(x_1) \le f(x_2) \quad &\land \quad g(x_1) \le g(x_2) \\"
            r"\implies f(x_1) + g(x_1) &\le f(x_2) + g(x_2) \\"
            r"\therefore \quad (f+g)(x_1) &\le (f+g)(x_2) \quad [f+g \nearrow]"
            r"\end{aligned}",
            font_size=22,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Punto 1 (Suma de crecientes):\n"
            "Como f y g son crecientes, sumamos miembro\n"
            "a miembro por los axiomas de orden en ℝ:\n"
            "f(x₁) + g(x₁) ≤ f(x₂) + g(x₂).\n"
            "Por definición de suma: (f+g)(x) = f(x) + g(x).\n"
            "Concluimos que f + g es creciente en I."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Punto 2 — Creciente + Estrictamente Creciente
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"f(x_1) \le f(x_2) \quad &\land \quad g(x_1) < g(x_2) \\"
            r"\implies f(x_1) + g(x_1) &< f(x_2) + g(x_2) \\"
            r"\therefore \quad (f+g)(x_1) &< (f+g)(x_2) \quad [f+g \nearrow\nearrow]"
            r"\end{aligned}",
            font_size=22,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Punto 2 (Creciente + estricta):\n"
            "En ℝ, si a ≤ b y c < d, entonces a + c < b + d.\n"
            "La desigualdad estricta de g domina la suma:\n"
            "f(x₁) + g(x₁) < f(x₂) + g(x₂).\n"
            "Se concluye: (f+g)(x₁) < (f+g)(x₂).\n"
            "Por tanto, f + g es estrictamente creciente."
        )

        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Punto 3 — Decreciente + Estrictamente Decreciente
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"f(x_1) \ge f(x_2) \quad &\land \quad g(x_1) > g(x_2) \\"
            r"\implies f(x_1) + g(x_1) &> f(x_2) + g(x_2) \\"
            r"\therefore \quad (f+g)(x_1) &> (f+g)(x_2) \quad [f+g \searrow\searrow]"
            r"\end{aligned}",
            font_size=22,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Punto 3 (Decrecientes):\n"
            "Para decrecientes el orden se invierte:\n"
            "f(x₁) ≥ f(x₂) y g(x₁) > g(x₂).\n"
            "Sumando miembro a miembro:\n"
            "(f+g)(x₁) > (f+g)(x₂).\n"
            "Concluimos que f + g es estrictamente decreciente."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=4.8)

        # ==========================================================
        # PASO 5: Criterio de la Tasa de Variación (Sección 5.7.2)
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"\alpha_{f+g} &= \frac{(f+g)(x_2) - (f+g)(x_1)}{x_2 - x_1} \\"
            r"&= \frac{f(x_2)-f(x_1)}{x_2-x_1} + \frac{g(x_2)-g(x_1)}{x_2-x_1} = \alpha_f + \alpha_g \\"
            r"\alpha_f \ge 0 &, \alpha_g > 0 \implies \alpha_{f+g} > 0"
            r"\end{aligned}",
            font_size=21,
            color=THEME["success"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Criterio de tasa de variación:\n"
            "La tasa α mide la pendiente secante:\n"
            "α(f+g) = α(f) + α(g) (operador aditivo).\n"
            "Como α(f) ≥ 0 y α(g) > 0:\n"
            "α(f+g) > 0 en todo el intervalo I.\n"
            "Por el criterio de la Sec. 5.7.2, f+g es ↗↗."
        )

        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.2)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Interpretación geométrica
        t_title = Text("Superposición gráfica:", font_size=16, color=THEME["header_color"], weight=BOLD)
        eq_ej = MathTex(r"f(x) = x, \quad g(x) = x^3 \implies (f+g)(x) = x + x^3", font_size=16, color=THEME["highlight"])
        t_desc1 = Text("• f(x) = x es estrictamente creciente (recta).", font_size=13, color=THEME["statement_text"])
        t_desc2 = Text("• g(x) = x³ es estrictamente creciente (cúbica).", font_size=13, color=THEME["curve"])
        t_desc3 = Text("• (f+g)(x) = x + x³ suma sus ordenadas y", font_size=13, color=THEME["success"])
        t_desc4 = Text("  genera una pendiente secante estrictamente mayor.", font_size=13, color=THEME["success"])

        info_content = VGroup(t_title, eq_ej, t_desc1, t_desc2, t_desc3, t_desc4).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        info_box = SurroundingRectangle(info_content, color=THEME["statement_box"], buff=0.2, stroke_width=1.5, corner_radius=0.08)
        info_grp = VGroup(info_box, info_content).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos comparativos
        axes, axes_labels = self.setup_axes(
            x_range=[-1.6, 1.6, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=5.6,
            y_length=3.8,
            center=[2.8, -0.45, 0],
            include_numbers=True
        )

        # Curva 1: f(x) = x
        curve_f = axes.plot(lambda x: x, x_range=[-1.5, 1.5], color=THEME["statement_text"], stroke_width=2.0)
        lbl_f = MathTex(r"f(x) = x", font_size=13, color=THEME["statement_text"]).next_to(axes.c2p(1.4, 1.4), DR, buff=0.08)

        # Curva 2: g(x) = x³
        curve_g = axes.plot(lambda x: x**3, x_range=[-1.35, 1.35], color=THEME["curve"], stroke_width=2.5)
        lbl_g = MathTex(r"g(x) = x^3", font_size=13, color=THEME["curve"]).next_to(axes.c2p(1.35, 2.4), RIGHT, buff=0.08)

        # Curva Suma: (f+g)(x) = x + x³
        curve_sum = axes.plot(lambda x: x + x**3, x_range=[-1.2, 1.2], color=THEME["highlight"], stroke_width=3.2)
        lbl_sum = MathTex(r"(f+g)(x) = x + x^3", font_size=13, color=THEME["highlight"]).next_to(axes.c2p(1.15, 2.4), LEFT, buff=0.1)

        # Marcadores comparativos en x = 1: f(1) = 1, g(1) = 1, (f+g)(1) = 2
        p_1_base = axes.c2p(1.0, 1.0)
        p_1_sum = axes.c2p(1.0, 2.0)
        dot_base = Dot(p_1_base, radius=0.06, color=THEME["curve"])
        dot_sum = Dot(p_1_sum, radius=0.07, color=THEME["highlight"])

        eval_line = DashedLine(axes.c2p(1.0, 0), p_1_sum, color=THEME["axes"], stroke_width=1.5)
        lbl_sum_val = MathTex(r"(1, 2)", font_size=13, color=THEME["highlight"]).next_to(p_1_sum, LEFT, buff=0.1)

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

        # Trazado de las curvas f, g y la curva suma f+g
        self.play(
            Create(curve_f), Write(lbl_f),
            Create(curve_g), Write(lbl_g),
            run_time=1.6
        )
        self.play(
            Create(curve_sum), Write(lbl_sum),
            run_time=1.4
        )

        # Resaltado de la suma de ordenadas en x = 1
        self.play(
            Create(eval_line),
            FadeIn(dot_base),
            FadeIn(dot_sum), Write(lbl_sum_val),
            run_time=1.4
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_f, lbl_f,
            curve_g, lbl_g,
            curve_sum, lbl_sum,
            eval_line, dot_base, dot_sum, lbl_sum_val
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
