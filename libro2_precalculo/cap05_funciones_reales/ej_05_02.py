"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
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
        # ==========================================================
        # ACTO 1: Encabezado y Enunciado
        # ==========================================================
        header = self.show_header(
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
        
        # Presentar y minimizar
        stmt_card = self.present_statement(enunciado_grp, read_time=4.5)

        # ==========================================================
        # ACTO 2: Condiciones de la Regla del Máximo Dominio (RMD)
        # ==========================================================
        paso1_title = Text("Paso 1: Restricciones de existencia en ℝ", font_size=21, color=THEME["header_color"])
        paso1_title.to_edge(LEFT, buff=1.0).shift(UP * 1.5)
        self.play(FadeIn(paso1_title, shift=RIGHT * 0.2), run_time=0.7)

        c1_desc = Text("1) Denominador no nulo:", font_size=18, color=THEME["statement_text"])
        c1_math = MathTex(r"x + 1 \neq 0 \iff x \neq -1", font_size=22, color=THEME["secondary"])
        c1_grp = VGroup(c1_desc, c1_math).arrange(RIGHT, buff=0.3)

        c2_desc = Text("2) Argumento del logaritmo estrictamente positivo:", font_size=18, color=THEME["statement_text"])
        c2_math = MathTex(r"\frac{x^3 + 1}{x + 1} > 0", font_size=24, color=THEME["highlight"])
        c2_grp = VGroup(c2_desc, c2_math).arrange(RIGHT, buff=0.3)

        conds_grp = VGroup(c1_grp, c2_grp).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        conds_grp.next_to(paso1_title, DOWN, buff=0.3, aligned_edge=LEFT)

        self.play(FadeIn(c1_grp, shift=UP * 0.1), run_time=0.9)
        self.wait(1.2)
        self.play(FadeIn(c2_grp, shift=UP * 0.1), run_time=0.9)
        self.wait(2.2)

        # Limpiar Paso 1 para dar espacio al desarrollo algebraico
        self.play(FadeOut(paso1_title), FadeOut(conds_grp), run_time=0.6)

        # ==========================================================
        # ACTO 3: Desarrollo Algebraico Intermedio Detallado
        # ==========================================================
        paso2_title = Text("Paso 2: Factorización y Simplificación del Argumento", font_size=21, color=THEME["header_color"])
        paso2_title.to_edge(LEFT, buff=1.0).shift(UP * 1.5)
        self.play(FadeIn(paso2_title, shift=RIGHT * 0.2), run_time=0.7)

        # Recordar identidad notable
        ident_text = Text("Aplicamos la identidad de suma de cubos  a³ + b³ = (a + b)(a² - ab + b²):", font_size=17, color=THEME["statement_text"])
        ident_text.next_to(paso2_title, DOWN, buff=0.25, aligned_edge=LEFT)

        cubo_math = MathTex(
            r"x^3 + 1 = x^3 + 1^3 = (x + 1)(x^2 - x + 1)",
            font_size=23,
            color=THEME["highlight"]
        ).next_to(ident_text, DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(FadeIn(ident_text), Write(cubo_math), run_time=1.3)
        self.wait(2.0)

        # Fracción factorizada
        frac_text = Text("Sustituyendo en el cociente para  x ≠ -1:", font_size=17, color=THEME["statement_text"])
        frac_text.next_to(cubo_math, DOWN, buff=0.3, aligned_edge=LEFT)

        frac_math = MathTex(
            r"\frac{x^3 + 1}{x + 1} = \frac{(x + 1)(x^2 - x + 1)}{x + 1}",
            font_size=24,
            color=WHITE
        ).next_to(frac_text, DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(FadeIn(frac_text), Write(frac_math), run_time=1.2)
        self.wait(1.5)

        # Simplificación directa
        simpl_math = MathTex(
            r"= x^2 - x + 1 \quad (\text{para todo } x \neq -1)",
            font_size=24,
            color=THEME["secondary"]
        ).next_to(frac_math, DOWN, buff=0.25, aligned_edge=LEFT)

        self.play(Write(simpl_math), run_time=1.0)
        self.wait(2.5)

        # Limpiar Paso 2
        self.play(
            FadeOut(paso2_title),
            FadeOut(ident_text),
            FadeOut(cubo_math),
            FadeOut(frac_text),
            FadeOut(frac_math),
            FadeOut(simpl_math),
            run_time=0.6
        )

        # ==========================================================
        # ACTO 4: Análisis del Trinomio (Completando Cuadrados)
        # ==========================================================
        paso3_title = Text("Paso 3: Análisis de Signo del Trinomio  x² - x + 1", font_size=21, color=THEME["header_color"])
        paso3_title.to_edge(LEFT, buff=1.0).shift(UP * 1.5)
        self.play(FadeIn(paso3_title, shift=RIGHT * 0.2), run_time=0.7)

        trin_intro = Text("Completamos el trinomio cuadrado perfecto:", font_size=18, color=THEME["statement_text"])
        trin_intro.next_to(paso3_title, DOWN, buff=0.25, aligned_edge=LEFT)

        paso_cuad1 = MathTex(
            r"x^2 - x + 1 = \left(x^2 - 2 \cdot \frac{1}{2}x + \frac{1}{4}\right) + \left(1 - \frac{1}{4}\right)",
            font_size=23,
            color=WHITE
        ).next_to(trin_intro, DOWN, buff=0.25, aligned_edge=LEFT)

        paso_cuad2 = MathTex(
            r"= \left(x - \frac{1}{2}\right)^2 + \frac{3}{4}",
            font_size=24,
            color=THEME["highlight"]
        ).next_to(paso_cuad1, DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(FadeIn(trin_intro), Write(paso_cuad1), run_time=1.4)
        self.wait(1.5)
        self.play(Write(paso_cuad2), run_time=1.1)
        self.wait(1.8)

        # Justificación de positividad
        just_1 = MathTex(r"\text{Como } \left(x - \frac{1}{2}\right)^2 \ge 0 \quad \text{y} \quad \frac{3}{4} > 0:", font_size=20, color=WHITE)
        just_1.next_to(paso_cuad2, DOWN, buff=0.3, aligned_edge=LEFT)

        just_2 = MathTex(
            r"\implies x^2 - x + 1 \ge \frac{3}{4} > 0 \quad (\forall x \in \mathbb{R})",
            font_size=23,
            color=THEME["curve"]
        ).next_to(just_1, DOWN, buff=0.2, aligned_edge=LEFT)

        concl_box = Text("¡El argumento siempre es estrictamente positivo! La única exclusión es x = -1.", font_size=17, color=THEME["statement_text"])
        concl_box.next_to(just_2, DOWN, buff=0.3, aligned_edge=LEFT)

        self.play(Write(just_1), run_time=1.0)
        self.play(Write(just_2), run_time=1.0)
        self.play(FadeIn(concl_box), run_time=0.8)
        self.wait(3.0)

        # Limpiar Paso 3
        self.play(
            FadeOut(paso3_title),
            FadeOut(trin_intro),
            FadeOut(paso_cuad1),
            FadeOut(paso_cuad2),
            FadeOut(just_1),
            FadeOut(just_2),
            FadeOut(concl_box),
            run_time=0.6
        )

        # ==========================================================
        # ACTO 5: Representación en la Recta Numérica Real (ℝ)
        # ==========================================================
        paso4_title = Text("Paso 4: Representación Geométrica en la Recta Real", font_size=21, color=THEME["header_color"])
        paso4_title.to_edge(LEFT, buff=1.0).shift(UP * 1.5)
        self.play(FadeIn(paso4_title, shift=RIGHT * 0.2), run_time=0.7)

        # Eje de números reales
        linea_real = NumberLine(
            x_range=[-4, 3, 1],
            length=8.5,
            color=THEME["axes"],
            include_numbers=True,
            font_size=18
        ).shift(UP * 0.1)

        self.play(Create(linea_real), run_time=1.2)

        # Rayos coloreados (intervalos válidos)
        # De -4 a -1
        izq_ray = Line(
            start=linea_real.n2p(-4),
            end=linea_real.n2p(-1),
            color=THEME["curve"],
            stroke_width=6
        )
        # De -1 a 3
        der_ray = Line(
            start=linea_real.n2p(-1),
            end=linea_real.n2p(3),
            color=THEME["curve"],
            stroke_width=6
        )

        # Punto abierto en -1
        punto_abierto = Dot(
            point=linea_real.n2p(-1),
            radius=0.12,
            color=THEME["poncho_red"],
            fill_opacity=0,
            stroke_width=3
        )
        punto_label = Text("x = -1 (excluido)", font_size=16, color=THEME["poncho_red"]).next_to(punto_abierto, UP, buff=0.35)

        self.play(Create(izq_ray), Create(der_ray), run_time=1.0)
        self.play(Create(punto_abierto), FadeIn(punto_label, shift=DOWN * 0.1), run_time=0.9)
        self.wait(2.5)

        # Limpiar para la respuesta final
        self.play(
            FadeOut(paso4_title),
            FadeOut(linea_real),
            FadeOut(izq_ray),
            FadeOut(der_ray),
            FadeOut(punto_abierto),
            FadeOut(punto_label),
            run_time=0.6
        )

        # ==========================================================
        # ACTO 6: Solución y Definición Formal de la Función
        # ==========================================================
        concl_header = Text("Conjunto Dominio de Definición:", font_size=23, color=THEME["header_color"]).shift(UP * 1.0)

        dom_math = MathTex(
            r"\operatorname{Dom}(h) = \mathbb{R} \setminus \{-1\} = (-\infty, -1) \cup (-1, +\infty)",
            font_size=29,
            color=THEME["highlight"]
        ).next_to(concl_header, DOWN, buff=0.35)

        func_def = MathTex(
            r"h: \mathbb{R} \setminus \{-1\} \longrightarrow \mathbb{R}, \quad x \longmapsto \ln(x^2 - x + 1)",
            font_size=26,
            color=THEME["success"]
        ).next_to(dom_math, DOWN, buff=0.45)

        self.play(FadeIn(concl_header), Write(dom_math), run_time=1.2)
        self.wait(1.5)
        self.play(Write(func_def), run_time=1.2)

        # Destacar la conclusión final con recuadro verde andino y pausar
        resp_box = VGroup(dom_math, func_def)
        self.conclude_solution(resp_box, wait_time=4.5)
