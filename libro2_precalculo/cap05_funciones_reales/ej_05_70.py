"""
Ejercicio 5.70 - Precálculo 2 (Colección Yachay Tech / Editorial Amarun)
Capítulo 5: Funciones Reales
Tema: Ecuación e inecuación con producto de funciones logarítmicas:
      f(x) = ln(5x - 3) · ln(2x + 3).
      1. Dominio y definición formal de f.
      2. f(x) = 0, x ∈ ℝ.
      3. f(x) > 0, x ∈ ℝ.

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica y rigurosa en 6 pasos.
"""

from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME


class Ejercicio05_70(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.70",
            topic="Producto de Logaritmos: Dominio, Raíz e Inecuación"
        )

        # 2. Enunciado institucional permanente (y = 2.5)
        self.setup_statement(
            desc_text="Dada la fórmula f(x) = ln(5x - 3) · ln(2x + 3):",
            math_tex=r"1.\; \text{Definir } f; \qquad 2.\; \text{Resolver } f(x) = 0, \; x \in \mathbb{R}; \qquad 3.\; \text{Resolver } f(x) > 0, \; x \in \mathbb{R}.",
            desc_font_size=13,
            math_font_size=12,
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (6 pasos)
        self.setup_progress_bar([
            "1/6: Dominio y Definición Formal",
            "2/6: Resolución de la Ecuación f(x) = 0",
            "3/6: Análisis de Signos de Factores",
            "4/6: Inecuación f(x) > 0",
            "5/6: Comportamiento y Asíntota",
            "6/6: Esquema Gráfico y Síntesis"
        ])

        # ==========================================================
        # PASO 1: Dominio y Definición Formal de f
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Régimen Máximo de Definición (RMD):} \\[4pt]"
            r"&f(x) = \ln(5x - 3) \cdot \ln(2x + 3) \\[4pt]"
            r"&\text{Existencia del logaritmo natural exige argumentos positivos:} \\[3pt]"
            r"&\bullet\; 5x - 3 > 0 \iff 5x > 3 \iff \mathbf{x > 3/5 = 0.6} \\[4pt]"
            r"&\bullet\; 2x + 3 > 0 \iff 2x > -3 \iff \mathbf{x > -3/2 = -1.5} \\[5pt]"
            r"&\operatorname{Dom}(f) = \left]\tfrac{3}{5}, +\infty\right[ \cap \left]-\tfrac{3}{2}, +\infty\right[ = \mathbf{\left]\tfrac{3}{5}, +\infty\right[} \\[5pt]"
            r"&\mathbf{f:} \; \left]\tfrac{3}{5}, +\infty\right[ \to \mathbb{R}, \quad f(x) = \ln(5x - 3) \cdot \ln(2x + 3)"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Dominio y Definición:\n"
            "• Ambos logaritmos exigen argumento positivo.\n"
            "• 5x - 3 > 0 ⟺ x > 3/5.\n"
            "• 2x + 3 > 0 ⟺ x > -3/2.\n"
            "• La intersección es el intervalo abierto ]3/5, +∞[.\n"
            "• Para x ≤ 3/5 la función no está definida en ℝ."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Resolución de la Ecuación f(x) = 0
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Resolución de la Ecuación } f(x) = 0: \\[4pt]"
            r"&\ln(5x - 3) \cdot \ln(2x + 3) = 0 \iff \ln(5x - 3) = 0 \;\lor\; \ln(2x + 3) = 0 \\[5pt]"
            r"&\bullet\; \ln(5x - 3) = 0 \iff 5x - 3 = 1 \iff 5x = 4 \iff \mathbf{x = 4/5 = 0.8} \\[3pt]"
            r"&\quad \text{Verificación: } \tfrac{4}{5} > \tfrac{3}{5} \implies \mathbf{4/5 \in \operatorname{Dom}(f)} \quad (\textbf{Solución válida}) \\[5pt]"
            r"&\bullet\; \ln(2x + 3) = 0 \iff 2x + 3 = 1 \iff 2x = -2 \iff \mathbf{x = -1} \\[3pt]"
            r"&\quad \text{Verificación: } -1 \notin \left]\tfrac{3}{5}, +\infty\right[ \implies x = -1 \text{ \textbf{es RAÍZ EXTRAÑA}} \\[5pt]"
            r"&\textbf{Conjunto Solución:} \quad \mathbf{CS_1 = \{4/5\}} \quad (\text{Única raíz real})"
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Ecuación f(x) = 0:\n"
            "• Un producto se anula si algún factor es cero.\n"
            "• ln(5x-3)=0 ⟹ 5x-3=1 ⟹ x=4/5 (pertenece al dominio).\n"
            "• ln(2x+3)=0 ⟹ 2x+3=1 ⟹ x=-1.\n"
            "• ¡Cuidado! x = -1 queda fuera de ]3/5, +∞[.\n"
            "  En x=-1, 5x-3 = -8 < 0 (no existe en ℝ).\n"
            "• Conclusión: CS₁ = {4/5}."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=5.0)

        # ==========================================================
        # PASO 3: Análisis de Signos de los Factores
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Signos de Factores en } \operatorname{Dom}(f) = \left]\tfrac{3}{5}, +\infty\right[: \\[4pt]"
            r"&\bullet\; \textbf{Factor 1: } \ln(5x - 3) \\[3pt]"
            r"&\quad \text{Para } x \in \left]\tfrac{3}{5}, \tfrac{4}{5}\right[: \; 0 < 5x - 3 < 1 \implies \mathbf{\ln(5x - 3) < 0} \\[3pt]"
            r"&\quad \text{Para } x \in \left]\tfrac{4}{5}, +\infty\right[: \; 5x - 3 > 1 \implies \mathbf{\ln(5x - 3) > 0} \\[5pt]"
            r"&\bullet\; \textbf{Factor 2: } \ln(2x + 3) \\[3pt]"
            r"&\quad \text{Para todo } x > \tfrac{3}{5}: \quad 2x + 3 > 2\left(\tfrac{3}{5}\right) + 3 = \tfrac{21}{5} = 4.2 > 1 \\[3pt]"
            r"&\quad \implies \mathbf{\ln(2x + 3) > 0} \quad (\textbf{Estrictamente positivo en TODO el dominio})"
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Signos de Factores:\n"
            "• ln(u) > 0 si u > 1; ln(u) < 0 si 0 < u < 1.\n"
            "• El factor ln(5x-3) cambia de signo en x = 4/5.\n"
            "• El factor ln(2x+3) tiene argumento 2x+3 > 4.2 > 1\n"
            "  en TODO el dominio ]3/5, +∞[.\n"
            "• ln(2x+3) es siempre positivo y no altera el signo."
        )

        self.morph_step(eq3, just3, box_color=THEME["success"], advance_to_step=2, wait_time=5.0)

        # ==========================================================
        # PASO 4: Inecuación f(x) > 0
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Resolución de la Inecuación } f(x) > 0: \\[4pt]"
            r"&\ln(5x - 3) \cdot \ln(2x + 3) > 0 \\[4pt]"
            r"&\text{Como } \ln(2x + 3) > 0 \quad (\forall x \in \operatorname{Dom}(f)): \\[4pt]"
            r"&\ln(5x - 3) \cdot \underbrace{\ln(2x + 3)}_{> 0} > 0 \iff \mathbf{\ln(5x - 3) > 0} \\[5pt]"
            r"&\iff 5x - 3 > 1 \iff 5x > 4 \iff \mathbf{x > 4/5} \\[5pt]"
            r"&\textbf{Conjunto Solución de la Inecuación:} \\[3pt]"
            r"&\mathbf{CS_2 = \left]\frac{4}{5}, +\infty\right[ = ]0.8, +\infty[}"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Inecuación f(x) > 0:\n"
            "• Un producto de dos factores es positivo si\n"
            "  ambos tienen el mismo signo (+)(+) o (-)(-).\n"
            "• Como el segundo factor es permanentemente positivo,\n"
            "  la desigualdad reduce a: ln(5x - 3) > 0.\n"
            "• 5x - 3 > 1 ⟺ x > 4/5.\n"
            "• CS₂ = ]4/5, +∞[."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=5.0)

        # ==========================================================
        # PASO 5: Comportamiento Asintótico y Monotonía
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Análisis Asintótico y Crecimiento:} \\[4pt]"
            r"&\bullet\; \text{Asíntota vertical en la frontera } x = 3/5: \\[3pt]"
            r"&\quad \lim_{x \to (3/5)^+} (5x - 3) = 0^+ \implies \lim_{x \to (3/5)^+} \ln(5x - 3) = -\infty \\[3pt]"
            r"&\quad \lim_{x \to (3/5)^+} \ln(2x + 3) = \ln(21/5) \approx 1.435 > 0 \\[3pt]"
            r"&\quad \implies \mathbf{\lim_{x \to (3/5)^+} f(x) = -\infty} \quad (\textbf{Asíntota vertical } x = 3/5) \\[5pt]"
            r"&\bullet\; \text{Comportamiento en el infinito:} \\[3pt]"
            r"&\quad \lim_{x \to +\infty} \ln(5x - 3) = +\infty, \quad \lim_{x \to +\infty} \ln(2x + 3) = +\infty \\[3pt]"
            r"&\quad \implies \mathbf{\lim_{x \to +\infty} f(x) = +\infty} \quad (\textbf{Estricto crecimiento})"
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Comportamiento y Asíntota:\n"
            "• Al acercarse a x = 3/5 por la derecha, el primer\n"
            "  logaritmo tiende a -∞ mientras el segundo es ~1.43.\n"
            "• Por ende, la curva cae a -∞ en la asíntota vertical x = 0.6.\n"
            "• Cuando x crece, ambos logaritmos son crecientes y\n"
            "  positivos, enviando la función a +∞.\n"
            "• Cruza el eje X exactamente en x = 0.8."
        )

        self.morph_step(eq5, just5, box_color=THEME["curve"], advance_to_step=4, wait_time=5.2)

        # ==========================================================
        # PASO 6: Síntesis Comparativa y Gráfica Cartesiana
        # ==========================================================
        # Panel izquierdo: Cuadro Síntesis
        t_title = Text("Síntesis Completa (Ej. 5.70)", font_size=13, color=THEME["header_color"], weight=BOLD)
        t_dom = MathTex(r"\operatorname{Dom}(f) = \left]\tfrac{3}{5}, +\infty\right[ \quad (x > 0.6)", font_size=11, color=THEME["highlight"])
        t_sol = MathTex(r"f(x) = 0 \iff \mathbf{CS_1 = \{4/5\}} \quad (x = 0.8)", font_size=11, color=THEME["success"])
        t_ineq = MathTex(r"f(x) > 0 \iff \mathbf{CS_2 = \left]\tfrac{4}{5}, +\infty\right[} \quad (x > 0.8)", font_size=11, color=THEME["secondary"])
        t_asym = MathTex(r"\text{Asíntota: } x = 3/5 = 0.6 \quad (f(x) \to -\infty)", font_size=11, color=THEME["curve"])

        table_grp = VGroup(t_title, t_dom, t_sol, t_ineq, t_asym).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        table_box = SurroundingRectangle(table_grp, color=THEME["statement_box"], buff=0.18, stroke_width=1.5, corner_radius=0.08)
        left_summary = VGroup(table_box, table_grp).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos para ilustrar f(x)
        axes, axes_labels = self.setup_axes(
            x_range=[-0.5, 3.5, 1],
            y_range=[-3.0, 4.0, 1],
            x_length=4.8,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True
        )
        graph_title = Text("Gráfica: f(x) = ln(5x - 3) · ln(2x + 3)", font_size=12, color=WHITE).next_to(axes, UP, buff=0.15)

        # Asíntota vertical: x = 0.6
        asym_v = DashedLine(
            start=axes.c2p(0.6, -3.0),
            end=axes.c2p(0.6, 4.0),
            color=THEME["statement_box"],
            stroke_width=1.4,
            dash_length=0.08
        )
        lbl_asym = MathTex(r"x = 0.6", font_size=9, color=THEME["statement_box"]).move_to(axes.c2p(0.95, -2.5))

        # Curva de f(x) para x ∈ [0.63, 3.2]
        curve_f = axes.plot(
            lambda x: np.log(5.0 * x - 3.0) * np.log(2.0 * x + 3.0),
            x_range=[0.63, 3.2],
            color=THEME["curve"],
            stroke_width=2.6
        )

        # Cero real de la función: (0.8, 0)
        dot_root = Dot(axes.c2p(0.8, 0.0), color=THEME["success"], radius=0.065)
        lbl_root = MathTex(r"(0.8, 0)", font_size=10, color=THEME["success"]).next_to(dot_root, DOWN + RIGHT, buff=0.08)

        # Región solución f(x) > 0 destacada sobre el eje X: [0.8, 3.4]
        line_sol = Line(
            start=axes.c2p(0.8, 0),
            end=axes.c2p(3.4, 0),
            color=THEME["secondary"],
            stroke_width=4.0
        )
        lbl_pos = Text("f(x) > 0", font_size=10, color=THEME["secondary"]).move_to(axes.c2p(2.2, 0.4))

        prog_anims = self.get_advance_progress_anims(5)

        self.play(
            FadeOut(self.active_math),
            FadeOut(self.active_just),
            FadeOut(self.active_box),
            FadeIn(left_summary),
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
            Create(asym_v),
            Write(lbl_asym),
            Create(curve_f),
            run_time=1.4
        )
        self.play(
            FadeIn(dot_root),
            Write(lbl_root),
            Create(line_sol),
            Write(lbl_pos),
            run_time=1.4
        )
        self.wait(6.0)

        # Cierre suave
        extra_mobs = [
            left_summary, axes, axes_labels, graph_title,
            asym_v, lbl_asym, curve_f, dot_root, lbl_root, line_sol, lbl_pos
        ]
        self.finish_exercise(extra_mobjects=extra_mobs)
        self.wait(0.5)
