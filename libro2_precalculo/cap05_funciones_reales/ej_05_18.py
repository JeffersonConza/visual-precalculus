"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.8: Algunas funciones importantes (Exponenciales y Logarítmicas)
Ejercicio 5.18 (Página 85 del libro / Página 104 del PDF)

Demostración del Teorema 5.22 (Operando con logaritmos):
- Punto 1: Recursos fundamentales (biyectividad/inyectividad de exp_a e inversa log_a).
- Punto 2: Demostración de log_a(x · y) = log_a(x) + log_a(y).
- Punto 3: Demostración de log_a(xʸ) = y · log_a(x).
- Inyectividad de exp_a: exp_a(u) = exp_a(v) ⟹ u = v.
- Interpretación gráfica cartesiana: simetría respecto a la identidad y = x entre 2ˣ y log₂(x).
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_18(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.18",
            topic="Propiedades de Logaritmos (Teorema 5.22)"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Teorema 5.22: Sea a ∈ ]0, +∞[ \\ {1}. Probar las propiedades logarítmicas:",
            math_tex=r"\log_a(x \cdot y) = \log_a(x) + \log_a(y) \quad \text{y} \quad \log_a(x^y) = y \cdot \log_a(x)",
            desc_font_size=15,
            math_font_size=15,
            read_time=4.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Recursos Fundamentales",
            "2/6: Logaritmo de un Producto (I)",
            "3/6: Logaritmo de un Producto (II)",
            "4/6: Logaritmo de una Potencia (I)",
            "5/6: Logaritmo de una Potencia (II)",
            "6/6: Gráfica y Simetría Inversa"
        ])

        # ==========================================================
        # PASO 1: Recursos Fundamentales (Punto 1)
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"\exp_a : \mathbb{R} &\to ]0, +\infty[, \quad \exp_a(t) = a^t \quad (\text{Inyectiva}) \\[4pt]"
            r"\log_a : \; ]0, +\infty[ &\to \mathbb{R} \quad (\text{Función inversa}) \\[4pt]"
            r"\forall u > 0 &: \exp_a(\log_a(u)) = a^{\log_a(u)} = u \\[4pt]"
            r"a^{u+v} &= a^u \cdot a^v, \quad (a^u)^v = a^{uv}"
            r"\end{aligned}",
            font_size=20,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Recursos teóricos (Punto 1):\n"
            "La función exponencial exp_a es inyectiva:\n"
            "exp_a(u) = exp_a(v) ⟹ u = v.\n"
            "La función logaritmo log_a es su inversa:\n"
            "a^(log_a(u)) = u para todo u > 0.\n"
            "Se aplican las leyes de exponentes en ℝ."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Logaritmo de un Producto (Evaluación)
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"\text{Sean } &x, y \in ]0, +\infty[: \\[6pt]"
            r"\text{Lado Izq: } &\exp_a(\log_a(x \cdot y)) = x \cdot y \\[6pt]"
            r"\text{Lado Der: } &\exp_a(\log_a(x) + \log_a(y)) = a^{\log_a(x) + \log_a(y)} \\[4pt]"
            r"&= a^{\log_a(x)} \cdot a^{\log_a(y)} = x \cdot y"
            r"\end{aligned}",
            font_size=21,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Producto - Paso I (Punto 2):\n"
            "Tomamos x, y > 0 genéricos.\n"
            "Aplicamos exp_a a ambos miembros:\n"
            "• A la izquierda: exp_a(log_a(x·y)) = x·y.\n"
            "• A la derecha: convertimos la suma en\n"
            "  producto de potencias: a^(log x) · a^(log y) = x·y."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Logaritmo de un Producto (Inyectividad)
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"\exp_a(\log_a(x \cdot y)) &= \exp_a(\log_a(x) + \log_a(y)) \\[8pt]"
            r"\text{Por la } &\text{inyectividad de } \exp_a : \\[6pt]"
            r"\therefore \quad \log_a(x \cdot y) &= \log_a(x) + \log_a(y) \quad \blacksquare"
            r"\end{aligned}",
            font_size=22,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Producto - Paso II (Conclusión):\n"
            "Ambas expresiones tienen la misma imagen:\n"
            "exp_a(log_a(x·y)) = exp_a(log_a(x) + log_a(y)).\n"
            "Puesto que exp_a es inyectiva en ℝ,\n"
            "sus argumentos deben ser idénticos.\n"
            "Queda demostrado: log_a(x·y) = log_a(x) + log_a(y)."
        )

        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=5.0)

        # ==========================================================
        # PASO 4: Logaritmo de una Potencia (Evaluación)
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"\text{Sean } x &\in ]0, +\infty[, \quad y \in \mathbb{R}: \\[6pt]"
            r"\text{Lado Izq: } &\exp_a(\log_a(x^y)) = x^y \\[6pt]"
            r"\text{Lado Der: } &\exp_a(y \cdot \log_a(x)) = a^{y \cdot \log_a(x)} \\[4pt]"
            r"&= \left(a^{\log_a(x)}\right)^y = (x)^y = x^y"
            r"\end{aligned}",
            font_size=21,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Potencia - Paso I (Punto 3):\n"
            "Sean x > 0 y el exponente y ∈ ℝ.\n"
            "Evaluamos la exponencial en ambos miembros:\n"
            "• exp_a(log_a(xʸ)) = xʸ (por función inversa).\n"
            "• exp_a(y · log_a(x)) = a^(y · log_a(x)) = (a^(log_a x))ʸ.\n"
            "Como a^(log_a(x)) = x, el resultado es xʸ."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=4.8)

        # ==========================================================
        # PASO 5: Logaritmo de una Potencia (Inyectividad)
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"\exp_a(\log_a(x^y)) &= \exp_a(y \cdot \log_a(x)) \\[8pt]"
            r"\text{Por la } &\text{inyectividad de } \exp_a : \\[6pt]"
            r"\therefore \quad \log_a(x^y) &= y \cdot \log_a(x) \quad \blacksquare"
            r"\end{aligned}",
            font_size=22,
            color=THEME["success"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Potencia - Paso II (Conclusión):\n"
            "Ambas evaluaciones exponenciales coinciden:\n"
            "exp_a(log_a(xʸ)) = exp_a(y · log_a(x)).\n"
            "Nuevamente, por la inyectividad de exp_a,\n"
            "concluimos que los argumentos son iguales:\n"
            "log_a(xʸ) = y · log_a(x) para todo y ∈ ℝ."
        )

        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana y Simetría Inversa
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen conceptual
        t_title = Text("Dualidad Exponencial - Logarítmica:", font_size=15, color=THEME["header_color"], weight=BOLD)
        eq_base = MathTex(r"a = 2: \quad f(x) = 2^x \iff f^{-1}(x) = \log_2(x)", font_size=15, color=THEME["highlight"])
        t_desc1 = Text("• Simetría especular respecto a la recta y = x.", font_size=12, color=THEME["statement_text"])
        t_desc2 = Text("• exp₂(0) = 1  ⟺  log₂(1) = 0.", font_size=12, color=THEME["secondary"])
        t_desc3 = Text("• exp₂(2) = 4  ⟺  log₂(4) = 2.", font_size=12, color=THEME["curve"])
        t_desc4 = Text("• Isomorfismo fundamental:", font_size=12, color=THEME["success"], weight=BOLD)
        t_desc5 = Text("  Convierte productos en sumas y potencias", font_size=12, color=THEME["success"])
        t_desc6 = Text("  en productos (propiedad de escala).", font_size=12, color=THEME["success"])

        info_content = VGroup(t_title, eq_base, t_desc1, t_desc2, t_desc3, t_desc4, t_desc5, t_desc6).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        info_box = SurroundingRectangle(info_content, color=THEME["statement_box"], buff=0.2, stroke_width=1.5, corner_radius=0.08)
        info_grp = VGroup(info_box, info_content).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos
        axes, axes_labels = self.setup_axes(
            x_range=[-2.2, 4.4, 1],
            y_range=[-2.2, 4.4, 1],
            x_length=5.6,
            y_length=3.8,
            center=[2.8, -0.45, 0],
            include_numbers=True
        )

        # Recta identidad y = x
        diag_line = axes.plot(lambda x: x, x_range=[-1.8, 4.0], color=THEME["statement_text"], stroke_width=1.5)
        lbl_diag = MathTex(r"y = x", font_size=13, color=THEME["statement_text"]).next_to(axes.c2p(3.8, 3.8), DR, buff=0.08)

        # Curva exponencial f(x) = 2^x
        curve_exp = axes.plot(lambda x: 2**x, x_range=[-2.0, 2.05], color=THEME["highlight"], stroke_width=3.0)
        lbl_exp = MathTex(r"2^x", font_size=14, color=THEME["highlight"]).next_to(axes.c2p(1.9, 3.8), LEFT, buff=0.08)

        # Curva logarítmica g(x) = log₂(x)
        curve_log = axes.plot(lambda x: np.log2(x), x_range=[0.24, 4.2], color=THEME["curve"], stroke_width=3.0)
        lbl_log = MathTex(r"\log_2(x)", font_size=14, color=THEME["curve"]).next_to(axes.c2p(4.0, 2.0), UR, buff=0.08)

        # Puntos simétricos (0, 1) y (1, 0)
        p_exp_0 = axes.c2p(0.0, 1.0)
        p_log_0 = axes.c2p(1.0, 0.0)
        dot_exp_0 = Dot(p_exp_0, radius=0.06, color=THEME["highlight"])
        dot_log_0 = Dot(p_log_0, radius=0.06, color=THEME["curve"])
        lbl_exp_0 = MathTex(r"(0, 1)", font_size=11, color=THEME["highlight"]).next_to(p_exp_0, LEFT, buff=0.08)
        lbl_log_0 = MathTex(r"(1, 0)", font_size=11, color=THEME["curve"]).next_to(p_log_0, DOWN, buff=0.08)

        # Puntos simétricos (2, 4) y (4, 2)
        p_exp_2 = axes.c2p(2.0, 4.0)
        p_log_4 = axes.c2p(4.0, 2.0)
        dot_exp_2 = Dot(p_exp_2, radius=0.06, color=THEME["highlight"])
        dot_log_4 = Dot(p_log_4, radius=0.06, color=THEME["curve"])
        lbl_exp_2 = MathTex(r"(2, 4)", font_size=11, color=THEME["highlight"]).next_to(p_exp_2, UP, buff=0.08)
        lbl_log_4 = MathTex(r"(4, 2)", font_size=11, color=THEME["curve"]).next_to(p_log_4, RIGHT, buff=0.08)
        symm_seg = DashedLine(p_exp_2, p_log_4, color=THEME["success"], stroke_width=1.5)

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

        # Trazado de identidad y curvas duales
        self.play(
            Create(diag_line), Write(lbl_diag),
            Create(curve_exp), Write(lbl_exp),
            Create(curve_log), Write(lbl_log),
            run_time=2.0
        )

        # Resaltado de puntos canónicos de corte
        self.play(
            FadeIn(dot_exp_0), Write(lbl_exp_0),
            FadeIn(dot_log_0), Write(lbl_log_0),
            run_time=1.2
        )

        # Resaltado de simetría en (2,4) y (4,2)
        self.play(
            Create(symm_seg),
            FadeIn(dot_exp_2), Write(lbl_exp_2),
            FadeIn(dot_log_4), Write(lbl_log_4),
            run_time=1.4
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            diag_line, lbl_diag,
            curve_exp, lbl_exp,
            curve_log, lbl_log,
            dot_exp_0, lbl_exp_0,
            dot_log_0, lbl_log_0,
            symm_seg, dot_exp_2, lbl_exp_2, dot_log_4, lbl_log_4
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
