"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.1.4: Regla del Máximo Dominio (RMD)
Ejercicio 5.2 (Página 27 del libro / Página 46 del PDF)

Estructura de dos columnas (sin líneas divisorias):
- Columna Izquierda: Desarrollo algebraico con resaltado de términos modificados.
- Columna Derecha: Justificación ("¿qué se hizo en este paso?").
- Avance de diapositivas fluido hacia abajo (shift=DOWN).
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
        # 1. Barra superior limpia (sin solapamientos)
        # ==========================================================
        top_bar = self.show_top_bar(
            chapter="5",
            exercise_num=2,
            topic="Regla del Máximo Dominio (RMD)"
        )

        # 2. Enunciado inicial
        enunciado_line = Text("Determinar el dominio de definición de:", font_size=22, color=THEME["statement_text"])
        enunciado_math = MathTex(
            r"h(x) = \ln\left(\frac{x^3 + 1}{x + 1}\right)",
            font_size=32,
            color=THEME["highlight"]
        )
        enunciado_content = VGroup(enunciado_line, enunciado_math).arrange(DOWN, buff=0.25)
        
        # Pastilla compacta que se ubicará arriba tras la lectura
        badge_tex = MathTex(
            r"\text{Función: } h(x) = \ln\left(\frac{x^3 + 1}{x + 1}\right)",
            font_size=19,
            color=THEME["highlight"]
        )
        
        # Presentar centrado y luego compactar hacia arriba
        top_badge = self.present_initial_statement(
            statement_content=enunciado_content,
            formula_badge=badge_tex,
            read_time=3.5
        )

        # ==========================================================
        # 3. Encabezados de Columnas (Sin líneas divisorias)
        # ==========================================================
        head_izq = Text("Desarrollo Matemático", font_size=17, color=THEME["header_color"], weight=BOLD)
        head_izq.move_to([-3.4, 2.0, 0])

        head_der = Text("¿Qué se hizo en este paso?", font_size=17, color=THEME["header_color"], weight=BOLD)
        head_der.move_to([3.1, 2.0, 0])

        column_heads = VGroup(head_izq, head_der)
        self.play(FadeIn(column_heads, shift=DOWN * 0.3), run_time=0.7)
        self.wait(0.5)

        # Helper para crear pares de (Ecuación | Justificación)
        def create_step(y_center, eq_obj, just_text_str):
            eq_obj.move_to([-3.4, y_center, 0])
            just_obj = Text(
                just_text_str,
                font_size=15,
                color=THEME["statement_text"],
                line_spacing=1.2
            ).move_to([3.1, y_center, 0])
            return eq_obj, just_obj

        # ==========================================================
        # DIAPOSITIVA 1: Condiciones de Existencia (RMD) y Factorización
        # ==========================================================
        # Fila 1: Condiciones RMD
        eq_1 = MathTex(
            r"\begin{cases} x + 1 \neq 0 \implies x \neq -1 \\ \dfrac{x^3 + 1}{x + 1} > 0 \end{cases}",
            font_size=23,
            color=WHITE
        )
        eq_1_m, just_1 = create_step(
            0.9,
            eq_1,
            "1. Regla del Máximo Dominio (RMD):\nEl denominador no puede ser 0\ny el argumento de ln debe ser > 0."
        )

        # Fila 2: Factorización suma de cubos
        eq_2 = MathTex(
            r"x^3 + 1 = (x + 1)(x^2 - x + 1)",
            font_size=23,
            color=THEME["highlight"]
        )
        eq_2_m, just_2 = create_step(
            -0.7,
            eq_2,
            "2. Factorización de suma de cubos:\nAplicamos la identidad notable\na³ + b³ = (a + b)(a² - ab + b²)."
        )

        slide_1 = VGroup(eq_1_m, just_1, eq_2_m, just_2)
        
        # Entrada con avance hacia abajo
        self.play(FadeIn(slide_1, shift=DOWN * 0.4), run_time=1.0)

        # Resaltados específicos paso a paso
        hl_1 = SurroundingRectangle(eq_1_m, color=THEME["secondary"], buff=0.12, stroke_width=2)
        self.play(Create(hl_1), run_time=0.5)
        self.wait(2.2)

        hl_2 = SurroundingRectangle(eq_2_m, color=THEME["highlight"], buff=0.12, stroke_width=2)
        self.play(Create(hl_2), run_time=0.5)
        self.wait(2.5)

        # Salida hacia abajo (avance de diapositiva hacia abajo)
        self.play(
            FadeOut(slide_1, shift=DOWN * 0.4),
            FadeOut(hl_1, shift=DOWN * 0.4),
            FadeOut(hl_2, shift=DOWN * 0.4),
            run_time=0.7
        )

        # ==========================================================
        # DIAPOSITIVA 2: Simplificación Fraccionaria y Cuadrados
        # ==========================================================
        # Fila 3: Simplificación de la fracción
        eq_3 = MathTex(
            r"\frac{x^3 + 1}{x + 1} = \frac{(x+1)(x^2 - x + 1)}{x+1} = x^2 - x + 1",
            font_size=21,
            color=WHITE
        )
        eq_3_m, just_3 = create_step(
            0.9,
            eq_3,
            "3. Simplificación de la fracción:\nCancelamos el factor común (x + 1)\nya que x ≠ -1 garantiza división válida."
        )

        # Fila 4: Completación de cuadrados
        eq_4 = MathTex(
            r"x^2 - x + 1 = \left(x - \frac{1}{2}\right)^2 + \frac{3}{4} \ge \frac{3}{4} > 0",
            font_size=21,
            color=THEME["highlight"]
        )
        eq_4_m, just_4 = create_step(
            -0.7,
            eq_4,
            "4. Completando el cuadrado:\nTodo cuadrado es ≥ 0 y 3/4 > 0.\nEl argumento siempre es > 0 (∀ x ∈ ℝ)."
        )

        slide_2 = VGroup(eq_3_m, just_3, eq_4_m, just_4)

        # Entrada con avance hacia abajo
        self.play(FadeIn(slide_2, shift=DOWN * 0.4), run_time=1.0)

        # Resaltados paso a paso
        hl_3 = SurroundingRectangle(eq_3_m, color=THEME["secondary"], buff=0.12, stroke_width=2)
        self.play(Create(hl_3), run_time=0.5)
        self.wait(2.2)

        hl_4 = SurroundingRectangle(eq_4_m, color=THEME["curve"], buff=0.12, stroke_width=2)
        self.play(Create(hl_4), run_time=0.5)
        self.wait(2.8)

        # Salida hacia abajo
        self.play(
            FadeOut(slide_2, shift=DOWN * 0.4),
            FadeOut(hl_3, shift=DOWN * 0.4),
            FadeOut(hl_4, shift=DOWN * 0.4),
            run_time=0.7
        )

        # ==========================================================
        # DIAPOSITIVA 3: Conclusión y Función Bien Definida
        # ==========================================================
        eq_5 = MathTex(
            r"\operatorname{Dom}(h) = \mathbb{R} \setminus \{-1\}",
            font_size=26,
            color=THEME["success"]
        )
        eq_5_m, just_5 = create_step(
            0.9,
            eq_5,
            "5. Conclusión del Dominio:\nComo el argumento siempre es positivo,\nla única exclusión es el cero del denominador."
        )

        eq_6 = MathTex(
            r"h: \mathbb{R} \setminus \{-1\} \longrightarrow \mathbb{R}, \quad x \longmapsto \ln(x^2 - x + 1)",
            font_size=21,
            color=THEME["highlight"]
        )
        eq_6_m, just_6 = create_step(
            -0.7,
            eq_6,
            "6. Función Formal (RMD):\nDefinida con su dominio máximo y\nregla de correspondencia simplificada."
        )

        slide_3 = VGroup(eq_5_m, just_5, eq_6_m, just_6)

        # Entrada hacia abajo
        self.play(FadeIn(slide_3, shift=DOWN * 0.4), run_time=1.0)

        hl_5 = SurroundingRectangle(eq_5_m, color=THEME["success"], buff=0.15, stroke_width=2.5)
        self.play(Create(hl_5), run_time=0.5)
        self.wait(2.0)

        hl_6 = SurroundingRectangle(eq_6_m, color=THEME["highlight"], buff=0.12, stroke_width=2)
        self.play(Create(hl_6), run_time=0.5)
        self.wait(3.0)

        # Salida hacia abajo de todo el espacio de trabajo para la pantalla final
        self.play(
            FadeOut(column_heads, shift=DOWN * 0.4),
            FadeOut(slide_3, shift=DOWN * 0.4),
            FadeOut(hl_5, shift=DOWN * 0.4),
            FadeOut(hl_6, shift=DOWN * 0.4),
            FadeOut(top_badge, shift=DOWN * 0.4),
            FadeOut(top_bar, shift=DOWN * 0.4),
            run_time=0.8
        )

        # ==========================================================
        # 4. Pantalla Final Limpia y Centrada (Avanza hacia abajo)
        # ==========================================================
        concl_title = Text("Resultado Final:", font_size=24, color=THEME["header_color"]).shift(UP * 0.8)
        concl_res = MathTex(
            r"\operatorname{Dom}(h) = \mathbb{R} \setminus \{-1\} = (-\infty, -1) \cup (-1, +\infty)",
            font_size=30,
            color=THEME["success"]
        ).next_to(concl_title, DOWN, buff=0.4)

        final_group = VGroup(concl_title, concl_res)
        self.play(FadeIn(final_group, shift=DOWN * 0.4), run_time=1.0)
        self.conclude_solution(concl_res, wait_time=4.0)
