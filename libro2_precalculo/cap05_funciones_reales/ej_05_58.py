"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.58 (Página 115 del libro / Página 134 del PDF)

Dada f(x) = (1 + x) / (1 - x):
1. Resolver f(x) = 0:
   ⟹ 1 + x = 0 ∧ 1 - x ≠ 0 ⟹ x = -1. CS₁ = {-1}.

2. Determinar el conjunto:
   I = { (x, y) ∈ ℝ² : f(x) + f(y) = f((x + y)/(1 + xy)) }
   ⟹ 2(1 - xy) / ((1 - x)(1 - y)) = (1 + x)(1 + y) / ((1 - x)(1 - y))
   ⟹ 2 - 2xy = 1 + x + y + xy ⟹ 3xy + x + y - 1 = 0
   ⟹ y = (1 - x) / (3x + 1) (hipérbola equilátera rotada).
   Exclusiones: x ≠ -1/3, x ≠ 0 (y ≠ 1), x ≠ 1, x ≠ 2 ± √5 (1 + xy ≠ 0).
   Punto notable: (-1, -1) ∈ I (donde f(-1) + f(-1) = 0 = f(-1)).
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_58(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.58",
            topic="Ecuaciones Funcionales y Relación Homográfica"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Dada f(x) = (1 + x)/(1 - x), resuelve f(x) = 0 y determina el conjunto de pares (x, y) ∈ ℝ²:",
            math_tex=r"1.\; f(x) = 0, \; x \in \mathbb{R}; \qquad 2.\; I = \left\{ (x, y) \in \mathbb{R}^2 : f(x) + f(y) = f\left(\frac{x+y}{1+xy}\right) \right\}.",
            desc_font_size=14,
            math_font_size=13,
            read_time=4.0
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Resolución de f(x) = 0",
            "2/6: Condiciones de Existencia en ℝ²",
            "3/6: Deducción de Miembros LHS y RHS",
            "4/6: Ecuación de la Hipérbola",
            "5/6: Puntos Excluidos y Par (-1, -1)",
            "6/6: Resumen y Gráfica del Conjunto I"
        ])

        # ==========================================================
        # PASO 1: Resolución de f(x) = 0
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Resolución de } f(x) = 0: \\[4pt]"
            r"&f(x) = \frac{1+x}{1-x}, \quad \operatorname{Dom}(f) = \mathbb{R} \setminus \{1\} \\[5pt]"
            r"&\frac{1+x}{1-x} = 0 \iff 1 + x = 0 \;\land\; 1 - x \neq 0 \\[4pt]"
            r"&\iff x = -1 \;\land\; x \neq 1 \\[6pt]"
            r"&\textbf{Conjunto Solución:} \quad \mathbf{CS_1} = \{-1\} \\[5pt]"
            r"&\text{Cero \'unico de la funci\'on homogr\'afica: } f(-1) = 0"
            r"\end{aligned}",
            font_size=17,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Resolución de f(x) = 0:\n"
            "• El dominio exige denominador no nulo: x ≠ 1.\n"
            "• Una fracción se anula si y solo si su\n"
            "  numerador es cero: 1 + x = 0 ⟹ x = -1.\n"
            "• Como -1 ≠ 1, x = -1 es la única raíz real.\n"
            "• CS₁ = {-1}."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Condiciones de Existencia de I
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Condiciones de Existencia del Conjunto } I: \\[4pt]"
            r"&I = \left\{ (x, y) \in \mathbb{R}^2 : f(x) + f(y) = f\left(\frac{x+y}{1+xy}\right) \right\} \\[6pt]"
            r"&\text{Para que todas las evaluaciones existan en } \mathbb{R}: \\[4pt]"
            r"&1)\; x \neq 1 \;\text{ y }\; y \neq 1 \quad (\text{por } \operatorname{Dom}(f)) \\[3pt]"
            r"&2)\; 1 + xy \neq 0 \iff xy \neq -1 \quad (\text{denominador interno}) \\[3pt]"
            r"&3)\; \frac{x+y}{1+xy} \neq 1 \iff (1 - x)(1 - y) \neq 0 \quad (\text{garantizado por } 1)"
            r"\end{aligned}",
            font_size=16,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Condiciones de Existencia de I:\n"
            "• Se deben cumplir simultáneamente:\n"
            "  a) x ≠ 1 e y ≠ 1 para que f(x) y f(y) existan.\n"
            "  b) 1 + xy ≠ 0 para poder evaluar el argumento.\n"
            "  c) El argumento no debe ser 1; esto equivale\n"
            "     a (1 - x)(1 - y) ≠ 0, ya cubierto por (a)."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], wait_time=4.8)

        # ==========================================================
        # PASO 3: Deducción de Miembros LHS y RHS
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{Miembro Izquierdo (Suma):} \\[3pt]"
            r"&f(x) + f(y) = \frac{1+x}{1-x} + \frac{1+y}{1-y} = \frac{(1+x)(1-y) + (1+y)(1-x)}{(1-x)(1-y)} \\[4pt]"
            r"&= \frac{(1 - y + x - xy) + (1 - x + y - xy)}{(1-x)(1-y)} = \mathbf{\frac{2(1 - xy)}{(1-x)(1-y)}} \\[6pt]"
            r"&\textbf{Miembro Derecho (Evaluaci\'on):} \\[3pt]"
            r"&f\left(\frac{x+y}{1+xy}\right) = \frac{1 + \frac{x+y}{1+xy}}{1 - \frac{x+y}{1+xy}} = \frac{1 + xy + x + y}{1 + xy - x - y} = \mathbf{\frac{(1+x)(1+y)}{(1-x)(1-y)}}"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Deducción de Miembros LHS y RHS:\n"
            "• Sumamos las fracciones de f(x) y f(y):\n"
            "  LHS = 2(1 - xy) / ((1 - x)(1 - y)).\n"
            "• Simplificamos el cociente compuesto RHS:\n"
            "  numerador: (1 + x)(1 + y),\n"
            "  denominador: (1 - x)(1 - y).\n"
            "• Ambos miembros comparten el denominador común."
        )

        self.morph_step(eq3, just3, box_color=THEME["success"], wait_time=5.0)

        # ==========================================================
        # PASO 4: Ecuación de la Hipérbola
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\text{Igualando miembros con } (1-x)(1-y) \neq 0: \\[4pt]"
            r"&2(1 - xy) = (1 + x)(1 + y) \\[4pt]"
            r"&2 - 2xy = 1 + x + y + xy \\[5pt]"
            r"&\iff \mathbf{3xy + x + y - 1 = 0} \\[6pt]"
            r"&\text{Despejando } y \text{ en funci\'on de } x: \\[4pt]"
            r"&y(3x + 1) = 1 - x \iff \mathbf{y = \frac{1 - x}{3x + 1}} \\[5pt]"
            r"&\text{Curva sim\'etrica: } x = \frac{1 - y}{3y + 1} \quad (\text{Hip\'erbola equil\'atera rotada})"
            r"\end{aligned}",
            font_size=16,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Ecuación de la Hipérbola:\n"
            "• Al simplificar denominadores, la igualdad se reduce a:\n"
            "  2 - 2xy = 1 + x + y + xy ⟹ 3xy + x + y - 1 = 0.\n"
            "• Es simétrica respecto al intercambio de x e y.\n"
            "• Despejando y obtenemos la función racional:\n"
            "  y = (1 - x) / (3x + 1).\n"
            "• Asíntotas en x = -1/3 e y = -1/3."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 5: Puntos Excluidos y Par Notable (-1, -1)
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{Puntos Excluidos de la Curva } y = \frac{1-x}{3x+1}: \\[3pt]"
            r"&\bullet\; 3x + 1 = 0 \implies x = -1/3 \quad (\text{as\'intota vertical}) \\[2pt]"
            r"&\bullet\; y = 1 \implies \frac{1-x}{3x+1} = 1 \implies x = 0 \quad (\text{excluye } (0, 1)) \\[2pt]"
            r"&\bullet\; x = 1 \implies y = 0 \quad (\text{excluye } (1, 0) \text{ por } x \neq 1) \\[2pt]"
            r"&\bullet\; 1 + xy = 0 \implies x = 2 \pm \sqrt{5} \\[5pt]"
            r"&\textbf{Punto Notable } (-1, -1) \in I: \\[4pt]"
            r"&\text{Para } x = -1 \implies y = \frac{1 - (-1)}{3(-1)+1} = \frac{2}{-2} = -1 \\[3pt]"
            r"&f(-1) + f(-1) = 0 + 0 = 0 = f\left(\tfrac{-2}{2}\right) = f(-1) \quad \checkmark"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Puntos Excluidos y Par (-1, -1):\n"
            "• Puntos abiertos retirados:\n"
            "  (0, 1) y (1, 0) por no pertenecer al dominio.\n"
            "  x = -1/3 por anulación de denominador.\n"
            "  x = 2 ± √5 donde 1 + xy = 0.\n"
            "• Conexión notable con el Ítem 1:\n"
            "  El par (-1, -1) satisface f(-1)+f(-1) = 0 = f(-1)."
        )

        self.morph_step(eq5, just5, box_color=THEME["statement_box"], wait_time=5.0)

        # ==========================================================
        # PASO 6: Resumen y Gráfica del Conjunto I
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen formal
        t_title = Text("Resumen del Ejercicio 5.58:", font_size=13, color=THEME["header_color"], weight=BOLD)
        t_sol1 = MathTex(r"\mathbf{1.\;} f(x) = 0 \iff \mathbf{CS_1 = \{-1\}}", font_size=12, color=THEME["highlight"])
        t_set_I = MathTex(r"\mathbf{2.\;} I = \left\{\left(x, \tfrac{1-x}{3x+1}\right) : x \notin \left\{-\tfrac{1}{3}, 0, 1, 2\pm\sqrt{5}\right\}\right\}", font_size=11, color=THEME["success"])
        t_eq_hyp = MathTex(r"3xy + x + y - 1 = 0 \quad (\text{Hip\'erbola})", font_size=11, color=THEME["curve"])
        t_pt_not = MathTex(r"(-1, -1) \in I \quad (f(-1) = 0)", font_size=11, color=THEME["secondary"])
        t_note_mult = Text("• Nota: f(x)·f(y) = f((x+y)/(1+xy)) es identidad.", font_size=10, color=WHITE)

        info_grp = VGroup(t_title, t_sol1, t_set_I, t_eq_hyp, t_pt_not, t_note_mult).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        info_box = SurroundingRectangle(info_grp, color=THEME["statement_box"], buff=0.18, stroke_width=1.5, corner_radius=0.08)
        left_grp = VGroup(info_box, info_grp).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos para graficar la hipérbola
        axes, axes_labels = self.setup_axes(
            x_range=[-3.0, 3.0, 1],
            y_range=[-3.0, 3.0, 1],
            x_length=4.8,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True
        )

        # Rama izquierda: [-2.8, -0.38]
        branch_left = axes.plot(
            lambda x: (1 - x)/(3*x + 1),
            x_range=[-2.8, -0.38],
            color=THEME["curve"],
            stroke_width=2.5
        )
        # Rama derecha: [-0.28, 2.8]
        branch_right = axes.plot(
            lambda x: (1 - x)/(3*x + 1),
            x_range=[-0.28, 2.8],
            color=THEME["curve"],
            stroke_width=2.5
        )

        # Asíntota vertical en x = -1/3
        asym_v = DashedLine(axes.c2p(-1/3, -2.8), axes.c2p(-1/3, 2.8), color=THEME["statement_box"], stroke_width=1.5)
        # Asíntota horizontal en y = -1/3
        asym_h = DashedLine(axes.c2p(-2.8, -1/3), axes.c2p(2.8, -1/3), color=THEME["statement_box"], stroke_width=1.5)

        # Punto notable (-1, -1)
        dot_notable = Dot(axes.c2p(-1.0, -1.0), radius=0.065, color=THEME["highlight"])
        lbl_notable = MathTex(r"(-1, -1)", font_size=10, color=THEME["highlight"]).next_to(dot_notable, DL, buff=0.08)

        # Puntos abiertos excluidos (0, 1) y (1, 0)
        dot_excl1 = Dot(axes.c2p(0.0, 1.0), radius=0.06, stroke_width=1.5, stroke_color=THEME["statement_box"], fill_color=THEME["bg_color"])
        dot_excl2 = Dot(axes.c2p(1.0, 0.0), radius=0.06, stroke_width=1.5, stroke_color=THEME["statement_box"], fill_color=THEME["bg_color"])

        graph_title = Text("Hipérbola del Conjunto I", font_size=13, color=THEME["header_color"]).next_to(axes, UP, buff=0.15)

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
            Create(asym_v),
            Create(asym_h),
            run_time=1.0
        )
        self.play(
            Create(branch_left),
            Create(branch_right),
            FadeIn(dot_notable),
            Write(lbl_notable),
            FadeIn(dot_excl1),
            FadeIn(dot_excl2),
            run_time=1.5
        )
        self.wait(6.5)

        # Cierre suave
        extra_mobs = [
            left_grp, axes, axes_labels, graph_title,
            asym_v, asym_h, branch_left, branch_right,
            dot_notable, lbl_notable, dot_excl1, dot_excl2
        ]
        self.finish_exercise(extra_mobjects=extra_mobs)
        self.wait(0.5)
