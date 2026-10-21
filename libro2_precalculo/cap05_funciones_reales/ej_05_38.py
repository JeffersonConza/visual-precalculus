"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.38 (Página 110 del libro / Página 129 del PDF)

Inecuación racional con valores absolutos: (|2x-1| - |4x-3|) / p(x) < 0.
- Signo del numerador: |u| - |v| tiene el mismo signo que u² - v² = -4(3x - 2)(x - 1).
  Por tanto: (|2x-1| - |4x-3|) / p(x) < 0 ⟺ (3x - 2)(x - 1) / p(x) > 0.
1. p(x) = x² - x - 2 = (x - 2)(x + 1) ⟹ CS₁ = ]-∞, -1[ ∪ ]2/3, 1[ ∪ ]2, +∞[.
2. p(x) = x² - 2x - 3 = (x - 3)(x + 1) ⟹ CS₂ = ]-∞, -1[ ∪ ]2/3, 1[ ∪ ]3, +∞[.
3. p(x) = (x⁴ + 1)(x² - x - 2) ⟹ CS₃ = CS₁ = ]-∞, -1[ ∪ ]2/3, 1[ ∪ ]2, +∞[.
- Interpretación gráfica cartesiana: Curva f(x) para Caso 1, asíntotas en x = -1, 2, y regiones negativas.
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_38(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.38",
            topic="Inecuación con Valores Absolutos y Polinomios"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Resuelve la inecuación fraccionaria en ℝ para cada uno de los polinomios dados:",
            math_tex=r"\frac{|2x - 1| - |4x - 3|}{p(x)} < 0, \quad p_1(x) = x^2-x-2, \quad p_2(x) = x^2-2x-3, \quad p_3(x) = x^6-x^5-2x^4+x^2-x-2",
            desc_font_size=14,
            math_font_size=13,
            read_time=4.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Equivalencia de Signos",
            "2/6: Caso 1 (p₁ = x² - x - 2)",
            "3/6: Caso 2 (p₂ = x² - 2x - 3)",
            "4/6: Caso 3 (Factorización p₃)",
            "5/6: Caso 3 y Cuadro Resumen",
            "6/6: Gráfica Cartesiana de f(x)"
        ])

        # ==========================================================
        # PASO 1: Equivalencia de Signos del Numerador
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"\text{Propiedad: } &\operatorname{sgn}(|u| - |v|) = \operatorname{sgn}(u^2 - v^2) = \operatorname{sgn}((u - v)(u + v)) \\[6pt]"
            r"u - v &= (2x - 1) - (4x - 3) = -2(x - 1) \\[4pt]"
            r"u + v &= (2x - 1) + (4x - 3) = 2(3x - 2) \\[6pt]"
            r"\implies &|2x - 1| - |4x - 3| \sim -4(3x - 2)(x - 1) \\[6pt]"
            r"\therefore \quad &\frac{|2x - 1| - |4x - 3|}{p(x)} < 0 \iff \frac{(3x - 2)(x - 1)}{p(x)} > 0"
            r"\end{aligned}",
            font_size=19,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Equivalencia de signo del numerador:\n"
            "El signo de |u| - |v| coincide con el de u² - v².\n"
            "Calculamos: u - v = -2(x - 1) y u + v = 2(3x - 2).\n"
            "El numerador tiene el signo de -4(3x - 2)(x - 1).\n"
            "Al multiplicar por -1, la inecuación equivale a:\n"
            "(3x - 2)(x - 1) / p(x) > 0."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Caso 1: p₁(x) = x² - x - 2
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"\mathbf{Caso \; 1:} \quad &p_1(x) = x^2 - x - 2 = (x - 2)(x + 1) \\[6pt]"
            r"\frac{(3x - 2)(x - 1)}{(x + 1)(x - 2)} &> 0, \quad \text{Puntos críticos: } \{-1, \; 2/3, \; 1, \; 2\} \\[6pt]"
            r"\text{Signos: } &]-1, 2/3[\;(-) \quad ]2/3, 1[\;(+) \quad ]1, 2[\;(-) \quad ]2, +\infty[\;(+) \\[6pt]"
            r"\therefore \quad &CS_1 = \; ]-\infty, -1[ \;\cup\; ]2/3, 1[ \;\cup\; ]2, +\infty["
            r"\end{aligned}",
            font_size=19,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Caso 1 (p₁ = x² - x - 2):\n"
            "Factorizamos el denominador: (x - 2)(x + 1).\n"
            "Los 4 puntos críticos ordenados son: -1 < 2/3 < 1 < 2.\n"
            "Construyendo la tabla de signos de la fracción,\n"
            "los intervalos estrictamente positivos son:\n"
            "CS₁ = ]-∞, -1[ ∪ ]2/3, 1[ ∪ ]2, +∞[ (Nota 100)."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Caso 2: p₂(x) = x² - 2x - 3
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"\mathbf{Caso \; 2:} \quad &p_2(x) = x^2 - 2x - 3 = (x - 3)(x + 1) \\[6pt]"
            r"\frac{(3x - 2)(x - 1)}{(x + 1)(x - 3)} &> 0, \quad \text{Puntos críticos: } \{-1, \; 2/3, \; 1, \; 3\} \\[6pt]"
            r"\text{Signos: } &]-1, 2/3[\;(-) \quad ]2/3, 1[\;(+) \quad ]1, 3[\;(-) \quad ]3, +\infty[\;(+) \\[6pt]"
            r"\therefore \quad &CS_2 = \; ]-\infty, -1[ \;\cup\; ]2/3, 1[ \;\cup\; ]3, +\infty["
            r"\end{aligned}",
            font_size=19,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Caso 2 (p₂ = x² - 2x - 3):\n"
            "Factorizamos: p₂(x) = (x - 3)(x + 1).\n"
            "Los puntos críticos son: -1 < 2/3 < 1 < 3.\n"
            "El análisis de signos alternados arroja positivo en:\n"
            "]-∞, -1[, ]2/3, 1[ y ]3, +∞[.\n"
            "CS₂ = ]-∞, -1[ ∪ ]2/3, 1[ ∪ ]3, +∞[ (Nota 101)."
        )

        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Caso 3: Factorización de p₃(x)
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"\mathbf{Caso \; 3:} \quad &p_3(x) = x^6 - x^5 - 2x^4 + x^2 - x - 2 \\[6pt]"
            r"&= x^4(x^2 - x - 2) + 1(x^2 - x - 2) \\[6pt]"
            r"&= (x^4 + 1)(x^2 - x - 2) \\[6pt]"
            r"\text{Propiedad: } &\forall x \in \mathbb{R}, \quad x^4 + 1 \ge 1 > 0 \quad (\text{Estrictamente positivo})"
            r"\end{aligned}",
            font_size=19,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Caso 3 (Factorización por grupos):\n"
            "Agrupamos los términos de grado 6, 5, 4 y 2, 1, 0:\n"
            "p₃(x) = x⁴(x² - x - 2) + (x² - x - 2).\n"
            "Extraemos el factor común: (x⁴ + 1)(x² - x - 2).\n"
            "Al ser x⁴ + 1 ≥ 1 > 0 para todo x ∈ ℝ, este término\n"
            "no introduce raíces ni altera el signo del cociente."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=4.8)

        # ==========================================================
        # PASO 5: Caso 3 y Cuadro Resumen
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"\operatorname{sgn}(p_3(x)) &= \operatorname{sgn}(x^2 - x - 2) = \operatorname{sgn}(p_1(x)) \\[4pt]"
            r"\therefore \quad CS_3 &= CS_1 = \; ]-\infty, -1[ \;\cup\; ]2/3, 1[ \;\cup\; ]2, +\infty[ \\[8pt]"
            r"\text{\underline{Resumen de Conjuntos Solución:}} & \\[4pt]"
            r"CS_1 &= \; ]-\infty, -1[ \;\cup\; ]2/3, 1[ \;\cup\; ]2, +\infty[ \\[3pt]"
            r"CS_2 &= \; ]-\infty, -1[ \;\cup\; ]2/3, 1[ \;\cup\; ]3, +\infty[ \\[3pt]"
            r"CS_3 &= \; ]-\infty, -1[ \;\cup\; ]2/3, 1[ \;\cup\; ]2, +\infty["
            r"\end{aligned}",
            font_size=18,
            color=THEME["success"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Solución de Caso 3 y resumen:\n"
            "Dado que (x⁴ + 1) es estrictamente positivo,\n"
            "el signo de p₃(x) es idéntico al de p₁(x).\n"
            "Por ende, CS₃ coincide exactamente con CS₁.\n"
            "Consolidamos las tres soluciones del Ejercicio 5.38,\n"
            "concordantes al 100% con las notas del libro de texto."
        )

        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana (Caso 1)
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen geométrico
        t_title = Text("Geometría de f(x) (Caso 1):", font_size=15, color=THEME["header_color"], weight=BOLD)
        eq_f = MathTex(r"f(x) = \frac{|2x-1| - |4x-3|}{x^2 - x - 2}", font_size=14, color=THEME["highlight"])
        t_desc1 = Text("• Asíntotas verticales en x = -1 y x = 2.", font_size=12, color=THEME["statement_box"])
        t_desc2 = Text("• Ceros de la función: x = 2/3 y x = 1.", font_size=12, color=THEME["secondary"])
        t_desc3 = Text("• Regiones donde f(x) < 0 (curva bajo el eje):", font_size=12, color=THEME["success"], weight=BOLD)
        t_desc4 = Text("  ]-∞, -1[ ∪ ]2/3, 1[ ∪ ]2, +∞[ (tres zonas verdes).", font_size=12, color=THEME["success"])
        t_desc5 = Text("• Cero en x = 2/3 y x = 1 con cambio de signo.", font_size=12, color=THEME["curve"])

        info_content = VGroup(t_title, eq_f, t_desc1, t_desc2, t_desc3, t_desc4, t_desc5).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        info_box = SurroundingRectangle(info_content, color=THEME["statement_box"], buff=0.2, stroke_width=1.5, corner_radius=0.08)
        info_grp = VGroup(info_box, info_content).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos
        axes, axes_labels = self.setup_axes(
            x_range=[-2.5, 3.5, 1],
            y_range=[-3.0, 3.0, 1],
            x_length=5.6,
            y_length=3.8,
            center=[2.8, -0.45, 0],
            include_numbers=True
        )

        def f_eval(x):
            return (np.abs(2*x - 1) - np.abs(4*x - 3)) / (x**2 - x - 2)

        # Ramas de f(x)
        c_left = axes.plot(f_eval, x_range=[-2.3, -1.15], color=THEME["highlight"], stroke_width=2.5)
        c_mid = axes.plot(f_eval, x_range=[-0.85, 1.85], color=THEME["highlight"], stroke_width=2.5)
        c_right = axes.plot(f_eval, x_range=[2.15, 3.3], color=THEME["highlight"], stroke_width=2.5)

        # Asíntotas verticales x = -1 y x = 2
        asymp_1 = DashedLine(axes.c2p(-1.0, -2.8), axes.c2p(-1.0, 2.8), color=THEME["statement_box"], stroke_width=1.5)
        asymp_2 = DashedLine(axes.c2p(2.0, -2.8), axes.c2p(2.0, 2.8), color=THEME["statement_box"], stroke_width=1.5)

        # Ceros en x = 2/3 y x = 1
        p_c1 = axes.c2p(2/3, 0)
        p_c2 = axes.c2p(1.0, 0)
        dot_c1 = Dot(p_c1, radius=0.05, color=THEME["secondary"])
        dot_c2 = Dot(p_c2, radius=0.05, color=THEME["secondary"])

        # Intervalos solución sobre el eje X
        ray_l = Line(axes.c2p(-2.3, 0), axes.c2p(-1.0, 0), color=THEME["success"], stroke_width=4.5)
        seg_m = Line(axes.c2p(2/3, 0), axes.c2p(1.0, 0), color=THEME["success"], stroke_width=4.5)
        ray_r = Line(axes.c2p(2.0, 0), axes.c2p(3.3, 0), color=THEME["success"], stroke_width=4.5)

        dot_open_l = Dot(axes.c2p(-1.0, 0), radius=0.06, stroke_width=1.8, stroke_color=THEME["statement_box"], fill_color=THEME["bg_color"])
        dot_open_r = Dot(axes.c2p(2.0, 0), radius=0.06, stroke_width=1.8, stroke_color=THEME["statement_box"], fill_color=THEME["bg_color"])

        lbl_cs_txt = MathTex(r"CS_1 = ]-\infty, -1[ \cup ]2/3, 1[ \cup ]2, +\infty[", font_size=10, color=THEME["success"]).next_to(axes.c2p(0.5, 0), DOWN, buff=0.18)

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

        # Trazado de asíntotas y curvas
        self.play(
            Create(asymp_1), Create(asymp_2),
            Create(c_left), Create(c_mid), Create(c_right),
            run_time=2.2
        )

        # Marcado de ceros e intervalos solución
        self.play(
            FadeIn(dot_c1), FadeIn(dot_c2),
            Create(ray_l), Create(seg_m), Create(ray_r),
            FadeIn(dot_open_l), FadeIn(dot_open_r),
            Write(lbl_cs_txt),
            run_time=1.6
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            asymp_1, asymp_2,
            c_left, c_mid, c_right,
            dot_c1, dot_c2,
            ray_l, seg_m, ray_r,
            dot_open_l, dot_open_r,
            lbl_cs_txt
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
