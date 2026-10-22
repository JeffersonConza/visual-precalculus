"""
Ejercicio 5.68 - Precálculo 2 (Colección Yachay Tech / Editorial Amarun)
Capítulo 5: Funciones Reales
Tema: Ecuación e inecuaciones con funciones doblemente logarítmicas:
      f(x) = log_α(log_β(5ax² - 3bx)), con 20aβ^{1/α} + 9b² > 0.
      1. f(x) + 1 = 0, x ∈ ℝ
      2. f(x) + 1 > 0, x ∈ ℝ (a > 0)
      3. f(x) + 1 ≤ 0, x ∈ ℝ (a < 0)

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


class Ejercicio05_68(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.68",
            topic="Ecuaciones e Inecuaciones Doblemente Logarítmicas"
        )

        # 2. Enunciado institucional permanente (y = 2.5)
        self.setup_statement(
            desc_text="Sean α, β > 0 (≠1), a, b ∈ ℝ (a ≠ 0) con 20aβ^{1/α} + 9b² > 0. Para f(x) = log_α(log_β(5ax² - 3bx)):",
            math_tex=r"1.\; f(x) + 1 = 0; \qquad 2.\; f(x) + 1 > 0 \;\; (a > 0); \qquad 3.\; f(x) + 1 \le 0 \;\; (a < 0).",
            desc_font_size=12,
            math_font_size=12,
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (6 pasos)
        self.setup_progress_bar([
            "1/6: Estructura y Dominio de f(x)",
            "2/6: Resolución de la Ecuación f(x)+1=0",
            "3/6: Inecuación con a > 0 (f(x)+1 > 0)",
            "4/6: Inecuación con a < 0 (f(x)+1 ≤ 0)",
            "5/6: Análisis de Bases e Inversión",
            "6/6: Esquema Gráfico y Síntesis"
        ])

        # ==========================================================
        # PASO 1: Estructura de la Función y Dominio
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Estructura y Régimen Máximo de Definición:} \\[4pt]"
            r"&f(x) = \log_\alpha\left(\log_\beta(5ax^2 - 3bx)\right), \quad u(x) = 5ax^2 - 3bx \\[4pt]"
            r"&\text{Condiciones simultáneas de existencia del logaritmo:} \\[3pt]"
            r"&\bullet\; u(x) = 5ax^2 - 3bx > 0 \quad (\text{argumento de } \log_\beta) \\[4pt]"
            r"&\bullet\; \log_\beta(u(x)) > 0 \quad (\text{argumento de } \log_\alpha) \\[5pt]"
            r"&\text{Para bases canónicas } \alpha, \beta > 1: \quad \log_\beta(u(x)) > 0 \iff \mathbf{u(x) > 1} \\[4pt]"
            r"&\text{Hipótesis clave del problema: } \mathbf{\Delta = 9b^2 + 20a\beta^{1/\alpha} > 0}"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Estructura y Dominio:\n"
            "• Función compuesta por dos logaritmos sucesivos.\n"
            "• El argumento interno u(x) debe ser estrictamente\n"
            "  positivo, y a su vez log_β(u(x)) > 0.\n"
            "• Con bases mayores que 1, esto equivale a u(x) > 1.\n"
            "• La condición dada 20aβ^{1/α} + 9b² > 0 será\n"
            "  exactamente el discriminante del trinomio."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Resolución de la Ecuación f(x) + 1 = 0
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Resolución de la Ecuación } f(x) + 1 = 0: \\[4pt]"
            r"&f(x) = -1 \iff \log_\alpha\left(\log_\beta(5ax^2 - 3bx)\right) = -1 \\[4pt]"
            r"&\iff \log_\beta(5ax^2 - 3bx) = \alpha^{-1} = \frac{1}{\alpha} \\[4pt]"
            r"&\iff 5ax^2 - 3bx = \beta^{1/\alpha} \iff \mathbf{5ax^2 - 3bx - \beta^{1/\alpha} = 0} \\[5pt]"
            r"&\text{Discriminante: } \mathbf{\Delta = (-3b)^2 - 4(5a)(-\beta^{1/\alpha}) = 9b^2 + 20a\beta^{1/\alpha} > 0} \\[5pt]"
            r"&\textbf{Conjunto Solución:} \quad \mathbf{CS_1 = \{x_1, x_2\}} \\[3pt]"
            r"&x_{1, 2} = \frac{3b \pm \sqrt{9b^2 + 20a\beta^{1/\alpha}}}{10a} \quad (\text{Dos raíces reales distintas})"
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Ecuación f(x) + 1 = 0:\n"
            "• Despejamos el primer logaritmo: log_β(u) = 1/α.\n"
            "• Aplicando la base β: u = β^{1/α}.\n"
            "• Obtenemos la ecuación cuadrática estándar:\n"
            "  5ax² - 3bx - β^{1/α} = 0.\n"
            "• El discriminante Δ coincide con la hipótesis\n"
            "  y es estrictamente positivo: existen 2 raíces."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=5.0)

        # ==========================================================
        # PASO 3: Inecuación f(x) + 1 > 0 con a > 0
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Inecuación } f(x) + 1 > 0 \text{ con } a > 0 \;\; (\alpha, \beta > 1): \\[4pt]"
            r"&f(x) > -1 \iff \log_\alpha(\log_\beta(u(x))) > -1 \\[4pt]"
            r"&\text{Como } \alpha > 1 \implies \log_\beta(u(x)) > \frac{1}{\alpha} \\[4pt]"
            r"&\text{Como } \beta > 1 \implies u(x) > \beta^{1/\alpha} \iff \mathbf{5ax^2 - 3bx - \beta^{1/\alpha} > 0} \\[5pt]"
            r"&\text{Dado que } a > 0, \text{ la parábola } P(x) = 5ax^2 - 3bx - \beta^{1/\alpha} \text{ es convexa} \\[3pt]"
            r"&\text{y toma valores estrictamente positivos en el exterior de sus raíces:} \\[4pt]"
            r"&\mathbf{CS_2 = ]-\infty, x_1[ \;\cup\; ]x_2, +\infty[} \quad (x_1 < x_2)"
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Inecuación con a > 0:\n"
            "• Para α, β > 1, las funciones logarítmicas son\n"
            "  estrictamente crecientes y conservan la desigualdad:\n"
            "  f(x) > -1 ⟺ 5ax² - 3bx - β^{1/α} > 0.\n"
            "• Como a > 0, la parábola abre hacia arriba.\n"
            "• Es positiva en las ramas exteriores a las raíces:\n"
            "  CS₂ = ]-∞, x₁[ ∪ ]x₂, +∞[."
        )

        self.morph_step(eq3, just3, box_color=THEME["success"], advance_to_step=2, wait_time=5.0)

        # ==========================================================
        # PASO 4: Inecuación f(x) + 1 ≤ 0 con a < 0
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Inecuación } f(x) + 1 \le 0 \text{ con } a < 0 \;\; (\alpha, \beta > 1): \\[4pt]"
            r"&f(x) \le -1 \iff 0 < \log_\beta(u(x)) \le \frac{1}{\alpha} \quad (\text{exigencia de dominio}) \\[4pt]"
            r"&\iff 1 < 5ax^2 - 3bx \le \beta^{1/\alpha} \\[5pt]"
            r"&\bullet\; \text{Cota superior: } 5ax^2 - 3bx - \beta^{1/\alpha} \le 0 \\[3pt]"
            r"&\quad \text{Como } a < 0, \text{ la parábola abre hacia abajo } (\text{cóncava}), \\[3pt]"
            r"&\quad \text{por lo que es } \le 0 \text{ en el exterior: } x \in ]-\infty, x_1] \cup [x_2, +\infty[ \\[4pt]"
            r"&\bullet\; \text{Acotado internamente por la condición de existencia } 5ax^2 - 3bx > 1"
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Inecuación con a < 0:\n"
            "• f(x) ≤ -1 exige mantener el dominio: log_β(u) > 0.\n"
            "  Por tanto: 1 < 5ax² - 3bx ≤ β^{1/α}.\n"
            "• Al ser a < 0, la parábola abre hacia abajo.\n"
            "• La condición ≤ β^{1/α} se cumple hacia afuera,\n"
            "  mientras que > 1 restringe las ramas a una franja\n"
            "  acotada de valores reales bien definidos."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=5.2)

        # ==========================================================
        # PASO 5: Análisis de Parámetros y Variación de Bases
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Análisis de Inversión por Bases en } ]0, 1[: \\[4pt]"
            r"&\bullet\; \text{Si } 0 < \alpha < 1: \quad \log_\alpha(v) \text{ es estrictamente decreciente} \\[3pt]"
            r"&\quad f(x) > -1 \iff \log_\beta(u(x)) < \frac{1}{\alpha} \quad (\text{invierte el orden}) \\[4pt]"
            r"&\bullet\; \text{Si } 0 < \beta < 1: \quad \log_\beta(u) \text{ es estrictamente decreciente} \\[3pt]"
            r"&\quad \text{invierte nuevamente el sentido de la desigualdad sobre } u(x). \\[5pt]"
            r"&\textbf{Invariante Fundamental:} \\[3pt]"
            r"&\text{Sin importar el orden de las bases, las fronteras críticas} \\[3pt]"
            r"&\text{del conjunto solución siempre son las raíces reales } \mathbf{x_1} \text{ y } \mathbf{x_2}."
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Dependencia de las Bases:\n"
            "• Si una base pertenece al intervalo ]0, 1[,\n"
            "  la función logarítmica es decreciente e invierte\n"
            "  el sentido de las desigualdades.\n"
            "• Si ambas bases están en ]0, 1[, la doble inversión\n"
            "  restaura la orientación original.\n"
            "• Los ceros y fronteras x₁ y x₂ permanecen idénticos."
        )

        self.morph_step(eq5, just5, box_color=THEME["curve"], advance_to_step=4, wait_time=5.0)

        # ==========================================================
        # PASO 6: Síntesis Analítica y Esquema Gráfico
        # ==========================================================
        # Panel izquierdo: Cuadro Síntesis
        t_title = Text("Síntesis de Soluciones (Ej. 5.68)", font_size=13, color=THEME["header_color"], weight=BOLD)
        t_delta = MathTex(r"\Delta = 9b^2 + 20a\beta^{1/\alpha} > 0 \quad (\text{Hipótesis})", font_size=11, color=THEME["highlight"])
        t_cs1 = MathTex(r"\mathbf{1.\;} f(x) + 1 = 0 \iff \mathbf{CS_1 = \{x_1, x_2\}}", font_size=11, color=THEME["success"])
        t_cs2 = MathTex(r"\mathbf{2.\;} a > 0 \implies \mathbf{CS_2 = ]-\infty, x_1[ \;\cup\; ]x_2, +\infty[}", font_size=11, color=THEME["secondary"])
        t_cs3 = MathTex(r"\mathbf{3.\;} a < 0 \implies \mathbf{P(x) \le \beta^{1/\alpha} \text{ (Ramas exteriores)}}", font_size=11, color=THEME["curve"])

        table_grp = VGroup(t_title, t_delta, t_cs1, t_cs2, t_cs3).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        table_box = SurroundingRectangle(table_grp, color=THEME["statement_box"], buff=0.18, stroke_width=1.5, corner_radius=0.08)
        left_summary = VGroup(table_box, table_grp).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos para ilustrar parábola y corte y = β^{1/α}
        axes, axes_labels = self.setup_axes(
            x_range=[-3.0, 3.0, 1],
            y_range=[-1.0, 4.0, 1],
            x_length=4.8,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True
        )
        graph_title = Text("Esquema Gráfico: Parábola u(x) y Corte", font_size=12, color=WHITE).next_to(axes, UP, buff=0.15)

        # Línea de nivel y = β^{1/α} (e.g. nivel = 1.5)
        lvl_y = 1.5
        line_beta = DashedLine(
            start=axes.c2p(-2.8, lvl_y),
            end=axes.c2p(2.8, lvl_y),
            color=THEME["highlight"],
            stroke_width=1.4,
            dash_length=0.08
        )
        lbl_beta = MathTex(r"y = \beta^{1/\alpha}", font_size=10, color=THEME["highlight"]).move_to(axes.c2p(-1.8, lvl_y + 0.3))

        # Parábola convexa (caso a > 0): u(x) = 5ax² - 3bx (con vértice bajo la línea)
        parabola = axes.plot(lambda x: 1.2 * x**2 - 0.3 * x, x_range=[-1.6, 1.8], color=THEME["curve"], stroke_width=2.5)

        # Puntos de corte x₁ y x₂ con y = β^{1/α}
        # 1.2 x² - 0.3 x = 1.5 ⟹ 1.2 x² - 0.3 x - 1.5 = 0 ⟹ x ≈ -1.0, x ≈ 1.25
        x1_val = -1.0
        x2_val = 1.25
        dot_x1 = Dot(axes.c2p(x1_val, lvl_y), color=THEME["success"], radius=0.06)
        lbl_x1 = MathTex(r"x_1", font_size=11, color=THEME["success"]).next_to(dot_x1, UP + LEFT, buff=0.06)

        dot_x2 = Dot(axes.c2p(x2_val, lvl_y), color=THEME["success"], radius=0.06)
        lbl_x2 = MathTex(r"x_2", font_size=11, color=THEME["success"]).next_to(dot_x2, UP + RIGHT, buff=0.06)

        leg_parab = MathTex(r"u(x) = 5ax^2 - 3bx", font_size=10, color=THEME["curve"]).move_to(axes.c2p(1.5, 0.4))

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
            Create(line_beta),
            Write(lbl_beta),
            Create(parabola),
            Write(leg_parab),
            run_time=1.4
        )
        self.play(
            FadeIn(dot_x1),
            Write(lbl_x1),
            FadeIn(dot_x2),
            Write(lbl_x2),
            run_time=1.2
        )
        self.wait(6.0)

        # Cierre suave
        extra_mobs = [
            left_summary, axes, axes_labels, graph_title,
            line_beta, lbl_beta, parabola, leg_parab,
            dot_x1, lbl_x1, dot_x2, lbl_x2
        ]
        self.finish_exercise(extra_mobjects=extra_mobs)
        self.wait(0.5)
