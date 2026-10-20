"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.1.4: Regla del Máximo Dominio (RMD)
Ejercicio 5.2 (Página 27 del libro / Página 46 del PDF)

Implementación con AmarunExerciseScene (Clase Base Reutilizable).
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_02(AmarunExerciseScene):
    def construct(self):
        # 1. Encabezado permanente (sin "(Par)")
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.2",
            topic="Regla del Máximo Dominio (RMD)"
        )

        # 2. Enunciado permanente en la parte superior
        self.setup_statement(
            desc_text="Determinar el dominio de definición de la función:",
            math_tex=r"h(x) = \ln\left(\frac{x^3 + 1}{x + 1}\right)",
            read_time=4.5
        )

        # 3. Barra de progreso interactiva (6 pasos)
        self.setup_progress_bar([
            "1/6: Condiciones RMD",
            "2/6: Factorización de Cubos",
            "3/6: Cancelación de Factores",
            "4/6: Análisis de Signo",
            "5/6: Conclusión del Dominio",
            "6/6: Interpretación Gráfica"
        ])

        # ==========================================================
        # PASO 1: Condiciones iniciales de RMD
        # ==========================================================
        eq1 = MathTex(
            r"\begin{cases} x + 1 \neq 0 \implies x \neq -1 \\ \dfrac{x^3 + 1}{x + 1} > 0 \end{cases}",
            font_size=24,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Por Regla del Máximo Dominio:\n"
            "El denominador no puede anularse (x ≠ -1)\n"
            "y el argumento del logaritmo natural\n"
            "debe ser estrictamente positivo."
        )
        self.morph_step(eq1, just1, box_color=THEME["secondary"], wait_time=5.0)

        # ==========================================================
        # PASO 2: Factorización de Suma de Cubos
        # ==========================================================
        eq2 = MathTex(
            r"\frac{(x + 1)(x^2 - x + 1)}{x + 1}",
            font_size=28,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Factorización de suma de cubos:\n"
            "a³ + b³ = (a + b)(a² - ab + b²)\n"
            "con a = x  y  b = 1:\n"
            "x³ + 1 = (x + 1)(x² - x + 1)."
        )
        self.morph_step(eq2, just2, box_color=THEME["highlight"], advance_to_step=1, wait_time=6.0)

        # ==========================================================
        # PASO 3: Cancelación con Tachado Explícito en Rojo Poncho
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(2)
        top_factor = VGroup(*self.active_math[0][0:5])
        bot_factor = VGroup(*self.active_math[0][14:17])
        strike_top = self.create_strike_line(top_factor)
        strike_bot = self.create_strike_line(bot_factor)

        just3 = self.create_justification(
            "3. Simplificación fraccionaria:\n"
            "Cancelamos el factor común (x + 1)\n"
            "en numerador y denominador,\n"
            "válido para todo x ≠ -1."
        )

        self.play(
            FadeOut(self.active_box),
            FadeOut(self.active_just, shift=DOWN * 0.2),
            FadeIn(just3, shift=DOWN * 0.2),
            Create(strike_top),
            Create(strike_bot),
            *prog_anims,
            run_time=1.2
        )
        self.wait(3.0)

        eq3 = MathTex(
            r"x^2 - x + 1 \quad (\text{para } x \neq -1)",
            font_size=25,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])
        hl3 = SurroundingRectangle(eq3, color=THEME["secondary"], buff=0.15, stroke_width=2.0)

        self.play(
            ReplacementTransform(VGroup(self.active_math, strike_top, strike_bot), eq3),
            run_time=1.5
        )
        self.play(Create(hl3), run_time=0.6)
        self.active_math = eq3
        self.active_just = just3
        self.active_box = hl3
        self.wait(5.5)

        # ==========================================================
        # PASO 4: Completación de Cuadrados y Signo
        # ==========================================================
        eq4 = MathTex(
            r"x^2 - x + 1 = \left(x - \frac{1}{2}\right)^2 + \frac{3}{4} \ge \frac{3}{4} > 0",
            font_size=23,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Completación y signo:\n"
            "x² - x + 1 = (x - ½)² + ¾.\n"
            "Como (x - ½)² ≥ 0 y ¾ > 0,\n"
            "el argumento siempre es > 0 (∀ x ∈ ℝ)."
        )
        self.morph_step(eq4, just4, box_color=THEME["curve"], advance_to_step=3, wait_time=6.8)

        # ==========================================================
        # PASO 5: Conclusión Final y Función Formal
        # ==========================================================
        eq_dom = MathTex(
            r"\operatorname{Dom}(h) = \mathbb{R} \setminus \{-1\}",
            font_size=28,
            color=THEME["success"]
        ).move_to([-3.4, 0.6, 0])

        eq_form = MathTex(
            r"h: \mathbb{R} \setminus \{-1\} \longrightarrow \mathbb{R}, \quad x \longmapsto \ln(x^2 - x + 1)",
            font_size=20,
            color=WHITE
        ).move_to([-3.4, -0.4, 0])

        final_grp = VGroup(eq_dom, eq_form)
        just5 = self.create_justification(
            "5. Conclusión:\n"
            "La única restricción real proviene\n"
            "del denominador inicial.\n"
            "El dominio excluye únicamente a x = -1."
        )
        self.morph_step(final_grp, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica (Curva con punto abierto en x = -1)
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        info_title = Text("6. Interpretación Gráfica", font_size=18, color=THEME["header_color"], weight=BOLD).move_to([-3.4, 1.2, 0])
        info_pts = VGroup(
            MathTex(r"\bullet \quad h(x) = \ln(x^2 - x + 1)", font_size=20, color=WHITE),
            MathTex(r"\bullet \quad \operatorname{Dom}(h) = \mathbb{R} \setminus \{-1\}", font_size=20, color=THEME["success"]),
            MathTex(r"\bullet \quad \text{Punto abierto en } (-1, \ln 3)", font_size=19, color=THEME["poncho_red"]),
            MathTex(r"\bullet \quad \text{Mínimo en } \left(\frac{1}{2}, \ln\frac{3}{4}\right)", font_size=19, color=THEME["highlight"]),
            MathTex(r"\bullet \quad \text{Cortes con eje } X \text{ en } 0 \text{ y } 1", font_size=19, color=THEME["curve"])
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28).next_to(info_title, DOWN, buff=0.32)
        info_grp = VGroup(info_title, info_pts)

        # Configurar ejes con la clase base
        axes, axes_labels = self.setup_axes()

        # Curva en dos ramas para dejar el agujero en x = -1
        curve_left = axes.plot(
            lambda x: np.log(x**2 - x + 1),
            x_range=[-2.8, -1.04],
            color=THEME["curve"],
            stroke_width=3
        )
        curve_right = axes.plot(
            lambda x: np.log(x**2 - x + 1),
            x_range=[-0.96, 2.8],
            color=THEME["curve"],
            stroke_width=3
        )

        # Punto abierto creado con helper de la clase base
        hole_outer, hole_lbl, hole_arrow = self.create_open_point(
            axes, -1, np.log(3),
            label_tex=r"(-1, \ln 3) \notin \operatorname{Dom}(h)"
        )

        p_min = Dot(axes.c2p(0.5, np.log(0.75)), radius=0.06, color=THEME["highlight"])
        p_r1 = Dot(axes.c2p(0, 0), radius=0.05, color=THEME["success"])
        p_r2 = Dot(axes.c2p(1, 0), radius=0.05, color=THEME["success"])

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
        self.play(Create(curve_left), Create(curve_right), run_time=1.8)
        self.play(
            FadeIn(hole_outer),
            Write(hole_lbl),
            GrowArrow(hole_arrow),
            FadeIn(p_min),
            FadeIn(p_r1),
            FadeIn(p_r2),
            run_time=1.2
        )
        self.wait(7.0)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_left, curve_right,
            hole_outer, hole_lbl, hole_arrow,
            p_min, p_r1, p_r2
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
