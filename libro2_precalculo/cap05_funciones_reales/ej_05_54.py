"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.54 (Página 114 del libro / Página 133 del PDF)

Inyectividad, sobreyectividad y redefinición biyectiva de 6 funciones:
1. f(x) = 2x - 3:
   ⟹ Inyectiva: SÍ, Sobreyectiva: SÍ (en ℝ). Biyectiva: f: ℝ → ℝ.

2. f(x) = (x - 1)³ = x³ - 3x² + 3x - 1:
   ⟹ Inyectiva: SÍ, Sobreyectiva: SÍ (en ℝ). Biyectiva: f: ℝ → ℝ.

3. f(x) = x / (x + 1):
   ⟹ Inyectiva: SÍ, Sobreyectiva: NO (Rg = ℝ \ {1}).
   ⟹ Biyectiva: f: ℝ \ {-1} → ℝ \ {1}.

4. f(x) = (x + 1) / (x - 1):
   ⟹ Inyectiva: SÍ, Sobreyectiva: NO (Rg = ℝ \ {1}).
   ⟹ Biyectiva: f: ℝ \ {1} → ℝ \ {1}.

5. f(x) = { x - 2 si x < 3; √(x + 1) si x ≥ 3 }:
   ⟹ Inyectiva: SÍ (ramas crecientes con rangos disjuntos ]-∞, 1[ y [2, +∞[).
   ⟹ Sobreyectiva: NO (Rg = ]-∞, 1[ ∪ [2, +∞[).
   ⟹ Biyectiva: f: ℝ → ]-∞, 1[ ∪ [2, +∞[.

6. f(x) = x⁵ + 1:
   ⟹ Inyectiva: SÍ, Sobreyectiva: SÍ (en ℝ). Biyectiva: f: ℝ → ℝ.
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_54(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.54",
            topic="Inyectividad, Sobreyectividad y Construcción de Biyeciones"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Analizar inyectividad, sobreyectividad y definir funciones biyectivas ajustando el codominio:",
            math_tex=r"1.\; 2x-3; \;\; 2.\; (x-1)^3; \;\; 3.\; \frac{x}{x+1}; \;\; 4.\; \frac{x+1}{x-1}; \;\; 5.\; \text{trozos } (x<3, x\ge 3); \;\; 6.\; x^5+1.",
            desc_font_size=14,
            math_font_size=13,
            read_time=4.0
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Criterio de Biyectividad (Obs. 5.13)",
            "2/6: Ítems 1 y 2 (Biyectivas en ℝ)",
            "3/6: Ítems 3 y 4 (Homográficas y Asíntota)",
            "4/6: Ítem 5 (Trozos y Brecha [1, 2[)",
            "5/6: Ítem 6 y Tabla Resumen",
            "6/6: Resumen y Gráfica del Ítem 5"
        ])

        # ==========================================================
        # PASO 1: Criterio de Biyectividad y Redefinición
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{Definiciones Fundamentales (Secci\'on 5.5):} \\[4pt]"
            r"&\bullet\; f \text{ es inyectiva } \iff \forall x_1, x_2: f(x_1) = f(x_2) \implies x_1 = x_2. \\[4pt]"
            r"&\bullet\; f: A \to B \text{ es sobreyectiva } \iff \mathbf{Rg}(f) = B. \\[4pt]"
            r"&\bullet\; f \text{ es biyectiva } \iff f \text{ es inyectiva y sobreyectiva.} \\[6pt]"
            r"&\textbf{Observaci\'on 5.13 (Redefinici\'on hacia la Biyectividad):} \\[4pt]"
            r"&\text{Si } f: A \to \mathbb{R} \text{ es inyectiva, basta reemplazar el codominio} \\[3pt]"
            r"&\text{por su rango para obtener una funci\'on biyectiva:} \\[4pt]"
            r"&\widetilde{f}: A \to \mathbf{Rg}(f), \quad x \mapsto f(x) \quad (\text{Biyectiva})"
            r"\end{aligned}",
            font_size=16,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Criterio de Biyectividad (Obs. 5.13):\n"
            "• Inyectiva: imágenes distintas para argumentos\n"
            "  distintos (test de la recta horizontal: ≤ 1 corte).\n"
            "• Sobreyectiva: todo el conjunto de llegada B\n"
            "  es cubierto por el rango.\n"
            "• Si una función es inyectiva, su restricción al\n"
            "  rango Cod = Rg(f) siempre es biyectiva."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Ítems 1 y 2 (Biyectivas en ℝ)
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\mathbf{1.} \quad f(x) = 2x - 3, \quad \operatorname{Dom}(f) = \mathbb{R} \\[3pt]"
            r"&2x_1 - 3 = 2x_2 - 3 \implies 2x_1 = 2x_2 \implies x_1 = x_2 \implies \textbf{Inyectiva: SÍ} \\[3pt]"
            r"&\mathbf{Rg}(f) = \mathbb{R} \implies \textbf{Sobreyectiva: SÍ} \implies f: \mathbb{R} \to \mathbb{R} \text{ es biyectiva.} \\[6pt]"
            r"&\mathbf{2.} \quad f(x) = (x-1)^3 = x^3 - 3x^2 + 3x - 1, \quad \operatorname{Dom}(f) = \mathbb{R} \\[3pt]"
            r"&(x_1-1)^3 = (x_2-1)^3 \implies x_1 - 1 = x_2 - 1 \implies x_1 = x_2 \implies \textbf{Inyectiva: SÍ} \\[3pt]"
            r"&\mathbf{Rg}(f) = \mathbb{R} \implies \textbf{Sobreyectiva: SÍ} \implies f: \mathbb{R} \to \mathbb{R} \text{ es biyectiva.}"
            r"\end{aligned}",
            font_size=15,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Ítems 1 y 2 (Biyectivas en ℝ):\n"
            "• Ítem 1: Recta con pendiente m = 2 ≠ 0.\n"
            "  Cubre todo ℝ y es estrictamente monótona.\n"
            "  Es biyectiva sin modificar codominio.\n"
            "• Ítem 2: Cubo perfecto (x - 1)³.\n"
            "  La función cúbica es inyectiva en ℝ y su\n"
            "  rango es todo ℝ. Biyectiva directa."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], wait_time=5.0)

        # ==========================================================
        # PASO 3: Ítems 3 y 4 (Homográficas y Rango ℝ \ {1})
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\mathbf{3.} \quad f(x) = \frac{x}{x+1}, \quad \operatorname{Dom}(f) = \mathbb{R} \setminus \{-1\} \\[3pt]"
            r"&\frac{x_1}{x_1+1} = \frac{x_2}{x_2+1} \implies x_1 x_2 + x_1 = x_1 x_2 + x_2 \implies x_1 = x_2 \implies \textbf{Iny.: SÍ} \\[3pt]"
            r"&y = \frac{x}{x+1} \implies x = \frac{y}{1-y} \implies \mathbf{Rg}(f) = \mathbb{R} \setminus \{1\} \neq \mathbb{R} \quad (\textbf{Sob.: NO}) \\[3pt]"
            r"&\widetilde{f}: \mathbb{R} \setminus \{-1\} \to \mathbb{R} \setminus \{1\} \quad (\textbf{Biyectiva}) \\[6pt]"
            r"&\mathbf{4.} \quad f(x) = \frac{x+1}{x-1}, \quad \operatorname{Dom}(f) = \mathbb{R} \setminus \{1\} \\[3pt]"
            r"&\text{Invertible: } x = \frac{y+1}{y-1} \implies \mathbf{Rg}(f) = \mathbb{R} \setminus \{1\} \quad (\textbf{Iny.: SÍ, Sob.: NO}) \\[3pt]"
            r"&\widetilde{f}: \mathbb{R} \setminus \{1\} \to \mathbb{R} \setminus \{1\} \quad (\textbf{Biyectiva (Involuci\'on)})"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Ítems 3 y 4 (Homográficas):\n"
            "• Ambas hipérbolas tienen asíntota horizontal\n"
            "  en y = 1, omitiendo este valor en su rango.\n"
            "• Son estrictamente inyectivas en sus dominios.\n"
            "• No son sobreyectivas hacia ℝ.\n"
            "• Redefiniendo Cod = ℝ \\ {1}, ambas se\n"
            "  convierten en funciones biyectivas."
        )

        self.morph_step(eq3, just3, box_color=THEME["success"], wait_time=5.0)

        # ==========================================================
        # PASO 4: Ítem 5 (Trozos y Brecha [1, 2[)
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\mathbf{5.} \quad f(x) = \begin{cases} x-2, &\text{si } x < 3 \\ \sqrt{x+1}, &\text{si } x \ge 3 \end{cases}, \quad \operatorname{Dom}(f) = \mathbb{R} \\[4pt]"
            r"&x < 3 \implies f(x) < 3 - 2 = 1 \implies \mathbf{Rg}_1 = \; ]-\infty, 1[ \\[3pt]"
            r"&x \ge 3 \implies f(x) \ge \sqrt{3+1} = 2 \implies \mathbf{Rg}_2 = [2, +\infty[ \\[4pt]"
            r"&\text{Rangos disjuntos: } \operatorname{Rg}_1 \cap \operatorname{Rg}_2 = \emptyset \;\text{ y ambas ramas crecientes} \\[3pt]"
            r"&\implies \textbf{Inyectiva: SÍ} \quad (\text{ninguna ordenada se repite}) \\[4pt]"
            r"&\mathbf{Rg}(f) = \; ]-\infty, 1[ \;\cup\; [2, +\infty[ = \mathbb{R} \setminus [1, 2[ \quad (\textbf{Sob.: NO}) \\[4pt]"
            r"&\widetilde{f}: \mathbb{R} \to \; ]-\infty, 1[ \;\cup\; [2, +\infty[ \quad (\textbf{Biyectiva})"
            r"\end{aligned}",
            font_size=15,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Ítem 5 (Trozos y Brecha):\n"
            "• La rama lineal izquierda cubre ]-∞, 1[.\n"
            "• La rama radical derecha cubre [2, +∞[.\n"
            "• Como los rangos no se solapan y cada rama\n"
            "  es creciente, la función es INYECTIVA.\n"
            "• Omite la franja [1, 2[, por lo que no es sobre.\n"
            "• Codominio biyectivo: ℝ \\ [1, 2[."
        )

        self.morph_step(eq4, just4, box_color=THEME["statement_box"], wait_time=5.0)

        # ==========================================================
        # PASO 5: Ítem 6 y Tabla Resumen de Biyectividad
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\mathbf{6.} \quad f(x) = x^5 + 1 \implies x_1^5+1 = x_2^5+1 \implies x_1 = x_2 \quad (\textbf{Iny.: SÍ, Sob.: SÍ}) \\[5pt]"
            r"&\textbf{Tabla Comparativa de Biyectividad:} \\[4pt]"
            r"&\begin{array}{|c|c|c|c|c|} \hline"
            r"\text{\textbf{Ítem}} & \textbf{Dominio} & \textbf{¿Iny.?} & \textbf{¿Sob. en } \mathbb{R}\textbf{?} & \textbf{Codominio Biyectivo} \\ \hline"
            r"1 & \mathbb{R} & \textbf{SÍ} & \textbf{SÍ} & \mathbb{R} \\"
            r"2 & \mathbb{R} & \textbf{SÍ} & \textbf{SÍ} & \mathbb{R} \\"
            r"3 & \mathbb{R} \setminus \{-1\} & \textbf{SÍ} & \textbf{NO} & \mathbb{R} \setminus \{1\} \\"
            r"4 & \mathbb{R} \setminus \{1\} & \textbf{SÍ} & \textbf{NO} & \mathbb{R} \setminus \{1\} \\"
            r"5 & \mathbb{R} & \textbf{SÍ} & \textbf{NO} & ]-\infty, 1[ \cup [2, +\infty[ \\"
            r"6 & \mathbb{R} & \textbf{SÍ} & \textbf{SÍ} & \mathbb{R} \\ \hline"
            r"\end{array}"
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Ítem 6 y Tabla Resumen:\n"
            "• Ítem 6: x⁵ + 1 es estrictamente monótona;\n"
            "  es biyectiva directa de ℝ en ℝ.\n"
            "• Hallazgo pedagógico notable:\n"
            "  ¡LAS 6 FUNCIONES SON INYECTIVAS!\n"
            "• Los ítems 1, 2 y 6 son biyectivos en ℝ.\n"
            "• Los ítems 3, 4 y 5 requieren ajustar su\n"
            "  codominio al rango para ser biyecciones."
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 6: Resumen y Gráfica del Ítem 5 (Inyectiva a Trozos)
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen del Ítem 5
        t_title = Text("Geometría del Ítem 5 (Trozos Inyectivos):", font_size=13, color=THEME["header_color"], weight=BOLD)
        t_r1 = MathTex(r"x < 3: \; y = x - 2 \quad (\text{punto abierto en } (3, 1))", font_size=11, color=THEME["secondary"])
        t_r2 = MathTex(r"x \ge 3: \; y = \sqrt{x+1} \quad (\text{punto cerrado en } (3, 2))", font_size=11, color=THEME["curve"])
        t_gap = Text("• Brecha [1, 2[ excluida del rango.", font_size=11, color=THEME["statement_box"], weight=BOLD)
        t_test = Text("• Test de recta horizontal: corta ≤ 1 vez.", font_size=11, color=THEME["success"], weight=BOLD)
        t_bij = MathTex(r"\widetilde{f}: \mathbb{R} \to \; ]-\infty, 1[ \;\cup\; [2, +\infty[ \quad (\text{Biyectiva})", font_size=11, color=WHITE)

        info_grp = VGroup(t_title, t_r1, t_r2, t_gap, t_test, t_bij).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        info_box = SurroundingRectangle(info_grp, color=THEME["statement_box"], buff=0.18, stroke_width=1.5, corner_radius=0.08)
        left_grp = VGroup(info_box, info_grp).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos para graficar el Ítem 5
        axes, axes_labels = self.setup_axes(
            x_range=[-1.0, 6.0, 1],
            y_range=[-2.5, 4.0, 1],
            x_length=4.8,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True
        )

        # Rama 1: x in [-0.8, 2.98], y = x - 2
        branch1 = axes.plot(lambda x: x - 2, x_range=[-0.8, 2.98], color=THEME["secondary"], stroke_width=2.5)
        dot_open = Dot(axes.c2p(3.0, 1.0), radius=0.065, stroke_width=1.8, stroke_color=THEME["secondary"], fill_color=THEME["bg_color"])

        # Rama 2: x in [3.0, 5.8], y = sqrt(x + 1)
        branch2 = axes.plot(lambda x: np.sqrt(x + 1), x_range=[3.0, 5.8], color=THEME["curve"], stroke_width=2.5)
        dot_closed = Dot(axes.c2p(3.0, 2.0), radius=0.06, color=THEME["curve"])

        # Franja prohibida en el eje Y entre y = 1 e y = 2
        gap_line = Line(axes.c2p(0, 1.0), axes.c2p(0, 2.0), color=THEME["statement_box"], stroke_width=5.5)
        lbl_gap = Text("Brecha [1, 2[", font_size=9, color=THEME["statement_box"], weight=BOLD).next_to(axes.c2p(0, 1.5), LEFT, buff=0.1)

        # Línea de prueba horizontal que muestra inyectividad
        h_line = DashedLine(axes.c2p(-0.8, 2.5), axes.c2p(5.8, 2.5), color=THEME["success"], stroke_width=1.5)
        lbl_test = Text("Recta Horizontal (1 corte)", font_size=9, color=THEME["success"]).next_to(h_line, UP, buff=0.05)

        graph_title = Text("Gráfica y Brecha del Ítem 5", font_size=13, color=THEME["header_color"]).next_to(axes, UP, buff=0.15)

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
            Create(branch1),
            FadeIn(dot_open),
            run_time=1.2
        )
        self.play(
            Create(branch2),
            FadeIn(dot_closed),
            run_time=1.2
        )
        self.play(
            Create(gap_line),
            Write(lbl_gap),
            Create(h_line),
            Write(lbl_test),
            run_time=1.2
        )
        self.wait(5.5)

        # Cierre suave
        extra_mobs = [
            left_grp, axes, axes_labels, graph_title,
            branch1, dot_open, branch2, dot_closed,
            gap_line, lbl_gap, h_line, lbl_test
        ]
        self.finish_exercise(extra_mobjects=extra_mobs)
        self.wait(0.5)
