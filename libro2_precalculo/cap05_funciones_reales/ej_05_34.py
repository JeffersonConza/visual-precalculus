"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.34 (Página 110 del libro / Página 129 del PDF)

Ecuación con radicales de distinto orden (Método del Ejemplo 5.56):
- Enunciado: Resuelve la ecuación en ℝ:
  ⁵√(x² - 34x + 64) - ⁴√(x² - 34x + 33) = 1.
  Indicación: √257 ≈ 16.03.
- Paso 1: Cambio de variable: w = x² - 34x; u = ⁵√(w + 64), v = ⁴√(w + 33) ≥ 0 ⟹ u - v = 1.
- Paso 2: Eliminación de w: u⁵ - v⁴ = 31 ⟹ (v + 1)⁵ - v⁴ = 31.
- Paso 3: Expansión binomial: v⁵ + 4v⁴ + 10v³ + 10v² + 5v - 30 = 0.
- Paso 4: Raíz única: (v - 1)(v⁴ + 5v³ + 15v² + 25v + 30) = 0 ⟹ v = 1 (única en v ≥ 0).
- Paso 5: Restitución: w = -32 ⟹ x² - 34x + 32 = 0 ⟹ (x - 17)² = 257 ⟹ CS = {17 - √257, 17 + √257}.
- Paso 6: Interpretación gráfica cartesiana: Curva f(x) simétrica respecto a x = 17, recta y = 1,
  brecha en ]1, 33[ y cortes en x₁ ≈ 0.97 y x₂ ≈ 33.03.
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_34(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.34",
            topic="Ecuación con Radicales de Distinto Orden"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Resuelve la ecuación con radicales en ℝ aplicando el método del Ejemplo 5.56:",
            math_tex=r"\sqrt[5]{x^2 - 34x + 64} - \sqrt[4]{x^2 - 34x + 33} = 1, \quad x \in \mathbb{R}",
            desc_font_size=14,
            math_font_size=15,
            read_time=4.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Cambio de Variables (w, u, v)",
            "2/6: Eliminación de w",
            "3/6: Expansión Binomial",
            "4/6: Factorización y Solución de v",
            "5/6: Restitución Cuadrática (CS)",
            "6/6: Gráfica Cartesiana y Simetría"
        ])

        # ==========================================================
        # PASO 1: Cambio de Variables
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"\text{Núcleo cuadrático común: } &w = x^2 - 34x \\[6pt]"
            r"\text{Definimos: } &u = \sqrt[5]{w + 64} \in \mathbb{R}, \quad v = \sqrt[4]{w + 33} \ge 0 \\[6pt]"
            r"\text{La ecuación se reduce a: } &u - v = 1 \implies u = v + 1"
            r"\end{aligned}",
            font_size=20,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Cambio de variables estructural:\n"
            "Observamos que ambos radicandos comparten el\n"
            "bloque cuadrático w = x² - 34x.\n"
            "Definimos u como la raíz quinta y v como la raíz cuarta.\n"
            "La ecuación se convierte en la relación lineal:\n"
            "u - v = 1 ⟹ u = v + 1."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Eliminación de la Variable Intermedia w
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"u^5 &= w + 64 \quad \text{y} \quad v^4 = w + 33 \\[6pt]"
            r"u^5 - v^4 &= (w + 64) - (w + 33) = 31 \\[6pt]"
            r"\text{Sustituyendo } &u = v + 1: \\[4pt]"
            r"(v + 1)^5 - v^4 &= 31"
            r"\end{aligned}",
            font_size=21,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Eliminación de w:\n"
            "Elevamos a las respectivas potencias 5 y 4:\n"
            "u⁵ = w + 64  y  v⁴ = w + 33.\n"
            "Restando ambas ecuaciones cancelamos w:\n"
            "u⁵ - v⁴ = 31.\n"
            "Sustituyendo u = v + 1 obtenemos una sola variable: (v+1)⁵ - v⁴ = 31."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Expansión Binomial
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"(v + 1)^5 &= v^5 + 5v^4 + 10v^3 + 10v^2 + 5v + 1 \\[6pt]"
            r"(v + 1)^5 - v^4 &= v^5 + 4v^4 + 10v^3 + 10v^2 + 5v + 1 = 31 \\[6pt]"
            r"\implies v^5 + 4v^4 &+ 10v^3 + 10v^2 + 5v - 30 = 0"
            r"\end{aligned}",
            font_size=19,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Expansión binomial:\n"
            "Desarrollamos el binomio a la quinta con el triángulo\n"
            "de Pascal: coeficientes 1, 5, 10, 10, 5, 1.\n"
            "Restamos v⁴ y transponemos la constante 31:\n"
            "v⁵ + 4v⁴ + 10v³ + 10v² + 5v - 30 = 0."
        )

        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Factorización y Solución Única en v ≥ 0
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"\text{Evaluando en } v = 1: \quad &1 + 4 + 10 + 10 + 5 - 30 = 0 \implies v = 1 \\[6pt]"
            r"\text{Factorización: } &(v - 1)(v^4 + 5v^3 + 15v^2 + 25v + 30) = 0 \\[6pt]"
            r"\forall v \ge 0: \quad &v^4 + 5v^3 + 15v^2 + 25v + 30 \ge 30 > 0 \\[6pt]"
            r"\therefore \quad &v = 1 \implies u = 2"
            r"\end{aligned}",
            font_size=19,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Raíz y unicidad de v:\n"
            "Observamos que v = 1 anula el polinomio.\n"
            "Por división sintética factorizamos el binomio (v - 1).\n"
            "Dado que v = ⁴√(w+33) ≥ 0 por definición de raíz par,\n"
            "el factor de cuarto grado es estrictamente positivo (≥ 30).\n"
            "Por ende, v = 1 es la única raíz admisible."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=5.0)

        # ==========================================================
        # PASO 5: Restitución a x y Conjunto Solución
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"v = 1 \implies &w + 33 = 1^4 = 1 \implies w = -32 \\[6pt]"
            r"x^2 - 34x &= -32 \iff (x - 17)^2 - 289 + 32 = 0 \\[6pt]"
            r"(x - 17)^2 &= 257 \implies x = 17 \pm \sqrt{257} \\[6pt]"
            r"\therefore \quad CS &= \{17 - \sqrt{257}, \; 17 + \sqrt{257}\} \quad \blacksquare"
            r"\end{aligned}",
            font_size=20,
            color=THEME["success"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Restitución cuadrática:\n"
            "Con v = 1 tenemos w = -32.\n"
            "Reemplazamos w = x² - 34x y completamos el cuadrado:\n"
            "(x - 17)² = 289 - 32 = 257.\n"
            "Despejamos: x = 17 ± √257.\n"
            "Como 17 - √257 ≈ 0.97 y 17 + √257 ≈ 33.03 verifican\n"
            "el dominio x²-34x+33 ≥ 0, CS = {17 - √257, 17 + √257}."
        )

        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen geométrico
        t_title = Text("Geometría de la Ecuación:", font_size=15, color=THEME["header_color"], weight=BOLD)
        eq_curva = MathTex(r"f(x) = \sqrt[5]{x^2-34x+64} - \sqrt[4]{x^2-34x+33}", font_size=12, color=THEME["highlight"])
        t_desc1 = Text("• Simetría axial perfecta respecto a x = 17.", font_size=12, color=THEME["statement_text"])
        t_desc2 = Text("• Radicando cuarto negativo en ]1, 33[ (brecha en ℝ).", font_size=12, color=THEME["statement_box"])
        t_desc3 = Text("• Dos intersecciones exactas con la recta y = 1:", font_size=12, color=THEME["success"], weight=BOLD)
        t_desc4 = Text("  P₁(17 - √257, 1) ≈ (0.97, 1).", font_size=12, color=THEME["secondary"])
        t_desc5 = Text("  P₂(17 + √257, 1) ≈ (33.03, 1).", font_size=12, color=THEME["secondary"])
        t_desc6 = Text("• Nota 98 del texto confirmada al 100%.", font_size=12, color=THEME["success"])

        info_content = VGroup(t_title, eq_curva, t_desc1, t_desc2, t_desc3, t_desc4, t_desc5, t_desc6).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        info_box = SurroundingRectangle(info_content, color=THEME["statement_box"], buff=0.2, stroke_width=1.5, corner_radius=0.08)
        info_grp = VGroup(info_box, info_content).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos
        axes, axes_labels = self.setup_axes(
            x_range=[-4.0, 38.0, 6],
            y_range=[-1.0, 3.5, 1],
            x_length=5.6,
            y_length=3.8,
            center=[2.8, -0.45, 0],
            include_numbers=True
        )

        def f_eval(x):
            w = x**2 - 34*x
            r5 = np.sign(w + 64) * (np.abs(w + 64))**(1/5)
            r4 = (w + 33)**(1/4)
            return r5 - r4

        # Curva f(x) a la izquierda de x = 1 (x in [-3.5, 0.99])
        curve_left = axes.plot(f_eval, x_range=[-3.0, 0.98], color=THEME["highlight"], stroke_width=2.8)
        # Curva f(x) a la derecha de x = 33 (x in [33.01, 37.0])
        curve_right = axes.plot(f_eval, x_range=[33.02, 37.0], color=THEME["highlight"], stroke_width=2.8)

        lbl_f = MathTex(r"f(x)", font_size=13, color=THEME["highlight"]).next_to(axes.c2p(-1.5, f_eval(-1.5)), UR, buff=0.08)

        # Recta horizontal y = 1
        line_one = axes.plot(lambda x: 1.0, x_range=[-3.0, 37.0], color=THEME["secondary"], stroke_width=1.8)
        lbl_one = MathTex(r"y = 1", font_size=13, color=THEME["secondary"]).next_to(axes.c2p(36.0, 1.0), UP, buff=0.08)

        # Eje de simetría x = 17
        symm_axis = DashedLine(axes.c2p(17.0, -0.8), axes.c2p(17.0, 3.2), color=THEME["statement_text"], stroke_width=1.2)
        lbl_symm = MathTex(r"x = 17", font_size=11, color=THEME["statement_text"]).next_to(axes.c2p(17.0, 3.2), UP, buff=0.06)

        # Puntos de intersección
        x1_val = 17.0 - np.sqrt(257)
        x2_val = 17.0 + np.sqrt(257)
        p1 = axes.c2p(x1_val, 1.0)
        p2 = axes.c2p(x2_val, 1.0)

        dot1 = Dot(p1, radius=0.06, color=THEME["success"])
        dot2 = Dot(p2, radius=0.06, color=THEME["success"])

        lbl_p1 = MathTex(r"P_1", font_size=11, color=THEME["success"]).next_to(p1, UP, buff=0.08)
        lbl_p2 = MathTex(r"P_2", font_size=11, color=THEME["success"]).next_to(p2, UP, buff=0.08)

        # Guías al eje X
        g1 = DashedLine(p1, axes.c2p(x1_val, 0), color=THEME["statement_box"], stroke_width=1.3)
        g2 = DashedLine(p2, axes.c2p(x2_val, 0), color=THEME["statement_box"], stroke_width=1.3)

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

        # Trazado de las curvas, recta y eje de simetría
        self.play(
            Create(curve_left), Create(curve_right), Write(lbl_f),
            Create(line_one), Write(lbl_one),
            Create(symm_axis), Write(lbl_symm),
            run_time=2.2
        )

        # Marcado de intersecciones simétricas
        self.play(
            FadeIn(dot1), Write(lbl_p1), Create(g1),
            FadeIn(dot2), Write(lbl_p2), Create(g2),
            run_time=1.6
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_left, curve_right, lbl_f,
            line_one, lbl_one,
            symm_axis, lbl_symm,
            dot1, dot2, lbl_p1, lbl_p2,
            g1, g2
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
