"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.44 (Página 112 del libro / Página 131 del PDF)

Mediante la Regla del Máximo Dominio (RMD), definir las funciones asociadas a:
1. f(x) = (1/x) / (1 + 1/(1 + 1/x))
   ⟹ Dom(f) = ℝ \ {-1, -1/2, 0}
   ⟹ f(x) = (x + 1) / (x(2x + 1)).

2. g(x) = √[ ((x² - 1)(x + 1)) / ((1 - x²)(x² + 1)) ]
   ⟹ Dom(g) = ]-∞, -1[
   ⟹ g(x) = √[ (-x - 1) / (x² + 1) ].

3. h(x) = √[ x + 1/x ]
   ⟹ Dom(h) = ]0, +∞[
   ⟹ h(x) = √[ (x² + 1) / x ].

4. w(x) = √[ x⁴ - 5x² + 4 ]
   ⟹ Dom(w) = ]-∞, -2] ∪ [-1, 1] ∪ [2, +∞[.
   Visualización gráfica: Curva w(x) y zonas de exclusión ]-2, -1[ y ]1, 2[.
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_44(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.44",
            topic="Regla del Máximo Dominio (RMD) y Definición de Funciones"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Mediante la RMD define formalmente las funciones asociadas a las siguientes 4 fórmulas:",
            math_tex=r"f(x) = \frac{\frac{1}{x}}{1 + \frac{1}{1 + \frac{1}{x}}}, \quad g(x) = \sqrt{\frac{(x^2-1)(x+1)}{(1-x^2)(x^2+1)}}, \quad h(x) = \sqrt{x + \frac{1}{x}}, \quad w(x) = \sqrt{x^4 - 5x^2 + 4}.",
            desc_font_size=14,
            math_font_size=13,
            read_time=4.0
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Fundamento Axiomático RMD",
            "2/6: Función Fraccionaria f(x)",
            "3/6: Radical con Cociente g(x)",
            "4/6: Radical con Suma Inversa h(x)",
            "5/6: Radical Bicuadrático w(x)",
            "6/6: Resumen y Gráfica de w(x)"
        ])

        # ==========================================================
        # PASO 1: Fundamento Axiomático de la RMD
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{Axioma de la Regla del M\'aximo Dominio (RMD):} \\[4pt]"
            r"&\operatorname{Dom}(f) = \{x \in \mathbb{R} : f(x) \in \mathbb{R}\} \\[6pt]"
            r"&\textbf{Definici\'on formal de una funci\'on real:} \\[4pt]"
            r"&f: \operatorname{Dom}(f) \to \mathbb{R}, \quad x \mapsto f(x) \\[8pt]"
            r"&\textbf{Restricciones anal\'iticas b\'asicas en } \mathbb{R}: \\[4pt]"
            r"&1.\; \frac{P(x)}{Q(x)} \in \mathbb{R} \iff Q(x) \neq 0 \\[4pt]"
            r"&2.\; \sqrt[2n]{R(x)} \in \mathbb{R} \iff R(x) \ge 0 \quad (n \in \mathbb{N})"
            r"\end{aligned}",
            font_size=17,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Fundamento Axiomático RMD:\n"
            "• La RMD asigna a una fórmula el subconjunto\n"
            "  más grande de ℝ donde las operaciones\n"
            "  están bien definidas.\n"
            "• Una función requiere especificar su dominio,\n"
            "  codominio ℝ y regla de correspondencia.\n"
            "• Vigilamos divisiones por cero y radicandos\n"
            "  de índice par negativos."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Función Fraccionaria Continua f(x)
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&f(x) = \frac{\frac{1}{x}}{1 + \frac{1}{1 + \frac{1}{x}}} \\[5pt]"
            r"&\text{Cascada de denominadores no nulos:} \\[3pt]"
            r"&1)\; x \neq 0 \\[3pt]"
            r"&2)\; 1 + \frac{1}{x} = \frac{x+1}{x} \neq 0 \implies x \neq -1 \\[3pt]"
            r"&3)\; 1 + \frac{x}{x+1} = \frac{2x+1}{x+1} \neq 0 \implies x \neq -\frac{1}{2} \\[6pt]"
            r"&\mathbf{Dom}(f) = \mathbb{R} \setminus \left\{-1, -\tfrac{1}{2}, 0\right\} \\[5pt]"
            r"&f: \operatorname{Dom}(f) \to \mathbb{R}, \quad x \mapsto \frac{x+1}{x(2x+1)}"
            r"\end{aligned}",
            font_size=17,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Función Fraccionaria f(x):\n"
            "• Tres denominadores encadenados:\n"
            "  a) x ≠ 0 por la fracción interna 1/x.\n"
            "  b) 1 + 1/x = (x+1)/x ≠ 0 ⟹ x ≠ -1.\n"
            "  c) 1 + x/(x+1) = (2x+1)/(x+1) ≠ 0 ⟹ x ≠ -1/2.\n"
            "• Dom(f) = ℝ \\ {-1, -1/2, 0}.\n"
            "• Simplificación: f(x) = (x+1)/(x(2x+1))."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], wait_time=5.0)

        # ==========================================================
        # PASO 3: Radical con Cociente g(x)
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&g(x) = \sqrt{\frac{(x^2-1)(x+1)}{(1-x^2)(x^2+1)}} \\[5pt]"
            r"&\text{Denominador no nulo: } 1 - x^2 \neq 0 \implies x \neq \pm 1 \\[4pt]"
            r"&\text{Radicando no negativo: } \frac{(x^2-1)(x+1)}{-(x^2-1)(x^2+1)} \ge 0 \\[4pt]"
            r"&\text{Cancelando } (x^2-1) \neq 0: \quad -\frac{x+1}{x^2+1} \ge 0 \\[4pt]"
            r"&\text{Como } x^2+1 > 0: \quad x+1 \le 0 \implies x \le -1 \\[4pt]"
            r"&\text{Con } x \neq -1: \quad x < -1 \\[6pt]"
            r"&\mathbf{Dom}(g) = \; ]-\infty, -1[ \\[5pt]"
            r"&g: \; ]-\infty, -1[ \; \to \mathbb{R}, \quad x \mapsto \sqrt{\frac{-x-1}{x^2+1}}"
            r"\end{aligned}",
            font_size=16,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Radical con Cociente g(x):\n"
            "• El denominador exige 1 - x² ≠ 0 ⟹ x ≠ ±1.\n"
            "• Factorizamos el signo: 1 - x² = -(x² - 1).\n"
            "• Al cancelar (x² - 1) para x ≠ ±1, queda:\n"
            "  -(x + 1)/(x² + 1) ≥ 0 ⟹ x + 1 ≤ 0.\n"
            "• Como x ≠ -1, el dominio estricto es:\n"
            "  Dom(g) = ]-∞, -1[."
        )

        self.morph_step(eq3, just3, box_color=THEME["success"], wait_time=5.0)

        # ==========================================================
        # PASO 4: Radical con Suma Inversa h(x)
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&h(x) = \sqrt{x + \frac{1}{x}} = \sqrt{\frac{x^2+1}{x}} \\[5pt]"
            r"&\text{Restricci\'on 1 (Fracci\'on): } x \neq 0 \\[4pt]"
            r"&\text{Restricci\'on 2 (Radicando): } \frac{x^2+1}{x} \ge 0 \\[6pt]"
            r"&\text{Propiedad: } x^2 + 1 \ge 1 > 0 \quad \forall x \in \mathbb{R} \\[5pt]"
            r"&\implies \frac{x^2+1}{x} \ge 0 \iff x > 0 \\[6pt]"
            r"&\mathbf{Dom}(h) = \; ]0, +\infty[ \\[5pt]"
            r"&h: \; ]0, +\infty[ \; \to \mathbb{R}, \quad x \mapsto \sqrt{x + \frac{1}{x}}"
            r"\end{aligned}",
            font_size=17,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Radical con Suma Inversa h(x):\n"
            "• Fracción interna exige x ≠ 0.\n"
            "• El radicando se compacta a (x² + 1)/x ≥ 0.\n"
            "• Como el numerador cuadrático x² + 1 es\n"
            "  estrictamente positivo en todo ℝ, el signo\n"
            "  depende exclusivamente del denominador x.\n"
            "• Por ende, Dom(h) = ]0, +∞[."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 5: Radical Bicuadrático w(x)
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&w(x) = \sqrt{x^4 - 5x^2 + 4} \\[5pt]"
            r"&\text{Factorizaci\'on cuadr\'atica en } t = x^2 \ge 0: \\[3pt]"
            r"&t^2 - 5t + 4 = (t - 1)(t - 4) \ge 0 \implies t \le 1 \;\lor\; t \ge 4 \\[5pt]"
            r"&\iff (x^2 - 1)(x^2 - 4) \ge 0 \\[3pt]"
            r"&\iff (x-1)(x+1)(x-2)(x+2) \ge 0 \\[5pt]"
            r"&\text{Ra\'ices cr\'iticas: } \{-2, -1, 1, 2\} \\[5pt]"
            r"&\mathbf{Dom}(w) = \; ]-\infty, -2] \;\cup\; [-1, 1] \;\cup\; [2, +\infty[ \\[4pt]"
            r"&= \mathbb{R} \setminus (]-2, -1[ \;\cup\; ]1, 2[) \\[5pt]"
            r"&w: \operatorname{Dom}(w) \to \mathbb{R}, \quad x \mapsto \sqrt{x^4 - 5x^2 + 4}"
            r"\end{aligned}",
            font_size=16,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Radical Bicuadrático w(x):\n"
            "• Radicando no negativo: x⁴ - 5x² + 4 ≥ 0.\n"
            "• Con t = x²: (t - 1)(t - 4) ≥ 0 ⟹ t ≤ 1 ó t ≥ 4.\n"
            "• Regresando a x: x² ≤ 1 ⟹ x ∈ [-1, 1];\n"
            "  x² ≥ 4 ⟹ x ∈ ]-∞, -2] ∪ [2, +∞[.\n"
            "• Se excluyen los dos intervalos abiertos:\n"
            "  ]-2, -1[ y ]1, 2[."
        )

        self.morph_step(eq5, just5, box_color=THEME["statement_box"], wait_time=5.0)

        # ==========================================================
        # PASO 6: Resumen Comparativo y Gráfica Cartesiana de w(x)
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen de dominios
        t_title = Text("Resumen RMD de Funciones:", font_size=14, color=THEME["header_color"], weight=BOLD)
        t_f = MathTex(r"\mathbf{Dom}(f) = \mathbb{R} \setminus \{-1, -1/2, 0\}", font_size=13, color=THEME["secondary"])
        t_g = MathTex(r"\mathbf{Dom}(g) = \; ]-\infty, -1[", font_size=13, color=THEME["success"])
        t_h = MathTex(r"\mathbf{Dom}(h) = \; ]0, +\infty[", font_size=13, color=THEME["highlight"])
        t_w = MathTex(r"\mathbf{Dom}(w) = \; ]-\infty, -2] \cup [-1, 1] \cup [2, +\infty[", font_size=13, color=THEME["curve"])
        t_note = Text("Curva de w(x) a la derecha:", font_size=12, color=WHITE, weight=BOLD)
        t_sub = Text("• Cúpula central en [-1, 1] con w(0) = 2.\n• Zonas prohibidas: ]-2, -1[ y ]1, 2[.", font_size=11, color=THEME["statement_box"])

        info_grp = VGroup(t_title, t_f, t_g, t_h, t_w, t_note, t_sub).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        info_box = SurroundingRectangle(info_grp, color=THEME["statement_box"], buff=0.18, stroke_width=1.5, corner_radius=0.08)
        left_grp = VGroup(info_box, info_grp).move_to([-3.4, -0.45, 0])

        # Panel derecho: Gráfica cartesiana de w(x)
        axes, axes_labels = self.setup_axes(
            x_range=[-3.2, 3.2, 1],
            y_range=[-0.5, 3.2, 1],
            x_length=4.8,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True
        )

        # Ramas de w(x) = sqrt(x^4 - 5x^2 + 4)
        # Rama izquierda: [-3.0, -2.0]
        curve_left = axes.plot(
            lambda x: np.sqrt(x**4 - 5*x**2 + 4),
            x_range=[-2.6, -2.0],
            color=THEME["curve"],
            stroke_width=2.5
        )
        # Cúpula central: [-1.0, 1.0]
        curve_center = axes.plot(
            lambda x: np.sqrt(x**4 - 5*x**2 + 4),
            x_range=[-1.0, 1.0],
            color=THEME["curve"],
            stroke_width=2.5
        )
        # Rama derecha: [2.0, 3.0]
        curve_right = axes.plot(
            lambda x: np.sqrt(x**4 - 5*x**2 + 4),
            x_range=[2.0, 2.6],
            color=THEME["curve"],
            stroke_width=2.5
        )

        lbl_w = MathTex(r"w(x) = \sqrt{x^4-5x^2+4}", font_size=12, color=THEME["curve"]).next_to(axes.c2p(0, 2.0), UP, buff=0.12)

        # Zonas prohibidas sobre el eje X (rojo tenue)
        excl_left = Line(axes.c2p(-2.0, 0), axes.c2p(-1.0, 0), color=THEME["statement_box"], stroke_width=4.5)
        excl_right = Line(axes.c2p(1.0, 0), axes.c2p(2.0, 0), color=THEME["statement_box"], stroke_width=4.5)
        lbl_excl1 = Text("Excluido", font_size=9, color=THEME["statement_box"]).next_to(axes.c2p(-1.5, 0), DOWN, buff=0.15)
        lbl_excl2 = Text("Excluido", font_size=9, color=THEME["statement_box"]).next_to(axes.c2p(1.5, 0), DOWN, buff=0.15)

        # Puntos notables (-2, 0), (-1, 0), (0, 2), (1, 0), (2, 0)
        pts = [axes.c2p(-2, 0), axes.c2p(-1, 0), axes.c2p(0, 2), axes.c2p(1, 0), axes.c2p(2, 0)]
        dots = VGroup(*[Dot(p, radius=0.055, color=THEME["highlight"]) for p in pts])

        graph_title = Text("Gráfica de w(x) y Zonas Excluidas", font_size=13, color=THEME["header_color"]).next_to(axes, UP, buff=0.15)

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
            Create(curve_left),
            Create(curve_center),
            Create(curve_right),
            Write(lbl_w),
            run_time=1.4
        )
        self.play(
            Create(excl_left),
            Create(excl_right),
            Write(lbl_excl1),
            Write(lbl_excl2),
            FadeIn(dots, scale=1.3),
            run_time=1.2
        )
        self.wait(6.0)

        # Cierre suave
        extra_mobs = [
            left_grp, axes, axes_labels, graph_title,
            curve_left, curve_center, curve_right, lbl_w,
            excl_left, excl_right, lbl_excl1, lbl_excl2, dots
        ]
        self.finish_exercise(extra_mobjects=extra_mobs)
        self.wait(0.5)
