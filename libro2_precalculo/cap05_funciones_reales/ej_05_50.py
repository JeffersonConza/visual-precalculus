"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.50 (Página 113 del libro / Página 132 del PDF)

¿Cuál es la única función real que es, al mismo tiempo, par e impar?

Resolución deductiva:
1. Sea f: D → ℝ una función con dominio simétrico D ⊆ ℝ.
2. f es par  ⟺ ∀x ∈ D: f(-x) = f(x).
3. f es impar ⟺ ∀x ∈ D: f(-x) = -f(x).
4. Si f es simultáneamente par e impar:
   f(x) = f(-x) = -f(x) ⟹ f(x) = -f(x) ⟹ 2f(x) = 0 ⟹ f(x) = 0, ∀x ∈ D.
5. Conclusión:
   La única función real que es al mismo tiempo par e impar es la función nula:
   f₀: ℝ → ℝ, x ↦ 0 (o f₀: D → ℝ, x ↦ 0 en cualquier dominio simétrico D).
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_50(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.50",
            topic="Unicidad de la Función Simultáneamente Par e Impar"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Determinación y demostración formal de paridad simultánea en funciones reales:",
            math_tex=r"\text{¿Cuál es la única función real } f: D \to \mathbb{R} \text{ que es, al mismo tiempo, par e impar?}",
            desc_font_size=14,
            math_font_size=14,
            read_time=4.0
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Definiciones de Paridad en ℝ",
            "2/6: Hipótesis de Paridad Simultánea",
            "3/6: Deducción Algebraica Rigurosa",
            "4/6: Existencia y Unicidad de la Función Nula",
            "5/6: Dualidad Geométrica de Simetrías",
            "6/6: Resumen y Representación Cartesiana"
        ])

        # ==========================================================
        # PASO 1: Definiciones Axiomáticas de Paridad
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\text{Sea } f: D \to \mathbb{R} \text{ con dominio sim\'etrico: } \forall x \in D, -x \in D. \\[6pt]"
            r"&\textbf{1. Funci\'on Par (Definici\'on 5.4):} \\[4pt]"
            r"&\forall x \in D: \quad f(-x) = f(x) \\[8pt]"
            r"&\textbf{2. Funci\'on Impar (Definici\'on 5.4):} \\[4pt]"
            r"&\forall x \in D: \quad f(-x) = -f(x)"
            r"\end{aligned}",
            font_size=17,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Definiciones de Paridad en ℝ:\n"
            "• El dominio D debe ser simétrico respecto al\n"
            "  origen: si x ∈ D, entonces -x ∈ D.\n"
            "• Par: la función no cambia de signo bajo la\n"
            "  inversión del argumento (f(-x) = f(x)).\n"
            "• Impar: la función invierte su signo bajo la\n"
            "  inversión del argumento (f(-x) = -f(x))."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Hipótesis de Paridad Simultánea
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\text{Supongamos que } f: D \to \mathbb{R} \text{ es, al mismo tiempo,} \\[4pt]"
            r"&\text{par e impar en todo su dominio } D. \\[6pt]"
            r"&\text{Entonces, para todo } x \in D \text{ se cumplen ambas leyes:} \\[6pt]"
            r"&\begin{cases} f(-x) = f(x) \quad &(E_1: \text{por paridad}) \\[6pt] f(-x) = -f(x) \quad &(E_2: \text{por imparidad}) \end{cases}"
            r"\end{aligned}",
            font_size=17,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Hipótesis de Paridad Simultánea:\n"
            "• Formulamos la conjunción lógica:\n"
            "  f es par ∧ f es impar.\n"
            "• Cada punto x ∈ D evalúa f(-x) simultáneamente\n"
            "  a f(x) y a -f(x).\n"
            "• Esto establece un sistema directo de ligaduras\n"
            "  algebraicas sobre la imagen f(x)."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], wait_time=4.8)

        # ==========================================================
        # PASO 3: Deducción Algebraica Rigurosa
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\text{Por la propiedad transitiva de la igualdad sobre } f(-x): \\[5pt]"
            r"&f(x) = f(-x) = -f(x) \implies f(x) = -f(x) \\[6pt]"
            r"&\text{Sumando } f(x) \text{ a ambos miembros en el cuerpo } \mathbb{R}: \\[4pt]"
            r"&f(x) + f(x) = -f(x) + f(x) \\[4pt]"
            r"&\iff 2f(x) = 0 \\[6pt]"
            r"&\text{Multiplicando por el inverso } \frac{1}{2} \neq 0: \\[4pt]"
            r"&\mathbf{f(x) = 0} \quad \forall x \in D"
            r"\end{aligned}",
            font_size=17,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Deducción Algebraica Rigurosa:\n"
            "• Transitividad: si f(x) = f(-x) y f(-x) = -f(x),\n"
            "  entonces f(x) = -f(x).\n"
            "• En ℝ, el único número que es igual a su opuesto\n"
            "  aditivo es el cero:\n"
            "  2f(x) = 0 ⟹ f(x) = 0.\n"
            "• Esto debe ser válido para todo x en el dominio."
        )

        self.morph_step(eq3, just3, box_color=THEME["success"], wait_time=5.0)

        # ==========================================================
        # PASO 4: Existencia y Unicidad de la Función Nula
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Existencia (Comprobaci\'on Directa):} \\[4pt]"
            r"&\text{Sea } f_0(x) = 0. \text{ Para todo } x \in D: \\[3pt]"
            r"&f_0(-x) = 0 = f_0(x) \implies f_0 \text{ es par.} \\[3pt]"
            r"&f_0(-x) = 0 = -0 = -f_0(x) \implies f_0 \text{ es impar.} \\[6pt]"
            r"&\textbf{2. Unicidad:} \\[4pt]"
            r"&\text{Si } g \text{ es par e impar } \implies g(x) = 0 = f_0(x) \; \forall x \in D. \\[6pt]"
            r"&\textbf{Conclusión: La Función Nula} \\[4pt]"
            r"&f_0: \mathbb{R} \to \mathbb{R}, \quad x \mapsto 0"
            r"\end{aligned}",
            font_size=16,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Existencia y Unicidad:\n"
            "• Existencia: f₀(x) = 0 satisface 0 = 0 y 0 = -0;\n"
            "  es simultáneamente par e impar.\n"
            "• Unicidad: toda función que satisfaga ambas\n"
            "  propiedades colapsa algebraicamente a f₀(x) = 0.\n"
            "• La solución es única en cualquier dominio\n"
            "  simétrico D (en particular D = ℝ)."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 5: Dualidad Geométrica de Simetrías
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{Dualidad Geom\'etrica en el Plano } \mathbb{R}^2: \\[5pt]"
            r"&\text{Simetr\'ia Par: Reflexi\'on axial respecto al eje } Y: \\[3pt]"
            r"&(x, y) \mapsto (-x, y) \\[5pt]"
            r"&\text{Simetr\'ia Impar: Rotaci\'on de } 180^\circ \text{ respecto a } (0, 0): \\[3pt]"
            r"&(x, y) \mapsto (-x, -y) \\[6pt]"
            r"&\textbf{Composici\'on de simetr\'ias } \implies \text{Reflexi\'on en eje } X: \\[4pt]"
            r"&(x, y) \mapsto (x, -y) \implies y = -y \implies y = 0 \\[5pt]"
            r"&\text{Criterio de la recta vertical: la gr\'afica es la recta } y = 0."
            r"\end{aligned}",
            font_size=16,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Dualidad Geométrica de Simetrías:\n"
            "• La simetría par es una reflexión respecto al eje Y.\n"
            "• La simetría impar es una simetría central en (0,0).\n"
            "• Poseer ambas equivale a poseer simetría axial\n"
            "  respecto al eje X: (x, y) = (x, -y).\n"
            "• Para que una relación sea función real,\n"
            "  debe cumplir y = -y ⟹ y = 0."
        )

        self.morph_step(eq5, just5, box_color=THEME["statement_box"], wait_time=4.8)

        # ==========================================================
        # PASO 6: Resumen y Representación Cartesiana
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Cuadro sinóptico de conclusiones
        t_title = Text("Resumen de Paridad Simultánea:", font_size=14, color=THEME["header_color"], weight=BOLD)
        t_eq = MathTex(r"f(x) = f(-x) = -f(x) \implies 2f(x) = 0", font_size=13, color=THEME["highlight"])
        t_ans = MathTex(r"\mathbf{f_0(x) = 0} \quad \textbf{(Función Nula)}", font_size=14, color=THEME["success"])
        t_dom = MathTex(r"f_0: \mathbb{R} \to \mathbb{R}, \quad x \mapsto 0", font_size=13, color=WHITE)
        t_geom1 = Text("• Simetría axial respecto al eje Y.", font_size=11, color=THEME["curve"])
        t_geom2 = Text("• Simetría central respecto al origen (0,0).", font_size=11, color=THEME["secondary"])
        t_geom3 = Text("• Gráfica idéntica al propio eje X.", font_size=11, color=THEME["statement_box"], weight=BOLD)

        info_grp = VGroup(t_title, t_eq, t_ans, t_dom, t_geom1, t_geom2, t_geom3).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        info_box = SurroundingRectangle(info_grp, color=THEME["statement_box"], buff=0.18, stroke_width=1.5, corner_radius=0.08)
        left_grp = VGroup(info_box, info_grp).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos y gráfica de y = 0
        axes, axes_labels = self.setup_axes(
            x_range=[-3.2, 3.2, 1],
            y_range=[-2.2, 2.2, 1],
            x_length=4.8,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True
        )

        # Gráfica de f₀(x) = 0: recta horizontal gruesa sobre el eje X
        curve_null = axes.plot(
            lambda x: 0,
            x_range=[-3.0, 3.0],
            color=THEME["success"],
            stroke_width=4.5
        )

        lbl_null = MathTex(r"f_0(x) = 0", font_size=14, color=THEME["success"]).next_to(axes.c2p(1.5, 0), UP, buff=0.15)

        # Origen como centro de simetría (0, 0)
        dot_origin = Dot(axes.c2p(0, 0), radius=0.07, color=THEME["highlight"])
        lbl_origin = MathTex(r"(0, 0)", font_size=11, color=THEME["highlight"]).next_to(dot_origin, DL, buff=0.1)

        # Flechas de simetría axial respecto al eje Y
        sym_left = Dot(axes.c2p(-1.8, 0), radius=0.05, color=THEME["curve"])
        sym_right = Dot(axes.c2p(1.8, 0), radius=0.05, color=THEME["curve"])
        arc_axial = CurvedDoubleArrow(
            axes.c2p(-1.8, 0.4), axes.c2p(1.8, 0.4),
            color=THEME["curve"],
            tip_length=0.15
        )
        lbl_axial = Text("Simetría Axial (Par)", font_size=10, color=THEME["curve"]).next_to(arc_axial, UP, buff=0.08)

        graph_title = Text("La Recta y = 0 en el Plano ℝ²", font_size=13, color=THEME["header_color"]).next_to(axes, UP, buff=0.15)

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
            Create(curve_null),
            Write(lbl_null),
            FadeIn(dot_origin, scale=1.4),
            Write(lbl_origin),
            run_time=1.4
        )
        self.play(
            FadeIn(sym_left),
            FadeIn(sym_right),
            Create(arc_axial),
            Write(lbl_axial),
            run_time=1.2
        )
        self.wait(6.0)

        # Cierre suave
        extra_mobs = [
            left_grp, axes, axes_labels, graph_title,
            curve_null, lbl_null, dot_origin, lbl_origin,
            sym_left, sym_right, arc_axial, lbl_axial
        ]
        self.finish_exercise(extra_mobjects=extra_mobs)
        self.wait(0.5)
