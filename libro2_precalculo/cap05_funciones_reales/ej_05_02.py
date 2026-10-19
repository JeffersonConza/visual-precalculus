"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.1.4: Regla del Máximo Dominio (RMD)
Ejercicio 5.2 (Página 27 del libro / Página 46 del PDF)

Estructura de dos columnas con desplazamiento vertical real:
- Enunciado permanente en la parte superior durante todo el video.
- Sin "(Par)" en el título.
- Sin etiquetas de columnas ("Desarrollo Matemático" / "Qué se hizo").
- Desplazamiento físico en vertical de cada bloque (entra desde arriba, sale hacia abajo).
- Resaltados en los términos modificados.
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
        self.play(FadeIn(header, shift=DOWN * 0.2), run_time=0.6)

        # ==========================================================
        # 2. Enunciado Permanente (Se mantiene durante todo el video)
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

        # Entrada del enunciado permanente
        self.play(Create(stmt_box), Write(stmt_content), run_time=1.2)
        self.wait(2.5)

        # Helper para crear pares [Ecuación (Izquierda) | Justificación (Derecha)]
        def make_row(y_pos, eq_mobj, just_text_str):
            eq_mobj.move_to([-3.4, y_pos, 0])
            just_mobj = Text(
                just_text_str,
                font_size=15,
                color=THEME["statement_text"],
                line_spacing=1.2
            ).move_to([3.1, y_pos, 0])
            return eq_mobj, just_mobj

        # ==========================================================
        # DIAPOSITIVA 1: Condiciones RMD y Factorización de Cubos
        # ==========================================================
        eq_1 = MathTex(
            r"\begin{cases} x + 1 \neq 0 \implies x \neq -1 \\ \dfrac{x^3 + 1}{x + 1} > 0 \end{cases}",
            font_size=23,
            color=WHITE
        )
        eq_1_m, just_1 = make_row(
            0.8,
            eq_1,
            "1. Por Regla del Máximo Dominio:\nEl denominador no puede ser 0\ny el argumento de ln debe ser > 0."
        )

        eq_2 = MathTex(
            r"x^3 + 1 = (x + 1)(x^2 - x + 1)",
            font_size=23,
            color=THEME["highlight"]
        )
        eq_2_m, just_2 = make_row(
            -1.0,
            eq_2,
            "2. Suma de cubos notables:\na³ + b³ = (a + b)(a² - ab + b²)\naplicado con a = x  y  b = 1."
        )

        slide_1 = VGroup(eq_1_m, just_1, eq_2_m, just_2)
        
        # Desplazamiento vertical de entrada (desde arriba hacia su posición)
        slide_1.shift(UP * 4.5)
        self.play(slide_1.animate.shift(DOWN * 4.5), run_time=1.0)

        # Resaltado en la restricción x != -1
        hl_1 = SurroundingRectangle(eq_1_m, color=THEME["secondary"], buff=0.12, stroke_width=2)
        self.play(Create(hl_1), run_time=0.5)
        self.wait(2.2)

        # Resaltado en la factorización
        hl_2 = SurroundingRectangle(eq_2_m, color=THEME["highlight"], buff=0.12, stroke_width=2)
        self.play(Create(hl_2), run_time=0.5)
        self.wait(2.5)

        # Desplazamiento vertical de salida (se desplaza físicamente hacia abajo)
        self.play(
            slide_1.animate.shift(DOWN * 5.0),
            hl_1.animate.shift(DOWN * 5.0),
            hl_2.animate.shift(DOWN * 5.0),
            run_time=0.8
        )
        self.remove(slide_1, hl_1, hl_2)

        # ==========================================================
        # DIAPOSITIVA 2: Simplificación Fraccionaria y Cuadrados
        # ==========================================================
        eq_3 = MathTex(
            r"\frac{x^3 + 1}{x + 1} = \frac{(x+1)(x^2 - x + 1)}{x+1} = x^2 - x + 1",
            font_size=21,
            color=WHITE
        )
        eq_3_m, just_3 = make_row(
            0.8,
            eq_3,
            "3. Simplificación de la fracción:\nCancelamos el factor común (x + 1)\nya que x ≠ -1 garantiza división válida."
        )

        eq_4 = MathTex(
            r"x^2 - x + 1 = \left(x - \frac{1}{2}\right)^2 + \frac{3}{4} \ge \frac{3}{4} > 0",
            font_size=21,
            color=THEME["highlight"]
        )
        eq_4_m, just_4 = make_row(
            -1.0,
            eq_4,
            "4. Completando el cuadrado:\nTodo cuadrado es ≥ 0  y  3/4 > 0.\nEl argumento siempre es > 0 (∀ x ∈ ℝ)."
        )

        slide_2 = VGroup(eq_3_m, just_3, eq_4_m, just_4)

        # Desplazamiento vertical de entrada (desde arriba)
        slide_2.shift(UP * 4.5)
        self.play(slide_2.animate.shift(DOWN * 4.5), run_time=1.0)

        # Resaltado en el trinomio simplificado
        hl_3 = SurroundingRectangle(eq_3_m, color=THEME["secondary"], buff=0.12, stroke_width=2)
        self.play(Create(hl_3), run_time=0.5)
        self.wait(2.2)

        # Resaltado en la completación de cuadrado y positividad
        hl_4 = SurroundingRectangle(eq_4_m, color=THEME["curve"], buff=0.12, stroke_width=2)
        self.play(Create(hl_4), run_time=0.5)
        self.wait(2.8)

        # Desplazamiento vertical de salida (hacia abajo)
        self.play(
            slide_2.animate.shift(DOWN * 5.0),
            hl_3.animate.shift(DOWN * 5.0),
            hl_4.animate.shift(DOWN * 5.0),
            run_time=0.8
        )
        self.remove(slide_2, hl_3, hl_4)

        # ==========================================================
        # DIAPOSITIVA 3: Conclusión del Dominio y Función Formal
        # ==========================================================
        eq_5 = MathTex(
            r"\operatorname{Dom}(h) = \mathbb{R} \setminus \{-1\}",
            font_size=26,
            color=THEME["success"]
        )
        eq_5_m, just_5 = make_row(
            0.8,
            eq_5,
            "5. Conclusión del Dominio:\nAl ser el argumento siempre positivo,\nla única exclusión es el cero del denominador."
        )

        eq_6 = MathTex(
            r"h: \mathbb{R} \setminus \{-1\} \longrightarrow \mathbb{R}, \quad x \longmapsto \ln(x^2 - x + 1)",
            font_size=21,
            color=THEME["highlight"]
        )
        eq_6_m, just_6 = make_row(
            -1.0,
            eq_6,
            "6. Función Formal (RMD):\nDefinida con su dominio de definición\ny su regla simplificada correspondiente."
        )

        slide_3 = VGroup(eq_5_m, just_5, eq_6_m, just_6)

        # Desplazamiento vertical de entrada (desde arriba)
        slide_3.shift(UP * 4.5)
        self.play(slide_3.animate.shift(DOWN * 4.5), run_time=1.0)

        hl_5 = SurroundingRectangle(eq_5_m, color=THEME["success"], buff=0.15, stroke_width=2.5)
        self.play(Create(hl_5), run_time=0.5)
        self.wait(2.2)

        hl_6 = SurroundingRectangle(eq_6_m, color=THEME["highlight"], buff=0.12, stroke_width=2)
        self.play(Create(hl_6), run_time=0.5)
        self.wait(3.0)

        # Desplazamiento de salida hacia abajo
        self.play(
            slide_3.animate.shift(DOWN * 5.0),
            hl_5.animate.shift(DOWN * 5.0),
            hl_6.animate.shift(DOWN * 5.0),
            run_time=0.8
        )
        self.remove(slide_3, hl_5, hl_6)

        # ==========================================================
        # 4. Pantalla de Conclusión Final (Desplazamiento vertical)
        # ==========================================================
        res_label = Text("Dominio de Definición Obtenido:", font_size=21, color=THEME["header_color"])
        res_math = MathTex(
            r"\operatorname{Dom}(h) = \mathbb{R} \setminus \{-1\} = (-\infty, -1) \cup (-1, +\infty)",
            font_size=28,
            color=THEME["success"]
        )
        final_group = VGroup(res_label, res_math).arrange(DOWN, buff=0.35).move_to([0, -0.4, 0])
        
        final_box = SurroundingRectangle(
            final_group,
            color=THEME["success"],
            buff=0.25,
            corner_radius=0.12,
            stroke_width=2.5
        )

        final_scene = VGroup(final_group, final_box)
        final_scene.shift(UP * 4.5)

        # Entrada vertical desde arriba hacia el centro
        self.play(final_scene.animate.shift(DOWN * 4.5), run_time=1.0)
        self.wait(4.0)

        # Cierre final deslizándose hacia abajo
        self.play(
            final_scene.animate.shift(DOWN * 5.0),
            permanent_statement.animate.shift(DOWN * 5.0),
            header.animate.shift(DOWN * 5.0),
            run_time=1.0
        )
