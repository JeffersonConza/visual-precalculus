"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.1.4: Regla del Máximo Dominio (RMD)
Ejercicio 5.2 (Página 27 del libro / Página 46 del PDF)

Modo: Metamorfosis 3Blue1Brown con:
- Tachado explícito en color rojo poncho al cancelar el factor común.
- Barra de progreso interactiva en la parte inferior (6 pasos).
- Gráfico cartesiano de la función al final con punto abierto en x = -1.
- Enunciado permanente en la parte superior.
- Sin "(Par)" en el título.
- Sin etiquetas de columnas.
- Ritmo pedagógico óptimo.
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.styles import THEME

class Ejercicio05_02(Scene):
    def setup(self):
        self.camera.background_color = THEME["bg_color"]

    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (Sin "(Par)")
        # ==========================================================
        header = Text(
            "Precálculo 2  ·  Capítulo 5  ·  Ejercicio 5.2  —  Regla del Máximo Dominio (RMD)",
            font_size=17,
            color=THEME["header_color"],
            weight=BOLD
        ).to_edge(UP, buff=0.25)
        self.play(FadeIn(header, shift=DOWN * 0.2), run_time=0.7)

        # ==========================================================
        # 2. Enunciado Permanente (Fijo durante todo el video)
        # ==========================================================
        stmt_desc = Text("Determinar el dominio de definición de la función:", font_size=18, color=THEME["statement_text"])
        stmt_math = MathTex(
            r"h(x) = \ln\left(\frac{x^3 + 1}{x + 1}\right)",
            font_size=26,
            color=THEME["highlight"]
        )
        stmt_content = VGroup(stmt_desc, stmt_math).arrange(RIGHT, buff=0.35)
        
        stmt_box = SurroundingRectangle(
            stmt_content,
            color=THEME["statement_box"],
            buff=0.2,
            corner_radius=0.1,
            stroke_width=2.0
        )
        permanent_statement = VGroup(stmt_box, stmt_content).move_to([0, 2.5, 0])

        self.play(Create(stmt_box), Write(stmt_content), run_time=1.4)
        self.wait(4.5)

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 Pasos)
        # ==========================================================
        num_steps = 6
        step_labels = [
            "1/6: Condiciones RMD",
            "2/6: Factorización de Cubos",
            "3/6: Cancelación de Factores",
            "4/6: Análisis de Signo",
            "5/6: Conclusión del Dominio",
            "6/6: Interpretación Gráfica"
        ]
        dot_spacing = 1.05
        start_x = - (num_steps - 1) * dot_spacing / 2
        y_prog = -3.55

        prog_dots = []
        prog_track = VGroup()
        for i in range(num_steps):
            dot = Dot(point=[start_x + i * dot_spacing, y_prog, 0], radius=0.07, color=THEME["axes"])
            prog_dots.append(dot)
            if i > 0:
                seg = Line(prog_dots[i-1].get_center(), dot.get_center(), color=THEME["axes"], stroke_width=2)
                prog_track.add(seg)

        dots_grp = VGroup(*prog_dots)
        prog_label = Text(step_labels[0], font_size=13, color=THEME["header_color"]).next_to(dots_grp, UP, buff=0.14)
        progress_ui = VGroup(prog_track, dots_grp, prog_label)

        # Activar punto 1
        prog_dots[0].set_color(THEME["highlight"]).scale(1.25)
        self.play(FadeIn(progress_ui, shift=UP * 0.2), run_time=0.8)

        # Helper para avanzar la barra de progreso
        def advance_progress(current_idx, next_idx):
            anims = [
                prog_dots[current_idx].animate.set_color(THEME["success"]).scale(1.0 / 1.25),
                prog_dots[next_idx].animate.set_color(THEME["highlight"]).scale(1.25),
            ]
            new_lbl = Text(step_labels[next_idx], font_size=13, color=THEME["header_color"]).next_to(dots_grp, UP, buff=0.14)
            anims.append(FadeTransform(prog_label, new_lbl))
            return anims, new_lbl

        # Helper para explicaciones a la derecha
        def make_just(text_str):
            return Text(
                text_str,
                font_size=16,
                color=THEME["statement_text"],
                line_spacing=1.35
            ).move_to([3.1, 0.2, 0])

        # ==========================================================
        # PASO 1: Condiciones de RMD
        # ==========================================================
        eq_actual = MathTex(
            r"\begin{cases} x + 1 \neq 0 \implies x \neq -1 \\ \dfrac{x^3 + 1}{x + 1} > 0 \end{cases}",
            font_size=24,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just_actual = make_just(
            "1. Por Regla del Máximo Dominio:\n"
            "El denominador no puede anularse (x ≠ -1)\n"
            "y el argumento del logaritmo natural\n"
            "debe ser estrictamente positivo."
        )

        self.play(
            FadeIn(eq_actual, shift=DOWN * 0.3),
            FadeIn(just_actual, shift=DOWN * 0.3),
            run_time=1.1
        )
        
        hl_box = SurroundingRectangle(eq_actual, color=THEME["secondary"], buff=0.15, stroke_width=2.0)
        self.play(Create(hl_box), run_time=0.6)
        self.wait(5.0)

        # ==========================================================
        # PASO 2: Factorización de Suma de Cubos
        # ==========================================================
        # Avanzar progreso al paso 2
        prog_anims, prog_label = advance_progress(0, 1)

        eq_factorizada = MathTex(
            r"\frac{(x + 1)(x^2 - x + 1)}{x + 1}",
            font_size=28,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just_factor = make_just(
            "2. Factorización de suma de cubos:\n"
            "a³ + b³ = (a + b)(a² - ab + b²)\n"
            "con a = x  y  b = 1:\n"
            "x³ + 1 = (x + 1)(x² - x + 1)."
        )

        hl_factor = SurroundingRectangle(eq_factorizada, color=THEME["highlight"], buff=0.15, stroke_width=2.0)

        self.play(
            FadeOut(hl_box),
            ReplacementTransform(eq_actual, eq_factorizada),
            FadeOut(just_actual, shift=DOWN * 0.2),
            FadeIn(just_factor, shift=DOWN * 0.2),
            *prog_anims,
            run_time=1.8
        )
        self.play(Create(hl_factor), run_time=0.6)
        eq_actual = eq_factorizada
        just_actual = just_factor
        hl_box = hl_factor
        self.wait(6.0)

        # ==========================================================
        # PASO 3: Cancelación con Tachado Explícito en Rojo Poncho
        # ==========================================================
        prog_anims, prog_label = advance_progress(1, 2)

        # Ubicar los submobjects de (x + 1) en numerador y denominador
        top_factor = VGroup(*eq_actual[0][0:5])    # (x + 1) en numerador
        bot_factor = VGroup(*eq_actual[0][14:17])  # x + 1 en denominador

        # Líneas diagonales de tachado
        strike_top = Line(
            top_factor.get_corner(DL) + LEFT * 0.08 + DOWN * 0.04,
            top_factor.get_corner(UR) + RIGHT * 0.08 + UP * 0.04,
            color=THEME["poncho_red"],
            stroke_width=3.5
        )
        strike_bot = Line(
            bot_factor.get_corner(DL) + LEFT * 0.08 + DOWN * 0.04,
            bot_factor.get_corner(UR) + RIGHT * 0.08 + UP * 0.04,
            color=THEME["poncho_red"],
            stroke_width=3.5
        )

        just_cancel = make_just(
            "3. Simplificación fraccionaria:\n"
            "Cancelamos el factor común (x + 1)\n"
            "en numerador y denominador,\n"
            "válido para todo x ≠ -1."
        )

        # 1. Animamos el tachado explícito
        self.play(
            FadeOut(hl_box),
            FadeOut(just_actual, shift=DOWN * 0.2),
            FadeIn(just_cancel, shift=DOWN * 0.2),
            Create(strike_top),
            Create(strike_bot),
            *prog_anims,
            run_time=1.2
        )
        self.wait(3.0)  # Pausa para apreciar claramente el tachado físico

        # 2. Metamorfosis hacia el trinomio simplificado
        eq_simpl = MathTex(
            r"x^2 - x + 1 \quad (\text{para } x \neq -1)",
            font_size=25,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        hl_simpl = SurroundingRectangle(eq_simpl, color=THEME["secondary"], buff=0.15, stroke_width=2.0)

        self.play(
            ReplacementTransform(VGroup(eq_actual, strike_top, strike_bot), eq_simpl),
            run_time=1.5
        )
        self.play(Create(hl_simpl), run_time=0.6)
        eq_actual = eq_simpl
        just_actual = just_cancel
        hl_box = hl_simpl
        self.wait(5.5)

        # ==========================================================
        # PASO 4: Completación de Cuadrados y Signo
        # ==========================================================
        prog_anims, prog_label = advance_progress(2, 3)

        eq_cuad_pos = MathTex(
            r"x^2 - x + 1 = \left(x - \frac{1}{2}\right)^2 + \frac{3}{4} \ge \frac{3}{4} > 0",
            font_size=23,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just_signo = make_just(
            "4. Completación y signo:\n"
            "x² - x + 1 = (x - ½)² + ¾.\n"
            "Como (x - ½)² ≥ 0 y ¾ > 0,\n"
            "el argumento siempre es > 0 (∀ x ∈ ℝ)."
        )

        hl_cuad = SurroundingRectangle(eq_cuad_pos, color=THEME["curve"], buff=0.15, stroke_width=2.0)

        self.play(
            FadeOut(hl_box),
            ReplacementTransform(eq_actual, eq_cuad_pos),
            FadeOut(just_actual, shift=DOWN * 0.2),
            FadeIn(just_signo, shift=DOWN * 0.2),
            *prog_anims,
            run_time=1.8
        )
        self.play(Create(hl_cuad), run_time=0.6)
        eq_actual = eq_cuad_pos
        just_actual = just_signo
        hl_box = hl_cuad
        self.wait(6.8)

        # ==========================================================
        # PASO 5: Conclusión Final y Función Formal
        # ==========================================================
        prog_anims, prog_label = advance_progress(3, 4)

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

        final_eq_grp = VGroup(eq_dom, eq_form)

        just_final = make_just(
            "5. Conclusión:\n"
            "La única restricción real proviene\n"
            "del denominador inicial.\n"
            "El dominio excluye únicamente a x = -1."
        )

        hl_final = SurroundingRectangle(eq_dom, color=THEME["success"], buff=0.18, stroke_width=2.5)

        self.play(
            FadeOut(hl_box),
            ReplacementTransform(eq_actual, final_eq_grp),
            FadeOut(just_actual, shift=DOWN * 0.2),
            FadeIn(just_final, shift=DOWN * 0.2),
            *prog_anims,
            run_time=1.9
        )
        self.play(Create(hl_final), run_time=0.7)
        self.wait(5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica (Curva con punto abierto en x = -1)
        # ==========================================================
        prog_anims, prog_label = advance_progress(4, 5)

        # Panel izquierdo con resumen geométrico
        info_title = Text("6. Interpretación Gráfica", font_size=18, color=THEME["header_color"], weight=BOLD).move_to([-3.4, 1.2, 0])
        info_pts = VGroup(
            MathTex(r"\bullet \quad h(x) = \ln(x^2 - x + 1)", font_size=20, color=WHITE),
            MathTex(r"\bullet \quad \operatorname{Dom}(h) = \mathbb{R} \setminus \{-1\}", font_size=20, color=THEME["success"]),
            MathTex(r"\bullet \quad \text{Punto abierto en } (-1, \ln 3)", font_size=19, color=THEME["poncho_red"]),
            MathTex(r"\bullet \quad \text{Mínimo en } \left(\frac{1}{2}, \ln\frac{3}{4}\right)", font_size=19, color=THEME["highlight"]),
            MathTex(r"\bullet \quad \text{Cortes con eje } X \text{ en } 0 \text{ y } 1", font_size=19, color=THEME["curve"])
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28).next_to(info_title, DOWN, buff=0.32)
        info_grp = VGroup(info_title, info_pts)

        # Panel derecho: Ejes y gráfica de la función
        axes = Axes(
            x_range=[-3.2, 3.2, 1],
            y_range=[-1.0, 3.2, 1],
            x_length=5.6,
            y_length=3.8,
            tips=True,
            axis_config={
                "color": THEME["axes"],
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 14,
            }
        ).move_to([2.7, -0.45, 0])

        axes_labels = axes.get_axis_labels(
            x_label=MathTex("x", font_size=18, color=THEME["statement_text"]),
            y_label=MathTex("y", font_size=18, color=THEME["statement_text"])
        )

        # Curva en dos ramas para exhibir el punto abierto en x = -1
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

        # Punto abierto (agujero) en (-1, ln 3)
        hole_pt = axes.c2p(-1, np.log(3))
        hole_outer = Circle(
            radius=0.08,
            color=THEME["poncho_red"],
            stroke_width=3,
            fill_color=THEME["bg_color"],
            fill_opacity=1.0
        ).move_to(hole_pt)

        hole_lbl = MathTex(
            r"(-1, \ln 3) \notin \operatorname{Dom}(h)",
            font_size=15,
            color=THEME["poncho_red"]
        ).next_to(hole_outer, UP + LEFT, buff=0.15)

        hole_arrow = Arrow(
            hole_lbl.get_bottom(),
            hole_outer.get_top(),
            buff=0.05,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.25,
            color=THEME["poncho_red"]
        )

        # Puntos clave destacados: raíces y vértice mínimo
        p_min = Dot(axes.c2p(0.5, np.log(0.75)), radius=0.06, color=THEME["highlight"])
        p_r1 = Dot(axes.c2p(0, 0), radius=0.05, color=THEME["success"])
        p_r2 = Dot(axes.c2p(1, 0), radius=0.05, color=THEME["success"])

        # Transición hacia el paso 6
        self.play(
            FadeOut(hl_final),
            FadeOut(final_eq_grp, shift=DOWN * 0.2),
            FadeOut(just_final, shift=DOWN * 0.2),
            FadeIn(info_grp, shift=DOWN * 0.2),
            Create(axes),
            Write(axes_labels),
            *prog_anims,
            run_time=1.8
        )

        # Trazado de la curva continua con salto en x = -1
        self.play(
            Create(curve_left),
            Create(curve_right),
            run_time=1.8
        )

        # Resaltado del punto abierto, raíces y mínimo
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
        # Cierre suave
        # ==========================================================
        graph_mobs = VGroup(
            info_grp, axes, axes_labels,
            curve_left, curve_right,
            hole_outer, hole_lbl, hole_arrow,
            p_min, p_r1, p_r2
        )
        self.play(
            FadeOut(graph_mobs, shift=DOWN * 0.3),
            FadeOut(progress_ui, shift=DOWN * 0.3),
            FadeOut(permanent_statement, shift=DOWN * 0.3),
            FadeOut(header, shift=DOWN * 0.3),
            run_time=1.4
        )
