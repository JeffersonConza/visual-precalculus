"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.1.4: Regla del Máximo Dominio (RMD)
Ejercicio 5.2 (Página 27 del libro / Página 46 del PDF)

Modo: Metamorfosis 3Blue1Brown con:
- Tachado explícito en color rojo poncho al cancelar el factor común.
- Barra de progreso interactiva en la parte inferior (5 pasos).
- Enunciado permanente en la parte superior.
- Sin "(Par)" en el título.
- Sin etiquetas de columnas.
- Ritmo calibrado (~56 segundos).
"""
from manim import *
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
        # 3. Barra de Progreso Inferior (5 Pasos)
        # ==========================================================
        num_steps = 5
        step_labels = [
            "1/5: Condiciones RMD",
            "2/5: Factorización de Cubos",
            "3/5: Cancelación de Factores",
            "4/5: Análisis de Signo",
            "5/5: Conclusión del Dominio"
        ]
        dot_spacing = 1.1
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
        self.wait(8.2)

        # ==========================================================
        # Cierre suave
        # ==========================================================
        self.play(
            FadeOut(final_eq_grp, shift=DOWN * 0.3),
            FadeOut(just_final, shift=DOWN * 0.3),
            FadeOut(hl_final, shift=DOWN * 0.3),
            FadeOut(progress_ui, shift=DOWN * 0.3),
            FadeOut(permanent_statement, shift=DOWN * 0.3),
            FadeOut(header, shift=DOWN * 0.3),
            run_time=1.4
        )
