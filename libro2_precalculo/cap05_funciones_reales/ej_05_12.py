"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.5: Invertibilidad de funciones
Ejercicio 5.12 (Página 64 del libro / Página 83 del PDF)

Demostración del Teorema 5.15 (Paridad de la función inversa):
- Hipótesis: f: ℝ → ℝ es biyectiva e impar.
- Tesis: f⁻¹: ℝ → ℝ es impar (f⁻¹(-y) = -f⁻¹(y) ∀ y ∈ ℝ).
- Deducción algebraica mediante composición y transitividad.
- Interpretación geométrica: simetría respecto a la diagonal y = x vs. simetría central respecto al origen.
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_12(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.12",
            topic="Paridad de la Función Inversa (Teorema 5.15)"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Teorema 5.15: Sea f: ℝ → ℝ biyectiva e impar. Probar:",
            math_tex=r"f^{-1} \text{ es impar} \quad [\forall y \in \mathbb{R} : f^{-1}(-y) = -f^{-1}(y)]",
            desc_font_size=15,
            math_font_size=16,
            read_time=4.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Hipótesis de Imparidad",
            "2/6: Preimagen x = f⁻¹(y)",
            "3/6: Negación de la Imagen",
            "4/6: Aplicación de f⁻¹",
            "5/6: Conclusión del Teorema",
            "6/6: Simetría Cartesiana"
        ])

        # ==========================================================
        # PASO 1: Hipótesis e Identidad Fundamental
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"f \text{ es biyectiva} &\implies \exists f^{-1} : y = f(x) \iff x = f^{-1}(y) \\"
            r"f \text{ es impar} &\implies \forall x \in \mathbb{R} : f(-x) = -f(x)"
            r"\end{aligned}",
            font_size=23,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Definiciones e hipótesis:\n"
            "Por ser biyectiva (Def. 5.9), existe la inversa\n"
            "f⁻¹: ℝ → ℝ con f⁻¹(f(x)) = x y f(f⁻¹(y)) = y.\n"
            "Por ser f impar (Def. 5.3): f(-x) = -f(x).\n"
            "Objetivo: probar f⁻¹(-y) = -f⁻¹(y) (∀ y ∈ ℝ)."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Elección de un Elemento Genérico y Preimagen
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"\text{Sea } y \in \mathbb{R} \text{ genérico}, \quad &x = f^{-1}(y) \\"
            r"\implies f(x) = f(f^{-1}(y)) &= y"
            r"\end{aligned}",
            font_size=24,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Preimagen del elemento genérico:\n"
            "Tomamos y ∈ ℝ arbitrario.\n"
            "Sea x = f⁻¹(y) su preimagen en ℝ.\n"
            "Por el Teorema 5.13 (inversa):\n"
            "f(x) = f(f⁻¹(y)) = y."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Negación de la Imagen y Uso de la Imparidad
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"-y &= -f(x) \\"
            r"-f(x) &= f(-x) \implies -y = f(-x)"
            r"\end{aligned}",
            font_size=25,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Negación e imparidad de f:\n"
            "Multiplicamos por -1 ambos miembros:\n"
            "-y = -f(x).\n"
            "Como f es impar, -f(x) = f(-x).\n"
            "Por transitividad se deduce:\n"
            "-y = f(-x)."
        )

        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=5.0)

        # ==========================================================
        # PASO 4: Aplicación de la Función Inversa a Ambos Lados
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"f^{-1}(-y) &= f^{-1}(f(-x)) \\"
            r"&= -x \quad (\text{por propiedad cancelativa})"
            r"\end{aligned}",
            font_size=24,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Aplicación de f⁻¹:\n"
            "Aplicamos f⁻¹ a ambos lados de -y = f(-x):\n"
            "f⁻¹(-y) = f⁻¹(f(-x)).\n"
            "Por el Teorema 5.13: f⁻¹(f(u)) = u (con u = -x):\n"
            "f⁻¹(-y) = -x."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=5.2)

        # ==========================================================
        # PASO 5: Sustitución y Conclusión Formal del Teorema
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"x = f^{-1}(y) &\implies f^{-1}(-y) = -f^{-1}(y) \\"
            r"\therefore \quad f^{-1} &\text{ es una función impar}"
            r"\end{aligned}",
            font_size=24,
            color=THEME["success"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Conclusión del Teorema 5.15:\n"
            "Recordando que x = f⁻¹(y), sustituimos:\n"
            "f⁻¹(-y) = -(f⁻¹(y)) = -f⁻¹(y).\n"
            "Dado que y ∈ ℝ fue arbitrario, se cumple:\n"
            "∀ y ∈ ℝ: f⁻¹(-y) = -f⁻¹(y).\n"
            "Concluimos que f⁻¹ es impar."
        )

        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.2)

        # ==========================================================
        # PASO 6: Interpretación Geométrica y Simetría Cartesiana
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Fundamento geométrico
        t_title = Text("Simetría geométrica:", font_size=16, color=THEME["header_color"], weight=BOLD)
        eq_geom = MathTex(r"(x, y) \in \text{Gr}(f) \iff (y, x) \in \text{Gr}(f^{-1})", font_size=17, color=THEME["highlight"])
        t_desc1 = Text("• f impar: simétrica respecto al origen (0, 0).", font_size=13, color=THEME["statement_text"])
        t_desc2 = Text("• f⁻¹: reflexión respecto a la diagonal y = x.", font_size=13, color=THEME["statement_text"])
        t_desc3 = Text("• Si (x, y) ∈ Gr(f) ⟹ (-x, -y) ∈ Gr(f) (impar).", font_size=13, color=THEME["success"])
        t_desc4 = Text("• Entonces (-y, -x) ∈ Gr(f⁻¹): f⁻¹ es impar.", font_size=13, color=THEME["curve"])

        info_content = VGroup(t_title, eq_geom, t_desc1, t_desc2, t_desc3, t_desc4).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        info_box = SurroundingRectangle(info_content, color=THEME["statement_box"], buff=0.2, stroke_width=1.5, corner_radius=0.08)
        info_grp = VGroup(info_box, info_content).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos comparativos
        axes, axes_labels = self.setup_axes(
            x_range=[-2.2, 2.2, 1],
            y_range=[-2.2, 2.2, 1],
            x_length=5.6,
            y_length=3.8,
            center=[2.8, -0.45, 0],
            include_numbers=True
        )

        # Recta diagonal y = x
        line_diag = axes.plot(lambda x: x, x_range=[-1.8, 1.8], color=THEME["statement_text"], stroke_width=1.8)
        lbl_diag = MathTex(r"y = x", font_size=13, color=THEME["statement_text"]).next_to(axes.c2p(1.7, 1.7), UR, buff=0.05)

        # Curva impar directa: f(x) = x³
        curve_f = axes.plot(
            lambda x: x**3,
            x_range=[-1.28, 1.28],
            color=THEME["highlight"],
            stroke_width=3.0
        )
        lbl_f = MathTex(r"f(x) = x^3", font_size=14, color=THEME["highlight"]).next_to(axes.c2p(1.25, 1.95), UL, buff=0.08)

        # Curva impar inversa: f⁻¹(x) = ∛x
        curve_finv = axes.plot(
            lambda x: np.cbrt(x),
            x_range=[-2.0, 2.0],
            color=THEME["curve"],
            stroke_width=3.0
        )
        lbl_finv = MathTex(r"f^{-1}(x) = \sqrt[3]{x}", font_size=14, color=THEME["curve"]).next_to(axes.c2p(1.9, 1.25), DR, buff=0.08)

        # Puntos simétricos para ilustrar imparidad simultánea
        p_f_pos = Dot(axes.c2p(1.1, 1.1**3), radius=0.06, color=THEME["highlight"])
        p_f_neg = Dot(axes.c2p(-1.1, -(1.1**3)), radius=0.06, color=THEME["highlight"])
        line_sym_f = DashedLine(p_f_neg.get_center(), p_f_pos.get_center(), color=THEME["highlight"], stroke_width=1.5)

        p_inv_pos = Dot(axes.c2p(1.1**3, 1.1), radius=0.06, color=THEME["curve"])
        p_inv_neg = Dot(axes.c2p(-(1.1**3), -1.1), radius=0.06, color=THEME["curve"])
        line_sym_inv = DashedLine(p_inv_neg.get_center(), p_inv_pos.get_center(), color=THEME["curve"], stroke_width=1.5)

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

        # Trazado de la diagonal y las curvas simétricas
        self.play(
            Create(line_diag), Write(lbl_diag),
            run_time=1.0
        )
        self.play(
            Create(curve_f), Write(lbl_f),
            Create(curve_finv), Write(lbl_finv),
            run_time=1.8
        )

        # Resaltado de la simetría central respecto al origen para ambas curvas
        self.play(
            Create(line_sym_f), FadeIn(p_f_pos), FadeIn(p_f_neg),
            Create(line_sym_inv), FadeIn(p_inv_pos), FadeIn(p_inv_neg),
            run_time=1.4
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            line_diag, lbl_diag,
            curve_f, lbl_f,
            curve_finv, lbl_finv,
            line_sym_f, p_f_pos, p_f_neg,
            line_sym_inv, p_inv_pos, p_inv_neg
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
