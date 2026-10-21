"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.28 (Página 109 del libro / Página 128 del PDF)

Demostración de la Desigualdad Triangular Inversa:
- Enunciado: Sean x, y ∈ ℝ. Probar que:
  ||x| - |y|| ≤ |x - y|.
- Paso 1: Enunciado y criterio de acotación: -c ≤ u ≤ c ⟺ |u| ≤ c con c = |x - y|.
- Paso 2: Cota superior: x = (x - y) + y ⟹ |x| ≤ |x - y| + |y| ⟹ |x| - |y| ≤ |x - y|.
- Paso 3: Cota simétrica: y = (y - x) + x ⟹ |y| ≤ |y - x| + |x| ⟹ |y| - |x| ≤ |x - y|.
- Paso 4: Cota inferior: -(|x - y|) ≤ |x| - |y|.
- Paso 5: Doble desigualdad y conclusión: -|x - y| ≤ |x| - |y| ≤ |x - y| ⟹ ||x| - |y|| ≤ |x - y|.
- Paso 6: Interpretación gráfica cartesiana: Comparación de h(x) = ||x| - 2| frente a d(x, 2) = |x - 2|.
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_28(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.28",
            topic="Desigualdad Triangular Inversa"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Demostración rigurosa para cualesquiera números reales x, y ∈ ℝ:",
            math_tex=r"\big| |x| - |y| \big| \le |x - y|",
            desc_font_size=15,
            math_font_size=17,
            read_time=4.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Criterio de Acotación",
            "2/6: Cota Superior (|x| - |y|)",
            "3/6: Descomposición Simétrica",
            "4/6: Cota Inferior (-|x - y|)",
            "5/6: Integración y Conclusión",
            "6/6: Gráfica Métrica Comparativa"
        ])

        # ==========================================================
        # PASO 1: Criterio de Acotación
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"\text{Propiedad: } &\forall u \in \mathbb{R}, \; c \ge 0: \quad |u| \le c \iff -c \le u \le c \\[6pt]"
            r"\text{Haciendo } &u = |x| - |y| \quad \text{y} \quad c = |x - y| \ge 0: \\[6pt]"
            r"\big| |x| - |y| \big| &\le |x - y| \iff -|x - y| \le |x| - |y| \le |x - y|"
            r"\end{aligned}",
            font_size=21,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Criterio de acotación:\n"
            "Para probar una desigualdad del tipo |u| ≤ c,\n"
            "basta demostrar la doble desigualdad acotada:\n"
            "-c ≤ u ≤ c.\n"
            "Aquí tomamos u = |x| - |y| y c = |x - y| ≥ 0.\n"
            "Demostraremos las cotas superior e inferior."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Cota Superior (|x| - |y| ≤ |x - y|)
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"x &= (x - y) + y \quad (\text{Sumar y restar } y) \\[6pt]"
            r"|x| &= |(x - y) + y| \le |x - y| + |y| \quad (\text{Desig. Triangular}) \\[6pt]"
            r"\text{Restando } &|y| \text{ a ambos miembros:} \\[4pt]"
            r"|x| - |y| &\le |x - y| \quad \text{--- (Cota Superior)}"
            r"\end{aligned}",
            font_size=21,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Cota superior:\n"
            "Escribimos x como (x - y) + y.\n"
            "Aplicamos la desigualdad triangular directa:\n"
            "|a + b| ≤ |a| + |b| tomando a = x - y y b = y.\n"
            "Restamos |y| a ambos lados y obtenemos:\n"
            "|x| - |y| ≤ |x - y|."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Descomposición Simétrica de |y|
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"y &= (y - x) + x \quad (\text{Sumar y restar } x) \\[6pt]"
            r"|y| &= |(y - x) + x| \le |y - x| + |x| \\[6pt]"
            r"\text{Como } &|y - x| = |-(x - y)| = |x - y| : \\[4pt]"
            r"|y| &\le |x - y| + |x| \implies |y| - |x| \le |x - y|"
            r"\end{aligned}",
            font_size=21,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Descomposición simétrica:\n"
            "Intercambiamos los roles de x e y:\n"
            "y = (y - x) + x.\n"
            "Por simetría métrica: |y - x| = |x - y|.\n"
            "Aplicando la desigualdad triangular y restando |x|:\n"
            "|y| - |x| ≤ |x - y|."
        )

        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Cota Inferior (-|x - y| ≤ |x| - |y|)
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"|y| - |x| &\le |x - y| \\[6pt]"
            r"-(|x| - |y|) &\le |x - y| \\[6pt]"
            r"\text{Multiplicando } &\text{por } -1 \text{ (se invierte el orden):} \\[4pt]"
            r"|x| - |y| &\ge -|x - y| \iff -|x - y| \le |x| - |y|"
            r"\end{aligned}",
            font_size=21,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Cota inferior:\n"
            "Notamos que |y| - |x| = -(|x| - |y|).\n"
            "Al multiplicar la desigualdad por -1,\n"
            "el sentido de orden se invierte:\n"
            "|x| - |y| ≥ -|x - y|,\n"
            "lo que proporciona la cota inferior deseada."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=4.8)

        # ==========================================================
        # PASO 5: Integración y Conclusión
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"-|x - y| \le |x| - |y| \quad &\land \quad |x| - |y| \le |x - y| \\[8pt]"
            r"\implies -|x - y| &\le |x| - |y| \le |x - y| \\[8pt]"
            r"\therefore \quad \big| |x| - |y| \big| &\le |x - y| \quad \blacksquare"
            r"\end{aligned}",
            font_size=22,
            color=THEME["success"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Conclusión formal:\n"
            "Unificamos la cota inferior del Paso 4 con la\n"
            "cota superior del Paso 2 en una sola cadena:\n"
            "-|x - y| ≤ |x| - |y| ≤ |x - y|.\n"
            "Por el criterio de acotación del Paso 1, concluimos:\n"
            "||x| - |y|| ≤ |x - y| para cualesquiera x, y ∈ ℝ."
        )

        self.morph_step(eq5, just5, box_color=THEME["success"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Interpretación Gráfica Cartesiana
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen geométrico
        t_title = Text("Geometría métrica en ℝ (y = 2 fijo):", font_size=15, color=THEME["header_color"], weight=BOLD)
        eq_curvas = MathTex(r"h(x) = \big| |x| - 2 \big|, \quad d(x) = |x - 2|", font_size=15, color=THEME["highlight"])
        t_desc1 = Text("• d(x) = |x - 2| mide la distancia usual a 2.", font_size=12, color=THEME["secondary"])
        t_desc2 = Text("• h(x) = ||x| - 2| mide la diferencia de normas.", font_size=12, color=THEME["curve"])
        t_desc3 = Text("• Para x ≥ 0: h(x) = |x - 2| = d(x)  (Igualdad).", font_size=12, color=THEME["success"])
        t_desc4 = Text("• Para x < 0: h(x) = |x + 2| < |x - 2|  (Estricta).", font_size=12, color=THEME["highlight"])
        t_desc5 = Text("• En todo ℝ: la curva h(x) jamás supera a d(x):", font_size=12, color=THEME["success"], weight=BOLD)
        t_desc6 = Text("  ||x| - 2| ≤ |x - 2|  confirmado.", font_size=12, color=THEME["success"])

        info_content = VGroup(t_title, eq_curvas, t_desc1, t_desc2, t_desc3, t_desc4, t_desc5, t_desc6).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        info_box = SurroundingRectangle(info_content, color=THEME["statement_box"], buff=0.2, stroke_width=1.5, corner_radius=0.08)
        info_grp = VGroup(info_box, info_content).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos
        axes, axes_labels = self.setup_axes(
            x_range=[-4.0, 5.0, 1],
            y_range=[-1.0, 6.0, 1],
            x_length=5.6,
            y_length=3.8,
            center=[2.8, -0.45, 0],
            include_numbers=True
        )

        # Curva de cota superior: d(x) = |x - 2|
        curve_d = axes.plot(lambda x: np.abs(x - 2), x_range=[-3.8, 4.8], color=THEME["secondary"], stroke_width=2.4)
        lbl_d = MathTex(r"d(x) = |x - 2|", font_size=13, color=THEME["secondary"]).next_to(axes.c2p(-3.0, 5.0), RIGHT, buff=0.08)

        # Curva acotada: h(x) = ||x| - 2|
        curve_h = axes.plot(lambda x: np.abs(np.abs(x) - 2), x_range=[-3.8, 4.8], color=THEME["curve"], stroke_width=3.2)
        lbl_h = MathTex(r"h(x) = \big| |x| - 2 \big|", font_size=13, color=THEME["curve"]).next_to(axes.c2p(0, 2.0), UP, buff=0.08)

        # Puntos notables: vértice en (2,0) y cúspide en (0,2)
        p_corte = axes.c2p(2.0, 0.0)
        p_cusp = axes.c2p(0.0, 2.0)
        dot_corte = Dot(p_corte, radius=0.06, color=THEME["success"])
        dot_cusp = Dot(p_cusp, radius=0.06, color=THEME["curve"])

        lbl_corte = MathTex(r"(2, 0)", font_size=11, color=THEME["success"]).next_to(p_corte, DOWN, buff=0.08)
        lbl_cusp = MathTex(r"(0, 2)", font_size=11, color=THEME["curve"]).next_to(p_cusp, LEFT, buff=0.08)

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

        # Trazado de ambas curvas
        self.play(
            Create(curve_d), Write(lbl_d),
            Create(curve_h), Write(lbl_h),
            run_time=2.2
        )

        # Marcado de puntos de coincidencia y cúspide
        self.play(
            FadeIn(dot_corte), Write(lbl_corte),
            FadeIn(dot_cusp), Write(lbl_cusp),
            run_time=1.4
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_d, lbl_d,
            curve_h, lbl_h,
            dot_corte, dot_cusp,
            lbl_corte, lbl_cusp
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
