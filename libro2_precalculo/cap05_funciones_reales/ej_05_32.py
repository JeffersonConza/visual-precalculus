"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.32 (Página 109 del libro / Página 128 del PDF)

Ecuación con radicales simétricos:
- Enunciado: Resuelve la ecuación en ℝ:
  √(2x² + 3x + 5) + √(2x² - 3x + 5) = 3x.
  Indicación del libro: Aprovechar la similitud de los radicandos vía una racionalización.
- Paso 1: Dominio universal (Δ < 0 ⟹ radicandos siempre positivos) y condición x > 0.
- Paso 2: Multiplicación por el conjugado: A² - B² = 6x = 3x(A - B).
- Paso 3: Sistema lineal: A + B = 3x y A - B = 2 (al simplificar 3x > 0).
- Paso 4: Suma del sistema: 2A = 3x + 2 ⟹ A = (3x + 2)/2.
- Paso 5: Elevación al cuadrado: 8x² + 12x + 20 = 9x² + 12x + 4 ⟹ x² = 16 ⟹ x = 4 (CS = {4}).
- Paso 6: Interpretación gráfica cartesiana: Curva f(x) = A(x) + B(x), recta g(x) = 3x,
  intersección única en P(4, 12).
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_32(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.32",
            topic="Ecuación con Radicales (Racionalización)"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Resuelve la ecuación con radicales en ℝ aprovechando la similitud de radicandos:",
            math_tex=r"\sqrt{2x^2 + 3x + 5} + \sqrt{2x^2 - 3x + 5} = 3x, \quad x \in \mathbb{R}",
            desc_font_size=15,
            math_font_size=16,
            read_time=4.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Dominio y Positividad",
            "2/6: Artificio del Conjugado",
            "3/6: Sistema Lineal de Radicales",
            "4/6: Aislamiento de un Radical",
            "5/6: Cuadratura y Solución (x=4)",
            "6/6: Gráfica Cartesiana e Intersección"
        ])

        # ==========================================================
        # PASO 1: Dominio y Condición de Positividad
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"\text{Sean } &A = \sqrt{2x^2 + 3x + 5}, \quad B = \sqrt{2x^2 - 3x + 5} \\[6pt]"
            r"\Delta &= 9 - 40 = -31 < 0 \implies 2x^2 \pm 3x + 5 > 0 \quad (\forall x \in \mathbb{R}) \\[6pt]"
            r"\text{Como } &A > 0 \text{ y } B > 0 \implies A + B = 3x > 0 \iff x > 0"
            r"\end{aligned}",
            font_size=20,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Dominio y condición de signo:\n"
            "Los discriminantes de ambos trinomios son\n"
            "Δ = -31 < 0, con coeficiente principal 2 > 0.\n"
            "Por tanto, ambos radicandos son estrictamente\n"
            "positivos en todo ℝ (U = ℝ).\n"
            "Al ser suma de raíces positivas: 3x > 0 ⟹ x > 0."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Artificio del Conjugado (Racionalización)
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"A^2 - B^2 &= (2x^2 + 3x + 5) - (2x^2 - 3x + 5) = 6x \\[6pt]"
            r"(A + B)(A - B) &= 6x \\[6pt]"
            r"\text{Sustituyendo } &A + B = 3x : \\[4pt]"
            r"3x(A - B) &= 6x"
            r"\end{aligned}",
            font_size=22,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Artificio del conjugado:\n"
            "Restamos los dos radicandos para eliminar los\n"
            "términos cuadráticos y constantes:\n"
            "A² - B² = 6x.\n"
            "Por diferencia de cuadrados: (A + B)(A - B) = 6x.\n"
            "Sustituyendo la ecuación original: 3x(A - B) = 6x."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Sistema Lineal de Radicales
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"\text{Como } x > 0 \implies 3x &\neq 0, \quad \text{dividimos por } 3x: \\[6pt]"
            r"A - B &= \frac{6x}{3x} = 2 \\[8pt]"
            r"\text{Obtenemos el sistema: } &\begin{cases} A + B = 3x & \text{(I)} \\ A - B = 2 & \text{(II)} \end{cases}"
            r"\end{aligned}",
            font_size=21,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Sistema lineal de radicales:\n"
            "Dado que x > 0, dividimos lícitamente por 3x:\n"
            "A - B = 2.\n"
            "El problema no lineal se transforma en un sistema\n"
            "simétrico elemental para las variables A y B:\n"
            "A + B = 3x  y  A - B = 2."
        )

        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Aislamiento de un Solo Radical
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"\text{Sumando (I) y (II): } &2A = 3x + 2 \\[6pt]"
            r"A &= \frac{3x + 2}{2} \\[6pt]"
            r"\sqrt{2x^2 + 3x + 5} &= \frac{3x + 2}{2} \quad (\text{Ambos lados } > 0)"
            r"\end{aligned}",
            font_size=22,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Aislamiento de A:\n"
            "Sumamos miembro a miembro las dos ecuaciones:\n"
            "(A + B) + (A - B) = 3x + 2 ⟹ 2A = 3x + 2.\n"
            "Despejamos: A = (3x + 2)/2.\n"
            "Restituimos el radical original:\n"
            "√(2x² + 3x + 5) = (3x + 2)/2."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=4.8)

        # ==========================================================
        # PASO 5: Cuadratura, Cancelación y Solución
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"2x^2 + 3x + 5 &= \frac{9x^2 + 12x + 4}{4} \\[6pt]"
            r"8x^2 + 12x + 20 &= 9x^2 + 12x + 4 \\[6pt]"
            r"x^2 &= 16 \implies x = 4 \quad (x > 0) \\[6pt]"
            r"\therefore \quad CS &= \{4\} \quad \blacksquare"
            r"\end{aligned}",
            font_size=22,
            color=THEME["success"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Cuadratura y solución única:\n"
            "Elevamos al cuadrado y multiplicamos por 4:\n"
            "8x² + 12x + 20 = 9x² + 12x + 4.\n"
            "El término lineal 12x se cancela exactamente:\n"
            "x² = 16 ⟹ x = 4 (descartando -4 por x > 0).\n"
            "Comprobación: 7 + 5 = 12 = 3(4) ✅. CS = {4}."
        )

        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen geométrico
        t_title = Text("Geometría de la Intersección:", font_size=15, color=THEME["header_color"], weight=BOLD)
        eq_curva = MathTex(r"f(x) = \sqrt{2x^2+3x+5} + \sqrt{2x^2-3x+5}", font_size=13, color=THEME["highlight"])
        eq_recta = MathTex(r"g(x) = 3x", font_size=15, color=THEME["secondary"])
        t_desc1 = Text("• En x = 0: f(0) = 2√5 ≈ 4.47 > g(0) = 0.", font_size=12, color=THEME["statement_text"])
        t_desc2 = Text("• Pendiente asintótica de f: 2√2 ≈ 2.828.", font_size=12, color=THEME["curve"])
        t_desc3 = Text("• Pendiente de g: 3 > 2.828 (la recta corta a la curva).", font_size=12, color=THEME["statement_text"])
        t_desc4 = Text("• Intersección única en todo ℝ:", font_size=12, color=THEME["success"], weight=BOLD)
        t_desc5 = Text("  P(4, 12),  pues f(4) = 7 + 5 = 12 y g(4) = 12.", font_size=12, color=THEME["success"])
        t_desc6 = Text("• Veredicto: CS = {4} confirmado.", font_size=12, color=THEME["secondary"])

        info_content = VGroup(t_title, eq_curva, eq_recta, t_desc1, t_desc2, t_desc3, t_desc4, t_desc5, t_desc6).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        info_box = SurroundingRectangle(info_content, color=THEME["statement_box"], buff=0.2, stroke_width=1.5, corner_radius=0.08)
        info_grp = VGroup(info_box, info_content).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos
        axes, axes_labels = self.setup_axes(
            x_range=[-1.0, 6.0, 1],
            y_range=[-1.0, 16.0, 3],
            x_length=5.6,
            y_length=3.8,
            center=[2.8, -0.45, 0],
            include_numbers=True
        )

        # Curva f(x) = sqrt(2x^2+3x+5) + sqrt(2x^2-3x+5)
        curve_f = axes.plot(lambda x: np.sqrt(2*x**2 + 3*x + 5) + np.sqrt(2*x**2 - 3*x + 5), x_range=[-0.5, 5.5], color=THEME["highlight"], stroke_width=3.0)
        lbl_f = MathTex(r"f(x)", font_size=13, color=THEME["highlight"]).next_to(axes.c2p(2.2, np.sqrt(2*2.2**2 + 3*2.2 + 5) + np.sqrt(2*2.2**2 - 3*2.2 + 5)), UL, buff=0.08)

        # Recta g(x) = 3x
        line_g = axes.plot(lambda x: 3*x, x_range=[-0.3, 5.2], color=THEME["secondary"], stroke_width=2.2)
        lbl_g = MathTex(r"g(x) = 3x", font_size=13, color=THEME["secondary"]).next_to(axes.c2p(4.8, 14.4), DR, buff=0.08)

        # Punto de corte P(4, 12)
        p_corte = axes.c2p(4.0, 12.0)
        dot_corte = Dot(p_corte, radius=0.07, color=THEME["success"])
        lbl_corte = MathTex(r"(4, 12)", font_size=12, color=THEME["success"]).next_to(p_corte, UL, buff=0.08)

        # Guías al eje X y eje Y
        guide_x = DashedLine(p_corte, axes.c2p(4.0, 0), color=THEME["statement_box"], stroke_width=1.5)
        guide_y = DashedLine(p_corte, axes.c2p(0, 12.0), color=THEME["statement_box"], stroke_width=1.5)
        dot_x = Dot(axes.c2p(4.0, 0), radius=0.06, color=THEME["success"])
        lbl_x = MathTex(r"x = 4", font_size=12, color=THEME["success"]).next_to(axes.c2p(4.0, 0), DOWN, buff=0.15)

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

        # Trazado de la curva f(x) y la recta g(x)
        self.play(
            Create(curve_f), Write(lbl_f),
            Create(line_g), Write(lbl_g),
            run_time=2.2
        )

        # Resaltado del punto de intersección (4, 12) y proyección a los ejes
        self.play(
            FadeIn(dot_corte), Write(lbl_corte),
            Create(guide_x), Create(guide_y),
            FadeIn(dot_x), Write(lbl_x),
            run_time=1.6
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_f, lbl_f,
            line_g, lbl_g,
            dot_corte, lbl_corte,
            guide_x, guide_y,
            dot_x, lbl_x
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
