"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.52 (Páginas 113-114 del libro / Páginas 132-133 del PDF)

Análisis completo de 6 fórmulas reales:
1. f(x) = |3x+2| - 3x + 8 ⟹ Rg = [10, +∞[, No inyectiva.
2. f(x) = |x-3| + |x+2| + 1 ⟹ Rg = [6, +∞[, No inyectiva.
3. f(x) = 2|x| - |x-3| ⟹ Rg = [-3, +∞[, No inyectiva.
4. f(x) = |2x² - 5x + 4| = 2x² - 5x + 4 ⟹ Rg = [7/8, +∞[, No inyectiva.
5. f(x) = w(x) - g(x) con w a trozos ⟹ Discontinuidad de salto en x = 2, Rg = ]-∞, -1] ∪ ]3, 9/2], No inyectiva.
6. f(x) = x³ - 4x² + 5x - 1 ⟹ Rg = ℝ, extremos locales en (1, 1) y (5/3, 23/27), No inyectiva.
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_52(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.52",
            topic="Análisis Integral de Funciones: RMD, Rango e Inyectividad"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Analizar RMD, rango, monotonía e inyectividad para las 6 fórmulas reales:",
            math_tex=r"1.\; |3x+2|-3x+8; \;\; 2.\; |x-3|+|x+2|+1; \;\; 4.\; |2x^2-5x+4|; \;\; 5.\; w(x)-|2x-5|; \;\; 6.\; x^3-4x^2+5x-1.",
            desc_font_size=14,
            math_font_size=13,
            read_time=4.0
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Ítems 1 y 2 (Mesetas)",
            "2/6: Ítems 3 y 4 (Poligonal y Parábola)",
            "3/6: Ítem 5 (Salto y Rango Disjunto)",
            "4/6: Ítem 6 (Cúbica y Extremos)",
            "5/6: Maxima y Tabla de Inyectividad",
            "6/6: Resumen y Gráfica del Ítem 5"
        ])

        # ==========================================================
        # PASO 1: Ítems 1 y 2 (Funciones con Meseta Constante)
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\mathbf{1.} \quad f(x) = |3x+2| - 3x + 8, \quad \operatorname{Dom}(f) = \mathbb{R} \\[3pt]"
            r"&\begin{cases} x \ge -2/3 \implies (3x+2) - 3x + 8 = 10 \quad (\text{constante}) \\ x < -2/3 \implies -(3x+2) - 3x + 8 = -6x + 6 \end{cases} \\[4pt]"
            r"&\mathbf{Rg}(f) = [10, +\infty[, \quad \text{Inyectiva: } \textbf{NO} \quad (\text{meseta en } [-2/3, +\infty[) \\[6pt]"
            r"&\mathbf{2.} \quad f(x) = |x-3| + |x+2| + 1, \quad \operatorname{Dom}(f) = \mathbb{R} \\[3pt]"
            r"&\text{En } [-2, 3]: \; -(x-3) + (x+2) + 1 = 6 \quad (\text{meseta central}) \\[4pt]"
            r"&\mathbf{Rg}(f) = [6, +\infty[, \quad \text{Inyectiva: } \textbf{NO}"
            r"\end{aligned}",
            font_size=16,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Ítems 1 y 2 (Mesetas Constantes):\n"
            "• Ítem 1: Para x ≥ -2/3, las x se cancelan,\n"
            "  generando la semirrecta horizontal y = 10.\n"
            "  Rg = [10, +∞[. Falla inyectividad.\n"
            "• Ítem 2: Entre los nodos x = -2 y x = 3,\n"
            "  la suma de distancias es constante: y = 6.\n"
            "  Rg = [6, +∞[. Falla inyectividad."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Ítems 3 y 4 (Poligonal y Parábola Positiva)
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\mathbf{3.} \quad f(x) = 2|x| - |x-3|, \quad \operatorname{Dom}(f) = \mathbb{R} \\[3pt]"
            r"&x \le 0: -x-3; \quad 0 \le x \le 3: 3x-3; \quad x \ge 3: x+3 \\[3pt]"
            r"&\text{M\'inimo global en } x = 0 \implies f(0) = -3 \\[4pt]"
            r"&\mathbf{Rg}(f) = [-3, +\infty[, \quad \text{Inyectiva: } \textbf{NO} \\[6pt]"
            r"&\mathbf{4.} \quad f(x) = |2x^2 - 5x + 4| \\[3pt]"
            r"&\Delta = (-5)^2 - 4(2)(4) = -7 < 0 \implies 2x^2-5x+4 > 0 \;\forall x \\[3pt]"
            r"&\implies f(x) = 2x^2 - 5x + 4, \quad V = \left(\tfrac{5}{4}, \tfrac{7}{8}\right) \\[4pt]"
            r"&\mathbf{Rg}(f) = [7/8, +\infty[, \quad \text{Inyectiva: } \textbf{NO}"
            r"\end{aligned}",
            font_size=16,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Ítems 3 y 4 (Poligonal y Parábola):\n"
            "• Ítem 3: Función en 'V' asimétrica con vértice\n"
            "  mínimo en (0, -3). Decrece y luego crece,\n"
            "  por lo que no es inyectiva.\n"
            "• Ítem 4: Discriminante Δ = -7 < 0. El trinomio\n"
            "  es estrictamente positivo; el valor absoluto\n"
            "  es redundante. Parábola con vértice en (5/4, 7/8)."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], wait_time=5.0)

        # ==========================================================
        # PASO 3: Ítem 5 (Trozo con Salto y Rango Disjunto)
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\mathbf{5.} \quad f(x) = w(x) - |2x-5|, \quad w(x) = \begin{cases} x+2, &x > 2 \\ -x+2, &x \le 2 \end{cases} \\[4pt]"
            r"&x \le 2: \; f(x) = (-x+2) - (-2x+5) = x - 3 \implies \; ]-\infty, -1] \\[3pt]"
            r"&2 < x \le 2.5: \; f(x) = (x+2) - (-2x+5) = 3x - 3 \implies \; ]3, 4.5] \\[3pt]"
            r"&x > 2.5: \; f(x) = (x+2) - (2x-5) = -x + 7 \implies \; ]-\infty, 4.5[ \\[5pt]"
            r"&\textbf{Salto en } x = 2: \quad f(2) = -1, \quad \lim_{x \to 2^+} f(x) = 3 \\[5pt]"
            r"&\mathbf{Rg}(f) = \; ]-\infty, -1] \;\cup\; ]3, 9/2], \quad \text{Inyectiva: } \textbf{NO}"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Ítem 5 (Salto y Rango Disjunto):\n"
            "• Para x > 2, |x²-4|/(x-2) = x + 2.\n"
            "• En x = 2 hay un salto de 4 unidades:\n"
            "  f(2) = -1 mientras que por la derecha tiende a 3.\n"
            "• Máximo local en x = 2.5: f(2.5) = 4.5.\n"
            "• El rango es la unión disjunta ]-∞, -1] ∪ ]3, 9/2].\n"
            "• Falla inyectividad."
        )

        self.morph_step(eq3, just3, box_color=THEME["statement_box"], wait_time=5.0)

        # ==========================================================
        # PASO 4: Ítem 6 (Polinomio Cúbico y Extremos Locales)
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\mathbf{6.} \quad f(x) = x^3 - 4x^2 + 5x - 1, \quad \operatorname{Dom}(f) = \mathbb{R} \\[4pt]"
            r"&f'(x) = 3x^2 - 8x + 5 = (3x-5)(x-1) \\[4pt]"
            r"&\text{Puntos cr\'iticos: } x_1 = 1, \quad x_2 = 5/3 \\[4pt]"
            r"&\text{M\'aximo local: } f(1) = 1 \\[3pt]"
            r"&\text{M\'inimo local: } f(5/3) = 23/27 \approx 0.852 \\[5pt]"
            r"&\text{Oscila en } [5/3, 1] \implies 3 \text{ preim\'agenes para } y \in \; ]23/27, 1[ \\[5pt]"
            r"&\mathbf{Rg}(f) = \mathbb{R}, \quad \text{Inyectiva: } \textbf{NO}"
            r"\end{aligned}",
            font_size=16,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Ítem 6 (Cúbica y Extremos):\n"
            "• Derivada f'(x) = (3x - 5)(x - 1).\n"
            "• Crece en ]-∞, 1], decrece en [1, 5/3] y\n"
            "  vuelve a crecer en [5/3, +∞[.\n"
            "• Onda cúbica entre y = 23/27 e y = 1.\n"
            "• Como polinomio impar continuo, Rg(f) = ℝ.\n"
            "• Falla inyectividad por test de recta horizontal."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 5: Comparación Global y Comando Maxima
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{Tabla Comparativa de Inyectividad:} \\[5pt]"
            r"&\begin{array}{|c|c|c|c|} \hline"
            r"\text{\textbf{Ítem}} & \textbf{Dominio} & \textbf{Rango} & \textbf{¿Inyectiva?} \\ \hline"
            r"1 & \mathbb{R} & [10, +\infty[ & \textbf{NO} \\"
            r"2 & \mathbb{R} & [6, +\infty[ & \textbf{NO} \\"
            r"3 & \mathbb{R} & [-3, +\infty[ & \textbf{NO} \\"
            r"4 & \mathbb{R} & [7/8, +\infty[ & \textbf{NO} \\"
            r"5 & \mathbb{R} & ]-\infty, -1] \cup ]3, 9/2] & \textbf{NO} \\"
            r"6 & \mathbb{R} & \mathbb{R} & \textbf{NO} \\ \hline"
            r"\end{array} \\[6pt]"
            r"&\textbf{Maxima:} \; \texttt{plot2d([abs(3*x+2)-3*x+8], [x,-5,5]);}"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Tabla Comparativa e Inyectividad:\n"
            "• Conclusión central: ¡NINGUNA de las 6\n"
            "  funciones es inyectiva!\n"
            "• Todas admiten al menos una recta horizontal\n"
            "  que corta a la gráfica en múltiples puntos.\n"
            "• En Maxima, plot2d permite graficar cada\n"
            "  función con sus discontinuidades o quiebres."
        )

        self.morph_step(eq5, just5, box_color=THEME["secondary"], wait_time=5.0)

        # ==========================================================
        # PASO 6: Resumen y Gráfica del Ítem 5 (Discontinuidad de Salto)
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen del Ítem 5
        t_title = Text("Geometría del Ítem 5 (Salto y Cúspide):", font_size=13, color=THEME["header_color"], weight=BOLD)
        t_r1 = MathTex(r"x \le 2: \; y = x - 3 \quad (\text{punto cerrado en } (2, -1))", font_size=11, color=THEME["secondary"])
        t_r2 = MathTex(r"2 < x \le 2.5: \; y = 3x - 3 \quad (\text{abierto en } (2, 3))", font_size=11, color=THEME["highlight"])
        t_r3 = MathTex(r"x > 2.5: \; y = -x + 7 \quad (\text{c\'uspide en } (2.5, 4.5))", font_size=11, color=THEME["curve"])
        t_jump = Text("• Salto de 4 unidades en x = 2.", font_size=11, color=THEME["statement_box"], weight=BOLD)
        t_rg_desc = MathTex(r"\mathbf{Rg}(f) = \; ]-\infty, -1] \;\cup\; ]3, 4.5]", font_size=12, color=THEME["success"])

        info_grp = VGroup(t_title, t_r1, t_r2, t_r3, t_jump, t_rg_desc).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        info_box = SurroundingRectangle(info_grp, color=THEME["statement_box"], buff=0.18, stroke_width=1.5, corner_radius=0.08)
        left_grp = VGroup(info_box, info_grp).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos para graficar el Ítem 5
        axes, axes_labels = self.setup_axes(
            x_range=[-1.0, 5.0, 1],
            y_range=[-3.0, 5.5, 1],
            x_length=4.8,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True
        )

        # Rama 1: x in [-0.8, 2.0], y = x - 3
        branch1 = axes.plot(lambda x: x - 3, x_range=[-0.8, 2.0], color=THEME["secondary"], stroke_width=2.5)
        dot_closed = Dot(axes.c2p(2.0, -1.0), radius=0.06, color=THEME["secondary"])

        # Punto abierto en (2, 3)
        dot_open = Dot(axes.c2p(2.0, 3.0), radius=0.065, stroke_width=1.8, stroke_color=THEME["highlight"], fill_color=THEME["bg_color"])

        # Rama 2: x in [2.01, 2.5], y = 3x - 3
        branch2 = axes.plot(lambda x: 3*x - 3, x_range=[2.01, 2.5], color=THEME["highlight"], stroke_width=2.5)

        # Cúspide en (2.5, 4.5)
        dot_peak = Dot(axes.c2p(2.5, 4.5), radius=0.06, color=THEME["curve"])
        lbl_peak = MathTex(r"(2.5, 4.5)", font_size=10, color=THEME["curve"]).next_to(dot_peak, UP, buff=0.08)

        # Rama 3: x in [2.5, 4.8], y = -x + 7
        branch3 = axes.plot(lambda x: -x + 7, x_range=[2.5, 4.8], color=THEME["curve"], stroke_width=2.5)

        # Línea de salto punteada entre (2, -1) y (2, 3)
        jump_line = DashedLine(axes.c2p(2.0, -1.0), axes.c2p(2.0, 3.0), color=THEME["statement_box"], stroke_width=1.8)
        lbl_jump = Text("Salto", font_size=9, color=THEME["statement_box"]).next_to(jump_line, RIGHT, buff=0.08)

        graph_title = Text("Gráfica de f(x) en Ítem 5", font_size=13, color=THEME["header_color"]).next_to(axes, UP, buff=0.15)

        # Transición hacia el paso 6
        self.play(
            FadeOut(self.active_box),
            FadeOut(self.active_math, shift=DOWN * 0.2),
            FadeOut(self.active_just, shift=DOWN * 0.2),
            FadeIn(left_grp, shift=DOWN * 0.2),
            Create(axes),
            Write(axes_labels),
            Write(graph_title),
            *prog_anims,
            run_time=1.8
        )
        self.active_box = None
        self.active_math = None
        self.active_just = None

        self.play(
            Create(branch1),
            FadeIn(dot_closed),
            run_time=1.2
        )
        self.play(
            Create(jump_line),
            Write(lbl_jump),
            FadeIn(dot_open),
            run_time=1.0
        )
        self.play(
            Create(branch2),
            FadeIn(dot_peak),
            Write(lbl_peak),
            Create(branch3),
            run_time=1.4
        )
        self.wait(5.5)

        # Cierre suave
        extra_mobs = [
            left_grp, axes, axes_labels, graph_title,
            branch1, dot_closed, jump_line, lbl_jump, dot_open,
            branch2, dot_peak, lbl_peak, branch3
        ]
        self.finish_exercise(extra_mobjects=extra_mobs)
        self.wait(0.5)
