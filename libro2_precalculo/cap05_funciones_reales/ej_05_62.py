"""
Ejercicio 5.62 - Precálculo 2 (Colección Yachay Tech / Editorial Amarun)
Capítulo 5: Funciones Reales
Tema: Monotonía, biyectividad, cálculo de la función inversa y gráfica
      de la función f: ℝ → ]-1, 1[, f(x) = x / (1 + |x|).

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


class Ejercicio05_62(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.62",
            topic="Biyectividad, Función Inversa y Simetría"
        )

        # 2. Enunciado institucional permanente (y = 2.5)
        self.setup_statement(
            desc_text="Dada la función f: ℝ → ]-1, 1[ definida por f(x) = x / (1 + |x|):",
            math_tex=r"1.\; \text{Graficar } f; \qquad 2.\; \text{Analizar monotonía de } f; \qquad 3.\; \text{Determinar biyectividad y hallar } f^{-1}.",
            desc_font_size=13,
            math_font_size=12,
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (6 pasos)
        self.setup_progress_bar([
            "1/6: Definición por Tramos y Simetría",
            "2/6: Monotonía Estricta en ℝ",
            "3/6: Demostración de Inyectividad",
            "4/6: Demostración de Sobreyectividad",
            "5/6: Biyectividad y Función Inversa",
            "6/6: Gráfica de f, f⁻¹ y Recta Identidad"
        ])

        # ==========================================================
        # PASO 1: Definición por Tramos y Simetría Impar
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Expresión por Tramos y Simetría:} \\[4pt]"
            r"&f(x) = \frac{x}{1 + |x|}, \quad \operatorname{Dom}(f) = \mathbb{R}, \quad \operatorname{Cod}(f) = ]-1, 1[ \\[5pt]"
            r"&\bullet\; x \ge 0 \implies |x| = x \implies f(x) = \frac{x}{1+x} = 1 - \frac{1}{1+x} \\[4pt]"
            r"&\bullet\; x < 0 \implies |x| = -x \implies f(x) = \frac{x}{1-x} = -1 + \frac{1}{1-x} \\[5pt]"
            r"&\text{Simetría: } f(-x) = \frac{-x}{1+|-x|} = -\frac{x}{1+|x|} = -f(x) \\[4pt]"
            r"&\implies \textbf{f es una función IMPAR} \quad (\text{simetría central en } (0,0))"
            r"\end{aligned}",
            font_size=16,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Tramos y Simetría:\n"
            "• El denominador 1+|x| ≥ 1 jamás se anula en ℝ.\n"
            "• Al descomponer el valor absoluto:\n"
            "  Para x ≥ 0: f(x) = 1 - 1/(1+x).\n"
            "  Para x < 0: f(x) = -1 + 1/(1-x).\n"
            "• Satisface f(-x) = -f(x): es impar.\n"
            "• Su gráfica es simétrica respecto al origen."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Monotonía Estricta en todo ℝ
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Análisis Riguroso de Monotonía:} \\[4pt]"
            r"&\bullet\; \text{En } [0, +\infty[: \; 0 \le x_1 < x_2 \implies 1 + x_1 < 1 + x_2 \\[3pt]"
            r"&\quad \implies \frac{1}{1+x_1} > \frac{1}{1+x_2} \implies 1 - \frac{1}{1+x_1} < 1 - \frac{1}{1+x_2} \\[3pt]"
            r"&\quad \implies \mathbf{f(x_1) < f(x_2)} \quad (\text{estrictamente creciente}) \\[4pt]"
            r"&\bullet\; \text{En } ]-\infty, 0]: \text{ Por simetría impar o } x_1 < x_2 < 0: \\[3pt]"
            r"&\quad \implies 1 - x_1 > 1 - x_2 > 0 \implies \mathbf{f(x_1) < f(x_2)} \\[4pt]"
            r"&\bullet\; \text{Si } x_1 < 0 \le x_2 \implies f(x_1) < 0 \le f(x_2) \\[4pt]"
            r"&\implies \textbf{f es ESTRICTAMENTE CRECIENTE en todo } \mathbb{R}"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Monotonía Estricta:\n"
            "• En [0, +∞[, al crecer x, 1/(1+x) decrece,\n"
            "  haciendo que 1 - 1/(1+x) crezca estrictamente.\n"
            "• En ]-∞, 0[, el mismo comportamiento ocurre\n"
            "  por transitividad e imparidad.\n"
            "• Como f(x) < 0 para x < 0 y f(x) ≥ 0 para x ≥ 0,\n"
            "  la monotonía es continua y estricta en todo ℝ."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Demostración de Inyectividad
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Demostración de Inyectividad:} \\[4pt]"
            r"&\text{Criterio por Monotonía Estricta:} \\[3pt]"
            r"&\forall x_1, x_2 \in \mathbb{R}, \quad x_1 < x_2 \implies f(x_1) < f(x_2) \\[4pt]"
            r"&\text{Por contrarecíproco formal:} \\[3pt]"
            r"&x_1 \neq x_2 \implies (x_1 < x_2 \lor x_2 < x_1) \implies f(x_1) \neq f(x_2) \\[5pt]"
            r"&\text{Alternativa algebraica: Si } f(x_1) = f(x_2): \\[3pt]"
            r"&\operatorname{sign}(f(x)) = \operatorname{sign}(x) \implies x_1, x_2 \text{ tienen igual signo.} \\[3pt]"
            r"&\frac{x_1}{1+|x_1|} = \frac{x_2}{1+|x_2|} \implies x_1(1+|x_2|) = x_2(1+|x_1|) \implies x_1 = x_2 \\[4pt]"
            r"&\implies \textbf{f es INYECTIVA en } \mathbb{R}"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Inyectividad:\n"
            "• Toda función estrictamente monótona en un\n"
            "  intervalo es automáticamente inyectiva.\n"
            "• x₁ ≠ x₂ obliga a que f(x₁) ≠ f(x₂).\n"
            "• Algebraicamente, como f(x) conserva el signo\n"
            "  de x, al igualar imágenes el producto cruzado\n"
            "  reduce de inmediato a x₁ = x₂."
        )

        self.morph_step(eq3, just3, box_color=THEME["success"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Demostración de Sobreyectividad
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Demostración de Sobreyectividad:} \\[4pt]"
            r"&\text{Sea } y \in ]-1, 1[. \quad \text{Buscamos } x \in \mathbb{R} \text{ tal que } f(x) = y: \\[4pt]"
            r"&\bullet\; y \in [0, 1[: \; y = \frac{x}{1+x} \iff y + yx = x \iff y = x(1-y) \\[3pt]"
            r"&\quad \implies \mathbf{x = \frac{y}{1-y}} \ge 0 \quad (\text{pues } 1 - y > 0 \land y \ge 0) \\[4pt]"
            r"&\bullet\; y \in ]-1, 0[: \; y = \frac{x}{1-x} \iff y - yx = x \iff y = x(1+y) \\[3pt]"
            r"&\quad \implies \mathbf{x = \frac{y}{1+y}} < 0 \quad (\text{pues } 1 + y > 0 \land y < 0) \\[4pt]"
            r"&\implies \operatorname{Rg}(f) = ]-1, 1[ = \operatorname{Cod}(f) \implies \textbf{f es SOBREYECTIVA}"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Sobreyectividad:\n"
            "• Para cada y ∈ ]-1, 1[, encontramos su preimagen x.\n"
            "• Si y ≥ 0: x = y/(1 - y) ≥ 0, bien definido.\n"
            "• Si y < 0: x = y/(1 + y) < 0, bien definido.\n"
            "• Por ende, todo elemento del codominio ]-1, 1[\n"
            "  proviene de al menos un x ∈ ℝ.\n"
            "• Rg(f) = ]-1, 1[ = Cod(f) ⟹ Sobreyectiva."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=5.0)

        # ==========================================================
        # PASO 5: Biyectividad y Función Inversa
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Biyectividad y Función Inversa } f^{-1}: \\[4pt]"
            r"&\text{Al ser inyectiva y sobreyectiva } \implies \textbf{f es BIYECTIVA.} \\[4pt]"
            r"&\text{Unificando las fórmulas de preimagen con el valor absoluto:} \\[3pt]"
            r"&\text{Si } y \ge 0: \; 1 - y = 1 - |y|; \quad \text{Si } y < 0: \; 1 + y = 1 - |y| \\[5pt]"
            r"&\mathbf{f^{-1}: \; ]-1, 1[ \to \mathbb{R}, \quad f^{-1}(y) = \frac{y}{1 - |y|}} \\[6pt]"
            r"&\textbf{Comprobación de Identidad:} \\[3pt]"
            r"&f^{-1}(f(x)) = \frac{\frac{x}{1+|x|}}{1 - \frac{|x|}{1+|x|}} = \frac{x}{(1+|x|) - |x|} = \mathbf{x} \quad (\forall x \in \mathbb{R})"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Función Inversa:\n"
            "• Inyectiva + Sobreyectiva = Biyectiva.\n"
            "• Como 1-y y 1+y coinciden exactamente con 1-|y|,\n"
            "  la inversa se escribe de forma elegante y compacta:\n"
            "  f⁻¹(y) = y / (1 - |y|).\n"
            "• Dom(f⁻¹) = ]-1, 1[ y Cod(f⁻¹) = ℝ.\n"
            "• Se comprueba f⁻¹(f(x)) = x con rigor algebraico."
        )

        self.morph_step(eq5, just5, box_color=THEME["curve"], advance_to_step=4, wait_time=5.2)

        # ==========================================================
        # PASO 6: Síntesis Comparativa y Gráfica Conjunta (f, f⁻¹, y=x)
        # ==========================================================
        # Panel izquierdo: Cuadro Síntesis
        t_title = Text("Síntesis Analítica (Ej. 5.62)", font_size=13, color=THEME["header_color"], weight=BOLD)
        t_dir = MathTex(r"f: \mathbb{R} \to ]-1, 1[, \quad f(x) = \frac{x}{1+|x|}", font_size=12, color=THEME["curve"])
        t_inv = MathTex(r"f^{-1}: ]-1, 1[ \to \mathbb{R}, \quad f^{-1}(x) = \frac{x}{1-|x|}", font_size=12, color=THEME["success"])
        t_prop1 = Text("• Monotonía: Estrictamente creciente en ℝ", font_size=10, color=WHITE)
        t_prop2 = Text("• Biyectiva: Inyectiva y sobreyectiva", font_size=10, color=THEME["highlight"])
        t_prop3 = Text("• Simetría: Reflexión axial respecto a y = x", font_size=10, color=THEME["secondary"])

        table_grp = VGroup(t_title, t_dir, t_inv, t_prop1, t_prop2, t_prop3).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        table_box = SurroundingRectangle(table_grp, color=THEME["statement_box"], buff=0.18, stroke_width=1.5, corner_radius=0.08)
        left_summary = VGroup(table_box, table_grp).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos para ilustrar f, f⁻¹ y la diagonal y=x
        axes, axes_labels = self.setup_axes(
            x_range=[-3.2, 3.2, 1],
            y_range=[-3.2, 3.2, 1],
            x_length=4.8,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True
        )
        graph_title = Text("Simetría Inversa: f(x), f⁻¹(x) y y = x", font_size=12, color=WHITE).next_to(axes, UP, buff=0.15)

        # Recta identidad: y = x
        line_ident = DashedLine(
            start=axes.c2p(-3.0, -3.0),
            end=axes.c2p(3.0, 3.0),
            color=GRAY,
            stroke_width=1.3,
            dash_length=0.08
        )
        lbl_ident = MathTex(r"y = x", font_size=10, color=GRAY).move_to(axes.c2p(2.6, 2.85))

        # Asíntotas horizontales de f: y = 1, y = -1
        asym_h1 = DashedLine(start=axes.c2p(-3.2, 1.0), end=axes.c2p(3.2, 1.0), color=THEME["curve"], stroke_width=1.0, dash_length=0.08)
        asym_h2 = DashedLine(start=axes.c2p(-3.2, -1.0), end=axes.c2p(3.2, -1.0), color=THEME["curve"], stroke_width=1.0, dash_length=0.08)

        # Asíntotas verticales de f⁻¹: x = 1, x = -1
        asym_v1 = DashedLine(start=axes.c2p(1.0, -3.2), end=axes.c2p(1.0, 3.2), color=THEME["success"], stroke_width=1.0, dash_length=0.08)
        asym_v2 = DashedLine(start=axes.c2p(-1.0, -3.2), end=axes.c2p(-1.0, 3.2), color=THEME["success"], stroke_width=1.0, dash_length=0.08)

        # Curva directa: f(x) = x / (1 + |x|)
        curve_f = axes.plot(lambda x: x / (1.0 + abs(x)), x_range=[-3.1, 3.1], color=THEME["curve"], stroke_width=2.5)

        # Curva inversa: f⁻¹(x) = x / (1 - |x|) para x ∈ ]-1, 1[
        curve_finv = axes.plot(lambda x: x / (1.0 - abs(x)), x_range=[-0.74, 0.74], color=THEME["success"], stroke_width=2.5)

        # Punto de corte con la identidad: (0, 0)
        dot_origin = Dot(axes.c2p(0, 0), color=THEME["highlight"], radius=0.07)
        lbl_origin = MathTex(r"(0, 0)", font_size=10, color=THEME["highlight"]).next_to(dot_origin, DOWN + RIGHT, buff=0.08)

        # Etiquetas de curvas
        leg_f = MathTex(r"f(x) = \tfrac{x}{1+|x|}", font_size=11, color=THEME["curve"]).move_to(axes.c2p(1.9, 0.55))
        leg_finv = MathTex(r"f^{-1}(x) = \tfrac{x}{1-|x|}", font_size=11, color=THEME["success"]).move_to(axes.c2p(-1.7, -2.1))

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
            Create(line_ident),
            Write(lbl_ident),
            Create(asym_h1),
            Create(asym_h2),
            Create(asym_v1),
            Create(asym_v2),
            run_time=1.2
        )
        self.play(
            Create(curve_f),
            Create(curve_finv),
            FadeIn(dot_origin),
            Write(lbl_origin),
            Write(leg_f),
            Write(leg_finv),
            run_time=1.8
        )
        self.wait(6.0)

        # Cierre suave
        extra_mobs = [
            left_summary, axes, axes_labels, graph_title,
            line_ident, lbl_ident, asym_h1, asym_h2, asym_v1, asym_v2,
            curve_f, curve_finv, dot_origin, lbl_origin, leg_f, leg_finv
        ]
        self.finish_exercise(extra_mobjects=extra_mobs)
        self.wait(0.5)
