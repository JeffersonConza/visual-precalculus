"""
Ejercicio 5.64 - Precálculo 2 (Colección Yachay Tech / Editorial Amarun)
Capítulo 5: Funciones Reales
Tema: Monotonía, biyectividad, función inversa y gráfica de una
      función racional restringida: [3, 5] ∋ x ↦ f(x) = 3/(2 - x) ∈ [-3, -1].

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


class Ejercicio05_64(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.64",
            topic="Biyectividad e Inversa de una Función Racional"
        )

        # 2. Enunciado institucional permanente (y = 2.5)
        self.setup_statement(
            desc_text="Dada la función f: [3, 5] → [-3, -1] definida por f(x) = 3 / (2 - x):",
            math_tex=r"1.\; \text{Graficar } f; \qquad 2.\; \text{Analizar monotonía de } f; \qquad 3.\; \text{Determinar biyectividad y hallar } f^{-1}.",
            desc_font_size=13,
            math_font_size=12,
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (6 pasos)
        self.setup_progress_bar([
            "1/6: Definición Formal y Dominio",
            "2/6: Monotonía Estricta en [3, 5]",
            "3/6: Demostración de Inyectividad",
            "4/6: Sobreyectividad y Rango [-3, -1]",
            "5/6: Biyectividad y Función Inversa",
            "6/6: Gráfica de f, f⁻¹ y Simetría y = x"
        ])

        # ==========================================================
        # PASO 1: Definición Formal y Dominio
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Definición Formal de la Función:} \\[4pt]"
            r"&f: \; [3, 5] \to [-3, -1], \quad f(x) = \frac{3}{2 - x} \\[5pt]"
            r"&\bullet\; \text{Punto singular (asíntota vertical): } 2 - x = 0 \iff x = 2 \\[4pt]"
            r"&\bullet\; \text{Condición: } 2 \notin [3, 5] \implies 2 - x < 0 \quad (\forall x \in [3, 5]) \\[5pt]"
            r"&\text{Valores en los extremos del dominio:} \\[3pt]"
            r"&f(3) = \frac{3}{2 - 3} = \frac{3}{-1} = \mathbf{-3} \\[4pt]"
            r"&f(5) = \frac{3}{2 - 5} = \frac{3}{-3} = \mathbf{-1}"
            r"\end{aligned}",
            font_size=16,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Definición y Dominio:\n"
            "• El dominio restringido es el intervalo cerrado [3, 5].\n"
            "• El único valor donde el denominador se anula es x = 2.\n"
            "• Como 2 ∉ [3, 5], el denominador es estrictamente\n"
            "  negativo y f es continua en todo [3, 5].\n"
            "• En los extremos: f(3) = -3 y f(5) = -1."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Monotonía Estricta en [3, 5]
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Análisis Riguroso de Monotonía:} \\[4pt]"
            r"&\text{Sean } x_1, x_2 \in [3, 5] \text{ tales que } x_1 < x_2: \\[4pt]"
            r"&x_1 < x_2 \implies -x_1 > -x_2 \implies 2 - x_1 > 2 - x_2 \\[4pt]"
            r"&\text{Como } 2 - x_1 \text{ y } 2 - x_2 \text{ son negativos } (0 > 2 - x_1 > 2 - x_2): \\[4pt]"
            r"&\implies \frac{1}{2 - x_1} < \frac{1}{2 - x_2} \quad (\text{propiedad de inversos negativos}) \\[5pt]"
            r"&\implies \frac{3}{2 - x_1} < \frac{3}{2 - x_2} \iff \mathbf{f(x_1) < f(x_2)} \\[5pt]"
            r"&\implies \textbf{f es ESTRICTAMENTE CRECIENTE en } [3, 5]"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Monotonía Estricta:\n"
            "• Partimos de x₁ < x₂ en [3, 5].\n"
            "• Multiplicar por -1 invierte la desigualdad:\n"
            "  -x₁ > -x₂ ⟹ 2 - x₁ > 2 - x₂.\n"
            "• Al invertir números estrictamente negativos,\n"
            "  el orden se invierte nuevamente: 1/(2-x₁) < 1/(2-x₂).\n"
            "• Multiplicando por 3 > 0, concluimos f(x₁) < f(x₂)."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=5.0)

        # ==========================================================
        # PASO 3: Demostración de Inyectividad
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Demostración de Inyectividad:} \\[4pt]"
            r"&\textbf{Criterio por Monotonía Estricta:} \\[3pt]"
            r"&\text{Al ser } f \text{ estrictamente creciente en } [3, 5]: \\[3pt]"
            r"&\forall x_1, x_2 \in [3, 5], \quad x_1 \neq x_2 \implies f(x_1) \neq f(x_2) \\[5pt]"
            r"&\textbf{Comprobación Algebraica Directa:} \\[3pt]"
            r"&f(x_1) = f(x_2) \implies \frac{3}{2 - x_1} = \frac{3}{2 - x_2} \\[4pt]"
            r"&\iff 3(2 - x_2) = 3(2 - x_1) \iff 2 - x_2 = 2 - x_1 \\[4pt]"
            r"&\iff -x_2 = -x_1 \iff \mathbf{x_1 = x_2} \\[4pt]"
            r"&\implies \textbf{f es INYECTIVA en } [3, 5]"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Demostración de Inyectividad:\n"
            "• Monotonía estricta garantiza inyectividad:\n"
            "  si las entradas difieren, las salidas difieren.\n"
            "• Por igualación de imágenes f(x₁) = f(x₂),\n"
            "  la igualdad de fracciones con igual numerador\n"
            "  exige denominadores idénticos: 2 - x₁ = 2 - x₂.\n"
            "• Esto implica unívocamente x₁ = x₂."
        )

        self.morph_step(eq3, just3, box_color=THEME["success"], advance_to_step=2, wait_time=4.8)

        # ==========================================================
        # PASO 4: Sobreyectividad y Rango [-3, -1]
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Demostración de Sobreyectividad:} \\[4pt]"
            r"&\text{Dado que } f \text{ es continua y estrictamente creciente en } [3, 5]: \\[3pt]"
            r"&\operatorname{Rg}(f) = [f(3), f(5)] = [-3, -1] = \operatorname{Cod}(f) \\[5pt]"
            r"&\textbf{Construcción Explícita de la Preimagen:} \\[3pt]"
            r"&\text{Sea } y \in [-3, -1]. \quad \text{Resolvemos } f(x) = y: \\[3pt]"
            r"&y = \frac{3}{2 - x} \iff 2 - x = \frac{3}{y} \iff \mathbf{x = 2 - \frac{3}{y}} \\[5pt]"
            r"&\text{Verificación de pertenencia al dominio } [3, 5]: \\[3pt]"
            r"&-3 \le y \le -1 \implies -1 \le \frac{3}{y} \le -3 \dots \text{ (por } y < 0) \\[3pt]"
            r"&\iff 1 \ge -\frac{3}{y} \ge 3 \dots \text{ Sumando 2: } \mathbf{3 \le 2 - \frac{3}{y} \le 5} \\[4pt]"
            r"&\implies \textbf{f es SOBREYECTIVA sobre } [-3, -1]"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Demostración de Sobreyectividad:\n"
            "• Todo y ∈ [-3, -1] debe provenir de algún x ∈ [3, 5].\n"
            "• Despejando: 2 - x = 3/y ⟹ x = 2 - 3/y.\n"
            "• Si y = -3 ⟹ x = 2 - (-1) = 3 ∈ [3, 5].\n"
            "• Si y = -1 ⟹ x = 2 - (-3) = 5 ∈ [3, 5].\n"
            "• La preimagen x pertenece siempre a [3, 5].\n"
            "• Rg(f) = [-3, -1] = Cod(f) ⟹ Sobreyectiva."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=5.0)

        # ==========================================================
        # PASO 5: Biyectividad y Función Inversa
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Biyectividad y Función Inversa } f^{-1}: \\[4pt]"
            r"&\text{Al ser inyectiva y sobreyectiva } \implies \textbf{f es BIYECTIVA.} \\[4pt]"
            r"&\mathbf{f^{-1}: \; [-3, -1] \to [3, 5], \quad f^{-1}(y) = 2 - \frac{3}{y} = \frac{2y - 3}{y}} \\[6pt]"
            r"&\textbf{Comprobación Formal de Identidad:} \\[3pt]"
            r"&\bullet\; f^{-1}(f(x)) = 2 - \frac{3}{\frac{3}{2 - x}} = 2 - (2 - x) = \mathbf{x} \quad (\forall x \in [3, 5]) \\[4pt]"
            r"&\bullet\; f(f^{-1}(y)) = \frac{3}{2 - \left(2 - \frac{3}{y}\right)} = \frac{3}{\frac{3}{y}} = \mathbf{y} \quad (\forall y \in [-3, -1])"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Función Inversa f⁻¹:\n"
            "• La biyectividad garantiza existencia de f⁻¹.\n"
            "• Se intercambian dominio y codominio:\n"
            "  Dom(f⁻¹) = [-3, -1] y Cod(f⁻¹) = [3, 5].\n"
            "• Fórmula analítica: f⁻¹(y) = 2 - 3/y = (2y-3)/y.\n"
            "• Comprobamos f⁻¹(f(x)) = x y f(f⁻¹(y)) = y,\n"
            "  satisfaciendo la definición de función inversa."
        )

        self.morph_step(eq5, just5, box_color=THEME["curve"], advance_to_step=4, wait_time=5.2)

        # ==========================================================
        # PASO 6: Síntesis Analítica y Gráfica Conjunta (f, f⁻¹, y=x)
        # ==========================================================
        # Panel izquierdo: Cuadro Síntesis
        t_title = Text("Síntesis Analítica (Ej. 5.64)", font_size=13, color=THEME["header_color"], weight=BOLD)
        t_dir = MathTex(r"f: [3, 5] \to [-3, -1], \quad f(x) = \frac{3}{2-x}", font_size=12, color=THEME["curve"])
        t_inv = MathTex(r"f^{-1}: [-3, -1] \to [3, 5], \quad f^{-1}(x) = 2 - \frac{3}{x}", font_size=12, color=THEME["success"])
        t_prop1 = Text("• Monotonía: Estrictamente creciente en [3, 5]", font_size=10, color=WHITE)
        t_prop2 = Text("• Biyectiva: Inyectiva y sobreyectiva", font_size=10, color=THEME["highlight"])
        t_prop3 = Text("• Extremos: (3, -3) ↔ (-3, 3) y (5, -1) ↔ (-1, 5)", font_size=10, color=THEME["secondary"])

        table_grp = VGroup(t_title, t_dir, t_inv, t_prop1, t_prop2, t_prop3).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        table_box = SurroundingRectangle(table_grp, color=THEME["statement_box"], buff=0.18, stroke_width=1.5, corner_radius=0.08)
        left_summary = VGroup(table_box, table_grp).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos para ilustrar f, f⁻¹ y la diagonal y=x
        axes, axes_labels = self.setup_axes(
            x_range=[-4.0, 6.0, 2],
            y_range=[-4.0, 6.0, 2],
            x_length=4.8,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True
        )
        graph_title = Text("Simetría Inversa: f(x), f⁻¹(x) y y = x", font_size=12, color=WHITE).next_to(axes, UP, buff=0.15)

        # Recta identidad: y = x
        line_ident = DashedLine(
            start=axes.c2p(-3.8, -3.8),
            end=axes.c2p(5.8, 5.8),
            color=GRAY,
            stroke_width=1.3,
            dash_length=0.08
        )
        lbl_ident = MathTex(r"y = x", font_size=10, color=GRAY).move_to(axes.c2p(4.8, 5.4))

        # Asíntota vertical original de f: x = 2
        asym_f = DashedLine(start=axes.c2p(2.0, -3.8), end=axes.c2p(2.0, 5.8), color=THEME["curve"], stroke_width=1.0, dash_length=0.08)
        lbl_asym_f = MathTex(r"x = 2", font_size=9, color=THEME["curve"]).move_to(axes.c2p(2.3, -3.5))

        # Asíntota horizontal de f⁻¹: y = 2
        asym_finv = DashedLine(start=axes.c2p(-3.8, 2.0), end=axes.c2p(5.8, 2.0), color=THEME["success"], stroke_width=1.0, dash_length=0.08)
        lbl_asym_finv = MathTex(r"y = 2", font_size=9, color=THEME["success"]).move_to(axes.c2p(-3.2, 2.3))

        # Curva directa: f(x) = 3 / (2 - x) para x ∈ [3, 5]
        curve_f = axes.plot(lambda x: 3.0 / (2.0 - x), x_range=[3.0, 5.0], color=THEME["curve"], stroke_width=2.8)

        # Curva inversa: f⁻¹(x) = 2 - 3/x para x ∈ [-3, -1]
        curve_finv = axes.plot(lambda x: 2.0 - 3.0 / x, x_range=[-3.0, -1.0], color=THEME["success"], stroke_width=2.8)

        # Puntos extremos de f: (3, -3) y (5, -1)
        dot_f1 = Dot(axes.c2p(3, -3), color=THEME["curve"], radius=0.06)
        lbl_f1 = MathTex(r"(3, -3)", font_size=9, color=THEME["curve"]).next_to(dot_f1, DOWN, buff=0.06)

        dot_f2 = Dot(axes.c2p(5, -1), color=THEME["curve"], radius=0.06)
        lbl_f2 = MathTex(r"(5, -1)", font_size=9, color=THEME["curve"]).next_to(dot_f2, RIGHT, buff=0.06)

        # Puntos extremos de f⁻¹: (-3, 3) y (-1, 5)
        dot_inv1 = Dot(axes.c2p(-3, 3), color=THEME["success"], radius=0.06)
        lbl_inv1 = MathTex(r"(-3, 3)", font_size=9, color=THEME["success"]).next_to(dot_inv1, UP, buff=0.06)

        dot_inv2 = Dot(axes.c2p(-1, 5), color=THEME["success"], radius=0.06)
        lbl_inv2 = MathTex(r"(-1, 5)", font_size=9, color=THEME["success"]).next_to(dot_inv2, UP, buff=0.06)

        # Etiquetas de curvas
        leg_f = MathTex(r"f(x) = \tfrac{3}{2-x}", font_size=11, color=THEME["curve"]).move_to(axes.c2p(4.5, -2.4))
        leg_finv = MathTex(r"f^{-1}(x) = 2 - \tfrac{3}{x}", font_size=11, color=THEME["success"]).move_to(axes.c2p(-1.8, 3.8))

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
            Create(asym_f),
            Write(lbl_asym_f),
            Create(asym_finv),
            Write(lbl_asym_finv),
            run_time=1.2
        )
        self.play(
            Create(curve_f),
            FadeIn(dot_f1),
            Write(lbl_f1),
            FadeIn(dot_f2),
            Write(lbl_f2),
            Create(curve_finv),
            FadeIn(dot_inv1),
            Write(lbl_inv1),
            FadeIn(dot_inv2),
            Write(lbl_inv2),
            Write(leg_f),
            Write(leg_finv),
            run_time=1.8
        )
        self.wait(6.0)

        # Cierre suave
        extra_mobs = [
            left_summary, axes, axes_labels, graph_title,
            line_ident, lbl_ident, asym_f, lbl_asym_f, asym_finv, lbl_asym_finv,
            curve_f, dot_f1, lbl_f1, dot_f2, lbl_f2,
            curve_finv, dot_inv1, lbl_inv1, dot_inv2, lbl_inv2,
            leg_f, leg_finv
        ]
        self.finish_exercise(extra_mobjects=extra_mobs)
        self.wait(0.5)
