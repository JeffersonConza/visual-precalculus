"""
Ejercicio 6.6 - Precálculo 2 (Colección Yachay Tech / Editorial Amarun)
Capítulo 6: Funciones Trigonométricas
Tema: Corolario 6.13: Seno de la Diferencia, Ángulo Doble y Valores en 2π:
      (6.19) sen(2π) = 0,  (6.20) cos(2π) = 1,
      (6.21) sen(2x) = 2 sen(x) cos(x),
      (6.22) sen(x - y) = sen(x) cos(y) - sen(y) cos(x).

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


class Ejercicio06_06(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 6",
            exercise="Ejercicio 6.6",
            topic="Seno del Ángulo Doble, Diferencia y Evaluación en 2π"
        )

        # 2. Enunciado institucional permanente (y = 2.5)
        self.setup_statement(
            desc_text="Demostrar las cuatro identidades fundamentales del Corolario 6.13 en ℝ:",
            math_tex=r"\operatorname{sen}(2x) = 2\operatorname{sen}(x)\cos(x), \; \operatorname{sen}(x-y) = \operatorname{sen}(x)\cos(y)-\operatorname{sen}(y)\cos(x), \; \operatorname{sen}(2\pi)=0, \; \cos(2\pi)=1.",
            desc_font_size=13,
            math_font_size=11,
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (6 pasos)
        self.setup_progress_bar([
            "1/6: Marco Teórico: Teorema 6.12",
            "2/6: Seno del Ángulo Doble: sen(2x)",
            "3/6: Seno de la Diferencia: sen(x - y)",
            "4/6: Evaluación Notable: sen(2π) = 0",
            "5/6: Evaluación Notable: cos(2π) = 1",
            "6/6: Esquema Gráfico y Síntesis"
        ])

        # ==========================================================
        # PASO 1: Marco Teórico: Teorema 6.12
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Marco Teórico y Resultados Previos:} \\[4pt]"
            r"&\text{Disponemos de las siguientes identidades probadas previamente:} \\[5pt]"
            r"&\bullet \mathbf{\text{Teorema 6.12 (Seno de la suma):}} \\[2pt]"
            r"&\quad \forall x, y \in \mathbb{R}: \operatorname{sen}(x + y) = \operatorname{sen}(x)\cos(y) + \operatorname{sen}(y)\cos(x) \quad (6.18) \\[4pt]"
            r"&\bullet \mathbf{\text{Paridad e Imparidad: }} \cos(-y) = \cos(y) \text{ y } \operatorname{sen}(-y) = -\operatorname{sen}(y) \\[4pt]"
            r"&\bullet \mathbf{\text{Valores en } \pi: } \cos(\pi) = -1 \text{ (P2)} \quad \text{y} \quad \operatorname{sen}(\pi) = 0 \text{ (6.5)}"
            r"\end{aligned}",
            font_size=13.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Base Axiomática:\n"
            "• El Teorema 6.12 establece la fórmula de adición\n"
            "  para la función seno.\n"
            "• La paridad del coseno (Teorema 6.3) y la\n"
            "  imparidad del seno (Teorema 6.7) serán cruciales.\n"
            "• Los valores notables en π permiten calcular 2π."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=6.2)

        # ==========================================================
        # PASO 2: Seno del Ángulo Doble: sen(2x)
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Demostración de (6.21): } \operatorname{sen}(2x) = 2\operatorname{sen}(x)\cos(x): \\[4pt]"
            r"&\text{Sea } x \in \mathbb{R} \text{ genérico. Expresamos el argumento doble como } 2x = x + x: \\[5pt]"
            r"&\operatorname{sen}(2x) = \operatorname{sen}(x + x) \\[5pt]"
            r"&\text{Aplicando la fórmula de adición (6.18) tomando } y = x: \\[4pt]"
            r"&\operatorname{sen}(x + x) = \operatorname{sen}(x)\cos(x) + \operatorname{sen}(x)\cos(x) \\[5pt]"
            r"&\implies \mathbf{\operatorname{sen}(2x) = 2\operatorname{sen}(x)\cos(x)} \quad (6.21)"
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Duplicación del Argumento:\n"
            "• Al descomponer 2x en x + x, los dos sumandos de\n"
            "  la fórmula de adición resultan idénticos.\n"
            "• Sumando términos semejantes se obtiene el factor 2.\n"
            "• Esta fórmula descompone la oscilación doble en\n"
            "  producto de armónicos simples."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=6.2)

        # ==========================================================
        # PASO 3: Seno de la Diferencia: sen(x - y)
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Demostración de (6.22): Seno de la Diferencia:} \\[4pt]"
            r"&\text{Sean } x, y \in \mathbb{R} \text{ genéricos. Escribimos la resta como adición:} \\[4pt]"
            r"&\operatorname{sen}(x - y) = \operatorname{sen}(x + (-y)) \\[5pt]"
            r"&\text{Por la fórmula de la suma (6.18):} \\[4pt]"
            r"&\operatorname{sen}(x + (-y)) = \operatorname{sen}(x)\cos(-y) + \operatorname{sen}(-y)\cos(x) \\[5pt]"
            r"&\text{Sustituyendo } \cos(-y) = \cos(y) \text{ y } \operatorname{sen}(-y) = -\operatorname{sen}(y): \\[4pt]"
            r"&\operatorname{sen}(x - y) = \operatorname{sen}(x)\cos(y) + (-\operatorname{sen}(y))\cos(x) \\[5pt]"
            r"&\implies \mathbf{\operatorname{sen}(x - y) = \operatorname{sen}(x)\cos(y) - \operatorname{sen}(y)\cos(x)} \quad (6.22)"
            r"\end{aligned}",
            font_size=13.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Resta de Argumentos:\n"
            "• Transformamos la resta x - y en la suma x + (-y).\n"
            "• El coseno absorbe el signo negativo: cos(-y) = cos(y).\n"
            "• El seno extrae el signo negativo: sen(-y) = -sen(y).\n"
            "• El signo '+' de la suma cambia naturalmente a '-'."
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=6.2)

        # ==========================================================
        # PASO 4: Evaluación Notable: sen(2π) = 0
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Demostración de (6.19): } \operatorname{sen}(2\pi) = 0: \\[4pt]"
            r"&\text{Especializamos la fórmula del ángulo doble (6.21) en } x = \pi: \\[5pt]"
            r"&\operatorname{sen}(2\pi) = \operatorname{sen}(2 \cdot \pi) = 2\operatorname{sen}(\pi)\cos(\pi) \\[5pt]"
            r"&\text{Recordamos los valores previamente establecidos:} \\[4pt]"
            r"&\bullet \mathbf{\operatorname{sen}(\pi) = 0} \quad (\text{Propiedad (6.5)}) \\[3pt]"
            r"&\bullet \mathbf{\cos(\pi) = -1} \quad (\text{Postulado P2}) \\[5pt]"
            r"&\text{Sustituyendo aritméticamente:} \\[4pt]"
            r"&\operatorname{sen}(2\pi) = 2 \cdot (0) \cdot (-1) = \mathbf{0} \quad (6.19)"
            r"\end{aligned}",
            font_size=14.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Evaluación en 2π (Seno):\n"
            "• La fórmula del ángulo doble aplicada a π\n"
            "  produce directamente 2 sen(π) cos(π).\n"
            "• Al ser sen(π) = 0, el producto completo se anula.\n"
            "• Esto demuestra que la ordenada en una vuelta\n"
            "  completa de circunferencia regresa a cero."
        )

        self.morph_step(eq4, just4, box_color=THEME["success"], advance_to_step=3, wait_time=6.2)

        # ==========================================================
        # PASO 5: Evaluación Notable: cos(2π) = 1
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Demostración de (6.20): } \cos(2\pi) = 1: \\[4pt]"
            r"&\text{Especializamos la fórmula del coseno doble (6.14) en } x = \pi: \\[5pt]"
            r"&\cos(2\pi) = \cos(2 \cdot \pi) = \cos^2(\pi) - \operatorname{sen}^2(\pi) \\[5pt]"
            r"&\text{Reemplazando } \cos(\pi) = -1 \text{ y } \operatorname{sen}(\pi) = 0: \\[4pt]"
            r"&\cos(2\pi) = (-1)^2 - (0)^2 = 1 - 0 = \mathbf{1} \quad (6.20) \\[6pt]"
            r"&\text{Consecuencia Geométrica: El punto } (\cos(2\pi), \operatorname{sen}(2\pi)) = (1, 0) \\[3pt]"
            r"&\text{coincide exactamente con el origen angular } (\cos(0), \operatorname{sen}(0)) = (1, 0)."
            r"\end{aligned}",
            font_size=13.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Evaluación en 2π (Coseno) y Periodicidad:\n"
            "• Por el coseno doble: cos(2π) = cos²(π) - sen²(π).\n"
            "• (-1)² - 0² = 1 - 0 = 1.\n"
            "• En el círculo trigonométrico, el ángulo 2π\n"
            "  retorna al punto inicial (1, 0).\n"
            "• Queda completamente demostrado el Corolario 6.13."
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=6.2)

        # ==========================================================
        # PASO 6: Esquema Gráfico y Síntesis
        # ==========================================================
        left_summary = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Resumen del Corolario 6.13:} \\[4pt]"
            r"&\mathbf{\operatorname{sen}(2x) = 2\operatorname{sen}(x)\cos(x)} \quad (6.21) \\[4pt]"
            r"&\mathbf{\operatorname{sen}(x - y) = \operatorname{sen}(x)\cos(y) - \operatorname{sen}(y)\cos(x)} \quad (6.22) \\[4pt]"
            r"&\mathbf{\operatorname{sen}(2\pi) = 0} \quad (6.19) \\[4pt]"
            r"&\mathbf{\cos(2\pi) = 1} \quad (6.20) \\[5pt]"
            r"&\text{Demostrado para todo } x, y \in \mathbb{R}. \quad \blacksquare \\[5pt]"
            r"&\text{Gráfica: Círculo unitario y retorno en } 2\pi."
            r"\end{aligned}",
            font_size=13,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        box6 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.18, corner_radius=0.1)

        # Gráfico: Círculo trigonométrico unitario
        axes, axes_labels = self.setup_axes(
            x_range=[-1.5, 1.5, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=3.2,
            y_length=3.0,
            center=[3.0, -0.45, 0],
            include_numbers=True
        )
        graph_title = Text("Círculo Unitario: Retorno 2π", font_size=11, color=WHITE).next_to(axes, UP, buff=0.15)

        # Circunferencia unitaria x² + y² = 1
        unit_circle = axes.plot_parametric_curve(
            lambda t: np.array([np.cos(t), np.sin(t), 0]),
            t_range=[0, 2*np.pi],
            color=THEME["curve"],
            stroke_width=2.5
        )

        # Punto notable en 2π = (1, 0)
        dot_2pi = Dot(axes.c2p(1, 0), radius=0.07, color=THEME["highlight"])
        lbl_2pi = MathTex(r"(1, 0) \equiv 2\pi", font_size=10, color=THEME["highlight"]).next_to(dot_2pi, UR, buff=0.08)

        # Punto en π = (-1, 0)
        dot_pi = Dot(axes.c2p(-1, 0), radius=0.06, color=THEME["secondary"])
        lbl_pi = MathTex(r"(-1, 0) \equiv \pi", font_size=9.5, color=THEME["secondary"]).next_to(dot_pi, UL, buff=0.08)

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
            Create(unit_circle),
            FadeIn(dot_2pi),
            Write(lbl_2pi),
            FadeIn(dot_pi),
            Write(lbl_pi),
            run_time=2.2
        )
        self.wait(5.0)

        # Despedida y cierre institucional
        graph_group = VGroup(
            axes, axes_labels, graph_title,
            unit_circle, dot_2pi, lbl_2pi, dot_pi, lbl_pi
        )
        self.play(
            FadeOut(graph_group),
            FadeOut(self.active_math),
            FadeOut(self.active_box),
            run_time=1.4
        )
        self.wait(1.0)
