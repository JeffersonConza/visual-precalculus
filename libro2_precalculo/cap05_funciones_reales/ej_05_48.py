"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.48 (Página 113 del libro / Página 132 del PDF)

Funciones reales dadas:
f: ]-2, 2] → ℝ,    f(x) = -5x - 1
g: ]-13, 40] → ℝ,  g(x) = x³ - √|x|
h: ]-11, 9[ → ℝ,   h(x) = x³ - √|x|

Definir, en caso de ser posible, g ∘ f y h ∘ f:
1. Rango de f:
   x ∈ ]-2, 2] ⟹ -2 < x ≤ 2 ⟹ 10 > -5x ≥ -10 ⟹ -11 ≤ -5x - 1 < 9.
   ⟹ Rg(f) = [-11, 9[.

2. Función g ∘ f:
   Rg(f) = [-11, 9[ ⊆ ]-13, 40] = Dom(g).
   ⟹ SÍ EXISTE g ∘ f: ]-2, 2] → ℝ,
      (g ∘ f)(x) = -(5x + 1)³ - √|5x + 1| = -125x³ - 75x² - 15x - 1 - √|5x + 1|.

3. Función h ∘ f:
   Rg(f) = [-11, 9[ ⊈ ]-11, 9[ = Dom(h).
   El punto frontera -11 ∈ Rg(f) (para x = 2) no pertenece al abierto Dom(h).
   ⟹ Según la Definición 5.6 (Mayorga-Zambrano): NO EXISTE la función h ∘ f.
   (Con subdominio restringido: Dom(h ∘ f) = ]-2, 2[).
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_48(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.48",
            topic="Composición de Funciones y Puntos Frontera"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Dadas f: ]-2, 2] → ℝ, g: ]-13, 40] → ℝ y h: ]-11, 9[ → ℝ, define en caso de ser posible g ∘ f y h ∘ f:",
            math_tex=r"f(x) = -5x-1, \quad g(x) = x^3-\sqrt{|x|}, \quad h(x) = x^3-\sqrt{|x|} \implies \text{Verificar si } \operatorname{Rg}(f) \subseteq \operatorname{Dom}.",
            desc_font_size=14,
            math_font_size=13,
            read_time=4.0
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Criterio de Existencia (Def. 5.6)",
            "2/6: Rango Decreciente de f",
            "3/6: Composición g ∘ f (Existe)",
            "4/6: Inexistencia de h ∘ f (Punto -11)",
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
            r"&\text{Si } \operatorname{Rg}(f) \nsubseteq \operatorname{Dom}(g), \;\text{entonces } \textbf{NO EXISTE } \; g \circ f."
            r"\end{aligned}",
            font_size=17,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Criterio de Existencia (Def. 5.6):\n"
            "• Para definir g ∘ f sobre todo el dominio de f,\n"
            "  la imagen Rg(f) debe estar contenida en Dom(g).\n"
            "• Si tan solo un punto de Rg(f) no pertenece a\n"
            "  Dom(g), la composición global no existe.\n"
            "• Vigilamos especialmente las fronteras de los\n"
            "  intervalos abiertos y cerrados."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Cálculo Exacto del Rango Decreciente de f
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&f: \; ]-2, 2] \to \mathbb{R}, \quad f(x) = -5x - 1 \\[5pt]"
            r"&\text{Sea } x \in \; ]-2, 2] \iff -2 < x \le 2 \\[5pt]"
            r"&\text{Multiplicando por } -5 < 0 \text{ (se invierte el orden):} \\[3pt]"
            r"&10 > -5x \ge -10 \iff -10 \le -5x < 10 \\[5pt]"
            r"&\text{Restando } 1: \\[3pt]"
            r"&-11 \le -5x - 1 < 9 \iff -11 \le f(x) < 9 \\[6pt]"
            r"&\mathbf{Rg}(f) = [-11, 9["
            r"\end{aligned}",
            font_size=17,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Rango Decreciente de f:\n"
            "• La pendiente negativa m = -5 invierte la\n"
            "  orientación de las desigualdades:\n"
            "  -2 < x ≤ 2 ⟹ -10 ≤ -5x < 10 ⟹ -11 ≤ f(x) < 9.\n"
            "• El extremo x = 2 aporta el valor cerrado f(2) = -11.\n"
            "• El extremo abierto x = -2 da la cota superior 9.\n"
            "• Rg(f) = [-11, 9[."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], wait_time=5.0)

        # ==========================================================
        # PASO 3: Composición g ∘ f (Existe)
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\text{Verificamos para } g: \; ]-13, 40] \to \mathbb{R}: \\[4pt]"
            r"&\operatorname{Dom}(g) = \; ]-13, 40] \\[5pt]"
            r"&\text{Como } -13 < -11 \;\text{ y }\; 9 \le 40: \\[4pt]"
            r"&\mathbf{Rg}(f) = [-11, 9[ \;\subseteq\; ]-13, 40] = \operatorname{Dom}(g) \quad \checkmark \\[6pt]"
            r"&\implies \textbf{SÍ EXISTE} \quad g \circ f: \; ]-2, 2] \to \mathbb{R} \\[5pt]"
            r"&(g \circ f)(x) = (-5x-1)^3 - \sqrt{|-5x-1|} \\[4pt]"
            r"&= -(5x+1)^3 - \sqrt{|5x+1|} \\[4pt]"
            r"&= -125x^3 - 75x^2 - 15x - 1 - \sqrt{|5x+1|}"
            r"\end{aligned}",
            font_size=16,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Composición g ∘ f (Existe):\n"
            "• [-11, 9[ está totalmente contenido en ]-13, 40].\n"
            "• Se cumple la condición de inclusión de la\n"
            "  Definición 5.6 en todo el dominio.\n"
            "• Regla de correspondencia evaluada:\n"
            "  (g ∘ f)(x) = -(5x + 1)³ - √|5x + 1|\n"
            "             = -125x³ - 75x² - 15x - 1 - √|5x + 1|."
        )

        self.morph_step(eq3, just3, box_color=THEME["success"], wait_time=5.0)

        # ==========================================================
        # PASO 4: Inexistencia de h ∘ f (Punto Frontera -11)
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\text{Verificamos para } h: \; ]-11, 9[ \to \mathbb{R}: \\[4pt]"
            r"&\operatorname{Dom}(h) = \; ]-11, 9[ \\[5pt]"
            r"&\text{Comparando: } \mathbf{Rg}(f) = [-11, 9[ \;\nsubseteq\; ]-11, 9[ \quad \boldsymbol{\times} \\[6pt]"
            r"&\textbf{Punto de conflicto:} \quad \text{Para } x = 2 \in \operatorname{Dom}(f): \\[4pt]"
            r"&f(2) = -5(2) - 1 = -11 \notin \; ]-11, 9[ = \operatorname{Dom}(h) \\[5pt]"
            r"&h(f(2)) = h(-11) \text{ no est\'a definido.} \\[6pt]"
            r"&\textbf{Conclusión: NO EXISTE } \; h \circ f"
            r"\end{aligned}",
            font_size=16,
            color=THEME["statement_box"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Inexistencia de h ∘ f (Punto -11):\n"
            "• Dom(h) = ]-11, 9[ es estrictamente abierto.\n"
            "• Sin embargo, Rg(f) = [-11, 9[ contiene a -11.\n"
            "• En x = 2 ∈ Dom(f), f(2) = -11 ∉ Dom(h).\n"
            "• Por la Definición 5.6 y el Ejemplo 5.29,\n"
            "  NO EXISTE la función compuesta h ∘ f."
        )

        self.morph_step(eq4, just4, box_color=THEME["statement_box"], wait_time=5.0)

        # ==========================================================
        # PASO 5: Dominio Restringido para h ∘ f
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{Composici\'on en Subdominio Restringido:} \\[4pt]"
            r"&x \in \operatorname{Dom}(f) \;\land\; f(x) \in \operatorname{Dom}(h) \\[4pt]"
            r"&\iff -11 < -5x - 1 < 9 \\[3pt]"
            r"&\iff -10 < -5x < 10 \iff -2 < x < 2 \\[5pt]"
            r"&\text{Intersecando con } \operatorname{Dom}(f) = \; ]-2, 2]: \\[4pt]"
            r"&x \in \; ]-2, 2] \;\cap\; ]-2, 2[ = \; ]-2, 2[ \\[6pt]"
            r"&\widetilde{h \circ f}: \; ]-2, 2[ \; \to \mathbb{R}, \quad x \mapsto -(5x+1)^3 - \sqrt{|5x+1|}"
            r"\end{aligned}",
            font_size=16,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Dominio Restringido de h ∘ f:\n"
            "• Excluyendo el punto conflictivo x = 2:\n"
            "  -11 < -5x - 1 < 9 ⟹ -2 < x < 2.\n"
            "• Al intersecar con ]-2, 2], obtenemos ]-2, 2[.\n"
            "• La función restringida retira únicamente\n"
            "  el extremo derecho del dominio."
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 6: Resumen y Diagrama Métrico de Intervalos
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Cuadro sinóptico de conclusiones
        t_title = Text("Resumen de Composición:", font_size=14, color=THEME["header_color"], weight=BOLD)
        t_rg = MathTex(r"\mathbf{Rg}(f) = [-11, 9[", font_size=13, color=THEME["highlight"])
        t_g_ok = MathTex(r"\mathbf{g \circ f:} \text{ SÍ EXISTE } (\operatorname{Rg}(f) \subseteq \operatorname{Dom}(g))", font_size=12, color=THEME["success"])
        t_g_rule = MathTex(r"(g \circ f)(x) = -(5x+1)^3-\sqrt{|5x+1|}", font_size=11, color=WHITE)
        t_h_no = MathTex(r"\mathbf{h \circ f:} \text{ NO EXISTE } (\operatorname{Rg}(f) \nsubseteq \operatorname{Dom}(h))", font_size=12, color=THEME["statement_box"])
        t_h_sub = MathTex(r"\text{Restringida: } \widetilde{\operatorname{Dom}} = \; ]-2, 2[", font_size=11, color=THEME["secondary"])

        info_grp = VGroup(t_title, t_rg, t_g_ok, t_g_rule, t_h_no, t_h_sub).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        info_box = SurroundingRectangle(info_grp, color=THEME["statement_box"], buff=0.18, stroke_width=1.5, corner_radius=0.08)
        left_grp = VGroup(info_box, info_grp).move_to([-3.4, -0.45, 0])

        # Panel derecho: Eje real y comparación métrica de intervalos
        axes, axes_labels = self.setup_axes(
            x_range=[-15, 42, 10],
            y_range=[-1.0, 3.2, 1],
            x_length=4.8,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True
        )

        # 1. Dom(g) = ]-13, 40] a nivel y = 2.4
        y_g = 2.4
        line_dg = Line(axes.c2p(-13, y_g), axes.c2p(40, y_g), color=THEME["curve"], stroke_width=4.0)
        dot_dg_open = Dot(axes.c2p(-13, y_g), radius=0.05, stroke_width=1.5, stroke_color=THEME["curve"], fill_color=THEME["bg_color"])
        dot_dg_closed = Dot(axes.c2p(40, y_g), radius=0.05, color=THEME["curve"])
        lbl_dg = MathTex(r"\operatorname{Dom}(g) = \; ]-13, 40]", font_size=11, color=THEME["curve"]).next_to(axes.c2p(14, y_g), UP, buff=0.08)

        # 2. Dom(h) = ]-11, 9[ a nivel y = 1.6
        y_h = 1.6
        line_dh = Line(axes.c2p(-11, y_h), axes.c2p(9, y_h), color=THEME["success"], stroke_width=4.0)
        dot_dh_open1 = Dot(axes.c2p(-11, y_h), radius=0.05, stroke_width=1.5, stroke_color=THEME["success"], fill_color=THEME["bg_color"])
        dot_dh_open2 = Dot(axes.c2p(9, y_h), radius=0.05, stroke_width=1.5, stroke_color=THEME["success"], fill_color=THEME["bg_color"])
        lbl_dh = MathTex(r"\operatorname{Dom}(h) = \; ]-11, 9[", font_size=11, color=THEME["success"]).next_to(axes.c2p(-1, y_h), UP, buff=0.08)

        # 3. Rg(f) = [-11, 9[ a nivel y = 0.8
        y_rf = 0.8
        line_rf = Line(axes.c2p(-11, y_rf), axes.c2p(9, y_rf), color=THEME["highlight"], stroke_width=4.0)
        dot_rf_closed = Dot(axes.c2p(-11, y_rf), radius=0.05, color=THEME["highlight"])
        dot_rf_open = Dot(axes.c2p(9, y_rf), radius=0.05, stroke_width=1.5, stroke_color=THEME["highlight"], fill_color=THEME["bg_color"])
        lbl_rf = MathTex(r"\operatorname{Rg}(f) = [-11, 9[", font_size=11, color=THEME["highlight"]).next_to(axes.c2p(-1, y_rf), DOWN, buff=0.08)

        # 4. Punto conflictivo x = 2 => f(2) = -11 (cerrado en Rg(f), pero abierto en Dom(h))
        pt_conflict = Dot(axes.c2p(-11, y_rf), radius=0.07, color=THEME["statement_box"])
        lbl_conflict = Text("-11 ∉ Dom(h)", font_size=9, color=THEME["statement_box"], weight=BOLD).next_to(axes.c2p(-11, y_rf), UP, buff=0.1)

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
            FadeIn(dot_rf_closed),
            FadeIn(dot_rf_open),
            Write(lbl_rf),
            run_time=1.2
        )
        self.play(
            FadeIn(pt_conflict, scale=1.4),
            Write(lbl_conflict),
            run_time=1.0
        )
        self.wait(6.0)

        # Cierre suave
        extra_mobs = [
            left_grp, axes, axes_labels, graph_title,
            line_dg, dot_dg_open, dot_dg_closed, lbl_dg,
            line_dh, dot_dh_open1, dot_dh_open2, lbl_dh,
            line_rf, dot_rf_closed, dot_rf_open, lbl_rf,
            pt_conflict, lbl_conflict
        ]
        self.finish_exercise(extra_mobjects=extra_mobs)
        self.wait(0.5)
