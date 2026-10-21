"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.56 (Página 114 del libro / Página 133 del PDF)

Halle la función asociada a la fórmula:
f(x) = ln(x⁴ + 5x³ - 13x² - 53x + 60).

Resolución analítica:
1. Condición de existencia en ℝ:
   P(x) = x⁴ + 5x³ - 13x² - 53x + 60 > 0.
2. Factorización por Ruffini (raíces racionales):
   P(1) = 0, P(3) = 0 ⟹ P(x) = (x - 1)(x - 3)(x² + 9x + 20)
   ⟹ P(x) = (x + 5)(x + 4)(x - 1)(x - 3).
3. Tabla de signos:
   P(x) > 0 en ]-∞, -5[ ∪ ]-4, 1[ ∪ ]3, +∞[.
4. Definición de la función:
   f: ]-∞, -5[ ∪ ]-4, 1[ ∪ ]3, +∞[ → ℝ,
   x ↦ ln(x⁴ + 5x³ - 13x² - 53x + 60).
5. Rango: Rg(f) = ℝ (4 asíntotas verticales en x ∈ {-5, -4, 1, 3} con f(x) → -∞).
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_56(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.56",
            topic="Definición Formal de Función Logarítmica Cuártica"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Halle la función real asociada a la fórmula mediante la Regla del Máximo Dominio (RMD):",
            math_tex=r"f(x) = \ln\left(x^4 + 5x^3 - 13x^2 - 53x + 60\right) \implies \text{Factorizar, hallar } \operatorname{Dom}(f) \text{ y definir } f.",
            desc_font_size=14,
            math_font_size=13,
            read_time=4.0
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Condición del Logaritmo (RMD)",
            "2/6: Factorización Cuártica (Ruffini)",
            "3/6: Tabla de Signos por Intervalos",
            "4/6: Dominio y Definición Formal",
            "5/6: Asíntotas Verticales y Rango ℝ",
            "6/6: Resumen y Gráfica Cartesiana"
        ])

        # ==========================================================
        # PASO 1: Condición del Argumento Logarítmico (RMD)
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\text{F\'ormula dada: } \quad f(x) = \ln(P(x)) \\[4pt]"
            r"&P(x) = x^4 + 5x^3 - 13x^2 - 53x + 60 \\[6pt]"
            r"&\textbf{Regla del M\'aximo Dominio para el Logaritmo Natural:} \\[4pt]"
            r"&\ln(u) \in \mathbb{R} \iff u > 0 \quad (\text{argumento estrictamente positivo}) \\[6pt]"
            r"&\operatorname{Dom}(f) = \{x \in \mathbb{R} : P(x) > 0\} \\[4pt]"
            r"&\text{Excluye } P(x) \le 0 \implies \text{Resolver inecuaci\'on } P(x) > 0"
            r"\end{aligned}",
            font_size=17,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Condición del Logaritmo (RMD):\n"
            "• La función logaritmo natural solo está definida\n"
            "  para números estrictamente positivos.\n"
            "• El dominio está determinado por la inecuación\n"
            "  polinomial de cuarto grado: P(x) > 0.\n"
            "• El valor P(x) = 0 está excluido pues\n"
            "  ln(0) no existe en ℝ (asíntotas verticales)."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Factorización Cuártica por Ruffini
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\text{B\'usqueda de ra\'ices enteras entre divisores de } 60: \\[4pt]"
            r"&P(1) = 1 + 5 - 13 - 53 + 60 = 0 \implies (x - 1) \text{ es factor.} \\[3pt]"
            r"&P(3) = 81 + 135 - 117 - 159 + 60 = 0 \implies (x - 3) \text{ es factor.} \\[5pt]"
            r"&\text{Dividiendo sucesivamente (Ruffini):} \\[4pt]"
            r"&\frac{P(x)}{(x-1)(x-3)} = x^2 + 9x + 20 = (x + 4)(x + 5) \\[6pt]"
            r"&\mathbf{P(x) = (x + 5)(x + 4)(x - 1)(x - 3)} \\[4pt]"
            r"&\text{Ra\'ices cr\'iticas: } \{-5, -4, 1, 3\}"
            r"\end{aligned}",
            font_size=16,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Factorización por Ruffini:\n"
            "• Evaluamos el teorema del resto con divisores de 60.\n"
            "• x = 1 y x = 3 son raíces exactas.\n"
            "• El cociente cuadrático x² + 9x + 20 se\n"
            "  descompone de inmediato en (x + 4)(x + 5).\n"
            "• Obtenemos 4 factores lineales reales simples."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], wait_time=5.0)

        # ==========================================================
        # PASO 3: Tabla de Signos por Intervalos
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{Tabla de Variaci\'on de Signo de } P(x): \\[4pt]"
            r"&\begin{array}{|c|c|c|c|c||c|} \hline"
            r"\text{\textbf{Intervalo}} & x+5 & x+4 & x-1 & x-3 & \mathbf{P(x)} \\ \hline"
            r"]-\infty, -5[ & - & - & - & - & \mathbf{+} \; (>0) \\"
            r"]-5, -4[ & + & - & - & - & \mathbf{-} \; (<0) \\"
            r"]-4, 1[ & + & + & - & - & \mathbf{+} \; (>0) \\"
            r"]1, 3[ & + & + & + & - & \mathbf{-} \; (<0) \\"
            r"]3, +\infty[ & + & + & + & + & \mathbf{+} \; (>0) \\ \hline"
            r"\end{array} \\[5pt]"
            r"&\text{Signos estrictamente positivos en: } ]-\infty, -5[, \; ]-4, 1[ \;\text{ y }\; ]3, +\infty["
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Tabla de Signos por Intervalos:\n"
            "• Las 4 raíces simples alternan el signo de P(x).\n"
            "• P(x) > 0 en tres intervalos abiertos disjuntos:\n"
            "  ]-∞, -5[, ]-4, 1[ y ]3, +∞[.\n"
            "• En ]-5, -4[ y ]1, 3[, P(x) < 0;\n"
            "  el logaritmo no existe (zonas prohibidas)."
        )

        self.morph_step(eq3, just3, box_color=THEME["success"], wait_time=5.0)

        # ==========================================================
        # PASO 4: Dominio y Definición Formal de la Función
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{Dominio M\'aximo } \operatorname{Dom}(f): \\[4pt]"
            r"&\mathbf{Dom}(f) = \; ]-\infty, -5[ \;\cup\; ]-4, 1[ \;\cup\; ]3, +\infty[ \\[6pt]"
            r"&\textbf{Definici\'on Formal de la Funci\'on Asociada:} \\[4pt]"
            r"&f: \; ]-\infty, -5[ \;\cup\; ]-4, 1[ \;\cup\; ]3, +\infty[ \; \to \mathbb{R} \\[5pt]"
            r"&x \mapsto f(x) = \ln\left(x^4 + 5x^3 - 13x^2 - 53x + 60\right) \\[6pt]"
            r"&\text{Puntos frontera excluidos: } x \in \{-5, -4, 1, 3\}"
            r"\end{aligned}",
            font_size=16,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Definición Formal de la Función:\n"
            "• La función real queda rigurosamente definida\n"
            "  por la terna con su dominio máximo.\n"
            "• Es continua en cada uno de sus tres intervalos.\n"
            "• Los 4 ceros del polinomio quedan fuera del\n"
            "  dominio al exigir desigualdad estricta."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 5: Comportamiento Asintótico y Rango
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{L\'imites en las 4 As\'intotas Verticales:} \\[4pt]"
            r"&\lim_{x \to -5^-} f(x) = -\infty, \quad \lim_{x \to -4^+} f(x) = -\infty \\[3pt]"
            r"&\lim_{x \to 1^-} f(x) = -\infty, \quad \lim_{x \to 3^+} f(x) = -\infty \\[6pt]"
            r"&\textbf{Extremos Infinitos y M\'aximo Local:} \\[4pt]"
            r"&\lim_{x \to \pm\infty} f(x) = +\infty \\[3pt]"
            r"&\text{C\'upula en } ]-4, 1[: \; \text{M\'aximo en } x \approx -1.36 \implies y \approx 4.59 \\[6pt]"
            r"&\mathbf{Rango:\; Rg}(f) = \mathbb{R} \quad (\text{no acotado superior ni inferiormente})"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Asíntotas Verticales y Rango ℝ:\n"
            "• Al acercarse a las raíces desde el interior del\n"
            "  dominio, P(x) → 0⁺, luego ln(P(x)) → -∞.\n"
            "• Hay 4 asíntotas verticales: x = -5, -4, 1, 3.\n"
            "• Para |x| → ∞, P(x) → +∞, luego f(x) → +∞.\n"
            "• Por continuidad, el rango cubre todo ℝ: Rg = ℝ."
        )

        self.morph_step(eq5, just5, box_color=THEME["statement_box"], wait_time=4.8)

        # ==========================================================
        # PASO 6: Resumen y Representación Cartesiana
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Cuadro sinóptico de conclusiones
        t_title = Text("Resumen de la Función Asociada:", font_size=13, color=THEME["header_color"], weight=BOLD)
        t_dom_desc = MathTex(r"\mathbf{Dom}(f) = \; ]-\infty, -5[ \cup ]-4, 1[ \cup ]3, +\infty[", font_size=11, color=THEME["highlight"])
        t_rg_desc = MathTex(r"\mathbf{Rg}(f) = \mathbb{R}", font_size=12, color=THEME["success"])
        t_asymp = Text("• 4 Asíntotas verticales: x ∈ {-5, -4, 1, 3}.", font_size=11, color=THEME["statement_box"], weight=BOLD)
        t_excl = Text("• Franjas prohibidas: ]-5, -4[ y ]1, 3[.", font_size=11, color=THEME["secondary"])
        t_peak = Text("• Cúpula central con máximo y ≈ 4.59.", font_size=11, color=THEME["curve"])

        info_grp = VGroup(t_title, t_dom_desc, t_rg_desc, t_asymp, t_excl, t_peak).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        info_box = SurroundingRectangle(info_grp, color=THEME["statement_box"], buff=0.18, stroke_width=1.5, corner_radius=0.08)
        left_grp = VGroup(info_box, info_grp).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos para graficar f(x)
        axes, axes_labels = self.setup_axes(
            x_range=[-6.5, 4.5, 2],
            y_range=[-3.0, 5.5, 2],
            x_length=4.8,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True
        )

        # Función auxiliar segura para evaluar ln(P(x))
        def eval_f(x_val):
            val = (x_val + 5)*(x_val + 4)*(x_val - 1)*(x_val - 3)
            return np.log(val) if val > 1e-4 else -3.0

        # Rama izquierda: [-6.2, -5.08]
        curve_left = axes.plot(eval_f, x_range=[-6.2, -5.08], color=THEME["curve"], stroke_width=2.5)

        # Rama central (cúpula): [-3.92, 0.92]
        curve_center = axes.plot(eval_f, x_range=[-3.92, 0.92], color=THEME["curve"], stroke_width=2.5)

        # Rama derecha: [3.08, 4.2]
        curve_right = axes.plot(eval_f, x_range=[3.08, 4.2], color=THEME["curve"], stroke_width=2.5)

        # 4 Asíntotas verticales punteadas en x = -5, -4, 1, 3
        asym_x = [-5, -4, 1, 3]
        asym_lines = VGroup(*[
            DashedLine(axes.c2p(ax, -2.8), axes.c2p(ax, 5.2), color=THEME["statement_box"], stroke_width=1.5)
            for ax in asym_x
        ])

        # Zonas prohibidas en el eje X
        forbid1 = Line(axes.c2p(-5, 0), axes.c2p(-4, 0), color=THEME["statement_box"], stroke_width=5.0)
        forbid2 = Line(axes.c2p(1, 0), axes.c2p(3, 0), color=THEME["statement_box"], stroke_width=5.0)

        graph_title = Text("Gráfica de f(x) = ln(P(x))", font_size=13, color=THEME["header_color"]).next_to(axes, UP, buff=0.15)

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
            Create(asym_lines),
            Create(forbid1),
            Create(forbid2),
            run_time=1.2
        )
        self.play(
            Create(curve_left),
            Create(curve_center),
            Create(curve_right),
            run_time=1.5
        )
        self.wait(5.5)

        # Cierre suave
        extra_mobs = [
            left_grp, axes, axes_labels, graph_title,
            asym_lines, forbid1, forbid2,
            curve_left, curve_center, curve_right
        ]
        self.finish_exercise(extra_mobjects=extra_mobs)
        self.wait(0.5)
