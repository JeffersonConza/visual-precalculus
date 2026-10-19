"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.1.4: Regla del Máximo Dominio (RMD)
Ejercicio 5.2 (Página 27 del libro / Página 46 del PDF)

Modo: Metamorfosis 3Blue1Brown con ritmo pausado y pedagógico (~55 segundos)
- Enunciado permanente en la parte superior.
- Sin "(Par)" en el título.
- Sin etiquetas de columnas.
- Transiciones más suaves y tiempos de lectura generosos para asimilación.
- Resaltados sincronizados.
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
        self.play(FadeIn(header, shift=DOWN * 0.2), run_time=0.8)

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
        self.wait(3.5)  # Pausa cómoda para leer y asimilar el problema

        # Helper para posicionar explicaciones a la derecha
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
            run_time=1.2
        )
        
        hl_box = SurroundingRectangle(eq_actual, color=THEME["secondary"], buff=0.15, stroke_width=2.0)
        self.play(Create(hl_box), run_time=0.6)
        self.wait(3.5)  # Tiempo de lectura de las dos condiciones

        # ==========================================================
        # PASO 2: Aislamiento del argumento a simplificar
        # ==========================================================
        eq_next = MathTex(
            r"\frac{x^3 + 1}{x + 1}",
            font_size=32,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just_next = make_just(
            "2. Analizamos el argumento:\n"
            "Buscamos simplificar la expresión\n"
            "factorizando el numerador."
        )

        self.play(
            FadeOut(hl_box),
            ReplacementTransform(eq_actual, eq_next),
            FadeOut(just_actual, shift=DOWN * 0.2),
            FadeIn(just_next, shift=DOWN * 0.2),
            run_time=1.5  # Transición suave
        )
        eq_actual = eq_next
        just_actual = just_next
        self.wait(2.5)

        # ==========================================================
        # PASO 3: Metamorfosis - Expansión de suma de cubos
        # ==========================================================
        eq_next = MathTex(
            r"\frac{(x + 1)(x^2 - x + 1)}{x + 1}",
            font_size=28,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just_next = make_just(
            "Suma de cubos notables:\n"
            "a³ + b³ = (a + b)(a² - ab + b²)\n"
            "con a = x  y  b = 1:\n"
            "x³ + 1 = (x + 1)(x² - x + 1)."
        )

        hl_box = SurroundingRectangle(eq_next, color=THEME["highlight"], buff=0.15, stroke_width=2.0)

        self.play(
            ReplacementTransform(eq_actual, eq_next),
            FadeOut(just_actual, shift=DOWN * 0.2),
            FadeIn(just_next, shift=DOWN * 0.2),
            run_time=1.8  # Movimiento pausado de los términos
        )
        self.play(Create(hl_box), run_time=0.6)
        eq_actual = eq_next
        just_actual = just_next
        self.wait(4.0)  # Pausa generosa para revisar la factorización

        # ==========================================================
        # PASO 4: Metamorfosis - Cancelación del factor común
        # ==========================================================
        eq_next = MathTex(
            r"x^2 - x + 1 \quad (\text{para } x \neq -1)",
            font_size=25,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just_next = make_just(
            "3. Simplificación fraccionaria:\n"
            "Cancelamos el factor común (x + 1)\n"
            "en numerador y denominador,\n"
            "válido para todo x ≠ -1."
        )

        hl_next = SurroundingRectangle(eq_next, color=THEME["secondary"], buff=0.15, stroke_width=2.0)

        self.play(
            FadeOut(hl_box),
            ReplacementTransform(eq_actual, eq_next),
            FadeOut(just_actual, shift=DOWN * 0.2),
            FadeIn(just_next, shift=DOWN * 0.2),
            run_time=1.8
        )
        self.play(Create(hl_next), run_time=0.6)
        eq_actual = eq_next
        just_actual = just_next
        hl_box = hl_next
        self.wait(3.8)

        # ==========================================================
        # PASO 5: Metamorfosis - Completando el cuadrado
        # ==========================================================
        eq_next = MathTex(
            r"\left(x - \frac{1}{2}\right)^2 + \frac{3}{4}",
            font_size=28,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just_next = make_just(
            "4. Completamos el cuadrado:\n"
            "x² - x + 1 =\n"
            "(x² - 2·½x + ¼) + (1 - ¼) =\n"
            "(x - ½)² + ¾."
        )

        hl_next = SurroundingRectangle(eq_next, color=THEME["curve"], buff=0.15, stroke_width=2.0)

        self.play(
            FadeOut(hl_box),
            ReplacementTransform(eq_actual, eq_next),
            FadeOut(just_actual, shift=DOWN * 0.2),
            FadeIn(just_next, shift=DOWN * 0.2),
            run_time=1.8
        )
        self.play(Create(hl_next), run_time=0.6)
        eq_actual = eq_next
        just_actual = just_next
        hl_box = hl_next
        self.wait(4.0)

        # ==========================================================
        # PASO 6: Metamorfosis - Demostración de positividad estricta
        # ==========================================================
        eq_next = MathTex(
            r"\left(x - \frac{1}{2}\right)^2 + \frac{3}{4} \ge \frac{3}{4} > 0",
            font_size=26,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just_next = make_just(
            "Propiedad de no negatividad:\n"
            "Como (x - ½)² ≥ 0  y  ¾ > 0,\n"
            "el argumento siempre es > 0 (∀ x ∈ ℝ).\n"
            "¡No hay restricciones adicionales!"
        )

        hl_next = SurroundingRectangle(eq_next, color=THEME["highlight"], buff=0.15, stroke_width=2.0)

        self.play(
            FadeOut(hl_box),
            ReplacementTransform(eq_actual, eq_next),
            FadeOut(just_actual, shift=DOWN * 0.2),
            FadeIn(just_next, shift=DOWN * 0.2),
            run_time=1.8
        )
        self.play(Create(hl_next), run_time=0.6)
        eq_actual = eq_next
        just_actual = just_next
        hl_box = hl_next
        self.wait(4.5)

        # ==========================================================
        # PASO 7: Metamorfosis hacia la Conclusión Final
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

        final_eq_grp = VGroup(eq_dom, eq_form)

        just_next = make_just(
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
            FadeIn(just_next, shift=DOWN * 0.2),
            run_time=2.0  # Transición final muy elegante
        )
        self.play(Create(hl_final), run_time=0.7)
        self.wait(5.0)  # Tiempo final para asimilar la respuesta

        # ==========================================================
        # Cierre suave
        # ==========================================================
        self.play(
            FadeOut(final_eq_grp, shift=DOWN * 0.3),
            FadeOut(just_next, shift=DOWN * 0.3),
            FadeOut(hl_final, shift=DOWN * 0.3),
            FadeOut(permanent_statement, shift=DOWN * 0.3),
            FadeOut(header, shift=DOWN * 0.3),
            run_time=1.4
        )
