"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.46 (Página 112 del libro / Página 131 del PDF)

Funciones reales dadas:
f: ]3, 7] → ℝ,    f(x) = 3x + 2
g: ]-3, 25] → ℝ,  g(x) = cos(x²) - 2x + 1
h: ]12, 25[ → ℝ,  h(x) = cos(x²) - 2x + 1

Definir, en caso de ser posible, g ∘ f y h ∘ f:
1. Rango de f:
   x ∈ ]3, 7] ⟹ 3 < x ≤ 7 ⟹ 9 < 3x ≤ 21 ⟹ 11 < 3x + 2 ≤ 23.
   ⟹ Rg(f) = ]11, 23].

2. Función g ∘ f:
   Rg(f) = ]11, 23] ⊆ ]-3, 25] = Dom(g).
   ⟹ SÍ EXISTE g ∘ f: ]3, 7] → ℝ,
      (g ∘ f)(x) = cos(9x² + 12x + 4) - 6x - 3.

3. Función h ∘ f:
   Rg(f) = ]11, 23] ⊈ ]12, 25[ = Dom(h) (la franja ]11, 12] no pertenece a Dom(h)).
   ⟹ Según la Definición 5.6 (Mayorga-Zambrano): NO EXISTE la función h ∘ f.
   (Con dominio restringido: Dom(h ∘ f) = ]10/3, 7]).
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_46(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.46",
            topic="Composición de Funciones y Criterio de Existencia"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Dadas f: ]3, 7] → ℝ, g: ]-3, 25] → ℝ y h: ]12, 25[ → ℝ, define en caso de ser posible g ∘ f y h ∘ f:",
            math_tex=r"f(x) = 3x+2, \quad g(x) = \cos(x^2)-2x+1, \quad h(x) = \cos(x^2)-2x+1 \implies \text{Analizar si } \operatorname{Rg}(f) \subseteq \operatorname{Dom}.",
            desc_font_size=14,
            math_font_size=13,
            read_time=4.0
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Criterio de Existencia (Def. 5.6)",
            "2/6: Rango de la Función f",
            "3/6: Composición g ∘ f (Existe)",
            "4/6: Inexistencia de h ∘ f",
            "5/6: Dominio Restringido de h ∘ f",
            "6/6: Resumen y Diagrama Métrico"
        ])

        # ==========================================================
        # PASO 1: Criterio Axiomático de Existencia
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{Definici\'on 5.6 (Mayorga-Zambrano):} \\[4pt]"
            r"&\text{Dadas } f: I \to \mathbb{R} \;\text{ y }\; g: J \to \mathbb{R}, \\[4pt]"
            r"&g \circ f \text{ est\'a bien definida } \iff \mathbf{Rg}(f) \subseteq \mathbf{Dom}(g) \\[6pt]"
            r"&\text{En tal caso: } \quad g \circ f: I \to \mathbb{R}, \quad x \mapsto g(f(x)) \\[6pt]"
            r"&\textbf{Criterio de Inexistencia (Ejemplo 5.29):} \\[4pt]"
            r"&\text{Si } \operatorname{Rg}(f) \nsubseteq \operatorname{Dom}(g), \;\text{entonces } \mathbf{NO\; EXISTE } \; g \circ f."
            r"\end{aligned}",
            font_size=17,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Criterio de Existencia (Def. 5.6):\n"
            "• Para componer g ∘ f en todo Dom(f), cada\n"
            "  imagen f(x) debe ser admisible para g.\n"
            "• Condición necesaria y suficiente:\n"
            "  Rg(f) ⊆ Dom(g).\n"
            "• Si algún elemento de Rg(f) queda fuera de\n"
            "  Dom(g), la composición global no existe."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Cálculo Exacto del Rango de f
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&f: \; ]3, 7] \to \mathbb{R}, \quad f(x) = 3x + 2 \\[5pt]"
            r"&\text{Sea } x \in \; ]3, 7] \iff 3 < x \le 7 \\[5pt]"
            r"&\text{Multiplicando por } 3 > 0: \\[3pt]"
            r"&9 < 3x \le 21 \\[5pt]"
            r"&\text{Sumando } 2: \\[3pt]"
            r"&11 < 3x + 2 \le 23 \iff 11 < f(x) \le 23 \\[6pt]"
            r"&\mathbf{Rg}(f) = \; ]11, 23]"
            r"\end{aligned}",
            font_size=18,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Rango de la Función f:\n"
            "• Como f(x) = 3x + 2 es una función afin\n"
            "  estrictamente creciente en ℝ:\n"
            "  3 < x ≤ 7 ⟹ 9 < 3x ≤ 21 ⟹ 11 < f(x) ≤ 23.\n"
            "• El extremo izquierdo x = 3 es abierto (f(3)=11).\n"
            "• El extremo derecho x = 7 es cerrado (f(7)=23).\n"
            "• Rg(f) = ]11, 23]."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], wait_time=4.8)

        # ==========================================================
        # PASO 3: Composición g ∘ f (Existe)
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\text{Verificamos la inclusi\'on para } g: \; ]-3, 25] \to \mathbb{R}: \\[4pt]"
            r"&\operatorname{Dom}(g) = \; ]-3, 25] \\[5pt]"
            r"&\text{Como } -3 < 11 \;\text{ y }\; 23 \le 25: \\[4pt]"
            r"&\mathbf{Rg}(f) = \; ]11, 23] \;\subseteq\; ]-3, 25] = \operatorname{Dom}(g) \quad \checkmark \\[6pt]"
            r"&\implies \textbf{SÍ EXISTE} \quad g \circ f: \; ]3, 7] \to \mathbb{R} \\[5pt]"
            r"&(g \circ f)(x) = \cos((3x+2)^2) - 2(3x+2) + 1 \\[4pt]"
            r"&= \cos(9x^2 + 12x + 4) - 6x - 3"
            r"\end{aligned}",
            font_size=16,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Composición g ∘ f (Existe):\n"
            "• Comparamos intervalos: ]11, 23] ⊆ ]-3, 25].\n"
            "• La condición de la Def. 5.6 se cumple\n"
            "  estrictamente para todo x ∈ Dom(f).\n"
            "• Sustituimos f(x) en la regla de g:\n"
            "  (g ∘ f)(x) = cos((3x+2)²) - 2(3x+2) + 1\n"
            "             = cos(9x² + 12x + 4) - 6x - 3."
        )

        self.morph_step(eq3, just3, box_color=THEME["success"], wait_time=5.0)

        # ==========================================================
        # PASO 4: Inexistencia de h ∘ f (Def. 5.6)
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\text{Verificamos la inclusi\'on para } h: \; ]12, 25[ \to \mathbb{R}: \\[4pt]"
            r"&\operatorname{Dom}(h) = \; ]12, 25[ \\[5pt]"
            r"&\text{Comparando: } \mathbf{Rg}(f) = \; ]11, 23] \;\nsubseteq\; ]12, 25[ \quad \boldsymbol{\times} \\[6pt]"
            r"&\text{Contraejemplo: } \text{Para } x = \tfrac{19}{6} \approx 3.167 \in \; ]3, 7]: \\[4pt]"
            r"&f(19/6) = 3(19/6) + 2 = 11.5 \notin \operatorname{Dom}(h) \\[5pt]"
            r"&\text{La franja } ]11, 12] \subset \operatorname{Rg}(f) \text{ queda excluida.} \\[6pt]"
            r"&\textbf{Conclusión: NO EXISTE } \; h \circ f"
            r"\end{aligned}",
            font_size=16,
            color=THEME["statement_box"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Inexistencia de h ∘ f:\n"
            "• Dom(h) = ]12, 25[. Sin embargo, Rg(f) = ]11, 23].\n"
            "• Puesto que 11 < 12, los valores en ]11, 12]\n"
            "  no pueden ingresar a la función h.\n"
            "• Por el criterio canónico del texto\n"
            "  (Ejemplo 5.29), NO EXISTE la función h ∘ f."
        )

        self.morph_step(eq4, just4, box_color=THEME["statement_box"], wait_time=5.0)

        # ==========================================================
        # PASO 5: Dominio Restringido para h ∘ f
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{Composici\'on en Subdominio Restringido:} \\[4pt]"
            r"&x \in \operatorname{Dom}(f) \;\land\; f(x) \in \operatorname{Dom}(h) \\[4pt]"
            r"&\iff 12 < 3x + 2 < 25 \\[3pt]"
            r"&\iff 10 < 3x < 23 \iff \frac{10}{3} < x < \frac{23}{3} \\[5pt]"
            r"&\text{Intersecando con } \operatorname{Dom}(f) = \; ]3, 7]: \\[4pt]"
            r"&x \in \; ]3, 7] \;\cap\; \left]\frac{10}{3}, \frac{23}{3}\right[ = \left]\frac{10}{3}, 7\right] \\[6pt]"
            r"&\widetilde{h \circ f}: \left]\frac{10}{3}, 7\right] \to \mathbb{R}, \quad x \mapsto \cos(9x^2+12x+4)-6x-3"
            r"\end{aligned}",
            font_size=16,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Dominio Restringido de h ∘ f:\n"
            "• Si se restrige el dominio de f al conjunto\n"
            "  {x ∈ Dom(f) : f(x) ∈ Dom(h)}:\n"
            "  12 < 3x + 2 < 25 ⟹ 10/3 < x < 23/3.\n"
            "• Al intersecar con ]3, 7], obtenemos ]10/3, 7].\n"
            "• Así se define la versión restringida."
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 6: Resumen y Diagrama Métrico de Intervalos
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Cuadro sinóptico de conclusiones
        t_title = Text("Resumen de Composición:", font_size=14, color=THEME["header_color"], weight=BOLD)
        t_rg = MathTex(r"\mathbf{Rg}(f) = \; ]11, 23]", font_size=13, color=THEME["highlight"])
        t_g_ok = MathTex(r"\mathbf{g \circ f:} \text{ SÍ EXISTE } (\operatorname{Rg}(f) \subseteq \operatorname{Dom}(g))", font_size=12, color=THEME["success"])
        t_g_rule = MathTex(r"(g \circ f)(x) = \cos(9x^2+12x+4)-6x-3", font_size=11, color=WHITE)
        t_h_no = MathTex(r"\mathbf{h \circ f:} \text{ NO EXISTE } (\operatorname{Rg}(f) \nsubseteq \operatorname{Dom}(h))", font_size=12, color=THEME["statement_box"])
        t_h_sub = MathTex(r"\text{Restringida: } \widetilde{\operatorname{Dom}} = \left]\frac{10}{3}, 7\right]", font_size=11, color=THEME["secondary"])

        info_grp = VGroup(t_title, t_rg, t_g_ok, t_g_rule, t_h_no, t_h_sub).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        info_box = SurroundingRectangle(info_grp, color=THEME["statement_box"], buff=0.18, stroke_width=1.5, corner_radius=0.08)
        left_grp = VGroup(info_box, info_grp).move_to([-3.4, -0.45, 0])

        # Panel derecho: Eje real y comparación métrica de intervalos
        # Representamos los intervalos sobre un eje horizontal de -5 a 27
        axes, axes_labels = self.setup_axes(
            x_range=[-5, 27, 5],
            y_range=[-1.0, 3.2, 1],
            x_length=4.8,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True
        )

        # 1. Dom(g) = ]-3, 25] a nivel y = 2.4
        y_g = 2.4
        line_dg = Line(axes.c2p(-3, y_g), axes.c2p(25, y_g), color=THEME["curve"], stroke_width=4.0)
        dot_dg_open = Dot(axes.c2p(-3, y_g), radius=0.05, stroke_width=1.5, stroke_color=THEME["curve"], fill_color=THEME["bg_color"])
        dot_dg_closed = Dot(axes.c2p(25, y_g), radius=0.05, color=THEME["curve"])
        lbl_dg = MathTex(r"\operatorname{Dom}(g) = \; ]-3, 25]", font_size=11, color=THEME["curve"]).next_to(axes.c2p(11, y_g), UP, buff=0.08)

        # 2. Dom(h) = ]12, 25[ a nivel y = 1.6
        y_h = 1.6
        line_dh = Line(axes.c2p(12, y_h), axes.c2p(25, y_h), color=THEME["success"], stroke_width=4.0)
        dot_dh_open1 = Dot(axes.c2p(12, y_h), radius=0.05, stroke_width=1.5, stroke_color=THEME["success"], fill_color=THEME["bg_color"])
        dot_dh_open2 = Dot(axes.c2p(25, y_h), radius=0.05, stroke_width=1.5, stroke_color=THEME["success"], fill_color=THEME["bg_color"])
        lbl_dh = MathTex(r"\operatorname{Dom}(h) = \; ]12, 25[", font_size=11, color=THEME["success"]).next_to(axes.c2p(18.5, y_h), UP, buff=0.08)

        # 3. Rg(f) = ]11, 23] a nivel y = 0.8
        y_rf = 0.8
        line_rf = Line(axes.c2p(11, y_rf), axes.c2p(23, y_rf), color=THEME["highlight"], stroke_width=4.0)
        dot_rf_open = Dot(axes.c2p(11, y_rf), radius=0.05, stroke_width=1.5, stroke_color=THEME["highlight"], fill_color=THEME["bg_color"])
        dot_rf_closed = Dot(axes.c2p(23, y_rf), radius=0.05, color=THEME["highlight"])
        lbl_rf = MathTex(r"\operatorname{Rg}(f) = \; ]11, 23]", font_size=11, color=THEME["highlight"]).next_to(axes.c2p(17, y_rf), DOWN, buff=0.08)

        # 4. Franja de conflicto ]11, 12] que descalifica a h:
        line_conflict = Line(axes.c2p(11, y_rf), axes.c2p(12, y_rf), color=THEME["statement_box"], stroke_width=6.0)
        lbl_conflict = Text("]11, 12] ⊈ Dom(h)", font_size=9, color=THEME["statement_box"], weight=BOLD).next_to(axes.c2p(11.5, y_rf), UP, buff=0.1)

        graph_title = Text("Comparación de Dominios y Rango", font_size=13, color=THEME["header_color"]).next_to(axes, UP, buff=0.15)

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
            Create(line_dg),
            FadeIn(dot_dg_open),
            FadeIn(dot_dg_closed),
            Write(lbl_dg),
            run_time=1.2
        )
        self.play(
            Create(line_dh),
            FadeIn(dot_dh_open1),
            FadeIn(dot_dh_open2),
            Write(lbl_dh),
            run_time=1.2
        )
        self.play(
            Create(line_rf),
            FadeIn(dot_rf_open),
            FadeIn(dot_rf_closed),
            Write(lbl_rf),
            run_time=1.2
        )
        self.play(
            Create(line_conflict),
            Write(lbl_conflict),
            run_time=1.0
        )
        self.wait(6.0)

        # Cierre suave
        extra_mobs = [
            left_grp, axes, axes_labels, graph_title,
            line_dg, dot_dg_open, dot_dg_closed, lbl_dg,
            line_dh, dot_dh_open1, dot_dh_open2, lbl_dh,
            line_rf, dot_rf_open, dot_rf_closed, lbl_rf,
            line_conflict, lbl_conflict
        ]
        self.finish_exercise(extra_mobjects=extra_mobs)
        self.wait(0.5)
