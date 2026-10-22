"""
Ejercicio 6.2 - Precálculo 2 (Colección Yachay Tech / Editorial Amarun)
Capítulo 6: Funciones Trigonométricas
Tema: Teorema 6.3: Paridad de la Función Coseno:
      Demostración axiomática a partir de los postulados P1–P4 y (6.4):
      ∀ x ∈ ℝ: cos(-x) = cos(x).

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


class Ejercicio06_02(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 6",
            exercise="Ejercicio 6.2",
            topic="Paridad del Coseno y Simetría Axial"
        )

        # 2. Enunciado institucional permanente (y = 2.5)
        self.setup_statement(
            desc_text="A partir de los postulados P1–P4 y resultados previos, demostrar:",
            math_tex=r"\text{Teorema 6.3 (Paridad de } \cos\text{): } \forall x \in \mathbb{R}: \cos(-x) = \cos(x) \quad (6.7)",
            desc_font_size=13,
            math_font_size=12,
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (6 pasos)
        self.setup_progress_bar([
            "1/6: Marco Axiomático y Resultados Previos",
            "2/6: Artificio Algebraico: -x = 0 - x",
            "3/6: Aplicación del Postulado P3",
            "4/6: Sustitución de Valores Notables",
            "5/6: Generalización y Paridad Global",
            "6/6: Esquema Gráfico y Simetría"
        ])

        # ==========================================================
        # PASO 1: Marco Axiomático y Resultados Previos
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Marco Axiomático de la Trigonometría (Amarun):} \\[4pt]"
            r"&\text{En la teoría deductiva formal se disponen de las siguientes herramientas:} \\[5pt]"
            r"&\bullet \mathbf{\text{Postulado P3: }} \forall w, u \in \mathbb{R}: \\[2pt]"
            r"&\quad \cos(w - u) = \cos(w)\cos(u) + \operatorname{sen}(w)\operatorname{sen}(u) \\[4pt]"
            r"&\bullet \mathbf{\text{Postulado P2: }} \cos(0) = 1 \quad (\text{y } \cos(\pi) = -1) \\[4pt]"
            r"&\bullet \mathbf{\text{Propiedad (6.4): }} \operatorname{sen}(0) = 0 \quad (\text{Corolario 6.2 previamente probado}) \\[5pt]"
            r"&\text{Objetivo: Probar que para todo } x \in \mathbb{R}, \; \cos(-x) = \cos(x)."
            r"\end{aligned}",
            font_size=13.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Fundamentación Axiomática:\n"
            "• La teoría trigonométrica se construye rigurosamente\n"
            "  a partir de los postulados P1 a P4.\n"
            "• El postulado P3 modela el coseno de la diferencia.\n"
            "• El postulado P2 fija el valor cos(0) = 1.\n"
            "• El Corolario 6.2 derivó previamente que sen(0) = 0."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=6.2)

        # ==========================================================
        # PASO 2: Artificio Algebraico: -x = 0 - x
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Elección Genérica y Artificio de Sustracción:} \\[4pt]"
            r"&\text{Sea } x \in \mathbb{R} \text{ un número real arbitrariamente elegido.} \\[5pt]"
            r"&\text{Expresamos el opuesto aditivo } -x \text{ en términos de una resta:} \\[4pt]"
            r"&-x = 0 - x \\[5pt]"
            r"&\text{Por lo tanto, la expresión a calcular toma la forma:} \\[4pt]"
            r"&\cos(-x) = \cos(0 - x) \\[5pt]"
            r"&\text{Identificamos los parámetros en el Postulado P3:} \\[3pt]"
            r"&\mathbf{w = 0} \qquad \text{y} \qquad \mathbf{u = x}"
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Descomposición del Argumento:\n"
            "• Para aplicar el postulado de la resta P3,\n"
            "  expresamos el argumento monomio -x como 0 - x.\n"
            "• La variable w toma el valor constante 0 y la\n"
            "  variable u adopta el valor de la incógnita x.\n"
            "• Esto conecta el ángulo opuesto con el origen 0."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=6.2)

        # ==========================================================
        # PASO 3: Aplicación del Postulado P3
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Desarrollo por el Postulado P3:} \\[4pt]"
            r"&\text{Sustituimos } w = 0 \text{ y } u = x \text{ en la fórmula de la diferencia:} \\[5pt]"
            r"&\cos(w - u) = \cos(w)\cos(u) + \operatorname{sen}(w)\operatorname{sen}(u) \\[5pt]"
            r"&\Downarrow \\[5pt]"
            r"&\cos(0 - x) = \cos(0)\cos(x) + \operatorname{sen}(0)\operatorname{sen}(x) \\[5pt]"
            r"&\implies \mathbf{\cos(-x) = \cos(0)\cos(x) + \operatorname{sen}(0)\operatorname{sen}(x)}"
            r"\end{aligned}",
            font_size=14.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Expansión Deductiva:\n"
            "• El postulado P3 se cumple para cualesquiera\n"
            "  números reales w y u.\n"
            "• Al sustituir formalmente w = 0 y u = x, obtenemos\n"
            "  la suma de dos productos directos.\n"
            "• Cada producto asocia una función en 0 con una en x."
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=6.2)

        # ==========================================================
        # PASO 4: Sustitución de Valores Notables
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Evaluación con los Valores de Referencia:} \\[4pt]"
            r"&\text{Incorporamos los valores demostrados previamente:} \\[4pt]"
            r"&\bullet \mathbf{\cos(0) = 1} \quad (\text{por Postulado P2}) \\[3pt]"
            r"&\bullet \mathbf{\operatorname{sen}(0) = 0} \quad (\text{por Propiedad (6.4)}) \\[5pt]"
            r"&\text{Reemplazando directamente en la igualdad:} \\[4pt]"
            r"&\cos(-x) = (1) \cdot \cos(x) + (0) \cdot \operatorname{sen}(x) \\[5pt]"
            r"&\cos(-x) = \cos(x) + 0 \\[5pt]"
            r"&\implies \mathbf{\cos(-x) = \cos(x)}"
            r"\end{aligned}",
            font_size=14.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Simplificación Aritmética:\n"
            "• El factor cos(0) se sustituye por el neutro multiplicativo 1.\n"
            "• El factor sen(0) se sustituye por 0, anulando por\n"
            "  completo el término cruzado: 0 · sen(x) = 0.\n"
            "• La igualdad se reduce directamente a cos(x)."
        )

        self.morph_step(eq4, just4, box_color=THEME["success"], advance_to_step=3, wait_time=6.2)

        # ==========================================================
        # PASO 5: Generalización y Paridad Global
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Generalización Universal y Conclusión:} \\[4pt]"
            r"&\text{Puesto que } x \in \mathbb{R} \text{ fue seleccionado de manera arbitraria,} \\[4pt]"
            r"&\text{por la regla de Generalización Universal en lógica formal:} \\[5pt]"
            r"&\mathbf{\forall x \in \mathbb{R}: \quad \cos(-x) = \cos(x)} \quad (6.7) \\[6pt]"
            r"&\text{Definición: La función } \cos: \mathbb{R} \to [-1, 1] \text{ es una } \mathbf{\text{función PAR}.} \\[5pt]"
            r"&\text{Consecuencia: Su gráfica presenta } \mathbf{\text{simetría axial}} \text{ respecto al eje } OY."
            r"\end{aligned}",
            font_size=13.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Teorema Demostrado:\n"
            "• Al no haber impuesto ninguna restricción sobre x,\n"
            "  la propiedad es válida en todo el dominio ℝ.\n"
            "• Se formaliza el Teorema 6.3 del texto.\n"
            "• Esta propiedad de simetría par es fundamental\n"
            "  en el cálculo analítico y transformaciones de fase."
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=6.2)

        # ==========================================================
        # PASO 6: Esquema Gráfico y Síntesis
        # ==========================================================
        left_summary = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Síntesis Deductiva:} \\[4pt]"
            r"&\cos(-x) = \cos(0 - x) \\[3pt]"
            r"&= \cos(0)\cos(x) + \operatorname{sen}(0)\operatorname{sen}(x) \\[3pt]"
            r"&= (1)\cos(x) + (0)\operatorname{sen}(x) \\[3pt]"
            r"&= \cos(x) \\[5pt]"
            r"&\mathbf{\forall x \in \mathbb{R}: \cos(-x) = \cos(x)} \quad \blacksquare \\[6pt]"
            r"&\text{Gráfica: Simetría axial respecto a } x = 0."
            r"\end{aligned}",
            font_size=13.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        box6 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.18, corner_radius=0.1)

        # Gráfico cartesiano de la función coseno
        axes, axes_labels = self.setup_axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=3.6,
            y_length=2.8,
            center=[3.0, -0.45, 0],
            include_numbers=True
        )
        graph_title = Text("Simetría Par de y = cos(x)", font_size=11, color=WHITE).next_to(axes, UP, buff=0.15)

        # Curva de coseno
        cos_curve = axes.plot(
            lambda x: np.cos(x),
            x_range=[-3.3, 3.3],
            color=THEME["curve"],
            stroke_width=2.5
        )
        cos_lbl = MathTex(r"y = \cos(x)", font_size=10.5, color=THEME["curve"]).move_to(axes.c2p(2.2, 1.25))

        # Puntos simétricos x₀ = 1.2 y -x₀ = -1.2
        x0 = 1.2
        y0 = np.cos(x0)  # ≈ 0.362

        dot_pos = Dot(axes.c2p(x0, y0), radius=0.065, color=THEME["highlight"])
        lbl_pos = MathTex(r"(x, \cos(x))", font_size=9, color=THEME["highlight"]).next_to(dot_pos, UR, buff=0.06)

        dot_neg = Dot(axes.c2p(-x0, y0), radius=0.065, color=THEME["secondary"])
        lbl_neg = MathTex(r"(-x, \cos(-x))", font_size=9, color=THEME["secondary"]).next_to(dot_neg, UL, buff=0.06)

        # Línea horizontal de cota idéntica
        sym_line = DashedVMobject(
            Line(axes.c2p(-x0, y0), axes.c2p(x0, y0), color=THEME["statement_box"], stroke_width=1.8),
            num_dashes=12
        )
        lbl_level = MathTex(r"y = \cos(x) = \cos(-x)", font_size=8.5, color=THEME["statement_box"]).next_to(sym_line, DOWN, buff=0.08)

        prog_anims = self.get_advance_progress_anims(5)

        self.play(
            FadeOut(self.active_math),
            FadeOut(self.active_just),
            FadeOut(self.active_box),
            FadeIn(left_summary),
            Create(box6),
            Create(axes),
            Write(axes_labels),
            Write(graph_title),
            *prog_anims,
            run_time=1.8
        )
        self.active_box = box6
        self.active_math = left_summary
        self.active_just = None

        self.play(
            Create(cos_curve),
            Write(cos_lbl),
            FadeIn(dot_pos),
            Write(lbl_pos),
            FadeIn(dot_neg),
            Write(lbl_neg),
            Create(sym_line),
            Write(lbl_level),
            run_time=2.2
        )
        self.wait(5.0)

        # Despedida y cierre institucional
        graph_group = VGroup(
            axes, axes_labels, graph_title,
            cos_curve, cos_lbl,
            dot_pos, lbl_pos, dot_neg, lbl_neg,
            sym_line, lbl_level
        )
        self.play(
            FadeOut(graph_group),
            FadeOut(self.active_math),
            FadeOut(self.active_box),
            run_time=1.4
        )
        self.wait(1.0)
