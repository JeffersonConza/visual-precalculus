"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.1.4: Regla del Máximo Dominio (RMD)
Ejercicio 5.2 (Página 27 del libro / Página 46 del PDF)

Estructura de dos columnas:
- Columna Izquierda: Desarrollo algebraico con resaltado de términos modificados.
- Columna Derecha: Justificación ("¿qué se hizo en este paso?").
"""
from manim import *
import sys
import os

# Permitir importación del módulo común
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import BaseExerciseScene
from common.styles import THEME

class Ejercicio05_02(BaseExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado y Enunciado
        # ==========================================================
        self.show_header(
            chapter="5",
            exercise_num=2,
            topic="Regla del Máximo Dominio (RMD)"
        )

        enunciado_line = Text("Determinar el dominio de definición de la función:", font_size=23, color=THEME["statement_text"])
        enunciado_math = MathTex(
            r"h(x) = \ln\left(\frac{x^3 + 1}{x + 1}\right)",
            font_size=34,
            color=THEME["highlight"]
        )
        enunciado_grp = VGroup(enunciado_line, enunciado_math).arrange(DOWN, buff=0.25)
        
        # Presentar y minimizar arriba
        self.present_statement(enunciado_grp, read_time=4.0)

        # ==========================================================
        # 2. Estructura de Dos Columnas (Ecuaciones | Justificación)
        # ==========================================================
        col_x = 0.2  # Posición de la línea divisoria vertical
        
        # Encabezados de columnas
        head_izq = Text("Desarrollo Matemático", font_size=18, color=THEME["header_color"], weight=BOLD)
        head_izq.move_to([-3.4, 2.1, 0])
        
        head_der = Text("Justificación / Procedimiento", font_size=18, color=THEME["header_color"], weight=BOLD)
        head_der.move_to([3.6, 2.1, 0])

        # Divisor vertical y horizontal de encabezados
        v_divider = Line(UP * 2.3, DOWN * 3.0, color=THEME["axes"], stroke_width=1.5).move_to([col_x, -0.4, 0])
        h_divider = Line(LEFT * 6.5, RIGHT * 6.5, color=THEME["axes"], stroke_width=1.5).move_to([0, 1.8, 0])

        self.play(
            Create(v_divider),
            Create(h_divider),
            FadeIn(head_izq, shift=DOWN * 0.1),
            FadeIn(head_der, shift=DOWN * 0.1),
            run_time=0.9
        )
        self.wait(1.0)

        # Helper para crear fila de dos columnas
        def make_row(y_pos, eq_mobj, just_text_str, just_tex=None):
            eq_mobj.move_to([-3.4, y_pos, 0])
            txt = Text(just_text_str, font_size=15, color=THEME["statement_text"], line_spacing=1.2)
            if just_tex:
                grp_der = VGroup(txt, just_tex).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
            else:
                grp_der = txt
            grp_der.next_to(v_divider, RIGHT, buff=0.4).set_y(y_pos)
            return eq_mobj, grp_der

        # ----------------------------------------------------------
        # BLOQUE 1: Condiciones RMD y Factorización
        # ----------------------------------------------------------
        # Fila 1: Condiciones RMD
        eq_1 = MathTex(
            r"\begin{cases} x + 1 \neq 0 \implies x \neq -1 \\ \dfrac{x^3 + 1}{x + 1} > 0 \end{cases}",
            font_size=23,
            color=WHITE
        )
        eq_1_m, just_1 = make_row(
            1.0,
            eq_1,
            "1. RMD (Regla del Máximo Dominio):\nEl denominador no puede anularse\ny el argumento de ln debe ser > 0."
        )

        self.play(FadeIn(eq_1_m, shift=RIGHT * 0.2), FadeIn(just_1, shift=LEFT * 0.2), run_time=1.2)
        # Resaltado en x != -1
        hl_1 = SurroundingRectangle(eq_1_m, color=THEME["secondary"], buff=0.12, stroke_width=2)
        self.play(Create(hl_1), run_time=0.6)
        self.wait(2.2)

        # Fila 2: Factorización suma de cubos
        eq_2 = MathTex(
            r"x^3 + 1 = (x + 1)(x^2 - x + 1)",
            font_size=23,
            color=THEME["highlight"]
        )
        eq_2_m, just_2 = make_row(
            -0.6,
            eq_2,
            "2. Factorización de suma de cubos:\nAplicamos la identidad notable\na³ + b³ = (a + b)(a² - ab + b²)."
        )

        self.play(FadeIn(eq_2_m, shift=RIGHT * 0.2), FadeIn(just_2, shift=LEFT * 0.2), run_time=1.2)
        hl_2 = SurroundingRectangle(eq_2_m, color=THEME["highlight"], buff=0.12, stroke_width=2)
        self.play(Create(hl_2), run_time=0.6)
        self.wait(2.5)

        # Transición al siguiente bloque (limpiar filas 1 y 2 para mantener espacio amplio)
        self.play(
            FadeOut(eq_1_m), FadeOut(just_1), FadeOut(hl_1),
            FadeOut(eq_2_m), FadeOut(just_2), FadeOut(hl_2),
            run_time=0.6
        )

        # ----------------------------------------------------------
        # BLOQUE 2: Simplificación y Completación de Cuadrados
        # ----------------------------------------------------------
        # Fila 3: Simplificación fraccionaria
        eq_3 = MathTex(
            r"\frac{x^3 + 1}{x + 1} = \frac{(x+1)(x^2 - x + 1)}{x+1} = x^2 - x + 1",
            font_size=21,
            color=WHITE
        )
        eq_3_m, just_3 = make_row(
            1.0,
            eq_3,
            "3. Simplificación de la fracción:\nCancelamos el factor común (x + 1)\nya que x ≠ -1 garantiza división válida."
        )

        self.play(FadeIn(eq_3_m, shift=RIGHT * 0.2), FadeIn(just_3, shift=LEFT * 0.2), run_time=1.2)
        # Resaltado en el resultado simplificado x^2 - x + 1
        hl_3 = SurroundingRectangle(eq_3_m, color=THEME["secondary"], buff=0.12, stroke_width=2)
        self.play(Create(hl_3), run_time=0.6)
        self.wait(2.5)

        # Fila 4: Completación del cuadrado del trinomio
        eq_4 = MathTex(
            r"x^2 - x + 1 = \left(x - \frac{1}{2}\right)^2 + \frac{3}{4} \ge \frac{3}{4} > 0",
            font_size=21,
            color=THEME["highlight"]
        )
        eq_4_m, just_4 = make_row(
            -0.6,
            eq_4,
            "4. Completando cuadrados:\nTodo cuadrado es ≥ 0 y 3/4 > 0.\nEl argumento siempre es > 0 (∀ x ∈ ℝ)."
        )

        self.play(FadeIn(eq_4_m, shift=RIGHT * 0.2), FadeIn(just_4, shift=LEFT * 0.2), run_time=1.2)
        hl_4 = SurroundingRectangle(eq_4_m, color=THEME["curve"], buff=0.12, stroke_width=2)
        self.play(Create(hl_4), run_time=0.6)
        self.wait(3.0)

        # Limpiar filas 3 y 4
        self.play(
            FadeOut(eq_3_m), FadeOut(just_3), FadeOut(hl_3),
            FadeOut(eq_4_m), FadeOut(just_4), FadeOut(hl_4),
            run_time=0.6
        )

        # ----------------------------------------------------------
        # BLOQUE 3: Conclusión y Conjunto Solución
        # ----------------------------------------------------------
        eq_5 = MathTex(
            r"\operatorname{Dom}(h) = \mathbb{R} \setminus \{-1\}",
            font_size=26,
            color=THEME["success"]
        )
        eq_5_m, just_5 = make_row(
            0.9,
            eq_5,
            "5. Conclusión del Dominio:\nComo el argumento siempre es positivo,\nla única exclusión es el cero del denominador."
        )

        self.play(FadeIn(eq_5_m, shift=RIGHT * 0.2), FadeIn(just_5, shift=LEFT * 0.2), run_time=1.2)
        hl_5 = SurroundingRectangle(eq_5_m, color=THEME["success"], buff=0.15, stroke_width=2.5)
        self.play(Create(hl_5), run_time=0.6)
        self.wait(2.0)

        # Definición formal en la parte inferior
        formal_def = MathTex(
            r"h: \mathbb{R} \setminus \{-1\} \longrightarrow \mathbb{R}, \quad x \longmapsto \ln(x^2 - x + 1)",
            font_size=23,
            color=THEME["highlight"]
        ).move_to([-3.4, -0.6, 0])

        formal_desc = Text(
            "Función bien definida por RMD\ncon codominio en ℝ.",
            font_size=15,
            color=THEME["statement_text"],
            line_spacing=1.2
        ).next_to(v_divider, RIGHT, buff=0.4).set_y(-0.6)

        self.play(FadeIn(formal_def, shift=UP * 0.1), FadeIn(formal_desc, shift=UP * 0.1), run_time=1.0)
        self.wait(3.5)

        # Limpiar todo para la pantalla final de conclusión
        self.play(
            FadeOut(v_divider),
            FadeOut(h_divider),
            FadeOut(head_izq),
            FadeOut(head_der),
            FadeOut(eq_5_m),
            FadeOut(just_5),
            FadeOut(hl_5),
            FadeOut(formal_def),
            FadeOut(formal_desc),
            run_time=0.7
        )

        # ==========================================================
        # 3. Pantalla Final Destacada
        # ==========================================================
        concl_title = Text("Resultado Final:", font_size=24, color=THEME["header_color"]).shift(UP * 0.8)
        concl_res = MathTex(
            r"\operatorname{Dom}(h) = \mathbb{R} \setminus \{-1\} = (-\infty, -1) \cup (-1, +\infty)",
            font_size=30,
            color=THEME["success"]
        ).next_to(concl_title, DOWN, buff=0.4)

        self.play(FadeIn(concl_title), Write(concl_res), run_time=1.2)
        self.conclude_solution(concl_res, wait_time=4.0)
