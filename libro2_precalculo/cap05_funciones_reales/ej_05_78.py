"""
Ejercicio 5.78 - Precálculo 2 (Colección Yachay Tech / Editorial Amarun)
Capítulo 5: Funciones Reales
Tema: Ecuaciones Logarítmicas y Dominio de Validez (Detección de Raíces Extrañas):
      log₂(t² - 7t + 3) - log₂(2t + 1) = log₂(t² + 7t - 3) - log₂(2t - 1), t ∈ ℝ.

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


class Ejercicio05_78(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.78",
            topic="Ecuaciones Logarítmicas y Dominio de Existencia"
        )

        # 2. Enunciado institucional permanente (y = 2.5)
        self.setup_statement(
            desc_text="Resolver la ecuación logarítmica analizando su dominio de validez:",
            math_tex=r"\log_2(t^2 - 7t + 3) - \log_2(2t + 1) = \log_2(t^2 + 7t - 3) - \log_2(2t - 1), \quad t \in \mathbb{R}.",
            desc_font_size=13,
            math_font_size=12,
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (6 pasos)
        self.setup_progress_bar([
            "1/6: Condiciones de Existencia del Dominio",
            "2/6: Raíces de Frontera y Discriminantes",
            "3/6: Intersección: Dominio Efectivo",
            "4/6: Transformación y Raíces Algebraicas",
            "5/6: Contrastación y Raíces Extrañas",
            "6/6: Esquema Gráfico y Síntesis"
        ])

        # ==========================================================
        # PASO 1: Condiciones de Existencia del Dominio
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Condiciones de Existencia del Dominio } \operatorname{Dom}(E): \\[4pt]"
            r"&\text{Para que los cuatro logaritmos en base 2 estén bien definidos en } \mathbb{R}: \\[4pt]"
            r"&(C_1): \quad t^2 - 7t + 3 > 0 \\[3pt]"
            r"&(C_2): \quad 2t + 1 > 0 \implies t > -\frac{1}{2} = -0.5 \\[3pt]"
            r"&(C_3): \quad t^2 + 7t - 3 > 0 \\[3pt]"
            r"&(C_4): \quad 2t - 1 > 0 \implies \mathbf{t > \frac{1}{2} = 0.5} \\[5pt]"
            r"&\text{El dominio real es la intersección simultánea: } \operatorname{Dom}(E) = C_1 \cap C_2 \cap C_3 \cap C_4."
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Dominio de Existencia:\n"
            "• El logaritmo real solo admite argumentos\n"
            "  estrictamente positivos (> 0).\n"
            "• Toda operación algebraica previa a determinar el\n"
            "  dominio corre el riesgo de introducir raíces extrañas.\n"
            "• La condición (C₄) impone inmediatamente t > 1/2."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=6.2)

        # ==========================================================
        # PASO 2: Raíces de Frontera y Discriminantes
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Raíces de los Trinomios Cuadráticos:} \\[4pt]"
            r"&\bullet \text{ Para } (C_1): t^2 - 7t + 3 = 0 \implies \Delta_1 = 49 - 12 = \mathbf{37} \\[3pt]"
            r"&\quad t = \frac{7 \pm \sqrt{37}}{2} \implies \begin{cases} t_1 \approx \frac{7 - 6.083}{2} \approx \mathbf{0.458} \\ t_2 \approx \frac{7 + 6.083}{2} \approx \mathbf{6.542} \end{cases} \\[4pt]"
            r"&\quad \implies C_1 = \left] -\infty, \frac{7-\sqrt{37}}{2} \right[ \cup \left] \frac{7+\sqrt{37}}{2}, +\infty \right[ \\[5pt]"
            r"&\bullet \text{ Para } (C_3): t^2 + 7t - 3 = 0 \implies \Delta_2 = 49 + 12 = \mathbf{61} \\[3pt]"
            r"&\quad t = \frac{-7 \pm \sqrt{61}}{2} \implies \begin{cases} t_3 \approx \frac{-7 - 7.81}{2} \approx -7.405 \\ t_4 \approx \frac{-7 + 7.81}{2} \approx \mathbf{0.405} \end{cases} \\[4pt]"
            r"&\quad \implies C_3 = \left] -\infty, \frac{-7-\sqrt{61}}{2} \right[ \cup \left] \frac{-7+\sqrt{61}}{2}, +\infty \right["
            r"\end{aligned}",
            font_size=13,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Raíces Cuadráticas Críticas:\n"
            "• Aquí se utiliza la indicación del autor:\n"
            "  √37 ≈ 6.083  y  √61 ≈ 7.81.\n"
            "• Las raíces dividen la recta real en zonas de signo.\n"
            "• La parábola (C₁) es positiva fuera de [0.458, 6.542].\n"
            "• La parábola (C₃) es positiva a la derecha de 0.405."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=6.2)

        # ==========================================================
        # PASO 3: Intersección: Dominio Efectivo
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Intersección de Condiciones y Dominio Efectivo:} \\[4pt]"
            r"&\text{Combinamos la restricción lineal con la cuadrática:} \\[4pt]"
            r"&\bullet \text{ Por } (C_4), \text{ requerimos } t > \frac{1}{2} = 0.5. \\[4pt]"
            r"&\bullet \text{ Como } \frac{7-\sqrt{37}}{2} \approx 0.458 < 0.5, \text{ la rama izquierda de } C_1 \\[3pt]"
            r"&\quad \left] -\infty, 0.458 \right[ \text{ queda totalmente excluida por } (C_4). \\[5pt]"
            r"&\bullet \text{ Por lo tanto, en } t > 0.5, \text{ la condición } C_1 \text{ exige } t > \frac{7+\sqrt{37}}{2} \approx 6.542. \\[5pt]"
            r"&\implies \mathbf{\operatorname{Dom}(E) = \left] \frac{7+\sqrt{37}}{2}, \; +\infty \right[ \approx \left] 6.542, \; +\infty \right[}"
            r"\end{aligned}",
            font_size=13.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Dominio Efectivo:\n"
            "• Al interceptar todas las condiciones:\n"
            "  (C₄) exige t > 0.5.\n"
            "• Pero el intervalo ]0.458, 6.542[ hace negativo\n"
            "  al primer argumento (t² - 7t + 3).\n"
            "• En consecuencia, todo t ≤ 6.542 es inadmisible.\n"
            "• Solo los reales t > (7+√37)/2 son válidos."
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=6.2)

        # ==========================================================
        # PASO 4: Transformación y Raíces Algebraicas
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Transformación Algebraica de la Ecuación:} \\[4pt]"
            r"&\log_2\left( \frac{t^2 - 7t + 3}{2t + 1} \right) = \log_2\left( \frac{t^2 + 7t - 3}{2t - 1} \right) \\[5pt]"
            r"&\implies \frac{t^2 - 7t + 3}{2t + 1} = \frac{t^2 + 7t - 3}{2t - 1} \\[5pt]"
            r"&(t^2 - 7t + 3)(2t - 1) = (t^2 + 7t - 3)(2t + 1) \\[4pt]"
            r"&2t^3 - 15t^2 + 13t - 3 = 2t^3 + 15t^2 + t - 3 \\[5pt]"
            r"&30t^2 - 12t = 0 \iff 6t(5t - 2) = 0 \\[5pt]"
            r"&\implies \mathbf{t = 0} \quad \lor \quad \mathbf{t = \frac{2}{5} = 0.4} \quad (\text{Candidatos formales})"
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Manipulación Algebraica:\n"
            "• Igualando los cocientes e igualando el producto\n"
            "  cruzado se cancelan los términos cúbicos 2t³.\n"
            "• Se reduce a una ecuación cuadrática incompleta:\n"
            "  30t² - 12t = 0 ⇒ 6t(5t - 2) = 0.\n"
            "• Produce dos candidatos algebraicos: t = 0 y t = 0.4.\n"
            "• ¡Ambos deben contrastarse contra Dom(E)!"
        )

        self.morph_step(eq4, just4, box_color=THEME["secondary"], advance_to_step=3, wait_time=6.2)

        # ==========================================================
        # PASO 5: Contrastación y Raíces Extrañas
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Contrastación con el Dominio y Raíces Extrañas:} \\[4pt]"
            r"&\text{Comprobamos la pertenencia al dominio } \operatorname{Dom}(E) = \left] \frac{7+\sqrt{37}}{2}, +\infty \right[: \\[5pt]"
            r"&\bullet \text{ Para } t = 0: \quad 0 < 6.542 \implies \mathbf{0 \notin \operatorname{Dom}(E)} \\[3pt]"
            r"&\quad \text{En efecto, } 2(0) - 1 = -1 < 0 \implies \log_2(-1) \notin \mathbb{R}. \\[5pt]"
            r"&\bullet \text{ Para } t = \frac{2}{5} = 0.4: \quad 0.4 < 6.542 \implies \mathbf{\frac{2}{5} \notin \operatorname{Dom}(E)} \\[3pt]"
            r"&\quad \text{En efecto, } 2(0.4) - 1 = -0.2 < 0 \implies \log_2(-0.2) \notin \mathbb{R}. \\[6pt]"
            r"&\implies \textbf{Ambas son raíces extrañas.} \quad \mathbf{CS = \emptyset}"
            r"\end{aligned}",
            font_size=13.5,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Detección de Raíces Extrañas:\n"
            "• Ni 0 ni 0.4 pertenecen al dominio de existencia.\n"
            "• Al sustituir en la ecuación original, los argumentos\n"
            "  (2t - 1) resultan negativos, invalidando el logaritmo.\n"
            "• Aparecieron porque el cociente (-0.04)/(-0.2) = +0.2\n"
            "  oculta los signos negativos individuales.\n"
            "• Por lo tanto, el conjunto solución es VACÍO (∅)."
        )

        self.morph_step(eq5, just5, box_color=THEME["statement_box"], advance_to_step=4, wait_time=6.2)

        # ==========================================================
        # PASO 6: Esquema Gráfico y Síntesis
        # ==========================================================
        left_summary = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Síntesis y Conclusión Rigurosa:} \\[4pt]"
            r"&\operatorname{Dom}(E) = \left] \frac{7+\sqrt{37}}{2}, \; +\infty \right[ \approx \left] 6.542, \; +\infty \right[ \\[5pt]"
            r"&\text{Candidatos algebraicos:} \\[3pt]"
            r"&t_a = 0 \notin \operatorname{Dom}(E) \implies \text{Raíz extraña} \\[3pt]"
            r"&t_b = \frac{2}{5} \notin \operatorname{Dom}(E) \implies \text{Raíz extraña} \\[6pt]"
            r"&\mathbf{CS = \emptyset} \quad (\text{Sin solución en } \mathbb{R})"
            r"\end{aligned}",
            font_size=14,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        box6 = SurroundingRectangle(left_summary, color=THEME["statement_box"], buff=0.18, corner_radius=0.1)

        # Gráfico: Recta numérica mostrando la zona de validez y los puntos descartados
        axes, axes_labels = self.setup_axes(
            x_range=[-1.5, 8.5, 1],
            y_range=[-1.0, 1.5, 1],
            x_length=3.7,
            y_length=2.2,
            center=[3.0, -0.45, 0],
            include_numbers=True
        )
        graph_title = Text("Recta Real: Dominio y Raíces Extrañas", font_size=11, color=WHITE).next_to(axes, UP, buff=0.15)

        # Región de validez t > 6.542
        valid_line = axes.plot(lambda x: 0.0, x_range=[6.542, 8.3], color=THEME["success"], stroke_width=4.5)
        dot_valid = Dot(axes.c2p(6.542, 0), radius=0.06, color=THEME["success"])
        lbl_valid = MathTex(r"> 6.54", font_size=9.5, color=THEME["success"]).next_to(dot_valid, UP, buff=0.1)

        # Zona no permitida
        invalid_line = axes.plot(lambda x: 0.0, x_range=[-1.2, 6.542], color=THEME["statement_box"], stroke_width=2.5)

        # Candidatos tachados
        dot_c1 = Dot(axes.c2p(0, 0), radius=0.07, color=THEME["highlight"])
        lbl_c1 = MathTex(r"t=0 \times", font_size=9.5, color=THEME["highlight"]).next_to(dot_c1, DOWN, buff=0.12)

        dot_c2 = Dot(axes.c2p(0.4, 0), radius=0.07, color=THEME["secondary"])
        lbl_c2 = MathTex(r"t=0.4 \times", font_size=9.5, color=THEME["secondary"]).next_to(dot_c2, UP, buff=0.12)

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
            Create(invalid_line),
            Create(valid_line),
            FadeIn(dot_valid),
            Write(lbl_valid),
            FadeIn(dot_c1),
            Write(lbl_c1),
            FadeIn(dot_c2),
            Write(lbl_c2),
            run_time=2.2
        )
        self.wait(5.0)

        # Despedida y cierre institucional
        graph_group = VGroup(
            axes, axes_labels, graph_title,
            invalid_line, valid_line, dot_valid, lbl_valid,
            dot_c1, lbl_c1, dot_c2, lbl_c2
        )
        self.play(
            FadeOut(graph_group),
            FadeOut(self.active_math),
            FadeOut(self.active_box),
            run_time=1.4
        )
        self.wait(1.0)
