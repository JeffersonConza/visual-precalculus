"""
Precálculo 2 · Colección Yachay Tech / Amarun
Capítulo 5: Funciones reales
Sección 5.1.4: Regla del Máximo Dominio (RMD)
Ejercicio 5.2 (Página 27 del libro / Página 46 del PDF)

Enunciado:
Encuentre la función (dominio de definición) determinada por la fórmula:
    h(x) = ln((x^3 + 1) / (x + 1))
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
        # 1. Encabezado
        self.show_header(
            chapter="5",
            exercise_num=2,
            topic="Regla del Máximo Dominio (RMD)"
        )

        # 2. Enunciado
        enunciado_line1 = Text("Encontrar el dominio de definición de:", font_size=24, color=THEME["statement_text"])
        enunciado_math = MathTex(r"h(x) = \ln\left(\frac{x^3 + 1}{x + 1}\right)", font_size=34, color=THEME["highlight"])
        enunciado_grp = VGroup(enunciado_line1, enunciado_math).arrange(DOWN, buff=0.25)
        
        self.present_statement(enunciado_grp, read_time=5.0)

        # 3. Condiciones de RMD
        cond_title = Text("Condiciones para que h(x) exista en ℝ:", font_size=20, color=THEME["header_color"]).to_edge(LEFT, buff=1.0).shift(UP * 1.5)
        self.play(FadeIn(cond_title), run_time=0.8)

        cond1 = MathTex(r"\text{1) Denominador no nulo: } x + 1 \neq 0 \implies x \neq -1", font_size=24, color=WHITE)
        cond2 = MathTex(r"\text{2) Argumento del logaritmo: } \frac{x^3 + 1}{x + 1} > 0", font_size=24, color=WHITE)
        conds = VGroup(cond1, cond2).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(cond_title, DOWN, buff=0.3, aligned_edge=LEFT)

        self.play(Write(cond1), run_time=1.2)
        self.wait(1.5)
        self.play(Write(cond2), run_time=1.2)
        self.wait(2.0)

        # 4. Simplificación algebraica
        factor_text = Text("Factorizamos la suma de cubos en el numerador:", font_size=20, color=THEME["statement_text"]).next_to(conds, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(FadeIn(factor_text), run_time=0.8)

        factor_math = MathTex(
            r"x^3 + 1 = (x + 1)(x^2 - x + 1)",
            font_size=26,
            color=THEME["highlight"]
        ).next_to(factor_text, DOWN, buff=0.25, aligned_edge=LEFT)
        self.play(Write(factor_math), run_time=1.2)
        self.wait(2.0)

        cociente_math = MathTex(
            r"\text{Para } x \neq -1: \quad \frac{x^3 + 1}{x + 1} = \frac{(x+1)(x^2 - x + 1)}{x+1} = x^2 - x + 1",
            font_size=24,
            color=WHITE
        ).next_to(factor_math, DOWN, buff=0.25, aligned_edge=LEFT)
        self.play(Write(cociente_math), run_time=1.5)
        self.wait(2.5)

        # 5. Análisis del trinomio cuadrático
        cuadrado_math = MathTex(
            r"x^2 - x + 1 = \left(x - \frac{1}{2}\right)^2 + \frac{3}{4} > 0 \quad (\forall x \in \mathbb{R})",
            font_size=25,
            color=THEME["secondary"]
        ).next_to(cociente_math, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(cuadrado_math), run_time=1.5)
        self.wait(2.5)

        concl_text = Text("El argumento siempre es positivo. La única restricción es x ≠ -1.", font_size=19, color=THEME["statement_text"]).next_to(cuadrado_math, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(FadeIn(concl_text), run_time=0.8)
        self.wait(2.0)

        # 6. Limpieza para mostrar la solución final en grande
        self.play(
            FadeOut(cond_title),
            FadeOut(conds),
            FadeOut(factor_text),
            FadeOut(factor_math),
            FadeOut(cociente_math),
            FadeOut(cuadrado_math),
            FadeOut(concl_text),
            run_time=0.8
        )

        # 7. Respuesta final
        resp_title = Text("Conjunto Dominio de Definición:", font_size=24, color=THEME["header_color"]).shift(UP * 0.8)
        resp_math = MathTex(
            r"\operatorname{Dom}(h) = \mathbb{R} \setminus \{-1\} = (-\infty, -1) \cup (-1, +\infty)",
            font_size=32,
            color=THEME["success"]
        ).next_to(resp_title, DOWN, buff=0.4)

        self.play(FadeIn(resp_title), Write(resp_math), run_time=1.2)
        self.conclude_solution(resp_math, wait_time=4.5)
