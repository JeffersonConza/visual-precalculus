"""
Ejercicio 5.66 - Precálculo 2 (Colección Yachay Tech / Editorial Amarun)
Capítulo 5: Funciones Reales
Tema: Funciones Hiperbólicas (Seno y Coseno Hiperbólico):
      senh(x) = (eˣ - e⁻ˣ)/2, cosh(x) = (eˣ + e⁻ˣ)/2.
      Paridad, ecuaciones de ceros, identidades fundamentales, monotonía y gráficas.

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


class Ejercicio05_66(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.66",
            topic="Funciones Hiperbólicas: Ceros, Identidades y Gráfica"
        )

        # 2. Enunciado institucional permanente (y = 2.5)
        self.setup_statement(
            desc_text="Dadas senh(x) = (eˣ - e⁻ˣ)/2 y cosh(x) = (eˣ + e⁻ˣ)/2 en ℝ, analiza sus propiedades:",
            math_tex=r"1.\; \text{Paridad}; \; 2.\; \text{Ceros}; \; 3.\; \cosh^2(x)-\operatorname{senh}^2(x)=1; \; 4.\; \operatorname{senh}(2x)=2\operatorname{senh}(x)\cosh(x); \; 5.\; \text{Monotonía y gráfica}.",
            desc_font_size=12,
            math_font_size=11,
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (6 pasos)
        self.setup_progress_bar([
            "1/6: Paridad e Imparidad",
            "2/6: Ceros y Ecuaciones",
            "3/6: Identidad Fundamental",
            "4/6: Identidad del Ángulo Doble",
            "5/6: Monotonía Analítica",
            "6/6: Esquema Gráfico y Síntesis"
        ])

        # ==========================================================
        # PASO 1: Demostración de Paridad e Imparidad
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Simetría de las Funciones Hiperbólicas:} \\[4pt]"
            r"&\bullet\; \operatorname{senh}(-x) = \frac{e^{-x} - e^{-(-x)}}{2} = \frac{e^{-x} - e^x}{2} = -\frac{e^x - e^{-x}}{2} = -\operatorname{senh}(x) \\[5pt]"
            r"&\quad \implies \textbf{senh es una función IMPAR} \quad (\text{simetría central en } (0,0)) \\[5pt]"
            r"&\bullet\; \cosh(-x) = \frac{e^{-x} + e^{-(-x)}}{2} = \frac{e^{-x} + e^x}{2} = \frac{e^x + e^{-x}}{2} = \cosh(x) \\[5pt]"
            r"&\quad \implies \textbf{cosh es una función PAR} \quad (\text{simetría axial respecto al eje } Y)"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Paridad e Imparidad:\n"
            "• Evaluamos en -x usando e^{-(-x)} = e^x.\n"
            "• Para senh: el signo del numerador se invierte,\n"
            "  demostrando que senh(-x) = -senh(x) (impar).\n"
            "• Para cosh: la suma conmuta en el numerador,\n"
            "  demostrando que cosh(-x) = cosh(x) (par).\n"
            "• Propiedades análogas a sen(x) y cos(x)."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Resolución de las Ecuaciones de Ceros
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Ceros de las Funciones Hiperbólicas:} \\[4pt]"
            r"&\bullet\; \text{Ecuación (ES): } \operatorname{senh}(x) = 0 \iff \frac{e^x - e^{-x}}{2} = 0 \\[3pt]"
            r"&\quad \iff e^x - e^{-x} = 0 \iff e^{2x} = 1 \iff 2x = 0 \iff \mathbf{x = 0} \\[4pt]"
            r"&\quad \textbf{Conjunto Solución:} \quad \mathbf{CS_{ES} = \{0\}} \quad (\text{Cero único}) \\[5pt]"
            r"&\bullet\; \text{Ecuación (EC): } \cosh(x) = 0 \iff \frac{e^x + e^{-x}}{2} = 0 \\[3pt]"
            r"&\quad \iff e^x + e^{-x} = 0 \iff e^{2x} = -1 \\[4pt]"
            r"&\quad \text{Como } e^{2x} > 0 \quad (\forall x \in \mathbb{R}) \implies \mathbf{CS_{EC} = \emptyset} \quad (\textbf{Sin ceros reales})"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Ceros y Raíces Reales:\n"
            "• senh(x) = 0 exige e^x = e^{-x} ⟺ e^{2x} = 1.\n"
            "  La única solución real es x = 0.\n"
            "• cosh(x) = 0 exige e^{2x} = -1.\n"
            "  Imposible en ℝ pues la exponencial es positiva.\n"
            "• Por desigualdad de medias, cosh(x) ≥ 1 > 0.\n"
            "  cosh jamás corta el eje horizontal X."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=5.0)

        # ==========================================================
        # PASO 3: Identidad Fundamental Hiperbólica
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Identidad Fundamental } \cosh^2(x) - \operatorname{senh}^2(x) = 1: \\[4pt]"
            r"&\cosh^2(x) = \left(\frac{e^x + e^{-x}}{2}\right)^2 = \frac{e^{2x} + 2 + e^{-2x}}{4} \\[5pt]"
            r"&\operatorname{senh}^2(x) = \left(\frac{e^x - e^{-x}}{2}\right)^2 = \frac{e^{2x} - 2 + e^{-2x}}{4} \\[5pt]"
            r"&\cosh^2(x) - \operatorname{senh}^2(x) = \frac{(e^{2x} + 2 + e^{-2x}) - (e^{2x} - 2 + e^{-2x})}{4} \\[5pt]"
            r"&= \frac{2 - (-2)}{4} = \frac{4}{4} = \mathbf{1} \quad (\forall x \in \mathbb{R})"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Identidad Fundamental:\n"
            "• Elevamos al cuadrado cada definición.\n"
            "• Notamos los dobles productos: 2·e^x·e^{-x} = 2.\n"
            "• Al restar, los términos cuadráticos e^{2x} y e^{-2x}\n"
            "  se cancelan idénticamente.\n"
            "• Resta de dobles productos: (2 - (-2))/4 = 4/4 = 1.\n"
            "• Análoga a cos²(x) + sen²(x) = 1."
        )

        self.morph_step(eq3, just3, box_color=THEME["success"], advance_to_step=2, wait_time=5.0)

        # ==========================================================
        # PASO 4: Identidad del Ángulo Doble
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Identidad del Ángulo Doble } \operatorname{senh}(2x) = 2\operatorname{senh}(x)\cosh(x): \\[4pt]"
            r"&2\operatorname{senh}(x)\cosh(x) = 2 \left(\frac{e^x - e^{-x}}{2}\right)\left(\frac{e^x + e^{-x}}{2}\right) \\[5pt]"
            r"&= \frac{(e^x - e^{-x})(e^x + e^{-x})}{2} = \frac{(e^x)^2 - (e^{-x})^2}{2} \\[5pt]"
            r"&= \frac{e^{2x} - e^{-2x}}{2} = \mathbf{\operatorname{senh}(2x)} \quad (\forall x \in \mathbb{R}) \\[5pt]"
            r"&\text{Nota: Se demuestra la fórmula correcta, aclarando la errata del texto.}"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Identidad del Ángulo Doble:\n"
            "• Producto notable: suma por diferencia\n"
            "  (e^x - e^{-x})(e^x + e^{-x}) = (e^x)² - (e^{-x})².\n"
            "• Obtenemos (e^{2x} - e^{-2x})/2 = senh(2x).\n"
            "• Se corrige la errata tipográfica de impresión:\n"
            "  senh(2x) = 2 senh(x) cosh(x).\n"
            "• Reproduce exactamente la estructura de sen(2x)."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=5.0)

        # ==========================================================
        # PASO 5: Monotonía Analítica de senh y cosh
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Análisis Riguroso de Monotonía:} \\[4pt]"
            r"&\bullet\; \mathbf{senh(x):} \quad x \mapsto e^x \text{ y } x \mapsto -e^{-x} \text{ son estrictamente crecientes.} \\[4pt]"
            r"&\quad \text{Suma de funciones crecientes} \implies \mathbf{senh \text{ es ESTRICTAMENTE CRECIENTE en } \mathbb{R}} \\[4pt]"
            r"&\quad \operatorname{Rg}(\operatorname{senh}) = \mathbb{R} \quad (\textbf{Biyectiva de } \mathbb{R} \text{ en } \mathbb{R}) \\[5pt]"
            r"&\bullet\; \mathbf{cosh(x):} \quad \text{Para } x \ge 0: \; e^x \ge e^{-x} \implies \mathbf{creciente en } [0, +\infty[ \\[3pt]"
            r"&\quad \text{Por paridad, es } \mathbf{decreciente en } ]-\infty, 0]. \\[3pt]"
            r"&\quad \text{Mínimo global en } (0, 1): \quad \operatorname{Rg}(\cosh) = [1, +\infty["
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Monotonía Analítica:\n"
            "• senh(x) es suma de crecientes: e^x y -e^{-x}.\n"
            "  Es estrictamente creciente en todo ℝ.\n"
            "  Rg(senh) = ℝ, inyectiva y sobreyectiva (biyectiva).\n"
            "• cosh(x) decrece en ]-∞, 0] y crece en [0, +∞[.\n"
            "  Tiene vértice y mínimo absoluto en (0, 1).\n"
            "  Rg(cosh) = [1, +∞[."
        )

        self.morph_step(eq5, just5, box_color=THEME["curve"], advance_to_step=4, wait_time=5.2)

        # ==========================================================
        # PASO 6: Síntesis Comparativa y Esquema Gráfico
        # ==========================================================
        # Panel izquierdo: Cuadro Síntesis
        t_title = Text("Síntesis Hiperbólica (Ej. 5.66)", font_size=13, color=THEME["header_color"], weight=BOLD)
        t_senh = MathTex(r"\operatorname{senh}(x) = \tfrac{e^x - e^{-x}}{2} \quad (\text{Impar, Creciente, Raíz: } x=0)", font_size=11, color=THEME["curve"])
        t_cosh = MathTex(r"\cosh(x) = \tfrac{e^x + e^{-x}}{2} \quad (\text{Par, Mínimo en } (0, 1), \text{ Sin raíces})", font_size=11, color=THEME["secondary"])
        t_id1 = MathTex(r"\cosh^2(x) - \operatorname{senh}^2(x) = 1 \quad (\text{Hipérbola Equilátera})", font_size=11, color=THEME["highlight"])
        t_id2 = MathTex(r"\operatorname{senh}(2x) = 2\operatorname{senh}(x)\cosh(x) \quad (\text{Ángulo Doble})", font_size=11, color=THEME["success"])

        table_grp = VGroup(t_title, t_senh, t_cosh, t_id1, t_id2).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        table_box = SurroundingRectangle(table_grp, color=THEME["statement_box"], buff=0.18, stroke_width=1.5, corner_radius=0.08)
        left_summary = VGroup(table_box, table_grp).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos para ilustrar senh y cosh
        axes, axes_labels = self.setup_axes(
            x_range=[-3.0, 3.0, 1],
            y_range=[-3.0, 4.0, 1],
            x_length=4.8,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True
        )
        graph_title = Text("Gráfica: senh(x) y cosh(x) (Catenaria)", font_size=12, color=WHITE).next_to(axes, UP, buff=0.15)

        # Curva senh(x)
        curve_senh = axes.plot(lambda x: np.sinh(x), x_range=[-2.0, 2.0], color=THEME["curve"], stroke_width=2.6)

        # Curva cosh(x)
        curve_cosh = axes.plot(lambda x: np.cosh(x), x_range=[-2.0, 2.0], color=THEME["secondary"], stroke_width=2.6)

        # Puntos notables: (0, 0) para senh y (0, 1) para cosh
        dot_senh = Dot(axes.c2p(0, 0), color=THEME["curve"], radius=0.06)
        lbl_senh = MathTex(r"(0, 0)", font_size=9, color=THEME["curve"]).next_to(dot_senh, DOWN + RIGHT, buff=0.06)

        dot_cosh = Dot(axes.c2p(0, 1), color=THEME["secondary"], radius=0.06)
        lbl_cosh = MathTex(r"(0, 1)", font_size=9, color=THEME["secondary"]).next_to(dot_cosh, UP, buff=0.06)

        # Etiquetas de curvas
        leg_senh = MathTex(r"y = \operatorname{senh}(x)", font_size=11, color=THEME["curve"]).move_to(axes.c2p(1.7, -1.5))
        leg_cosh = MathTex(r"y = \cosh(x)", font_size=11, color=THEME["secondary"]).move_to(axes.c2p(-1.7, 3.2))

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
            Create(curve_senh),
            FadeIn(dot_senh),
            Write(lbl_senh),
            Write(leg_senh),
            run_time=1.4
        )
        self.play(
            Create(curve_cosh),
            FadeIn(dot_cosh),
            Write(lbl_cosh),
            Write(leg_cosh),
            run_time=1.4
        )
        self.wait(6.0)

        # Cierre suave
        extra_mobs = [
            left_summary, axes, axes_labels, graph_title,
            curve_senh, dot_senh, lbl_senh, leg_senh,
            curve_cosh, dot_cosh, lbl_cosh, leg_cosh
        ]
        self.finish_exercise(extra_mobjects=extra_mobs)
        self.wait(0.5)
