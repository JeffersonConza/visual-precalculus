"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.4: Paridad y valor absoluto
Ejercicio 5.6 (Página 48 del libro / Página 67 del PDF)

Demostración de la propiedad del valor absoluto de un producto (Teorema 5.6):
- Punto (5.30): |a · b| = |a| · |b| para todo a, b ∈ ℝ usando la definición |x| = √(x²).
- Corolario punto (5.31): |a / b| = |a| / |b| con b ≠ 0.
- Interpretación geométrica y funcional: dilatación y compresión métrica f_k(x) = |k · x| = |k||x|.
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_06(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.6",
            topic="Propiedades del Valor Absoluto (Teorema 5.6)"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Teorema 5.6: Sean a, b ∈ ℝ. Probar el punto (5.30):",
            math_tex=r"|a \cdot b| = |a| \cdot |b| \quad \left[\text{Sugerencia: use } |x| = \sqrt{x^2}\right]",
            desc_font_size=16,
            math_font_size=18,
            read_time=4.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos mínimos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Definición vía Raíz (5.28)",
            "2/6: Distributividad de Potencia",
            "3/6: Distributividad del Radical",
            "4/6: Conclusión del Producto",
            "5/6: Demostración del Cociente",
            "6/6: Interpretación Geométrica"
        ])

        # ==========================================================
        # PASO 1: Definición vía Raíz Cuadrada (5.28)
        # ==========================================================
        eq1 = MathTex(
            r"|a \cdot b| = \sqrt{(a \cdot b)^2}",
            font_size=28,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Definición formal (5.28):\n"
            "Para todo x ∈ ℝ, se define:\n"
            "|x| = √(x²).\n"
            "Sustituyendo el argumento x = a · b:\n"
            "|a · b| = √((a · b)²)."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Distributividad de Potencia en Factores Reales
        # ==========================================================
        eq2 = MathTex(
            r"\sqrt{(a \cdot b)^2} = \sqrt{a^2 \cdot b^2}",
            font_size=28,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Propiedad de la potencia:\n"
            "En los números reales (a · b)² = a² · b²\n"
            "(el exponente entero distribuye sobre\n"
            "el producto de factores en ℝ).\n"
            "El radicando resulta a² · b²."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=4.8)

        # ==========================================================
        # PASO 3: Distributividad del Radical sobre Factores No Negativos
        # ==========================================================
        eq3 = MathTex(
            r"\sqrt{a^2 \cdot b^2} = \sqrt{a^2} \cdot \sqrt{b^2}",
            font_size=28,
            color=THEME["curve"]
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Propiedad de la raíz en ℝ:\n"
            "Para u, v ≥ 0, se cumple √(u · v) = √u · √v.\n"
            "Dado que a² ≥ 0 y b² ≥ 0 para todo a, b ∈ ℝ,\n"
            "la raíz cuadrada distribuye exactamente:\n"
            "√(a² · b²) = √(a²) · √(b²)."
        )

        self.morph_step(eq3, just3, box_color=THEME["curve"], advance_to_step=2, wait_time=5.2)

        # ==========================================================
        # PASO 4: Conclusión Formal del Producto (5.30)
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"\sqrt{a^2} \cdot \sqrt{b^2} &= |a| \cdot |b| \\"
            r"\therefore \quad |a \cdot b| &= |a| \cdot |b|"
            r"\end{aligned}",
            font_size=26,
            color=THEME["success"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Conclusión formal (5.30):\n"
            "Reaplicando (5.28): √(a²) = |a| y √(b²) = |b|.\n"
            "Por transitividad de la igualdad:\n"
            "|a · b| = |a| · |b| (∀ a, b ∈ ℝ).\n"
            "Queda demostrado el punto (5.30)."
        )

        self.morph_step(eq4, just4, box_color=THEME["success"], advance_to_step=3, wait_time=5.5)

        # ==========================================================
        # PASO 5: Demostración del Cociente (Punto 5.31)
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"\left|\frac{a}{b}\right| &= |a \cdot b^{-1}| = |a| \cdot |b^{-1}| \\"
            r"&= |a| \cdot \frac{1}{|b|} = \frac{|a|}{|b|} \quad (b \neq 0)"
            r"\end{aligned}",
            font_size=23,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Cociente de valores absolutos (5.31):\n"
            "Para b ≠ 0, a/b = a · b⁻¹.\n"
            "Por la propiedad multiplicativa (5.30):\n"
            "|a · b⁻¹| = |a| · |b⁻¹|.\n"
            "Dado que |b⁻¹| = 1/|b|, concluimos:\n"
            "|a / b| = |a| / |b|."
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=5.5)

        # ==========================================================
        # PASO 6: Interpretación Geométrica y Funcional
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Explicación conceptual
        t_title = Text("Interpretación geométrica:", font_size=16, color=THEME["header_color"], weight=BOLD)
        eq_scaling = MathTex(r"f_k(x) = |k \cdot x| = |k| \cdot |x|", font_size=21, color=THEME["highlight"])
        t_desc1 = Text("• El factor |k| modula la pendiente métrica.", font_size=13, color=THEME["statement_text"])
        t_desc2 = Text("• Para k = -2: |-2x| = 2|x| (dilatación x2).", font_size=13, color=THEME["highlight"])
        t_desc3 = Text("• Para k = 1/2: |0.5x| = 0.5|x| (compresión a la mitad).", font_size=13, color=THEME["curve"])
        t_desc4 = Text("• El signo negativo no altera distancias en ℝ.", font_size=13, color=THEME["statement_text"])

        info_content = VGroup(t_title, eq_scaling, t_desc1, t_desc2, t_desc3, t_desc4).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        info_box = SurroundingRectangle(info_content, color=THEME["statement_box"], buff=0.2, stroke_width=1.5, corner_radius=0.08)
        info_grp = VGroup(info_box, info_content).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos comparativos
        axes, axes_labels = self.setup_axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-0.5, 3.2, 1],
            x_length=5.6,
            y_length=3.8,
            center=[2.7, -0.45, 0],
            include_numbers=True
        )

        # Curva base: |x|
        curve_base = axes.plot(lambda x: abs(x), x_range=[-2.2, 2.2], color=THEME["statement_text"], stroke_width=2.5)
        lbl_base = MathTex(r"|x|", font_size=16, color=THEME["statement_text"]).next_to(axes.c2p(2.2, 2.2), UR, buff=0.08)

        # Curva dilatada: |-2x| = 2|x|
        curve_dilated = axes.plot(lambda x: abs(-2 * x), x_range=[-1.5, 1.5], color=THEME["highlight"], stroke_width=3.2)
        lbl_dilated = MathTex(r"|-2x| = 2|x|", font_size=16, color=THEME["highlight"]).next_to(axes.c2p(1.5, 3.0), UR, buff=0.08)

        # Curva comprimida: |0.5x| = 0.5|x|
        curve_compressed = axes.plot(lambda x: abs(0.5 * x), x_range=[-2.4, 2.4], color=THEME["curve"], stroke_width=2.8)
        lbl_compressed = MathTex(r"|0.5x| = 0.5|x|", font_size=16, color=THEME["curve"]).next_to(axes.c2p(2.4, 1.2), DR, buff=0.08)

        # Marcadores comparativos en x = 1.0 (muestran las alturas 1/2, 1, 2)
        x_eval = 1.0
        p_x = axes.c2p(x_eval, 0)
        p_comp = axes.c2p(x_eval, 0.5)
        p_base = axes.c2p(x_eval, 1.0)
        p_dil = axes.c2p(x_eval, 2.0)

        eval_line = DashedLine(p_x, p_dil, color=THEME["axes"], stroke_width=1.5)
        dot_comp = Dot(p_comp, radius=0.06, color=THEME["curve"])
        dot_base = Dot(p_base, radius=0.06, color=THEME["statement_text"])
        dot_dil = Dot(p_dil, radius=0.06, color=THEME["highlight"])

        val_comp = MathTex(r"\frac{1}{2}", font_size=13, color=THEME["curve"]).next_to(dot_comp, RIGHT, buff=0.1)
        val_base = MathTex(r"1", font_size=13, color=THEME["statement_text"]).next_to(dot_base, RIGHT, buff=0.1)
        val_dil = MathTex(r"2", font_size=13, color=THEME["highlight"]).next_to(dot_dil, RIGHT, buff=0.1)

        # Transición hacia el paso 5
        self.play(
            FadeOut(self.active_box),
            FadeOut(self.active_math, shift=DOWN * 0.2),
            FadeOut(self.active_just, shift=DOWN * 0.2),
            FadeIn(info_grp, shift=DOWN * 0.2),
            Create(axes),
            Write(axes_labels),
            *prog_anims,
            run_time=1.8
        )
        self.active_box = None
        self.active_math = None
        self.active_just = None

        # Trazado de las curvas de valor absoluto
        self.play(
            Create(curve_base), Write(lbl_base),
            run_time=1.2
        )
        self.play(
            Create(curve_dilated), Write(lbl_dilated),
            Create(curve_compressed), Write(lbl_compressed),
            run_time=1.6
        )

        # Resaltado de la escala métrica en x = 1 con sus valores correspondientes
        self.play(
            Create(eval_line),
            FadeIn(dot_base), Write(val_base),
            FadeIn(dot_comp), Write(val_comp),
            FadeIn(dot_dil), Write(val_dil),
            run_time=1.4
        )
        self.wait(6.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_base, lbl_base,
            curve_dilated, lbl_dilated,
            curve_compressed, lbl_compressed,
            eval_line,
            dot_comp, dot_base, dot_dil,
            val_comp, val_base, val_dil
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
