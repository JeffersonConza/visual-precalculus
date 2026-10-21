"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.4: Paridad y valor absoluto
Ejercicio 5.8 (Página 52 del libro / Página 71 del PDF)

Demostración de las propiedades del valor absoluto (Corolario 5.11):
- Punto (5.36): Desigualdad triangular inversa: ||x| - |y|| ≤ |x - y| (∀ x, y ∈ ℝ).
- Punto (5.37): Desigualdad con punto intermedio: |x - y| ≤ |x - a| + |a - y| (∀ x, y, a ∈ ℝ).
- Interpretación métrica y funcional: análisis de la función distancia g(a) = |x - a| + |a - y|
  y la cota óptima de camino directo dist(x, y).
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_08(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.8",
            topic="Desigualdad Triangular (Corolario 5.11)"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Corolario 5.11: Sean x, y, a ∈ ℝ. Probar las propiedades:",
            math_tex=r"||x| - |y|| \le |x - y| \quad \text{y} \quad |x - y| \le |x - a| + |a - y|",
            desc_font_size=15,
            math_font_size=17,
            read_time=4.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Descomposición de x",
            "2/6: Descomposición de y",
            "3/6: Desigualdad Doble",
            "4/6: Triangular Inversa (5.36)",
            "5/6: Punto Intermedio (5.37)",
            "6/6: Interpretación Métrica"
        ])

        # ==========================================================
        # PASO 1: Descomposición de x y Cota Superior
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"|x| = |(x - y) + y| &\le |x - y| + |y| \\"
            r"\implies |x| - |y| &\le |x - y|"
            r"\end{aligned}",
            font_size=23,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Descomposición de x:\n"
            "Escribimos x = (x - y) + y.\n"
            "Aplicando la desigualdad triangular (5.35):\n"
            "|x| = |(x - y) + y| ≤ |x - y| + |y|.\n"
            "Restando |y| en ambos lados:\n"
            "|x| - |y| ≤ |x - y|."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Descomposición Simétrica de y
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"|y| = |(y - x) + x| &\le |x - y| + |x| \\"
            r"\implies -(|x| - |y|) &\le |x - y|"
            r"\end{aligned}",
            font_size=23,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Descomposición simétrica de y:\n"
            "Escribimos y = (y - x) + x.\n"
            "Por desigualdad triangular: |y| ≤ |y - x| + |x|.\n"
            "Como |y - x| = |-(x - y)| = |x - y|:\n"
            "|y| - |x| ≤ |x - y| ⟺ -(|x| - |y|) ≤ |x - y|."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Desigualdad Doble Acotada
        # ==========================================================
        eq3 = MathTex(
            r"-|x - y| \le |x| - |y| \le |x - y|",
            font_size=26,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Acotamiento simultáneo:\n"
            "Del paso 1 tenemos: |x| - |y| ≤ |x - y|.\n"
            "Del paso 2 tenemos: -|x - y| ≤ |x| - |y|.\n"
            "Combinando ambas desigualdades se obtiene:\n"
            "-|x - y| ≤ |x| - |y| ≤ |x - y|."
        )

        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Conclusión de la Triangular Inversa (5.36)
        # ==========================================================
        eq4 = MathTex(
            r"||x| - |y|| \le |x - y| \quad (\forall x, y \in \mathbb{R})",
            font_size=25,
            color=THEME["success"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Conclusión formal de (5.36):\n"
            "Por el Teorema 5.8 (punto 5.33):\n"
            "-M ≤ u ≤ M ⟺ |u| ≤ M (con M ≥ 0).\n"
            "Tomando u = |x| - |y| y M = |x - y| ≥ 0:\n"
            "||x| - |y|| ≤ |x - y|.\n"
            "Queda demostrada la propiedad (5.36)."
        )

        self.morph_step(eq4, just4, box_color=THEME["success"], advance_to_step=3, wait_time=5.2)

        # ==========================================================
        # PASO 5: Demostración del Punto Intermedio (5.37)
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"|x - y| &= |(x - a) + (a - y)| \\"
            r"&\le |x - a| + |a - y| \quad (\forall x, y, a \in \mathbb{R})"
            r"\end{aligned}",
            font_size=23,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Punto intermedio (5.37):\n"
            "Para cualquier punto intermedio a ∈ ℝ:\n"
            "Escribimos x - y = (x - a) + (a - y).\n"
            "Aplicando directamente el Teorema 5.10\n"
            "con u = x - a y v = a - y:\n"
            "|x - y| ≤ |x - a| + |a - y|."
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=5.2)

        # ==========================================================
        # PASO 6: Interpretación Métrica y Funcional
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Concepto métrico
        t_title = Text("Interpretación geométrica:", font_size=16, color=THEME["header_color"], weight=BOLD)
        eq_func = MathTex(r"g(a) = |x - a| + |a - y| \ge |x - y|", font_size=18, color=THEME["highlight"])
        t_desc1 = Text("• En ℝ: dist(x, y) ≤ dist(x, a) + dist(a, y).", font_size=13, color=THEME["statement_text"])
        t_desc2 = Text("• Para x = -1 e y = 2, la distancia directa es 3.", font_size=13, color=THEME["statement_text"])
        t_desc3 = Text("• La cota mínima g(a) = 3 ocurre si a ∈ [-1, 2].", font_size=13, color=THEME["success"])
        t_desc4 = Text("• Si a sale del segmento, la distancia crece.", font_size=13, color=THEME["curve"])

        info_content = VGroup(t_title, eq_func, t_desc1, t_desc2, t_desc3, t_desc4).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        info_box = SurroundingRectangle(info_content, color=THEME["statement_box"], buff=0.2, stroke_width=1.5, corner_radius=0.08)
        info_grp = VGroup(info_box, info_content).move_to([-3.4, -0.45, 0])

        # Panel derecho: Gráfica cartesiana de la función distancia
        axes, axes_labels = self.setup_axes(
            x_range=[-2.5, 3.5, 1],
            y_range=[0, 5.2, 1],
            x_length=5.6,
            y_length=3.8,
            center=[2.8, -0.45, 0],
            include_numbers=True
        )

        # Función cuenca: g(a) = |a + 1| + |a - 2|
        curve_basin = axes.plot(
            lambda a: abs(a + 1) + abs(a - 2),
            x_range=[-2.2, 3.2],
            color=THEME["highlight"],
            stroke_width=3.2
        )
        lbl_basin = MathTex(r"g(a) = |x - a| + |a - y|", font_size=14, color=THEME["highlight"]).next_to(axes.c2p(2.2, 4.4), UR, buff=0.05)

        # Línea de cota inferior: |x - y| = 3
        dist_line = axes.plot(
            lambda a: 3.0,
            x_range=[-2.4, 3.4],
            color=THEME["statement_box"],
            stroke_width=2.2
        )
        lbl_dist = MathTex(r"|x - y| = 3", font_size=14, color=THEME["statement_box"]).next_to(axes.c2p(3.2, 3.0), UR, buff=0.08)

        # Segmento de igualdad mínima: a ∈ [-1, 2] con g(a) = 3
        p_min_left = axes.c2p(-1.0, 3.0)
        p_min_right = axes.c2p(2.0, 3.0)
        min_seg = Line(p_min_left, p_min_right, color=THEME["success"], stroke_width=4.5)
        dot_left = Dot(p_min_left, radius=0.07, color=THEME["success"])
        dot_right = Dot(p_min_right, radius=0.07, color=THEME["success"])
        lbl_eq_zone = Text("Zona de igualdad (a ∈ [-1, 2])", font_size=11, color=THEME["success"]).next_to(min_seg, UP, buff=0.14)

        # Líneas guía de proyección vertical hacia los valores x = -1 e y = 2
        proj_left = DashedLine(p_min_left, axes.c2p(-1.0, 0), color=THEME["axes"], stroke_width=1.5)
        proj_right = DashedLine(p_min_right, axes.c2p(2.0, 0), color=THEME["axes"], stroke_width=1.5)

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

        # Trazado de la cota mínima y la función distancia
        self.play(
            Create(dist_line), Write(lbl_dist),
            run_time=1.2
        )
        self.play(
            Create(curve_basin), Write(lbl_basin),
            run_time=1.6
        )

        # Resaltado del piso de igualdad en el intervalo [-1, 2] y sus proyecciones
        self.play(
            Create(min_seg),
            Create(proj_left), Create(proj_right),
            FadeIn(dot_left), FadeIn(dot_right),
            Write(lbl_eq_zone),
            run_time=1.4
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            dist_line, lbl_dist,
            curve_basin, lbl_basin,
            min_seg, dot_left, dot_right, lbl_eq_zone,
            proj_left, proj_right
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
