"""
Ejercicio 5.60 - Precálculo 2 (Colección Yachay Tech / Editorial Amarun)
Capítulo 5: Funciones Reales
Tema: Definición formal, rango, sobreyectividad, monotonía y gráfica
      de fórmulas logarítmicas, racionales y de valor absoluto:
      1. F₁(t) = log₂(t⁸ - 2t⁴ + 1)
      2. F₂(t) = log_{1/2}(t⁸ - 2t⁴ + 1)
      3. F₃(t) = t + 1/t
      4. F₄(t) = t / (1 + |t|)

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


class Ejercicio05_60(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.60",
            topic="Análisis Completo de Fórmulas Reales"
        )

        # 2. Enunciado institucional permanente (y = 2.5)
        self.setup_statement(
            desc_text="Para cada fórmula F(t): 1. Definir F; 2. Graficar F; 3. Hallar Rg(F) y sobreyectividad; 4. Monotonía:",
            math_tex=r"F_1(t) = \log_2(t^8 - 2t^4 + 1), \quad F_2(t) = \log_{1/2}(t^8 - 2t^4 + 1), \quad F_3(t) = t + \tfrac{1}{t}, \quad F_4(t) = \tfrac{t}{1+|t|}.",
            desc_font_size=12,
            math_font_size=11,
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (6 pasos)
        self.setup_progress_bar([
            "1/6: Definición de Fórmulas Logarítmicas",
            "2/6: Definición de Racional y Modular",
            "3/6: Rango y Sobreyectividad de F₁ y F₂",
            "4/6: Rango y Sobreyectividad de F₃ y F₄",
            "5/6: Monotonía Analítica de las 4 Fórmulas",
            "6/6: Síntesis y Esquema Gráfico Comparativo"
        ])

        # ==========================================================
        # PASO 1: Definición de Fórmulas Logarítmicas (F₁ y F₂)
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Fórmulas Logarítmicas } F_1(t) \text{ y } F_2(t): \\[3pt]"
            r"&t^8 - 2t^4 + 1 = (t^4 - 1)^2 = (t-1)^2(t+1)^2(t^2+1)^2 \\[4pt]"
            r"&\operatorname{RMD}: (t^4 - 1)^2 > 0 \iff t^4 \neq 1 \iff t \notin \{-1, 1\} \\[4pt]"
            r"&\mathbf{F_1:} \; \mathbb{R} \setminus \{-1, 1\} \to \mathbb{R}, \quad F_1(t) = \log_2\left((t^4 - 1)^2\right) \\[4pt]"
            r"&\mathbf{F_2:} \; \mathbb{R} \setminus \{-1, 1\} \to \mathbb{R}, \quad F_2(t) = \log_{1/2}\left((t^4 - 1)^2\right) \\[4pt]"
            r"&\text{Relación fundamental: } \log_{1/2}(u) = -\log_2(u) \implies \mathbf{F_2(t) = -F_1(t)}"
            r"\end{aligned}",
            font_size=16,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Definición de F₁ y F₂:\n"
            "• El trinomio es un cuadrado perfecto: (t⁴-1)².\n"
            "• El argumento del logaritmo debe ser positivo:\n"
            "  (t⁴ - 1)² > 0 ⟺ t⁴ ≠ 1 ⟺ t ∉ {-1, 1}.\n"
            "• Dom(F₁) = Dom(F₂) = ℝ \\ {-1, 1}.\n"
            "• Propiedad: log_{1/2}(u) = -log₂(u).\n"
            "• F₂ es el reflejo vertical exacto de F₁."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.6)

        # ==========================================================
        # PASO 2: Definición de Fórmulas Racional y Modular (F₃ y F₄)
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Fórmulas Racional y Modular } F_3(t) \text{ y } F_4(t): \\[4pt]"
            r"&\bullet\; F_3(t) = t + \frac{1}{t}: \quad \text{Restricción: } t \neq 0 \\[3pt]"
            r"&\quad \mathbf{F_3:} \; \mathbb{R} \setminus \{0\} \to \mathbb{R}, \quad F_3(t) = t + \frac{1}{t} \\[5pt]"
            r"&\bullet\; F_4(t) = \frac{t}{1 + |t|}: \quad 1 + |t| \ge 1 > 0 \quad (\forall t \in \mathbb{R}) \\[3pt]"
            r"&\quad \text{Sin ceros en el denominador} \implies \operatorname{RMD} = \mathbb{R} \\[3pt]"
            r"&\quad \mathbf{F_4:} \; \mathbb{R} \to \mathbb{R}, \quad F_4(t) = \frac{t}{1 + |t|} \\[4pt]"
            r"&\text{Simetría: } F_3(-t) = -F_3(t), \; F_4(-t) = -F_4(t) \quad (\textbf{Impares})"
            r"\end{aligned}",
            font_size=16,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Definición de F₃ y F₄:\n"
            "• Para F₃(t) = t + 1/t, la división exige t ≠ 0.\n"
            "  Por ende, Dom(F₃) = ℝ* = ℝ \\ {0}.\n"
            "• Para F₄(t) = t/(1+|t|), el divisor 1+|t| ≥ 1\n"
            "  nunca se anula en ℝ. Dom(F₄) = ℝ completo.\n"
            "• Ambas fórmulas satisfacen F(-t) = -F(t),\n"
            "  siendo funciones impares (simetría central)."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Rango y Sobreyectividad de F₁ y F₂
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Rango y Sobreyectividad de } F_1 \text{ y } F_2: \\[4pt]"
            r"&\text{Sea } u(t) = (t^4 - 1)^2. \quad \text{Cuando } |t| \to 1, \; u \to 0^+. \\[3pt]"
            r"&\text{Cuando } |t| \to \infty, \; u \to +\infty. \implies u(\mathbb{R}\setminus\{\pm 1\}) = ]0, +\infty[ \\[5pt]"
            r"&\operatorname{Rg}(F_1) = \log_2(]0, +\infty[) = ]-\infty, +\infty[ = \mathbf{\mathbb{R}} \\[4pt]"
            r"&\operatorname{Rg}(F_2) = -\operatorname{Rg}(F_1) = \mathbf{\mathbb{R}} \\[5pt]"
            r"&\textbf{Conclusión:}\; \operatorname{Rg}(F_1) = \operatorname{Rg}(F_2) = \operatorname{Cod}(F) = \mathbb{R} \\[4pt]"
            r"&\implies \textbf{F}_1 \text{ y } \textbf{F}_2 \text{ son \textbf{SOBREYECTIVAS} en } \mathbb{R}"
            r"\end{aligned}",
            font_size=16,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Rango de F₁ y F₂:\n"
            "• El argumento (t⁴-1)² toma todo valor en ]0, +∞[.\n"
            "• La imagen de ]0, +∞[ bajo log₂ y log_{1/2}\n"
            "  es todo el conjunto de los números reales ℝ.\n"
            "• Al coincidir el rango con el codominio ℝ:\n"
            "  Rg(F₁) = ℝ = Cod(F₁) ⟹ Sobreyectiva.\n"
            "  Rg(F₂) = ℝ = Cod(F₂) ⟹ Sobreyectiva."
        )

        self.morph_step(eq3, just3, box_color=THEME["success"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Rango y Sobreyectividad de F₃ y F₄
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Rango y Sobreyectividad de } F_3 \text{ y } F_4: \\[4pt]"
            r"&\bullet\; F_3(t) = y \iff t^2 - yt + 1 = 0 \quad (\text{con } t \in \mathbb{R}^*) \\[3pt]"
            r"&\quad \Delta = y^2 - 4 \ge 0 \iff |y| \ge 2 \\[3pt]"
            r"&\quad \mathbf{\operatorname{Rg}(F_3) = ]-\infty, -2] \cup [2, +\infty[ \subsetneq \mathbb{R}} \implies \textbf{NO sobreyectiva} \\[5pt]"
            r"&\bullet\; F_4(t) = \frac{t}{1 + |t|}: \quad |F_4(t)| = \frac{|t|}{1+|t|} < 1 \quad (\forall t \in \mathbb{R}) \\[3pt]"
            r"&\quad \lim_{t \to \pm \infty} F_4(t) = \pm 1 \implies \mathbf{\operatorname{Rg}(F_4) = ]-1, 1[ \subsetneq \mathbb{R}} \\[4pt]"
            r"&\implies \textbf{F}_4 \text{ \textbf{NO es sobreyectiva} sobre } \mathbb{R} \quad (\text{acotada})"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Rango de F₃ y F₄:\n"
            "• Para F₃: t + 1/t = y tiene raíces reales ssi\n"
            "  discriminante Δ = y² - 4 ≥ 0 ⟺ |y| ≥ 2.\n"
            "  El intervalo ]-2, 2[ se omite. NO sobreyectiva.\n"
            "• Para F₄: el valor absoluto |t| < 1+|t| implica\n"
            "  |F₄(t)| < 1 en todo su dominio.\n"
            "  Rg(F₄) = ]-1, 1[ ≠ ℝ. NO sobreyectiva."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=5.0)

        # ==========================================================
        # PASO 5: Monotonía Analítica de las 4 Fórmulas
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Análisis Riguroso de Monotonía:} \\[4pt]"
            r"&\bullet\; \mathbf{F_1}: \; \text{Decrece en } ]-\infty, -1[ \text{ y } ]0, 1[; \text{ Crece en } ]-1, 0[ \text{ y } ]1, \infty[ \\[3pt]"
            r"&\bullet\; \mathbf{F_2}: \; \text{Opuesta a } F_1 \text{ (Crece en } ]-\infty, -1[\cup]0, 1[; \text{ Decrece en el resto)} \\[4pt]"
            r"&\bullet\; \mathbf{F_3}: \; \text{Para } 0 < t_1 < t_2 \le 1 \implies F_3(t_2) < F_3(t_1) \quad (\textbf{Decreciente}) \\[3pt]"
            r"&\quad \text{Crece en } ]-\infty, -1] \text{ y } [1, +\infty[; \text{ Decrece en } [-1, 0[ \text{ y } ]0, 1] \\[4pt]"
            r"&\bullet\; \mathbf{F_4}: \; t \ge 0 \implies F_4(t) = 1 - \frac{1}{1+t} \quad (\text{estrictamente creciente}) \\[3pt]"
            r"&\quad t < 0 \implies F_4(t) = -1 + \frac{1}{1-t} \quad (\text{estrictamente creciente}) \\[3pt]"
            r"&\quad \implies \textbf{F}_4 \text{ es \textbf{ESTRICTAMENTE CRECIENTE} en todo } \mathbb{R}"
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Monotonía Analítica:\n"
            "• F₁ y F₂ cambian de sentido en las raíces de\n"
            "  la derivada interna t = 0 y asíntotas t = ±1.\n"
            "• F₃ tiene extremos locales en t = 1 (mínimo y=2)\n"
            "  y en t = -1 (máximo local y=-2).\n"
            "• F₄ mantiene tasa de cambio positiva globalmente:\n"
            "  t₁ < t₂ ⟹ F₄(t₁) < F₄(t₂).\n"
            "  Es la única estrictamente creciente en todo ℝ."
        )

        self.morph_step(eq5, just5, box_color=THEME["curve"], advance_to_step=4, wait_time=5.2)

        # ==========================================================
        # PASO 6: Síntesis Comparativa y Esquema Gráfico
        # ==========================================================
        # Panel izquierdo: Cuadro sinóptico de las 4 fórmulas
        t_title = Text("Síntesis Comparativa (Ej. 5.60)", font_size=13, color=THEME["header_color"], weight=BOLD)
        t_f1 = MathTex(r"\mathbf{F_1:} \; \operatorname{Dom} = \mathbb{R}\setminus\{\pm 1\}, \; \operatorname{Rg} = \mathbb{R} \quad (\text{Sobreyectiva, Par})", font_size=11, color=THEME["highlight"])
        t_f2 = MathTex(r"\mathbf{F_2:} \; \operatorname{Dom} = \mathbb{R}\setminus\{\pm 1\}, \; \operatorname{Rg} = \mathbb{R} \quad (\text{Sobreyectiva, } F_2=-F_1)", font_size=11, color=THEME["highlight"])
        t_f3 = MathTex(r"\mathbf{F_3:} \; \operatorname{Dom} = \mathbb{R}^*, \; \operatorname{Rg} = \mathbb{R}\setminus]-2, 2[ \quad (\text{No Sobre, Extremos})", font_size=11, color=THEME["curve"])
        t_f4 = MathTex(r"\mathbf{F_4:} \; \operatorname{Dom} = \mathbb{R}, \; \operatorname{Rg} = ]-1, 1[ \quad (\text{No Sobre, Estr. Creciente})", font_size=11, color=THEME["secondary"])

        table_grp = VGroup(t_title, t_f1, t_f2, t_f3, t_f4).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        table_box = SurroundingRectangle(table_grp, color=THEME["statement_box"], buff=0.18, stroke_width=1.5, corner_radius=0.08)
        left_summary = VGroup(table_box, table_grp).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos para ilustrar las curvas F₃ y F₄
        axes, axes_labels = self.setup_axes(
            x_range=[-4.0, 4.0, 1],
            y_range=[-3.5, 3.5, 1],
            x_length=4.8,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True
        )
        graph_title = Text("Esquema Gráfico: F₃(t) y F₄(t)", font_size=12, color=WHITE).next_to(axes, UP, buff=0.15)

        # Asíntota oblicua de F₃: y = t
        asym_diag = DashedLine(
            start=axes.c2p(-3.2, -3.2),
            end=axes.c2p(3.2, 3.2),
            color=GRAY,
            stroke_width=1.2,
            dash_length=0.08
        )

        # Asíntotas horizontales de F₄: y = 1, y = -1
        asym_h1 = DashedLine(start=axes.c2p(-3.8, 1.0), end=axes.c2p(3.8, 1.0), color=THEME["secondary"], stroke_width=1.0, dash_length=0.08)
        asym_h2 = DashedLine(start=axes.c2p(-3.8, -1.0), end=axes.c2p(3.8, -1.0), color=THEME["secondary"], stroke_width=1.0, dash_length=0.08)

        # Curva F₃(t) = t + 1/t (dos ramas)
        f3_pos = axes.plot(lambda t: t + 1.0 / t, x_range=[0.32, 3.5], color=THEME["curve"], stroke_width=2.2)
        f3_neg = axes.plot(lambda t: t + 1.0 / t, x_range=[-3.5, -0.32], color=THEME["curve"], stroke_width=2.2)

        # Curva F₄(t) = t / (1 + |t|)
        f4_curve = axes.plot(lambda t: t / (1.0 + abs(t)), x_range=[-3.8, 3.8], color=THEME["secondary"], stroke_width=2.5)

        # Puntos críticos de F₃
        dot_min = Dot(axes.c2p(1, 2), color=THEME["success"], radius=0.06)
        lbl_min = MathTex(r"(1, 2)", font_size=10, color=THEME["success"]).next_to(dot_min, UP, buff=0.08)

        dot_max = Dot(axes.c2p(-1, -2), color=THEME["highlight"], radius=0.06)
        lbl_max = MathTex(r"(-1, -2)", font_size=10, color=THEME["highlight"]).next_to(dot_max, DOWN, buff=0.08)

        # Leyenda de curvas
        leg_f3 = MathTex(r"F_3(t) = t + \tfrac{1}{t}", font_size=10, color=THEME["curve"]).move_to(axes.c2p(2.2, -2.5))
        leg_f4 = MathTex(r"F_4(t) = \tfrac{t}{1+|t|}", font_size=10, color=THEME["secondary"]).move_to(axes.c2p(-2.2, 2.5))

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
            Create(asym_diag),
            Create(asym_h1),
            Create(asym_h2),
            run_time=1.0
        )
        self.play(
            Create(f3_pos),
            Create(f3_neg),
            Create(f4_curve),
            FadeIn(dot_min),
            Write(lbl_min),
            FadeIn(dot_max),
            Write(lbl_max),
            Write(leg_f3),
            Write(leg_f4),
            run_time=1.8
        )
        self.wait(6.0)

        # Cierre suave
        extra_mobs = [
            left_summary, axes, axes_labels, graph_title,
            asym_diag, asym_h1, asym_h2, f3_pos, f3_neg, f4_curve,
            dot_min, lbl_min, dot_max, lbl_max, leg_f3, leg_f4
        ]
        self.finish_exercise(extra_mobjects=extra_mobs)
        self.wait(0.5)
