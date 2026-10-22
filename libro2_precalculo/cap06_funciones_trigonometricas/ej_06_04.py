"""
Ejercicio 6.4 - Precálculo 2 (Colección Yachay Tech / Editorial Amarun)
Capítulo 6: Funciones Trigonométricas
Tema: Corolario 6.9: Coseno del Ángulo Doble:
      Demostración a partir del Corolario 6.8 (Coseno de la suma de dos ángulos):
      ∀ x ∈ ℝ: cos(2x) = cos²(x) - sen²(x).

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


class Ejercicio06_04(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 6",
            exercise="Ejercicio 6.4",
            topic="Coseno del Ángulo Doble y Formas Cuadráticas"
        )

        # 2. Enunciado institucional permanente (y = 2.5)
        self.setup_statement(
            desc_text="A partir del Corolario 6.8 (Coseno de la suma), demostrar formalmente:",
            math_tex=r"\text{Corolario 6.9: } \forall x \in \mathbb{R}: \cos(2x) = \cos^2(x) - \operatorname{sen}^2(x) \quad (6.14)",
            desc_font_size=13,
            math_font_size=12,
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (6 pasos)
        self.setup_progress_bar([
            "1/6: Marco Teórico y Corolario 6.8",
            "2/6: Artificio Aditivo: 2x = x + x",
            "3/6: Sustitución en la Fórmula de la Suma",
            "4/6: Reducción a Formas Cuadráticas",
            "5/6: Formas Equivalentes y Generalización",
            "6/6: Esquema Gráfico y Síntesis"
        ])

        # ==========================================================
        # PASO 1: Marco Teórico y Corolario 6.8
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Resultado Previo Fundamental (Corolario 6.8):} \\[4pt]"
            r"&\text{Se demostró previamente la fórmula para la suma de dos ángulos:} \\[5pt]"
            r"&\mathbf{\forall x, y \in \mathbb{R}: \quad \cos(x + y) = \cos(x)\cos(y) - \operatorname{sen}(x)\operatorname{sen}(y)} \quad (6.13) \\[6pt]"
            r"&\text{Objetivo del Ejercicio 6.4:} \\[3pt]"
            r"&\text{Deducir la expresión cerrada para el ángulo duplicado } 2x, \\[3pt]"
            r"&\text{restringiendo la suma binaria a dos argumentos coincidentes.} "
            r"\end{aligned}",
            font_size=13.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Base Teórica:\n"
            "• El Corolario 6.8 generalizó el postulado P3\n"
            "  para la suma cos(x + y) usando la paridad.\n"
            "• Establece una identidad universal válida para\n"
            "  cualesquiera pares de números reales (x, y).\n"
            "• El caso particular 2x se obtiene vinculando x e y."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=6.2)

        # ==========================================================
        # PASO 2: Artificio Aditivo: 2x = x + x
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Elección Genérica y Descomposición Aditiva:} \\[4pt]"
            r"&\text{Sea } x \in \mathbb{R} \text{ un número real arbitrariamente elegido.} \\[5pt]"
            r"&\text{Por definición elemental del producto escalar por 2:} \\[4pt]"
            r"&2x = x + x \\[5pt]"
            r"&\text{Por tanto, podemos expresar el coseno del ángulo doble como:} \\[4pt]"
            r"&\cos(2x) = \cos(x + x) \\[5pt]"
            r"&\text{Asignamos en el Corolario 6.8 la sustitución: } \mathbf{y = x}."
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Especialización de Variables:\n"
            "• La multiplicación por 2 equivale a sumar el\n"
            "  número consigo mismo: 2x = x + x.\n"
            "• Fijamos la segunda variable y exactamente igual a x.\n"
            "• Al ser x un real cualquiera, no se pierde generalidad."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=6.2)

        # ==========================================================
        # PASO 3: Sustitución en la Fórmula de la Suma
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Sustitución Directa en la Fórmula (6.13):} \\[4pt]"
            r"&\text{Tomando } y = x \text{ en la relación } \cos(x+y) = \cos(x)\cos(y) - \operatorname{sen}(x)\operatorname{sen}(y): \\[5pt]"
            r"&\cos(x + x) = \cos(x)\cos(x) - \operatorname{sen}(x)\operatorname{sen}(x) \\[6pt]"
            r"&\implies \mathbf{\cos(2x) = \cos(x)\cos(x) - \operatorname{sen}(x)\operatorname{sen}(x)}"
            r"\end{aligned}",
            font_size=14.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Desarrollo de la Identidad:\n"
            "• Reemplazamos formalmente cada aparición de y\n"
            "  por la variable x.\n"
            "• Cada uno de los dos términos se convierte en el\n"
            "  producto de una función trigonométrica por sí misma."
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=6.2)

        # ==========================================================
        # PASO 4: Reducción a Formas Cuadráticas
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Notación y Reducción de Potencias:} \\[4pt]"
            r"&\text{Por definición de las potencias de funciones reales:} \\[4pt]"
            r"&\bullet \; \cos(x) \cdot \cos(x) = \mathbf{\cos^2(x)} \\[4pt]"
            r"&\bullet \; \operatorname{sen}(x) \cdot \operatorname{sen}(x) = \mathbf{\operatorname{sen}^2(x)} \\[6pt]"
            r"&\text{Sustituyendo ambos productos cuadráticos:} \\[4pt]"
            r"&\mathbf{\cos(2x) = \cos^2(x) - \operatorname{sen}^2(x)}"
            r"\end{aligned}",
            font_size=14.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Simplificación Cuadrática:\n"
            "• Aplicamos la notación estándar de potencias\n"
            "  trigonométricas: f²(x) = [f(x)]².\n"
            "• Se obtiene la diferencia directa entre el cuadrado\n"
            "  del coseno y el cuadrado del seno."
        )

        self.morph_step(eq4, just4, box_color=THEME["success"], advance_to_step=3, wait_time=6.2)

        # ==========================================================
        # PASO 5: Formas Equivalentes y Generalización
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Generalización Universal y Variantes Pitagóricas:} \\[4pt]"
            r"&\text{Como } x \in \mathbb{R} \text{ fue arbitrario, por Generalización Universal:} \\[5pt]"
            r"&\mathbf{\forall x \in \mathbb{R}: \quad \cos(2x) = \cos^2(x) - \operatorname{sen}^2(x)} \quad (6.14) \\[6pt]"
            r"&\text{Utilizando la Identidad Fundamental } \operatorname{sen}^2(x) + \cos^2(x) = 1: \\[4pt]"
            r"&\bullet \; \cos(2x) = \cos^2(x) - (1 - \cos^2(x)) = \mathbf{2\cos^2(x) - 1} \\[4pt]"
            r"&\bullet \; \cos(2x) = (1 - \operatorname{sen}^2(x)) - \operatorname{sen}^2(x) = \mathbf{1 - 2\operatorname{sen}^2(x)}"
            r"\end{aligned}",
            font_size=13.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Teorema y Formas Alternas:\n"
            "• La identidad vale para todo x real sin excepción.\n"
            "• Mediante sen²(x) + cos²(x) = 1, la fórmula se expresa\n"
            "  únicamente en función de cos(x) o únicamente de sen(x).\n"
            "• Estas formas son la base de los ángulos medios."
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=6.2)

        # ==========================================================
        # PASO 6: Esquema Gráfico y Síntesis
        # ==========================================================
        left_summary = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Síntesis Deductiva:} \\[4pt]"
            r"&\cos(2x) = \cos(x + x) \\[3pt]"
            r"&= \cos(x)\cos(x) - \operatorname{sen}(x)\operatorname{sen}(x) \\[3pt]"
            r"&= \cos^2(x) - \operatorname{sen}^2(x) \\[5pt]"
            r"&\mathbf{\forall x \in \mathbb{R}: \cos(2x) = \cos^2(x) - \operatorname{sen}^2(x)} \quad \blacksquare \\[6pt]"
            r"&\text{Gráfica: } y = \cos(2x) \text{ de frecuencia doble } (T = \pi)."
            r"\end{aligned}",
            font_size=13.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        box6 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.18, corner_radius=0.1)

        # Gráfico cartesiano comparando cos(x) y cos(2x)
        axes, axes_labels = self.setup_axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=3.6,
            y_length=2.8,
            center=[3.0, -0.45, 0],
            include_numbers=True
        )
        graph_title = Text("Coseno y Ángulo Doble", font_size=11, color=WHITE).next_to(axes, UP, buff=0.15)

        # Curva de cos(x) (referencia, punteada)
        cos_ref = DashedVMobject(
            axes.plot(lambda x: np.cos(x), x_range=[-3.3, 3.3], color=THEME["statement_box"], stroke_width=1.8),
            num_dashes=18
        )
        lbl_ref = MathTex(r"y = \cos(x)", font_size=9.5, color=THEME["statement_box"]).move_to(axes.c2p(-2.0, -1.25))

        # Curva del ángulo doble cos(2x) = cos²(x) - sen²(x)
        cos_double = axes.plot(
            lambda x: np.cos(2 * x),
            x_range=[-3.3, 3.3],
            color=THEME["curve"],
            stroke_width=2.5
        )
        lbl_double = MathTex(r"y = \cos(2x)", font_size=10.5, color=THEME["curve"]).move_to(axes.c2p(2.0, 1.25))

        # Puntos clave: x = 0 (máximo y=1) y x = π/2 ≈ 1.57 (mínimo y=-1)
        dot_0 = Dot(axes.c2p(0, 1), radius=0.065, color=THEME["highlight"])
        dot_pi2 = Dot(axes.c2p(np.pi/2, -1), radius=0.065, color=THEME["secondary"])

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
            Create(cos_ref),
            Write(lbl_ref),
            Create(cos_double),
            Write(lbl_double),
            FadeIn(dot_0),
            FadeIn(dot_pi2),
            run_time=2.2
        )
        self.wait(5.0)

        # Despedida y cierre institucional
        graph_group = VGroup(
            axes, axes_labels, graph_title,
            cos_ref, lbl_ref, cos_double, lbl_double,
            dot_0, dot_pi2
        )
        self.play(
            FadeOut(graph_group),
            FadeOut(self.active_math),
            FadeOut(self.active_box),
            run_time=1.4
        )
        self.wait(1.0)
