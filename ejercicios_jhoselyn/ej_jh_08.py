"""
Ejercicio 8 - Tutorías y Preparación Quiz 4 (Jhoselyn)
Tema: Análisis de Inyectividad, Sobreyectividad, Biyectividad y Función Inversa:
      f: [0, +∞) -> [1, +∞), con f(x) = x^2 + 1.
      Definición formal (terna A, B, f), demostración formal de inyectividad (|x1| = |x2|),
      demostración formal de sobreyectividad (preimagen real no negativa),
      conclusión de biyectividad e invertibilidad, cálculo algebraico de f^-1(x) = sqrt(x - 1),
      verificación por composición (doble identidad f^-1 o f = I_A y f o f^-1 = I_B),
      cuadro horizontal de puntos homólogos (x, y) <-> (y, x),
      y representación gráfica cartesiana dual con simetría especular respecto a la recta y = x.

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica en 8 pasos con ecuaciones en LaTeX de gran legibilidad.
"""

from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

# Configuración de Plantilla LaTeX con Paleta Andina Editorial Amarun
AMARUN_TEX_TEMPLATE = TexTemplate()
AMARUN_TEX_TEMPLATE.add_to_preamble(r"""
\usepackage{xcolor}
\definecolor{amgold}{HTML}{F6B840}
\definecolor{amteal}{HTML}{5CE1E6}
\definecolor{amred}{HTML}{E53E3E}
\definecolor{amgreen}{HTML}{48BB78}
\definecolor{amorange}{HTML}{DB5A38}
""")
config.tex_template = AMARUN_TEX_TEMPLATE


class EjercicioJh_08(AmarunExerciseScene):
    def construct(self):
        # 1. Configuración de Metadatos y Encabezado
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Jhoselyn",
            exercise="Ejercicio 8",
            topic="Inyectividad, Biyectividad y Función Inversa",
            font_size=16.5
        )

        # 2. Enunciado institucional permanente con fórmula prominente (y = 2.65)
        self.setup_statement(
            desc_text="Analice la biyectividad y halle la inversa de:",
            math_tex=r"{\color{amteal}f: [0, +\infty) \to [1, +\infty)}, \quad {\color{amteal}f(x)} = {\color{amteal}x^2 + 1}",
            desc_font_size=18.0,
            math_font_size=23.5,
            box_pos=np.array([0.0, 2.65, 0.0]),
            read_time=3.8
        )

        # 3. Barra de Progreso Interactiva (8 pasos detallados)
        self.setup_progress_bar([
            "1/8: Dominio y Codominio",
            "2/8: Demostración Inyectividad",
            "3/8: Demostración Sobreyectividad",
            "4/8: Biyectividad e Invertibilidad",
            "5/8: Cálculo de la Inversa f⁻¹",
            "6/8: Verificación Composición",
            "7/8: Simetría y Puntos Homólogos",
            "8/8: Gráfica Dual y Resumen"
        ], dot_spacing=0.82, label_font_size=14.0)

        # ==========================================================
        # PASO 1: Dominio, Codominio y Definición Formal
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Definición Formal de la Función:} \\[5pt]"
            r"&\text{Una función está completamente definida por su terna } (A, B, f): \\[4pt]"
            r"&{\color{amteal}f: [0, +\infty) \longrightarrow [1, +\infty)}, \qquad {\color{amteal}f(x) = x^2 + 1} \\[6pt]"
            r"&\bullet \mathbf{\operatorname{Dom}(f) = A = {\color{amgold}[0, +\infty)}} \quad (\text{reales no negativos}) \\[4pt]"
            r"&\bullet \mathbf{\operatorname{Cod}(f) = B = {\color{amgold}[1, +\infty)}} \quad (\text{conjunto de llegada}) \\[5pt]"
            r"&\implies \text{La restricción a } x \ge 0 \text{ evita la pérdida de inyectividad.}"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{1. Estructura de la Función:}\\[6pt]"
            r"$\bullet$ Una función no es solo su fórmula, requiere especificar dominio y codominio:\\[3pt]"
            r"\hspace*{1.2em}$f: A \to B, \quad f(x) = x^2 + 1$.\\[5pt]"
            r"$\bullet$ Conjunto de partida (Dominio):\\[3pt]"
            r"\hspace*{1.2em}${\color{amgold}A = [0, +\infty)}$ (solo rama no negativa).\\[5pt]"
            r"$\bullet$ Conjunto de llegada (Codominio):\\[3pt]"
            r"\hspace*{1.2em}${\color{amgold}B = [1, +\infty)}$.\\[5pt]"
            r"$\bullet$ Restricción clave: en todo $\mathbb{R}$, $x^2+1$ no es inyectiva ($f(-1)=f(1)$). En $[0, +\infty)$ sí lo es."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=3.2)

        # ==========================================================
        # PASO 2: Demostración Formal de Inyectividad
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Demostración Formal de Inyectividad:} \\[5pt]"
            r"&\text{Definición: } \forall \, x_1, x_2 \in [0, +\infty), \; f(x_1) = f(x_2) \implies x_1 = x_2. \\[5pt]"
            r"&\text{Sean } x_1, x_2 \in [0, +\infty) \text{ tales que } f(x_1) = f(x_2): \\[4pt]"
            r"&x_1^2 + 1 = x_2^2 + 1 \implies x_1^2 = x_2^2 \implies \sqrt{x_1^2} = \sqrt{x_2^2} \\[5pt]"
            r"&\implies |x_1| = |x_2| \\[5pt]"
            r"&\text{Como } x_1 \ge 0 \text{ y } x_2 \ge 0 \implies |x_1| = x_1 \quad \text{y} \quad |x_2| = x_2 \\[5pt]"
            r"&\implies \mathbf{{\color{amgreen}x_1 = x_2}} \implies \mathbf{f \text{ es estrictamente INYECTIVA}.}"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{2. Demostración de Inyectividad:}\\[6pt]"
            r"$\bullet$ Aplicamos la plantilla formal de examen de la cátedra:\\[3pt]"
            r"\hspace*{1.2em}Hipótesis: $f(x_1) = f(x_2)$.\\[5pt]"
            r"$\bullet$ Cancelamos el término constante $+1$:\\[3pt]"
            r"\hspace*{1.2em}$x_1^2 = x_2^2 \implies |x_1| = |x_2|$.\\[5pt]"
            r"$\bullet$ Justificación fundamental del valor absoluto:\\[3pt]"
            r"\hspace*{1.2em}Al pertenecer al dominio $[0, +\infty)$, $x_i \ge 0 \implies |x_i| = x_i$.\\[5pt]"
            r"$\bullet$ Conclusión obligatoria: $x_1 = x_2 \implies {\color{amgreen}f \text{ es inyectiva}}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq2, just2, box_color=THEME["highlight"], advance_to_step=1, wait_time=3.2)

        # ==========================================================
        # PASO 3: Demostración Formal de Sobreyectividad
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Demostración Formal de Sobreyectividad:} \\[5pt]"
            r"&\text{Definición: } \forall \, y \in [1, +\infty), \; \exists \, x \in [0, +\infty) \text{ tal que } f(x) = y. \\[5pt]"
            r"&\text{Sea } y \in [1, +\infty) \text{ arbitrario. Resolvemos para } x: \\[4pt]"
            r"&y = x^2 + 1 \iff x^2 = y - 1 \implies |x| = \sqrt{y - 1} \\[5pt]"
            r"&\text{Dado que } x \in [0, +\infty) \implies \mathbf{x = {\color{amteal}+\sqrt{y - 1}}} \\[5pt]"
            r"&\text{Existencia real: } y \ge 1 \implies y - 1 \ge 0 \implies \sqrt{y - 1} \in \mathbb{R} \\[4pt]"
            r"&\text{Además, } \sqrt{y - 1} \ge 0 \implies x \in [0, +\infty) = A \\[5pt]"
            r"&\implies \operatorname{Ran}(f) = B \implies \mathbf{f \text{ es SOBREYECTIVA}.}"
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{3. Demostración de Sobreyectividad:}\\[6pt]"
            r"$\bullet$ Todo elemento del codominio $y \in [1, +\infty)$ debe tener preimagen en $[0, +\infty)$.\\[5pt]"
            r"$\bullet$ Despeje algebraico de la preimagen $x$:\\[3pt]"
            r"\hspace*{1.2em}$x^2 = y - 1 \implies x = \sqrt{y - 1}$.\\[5pt]"
            r"$\bullet$ Garantía de existencia en los reales:\\[3pt]"
            r"\hspace*{1.2em}Como $y \ge 1$, el radicando $y - 1 \ge 0$, por lo que la raíz es real y no negativa ($x \ge 0$).\\[5pt]"
            r"$\bullet$ Se cumple $\operatorname{Im}(f) = \operatorname{Cod}(f) \implies {\color{amgreen}f \text{ es sobreyectiva}}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq3, just3, box_color=THEME["highlight"], advance_to_step=2, wait_time=3.2)

        # ==========================================================
        # PASO 4: Conclusión de Biyectividad e Invertibilidad
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Conclusión de Biyectividad e Invertibilidad:} \\[5pt]"
            r"&\bullet \mathbf{f \text{ es Inyectiva}} \quad (\text{unívoca, pasa prueba recta horizontal}) \\[4pt]"
            r"&\bullet \mathbf{f \text{ es Sobreyectiva}} \quad (\text{su imagen coincide con } [1, +\infty)) \\[6pt]"
            r"&\implies \mathbf{f \text{ es una Función BIYECTIVA}} \\[6pt]"
            r"&\bullet \textbf{Teorema de Existencia de Función Inversa:} \\[3pt]"
            r"&\quad f \text{ admite inversa } f^{-1} \iff f \text{ es biyectiva.} \\[6pt]"
            r"&\bullet \textbf{Intercambio Canónico de Conjuntos:} \\[4pt]"
            r"&\quad \mathbf{\operatorname{Dom}(f^{-1}) = \operatorname{Ran}(f) = {\color{amgold}[1, +\infty)}} \\[4pt]"
            r"&\quad \mathbf{\operatorname{Ran}(f^{-1}) = \operatorname{Dom}(f) = {\color{amgold}[0, +\infty)}}"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{4. Biyectividad e Invertibilidad:}\\[6pt]"
            r"$\bullet$ Conexión formal: inyectiva $+$ sobreyectiva $\implies {\color{amgold}\text{BIYECTIVA}}$.\\[5pt]"
            r"$\bullet$ Teorema fundamental: una función posee inversa si y solo si es biyectiva.\\[5pt]"
            r"$\bullet$ Regla de inversión de conjuntos:\\[3pt]"
            r"\hspace*{1.2em}El dominio de $f^{-1}$ es el codominio de $f$ ($[1, +\infty)$).\\[3pt]"
            r"\hspace*{1.2em}El codominio de $f^{-1}$ es el dominio de $f$ ($[0, +\infty)$).\\[5pt]"
            r"$\bullet$ La correspondencia entre puntos es estrictamente biunívoca ($1$ a $1$)."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], advance_to_step=3, wait_time=3.2)

        # ==========================================================
        # PASO 5: Cálculo Canónico de la Regla de f^-1
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Cálculo Canónico de la Función Inversa } f^{-1}: \\[5pt]"
            r"&\text{Por definición, } y = f(x) \iff x = f^{-1}(y). \\[5pt]"
            r"&\text{Partimos de la relación: } y = x^2 + 1 \quad (x \ge 0, \; y \ge 1) \\[5pt]"
            r"&\text{Intercambiamos formalmente los roles de variables } x \leftrightarrow y: \\[4pt]"
            r"&x = y^2 + 1 \implies y^2 = x - 1 \\[5pt]"
            r"&\text{Como } y \in [0, +\infty) \implies \mathbf{y = {\color{amgreen}+\sqrt{x - 1}}} \\[6pt]"
            r"&\mathbf{f^{-1}: [1, +\infty) \longrightarrow [0, +\infty)} \\[5pt]"
            r"&\mathbf{{\color{amgreen}f^{-1}(x) = \sqrt{x - 1}}}"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{5. Despeje de la Función Inversa:}\\[6pt]"
            r"$\bullet$ Procedimiento canónico de inversión:\\[3pt]"
            r"\hspace*{1.2em}$y = f(x) \iff x = f^{-1}(y)$.\\[5pt]"
            r"$\bullet$ Despejamos la variable independiente $x$ en función de $y$:\\[3pt]"
            r"\hspace*{1.2em}$x = \sqrt{y - 1}$.\\[5pt]"
            r"$\bullet$ Reetiquetamos para expresar la regla en la variable canónica $x$:\\[3pt]"
            r"\hspace*{1.2em}${\color{amgreen}f^{-1}(x) = \sqrt{x - 1}}$.\\[5pt]"
            r"$\bullet$ Presentación institucional completa con su dominio: $f^{-1}: [1, +\infty) \to [0, +\infty)$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq5, just5, box_color=THEME["highlight"], advance_to_step=4, wait_time=3.2)

        # ==========================================================
        # PASO 6: Verificación por Composición (Identidad)
        # ==========================================================
        eq6 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Verificación de la Composición (Identidad):} \\[5pt]"
            r"&\text{La teoría exige: } f^{-1} \circ f = I_A \quad \text{y} \quad f \circ f^{-1} = I_B. \\[5pt]"
            r"&\bullet \mathbf{(f^{-1} \circ f)(x) = f^{-1}(f(x))}: \\[3pt]"
            r"&\quad = \sqrt{(x^2 + 1) - 1} = \sqrt{x^2} = |x| = \mathbf{{\color{amgreen}x}} \quad (\text{pues } x \ge 0) \\[4pt]"
            r"&\quad \implies \mathbf{f^{-1} \circ f = I_{[0, +\infty)}} \\[6pt]"
            r"&\bullet \mathbf{(f \circ f^{-1})(x) = f(f^{-1}(x))}: \\[3pt]"
            r"&\quad = (\sqrt{x - 1})^2 + 1 = (x - 1) + 1 = \mathbf{{\color{amgreen}x}} \quad (\text{pues } x \ge 1) \\[4pt]"
            r"&\quad \implies \mathbf{f \circ f^{-1} = I_{[1, +\infty)}}"
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{6. Comprobación por Composición:}\\[6pt]"
            r"$\bullet$ Propiedad unívoca de funciones inversas:\\[3pt]"
            r"\hspace*{1.2em}Aplicar $f$ y luego $f^{-1}$ devuelve el elemento original.\\[5pt]"
            r"$\bullet$ Primera composición:\\[3pt]"
            r"\hspace*{1.2em}$(f^{-1} \circ f)(x) = \sqrt{x^2} = x$ (identidad en $[0, +\infty)$).\\[5pt]"
            r"$\bullet$ Segunda composición:\\[3pt]"
            r"\hspace*{1.2em}$(f \circ f^{-1})(x) = (x - 1) + 1 = x$ (identidad en $[1, +\infty)$).\\[5pt]"
            r"$\bullet$ Queda rigurosamente demostrada la validez de $f^{-1}(x) = \sqrt{x - 1}$."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq6, just6, box_color=THEME["highlight"], advance_to_step=5, wait_time=3.2)

        # ==========================================================
        # PASO 7: Puntos Homólogos y Simetría a 45°
        # ==========================================================
        eq7 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{7. Cuadro de Puntos Homólogos y Simetría:} \\[6pt]"
            r"&\begin{array}{c|c|c|c|c}"
            r"\textbf{Punto en } f(x) & P_0(0, 1) & P_1(1, 2) & P_2(\sqrt{3}, 4) & P_3(2, 5) \\ \hline "
            r"\textbf{Punto en } f^{-1}(x) & P_0'(1, 0) & P_1'(2, 1) & P_2'(4, \sqrt{3}) & P_3'(5, 2)"
            r"\end{array} \\[8pt]"
            r"&\bullet \mathbf{\text{Propiedad Geométrica: }} (a, b) \in f \iff (b, a) \in f^{-1}. \\[4pt]"
            r"&\bullet \mathbf{\text{Eje de Simetría Especular: }} \text{La recta identidad } {\color{amgold}y = x}. \\[4pt]"
            r"&\bullet \mathbf{\text{Segmentos Conectores: }} \text{Unen } P_k \text{ con } P_k' \text{ perpendicularmente a } y = x."
            r"\end{aligned}",
            font_size=18.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{8.2cm}\raggedright "
            r"\textbf{7. Síntesis Geométrica:}\\[6pt]"
            r"$\bullet$ La inversión de una función intercambia las coordenadas cartesianas: $(x, y) \leftrightarrow (y, x)$.\\[5pt]"
            r"$\bullet$ El vértice $(0, 1)$ de la semiparábola vertical se transforma en el punto inicial $(1, 0)$ de la semiparábola horizontal.\\[5pt]"
            r"$\bullet$ La recta $y = x$ actúa como un espejo plano perfecto a $45^\circ$.\\[5pt]"
            r"$\bullet$ Base geométrica para la construcción de ambas curvas en el plano."
            r"\end{minipage}",
            font_size=22.0,
            pos=[3.35, -0.45, 0]
        )

        self.morph_step(eq7, just7, box_color=THEME["highlight"], advance_to_step=6, wait_time=3.6)

        # ==========================================================
        # PASO 8: Gráfica Cartesiana Dual y Resumen Formal
        # ==========================================================
        left_summary = MathTex(
            r"\begin{aligned}"
            r"&\textbf{8. Resumen Formal de Resultados:} \\[4pt]"
            r"&\bullet \mathbf{\operatorname{Dom}(f) = [0, +\infty)}, \quad \mathbf{\operatorname{Cod}(f) = [1, +\infty)} \\[4pt]"
            r"&\bullet \mathbf{\text{Inyectiva: }} x_1^2 + 1 = x_2^2 + 1 \implies x_1 = x_2 \\[4pt]"
            r"&\bullet \mathbf{\text{Sobreyectiva: }} \forall y \ge 1, \; x = \sqrt{y - 1} \in [0, +\infty) \\[4pt]"
            r"&\bullet \mathbf{\text{Biyectiva: }} \text{Inyectiva } \land \text{ Sobreyectiva} \\[4pt]"
            r"&\bullet \mathbf{\text{Función Inversa: }} {\color{amgreen}f^{-1}(x) = \sqrt{x - 1}} \\[4pt]"
            r"&\bullet \mathbf{\operatorname{Dom}(f^{-1}) = {\color{amgold}[1, +\infty)}}, \quad \mathbf{\operatorname{Ran}(f^{-1}) = {\color{amgold}[0, +\infty)}} \\[4pt]"
            r"&\bullet \mathbf{\text{Composición: }} f^{-1} \circ f = I_A, \quad f \circ f^{-1} = I_B \\[4pt]"
            r"&\bullet \mathbf{\text{Simetría: }} \text{Reflejo especular en } {\color{amgold}y = x} \quad {\color{amgreen}\blacksquare}"
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        box8 = SurroundingRectangle(left_summary, color=THEME["success"], buff=0.18, corner_radius=0.1)

        # Gráfico cartesiano ortonormal (escala 1:1)
        axes = Axes(
            x_range=[-0.5, 5.5, 1],
            y_range=[-0.5, 5.5, 1],
            x_length=4.8,
            y_length=4.8,
            tips=True,
            axis_config={
                "color": THEME["axes"],
                "stroke_width": 2,
                "include_numbers": True,
                "numbers_to_include": [2, 3, 4, 5],
                "font_size": 14,
                "tip_width": 0.12,
                "tip_height": 0.12,
            }
        ).move_to([3.3, -0.55, 0])

        x_lbl = MathTex("x", font_size=16, color=THEME["statement_text"]).next_to(axes.x_axis.get_end(), RIGHT, buff=0.10)
        y_lbl = MathTex("y", font_size=16, color=THEME["statement_text"]).next_to(axes.y_axis.get_end(), LEFT, buff=0.12)
        axes_labels = VGroup(x_lbl, y_lbl)

        graph_title = Tex(
            r"Gráfica de ${\color{amteal}f(x)}$ y su Inversa ${\color{amgreen}f^{-1}(x)}$",
            font_size=18.5,
            color=WHITE
        ).move_to([3.4, 2.15, 0])

        # Recta identidad y = x (eje de simetría a 45°)
        line_diag = DashedLine(
            axes.c2p(-0.4, -0.4), axes.c2p(5.2, 5.2),
            dash_length=0.08, color=THEME["highlight"], stroke_width=1.8
        )
        lbl_diag = MathTex(r"y = x", font_size=13.5, color=THEME["highlight"]).next_to(axes.c2p(4.8, 4.8), UP + LEFT, buff=0.06)

        # Curva f(x) = x^2 + 1 (x in [0, 2.1])
        curve_f = axes.plot(
            lambda x: x**2 + 1,
            x_range=[0.0, 2.1],
            color=THEME["curve"],
            stroke_width=2.5
        )
        lbl_f = MathTex(r"f(x) = x^2 + 1", font_size=13.5, color=THEME["curve"]).move_to(axes.c2p(1.1, 4.0))

        # Curva f^-1(x) = sqrt(x - 1) (x in [1, 5.4])
        curve_finv = axes.plot(
            lambda x: np.sqrt(x - 1),
            x_range=[1.0, 5.4],
            color=THEME["success"],
            stroke_width=2.5
        )
        lbl_finv = MathTex(r"f^{-1}(x) = \sqrt{x - 1}", font_size=13.5, color=THEME["success"]).move_to(axes.c2p(3.8, 1.1))

        # Puntos homólogos
        dot_p0 = Dot(axes.c2p(0.0, 1.0), radius=0.065, color=THEME["curve"])
        lbl_p0 = MathTex(r"(0, 1)", font_size=12.5, color=THEME["curve"]).next_to(dot_p0, LEFT, buff=0.10)

        dot_p0_inv = Dot(axes.c2p(1.0, 0.0), radius=0.065, color=THEME["success"])
        lbl_p0_inv = MathTex(r"(1, 0)", font_size=12.5, color=THEME["success"]).next_to(dot_p0_inv, DOWN, buff=0.10)

        dot_p1 = Dot(axes.c2p(1.0, 2.0), radius=0.065, color=THEME["curve"])
        lbl_p1 = MathTex(r"(1, 2)", font_size=12.5, color=THEME["curve"]).next_to(dot_p1, LEFT, buff=0.08)

        dot_p1_inv = Dot(axes.c2p(2.0, 1.0), radius=0.065, color=THEME["success"])
        lbl_p1_inv = MathTex(r"(2, 1)", font_size=12.5, color=THEME["success"]).next_to(dot_p1_inv, DOWN, buff=0.08)

        # Segmentos de conexión punteados entre puntos simétricos
        seg0 = DashedLine(axes.c2p(0.0, 1.0), axes.c2p(1.0, 0.0), dash_length=0.05, color=GRAY, stroke_width=1.2)
        seg1 = DashedLine(axes.c2p(1.0, 2.0), axes.c2p(2.0, 1.0), dash_length=0.05, color=GRAY, stroke_width=1.2)

        prog_anims = self.get_advance_progress_anims(7)

        self.play(
            FadeOut(self.active_math),
            FadeOut(self.active_just),
            FadeOut(self.active_box),
            FadeIn(left_summary),
            Create(box8),
            Create(axes),
            Write(axes_labels),
            Write(graph_title),
            *prog_anims,
            run_time=1.8
        )
        self.active_box = box8
        self.active_math = left_summary
        self.active_just = None

        self.play(
            Create(line_diag),
            Write(lbl_diag),
            Create(curve_f),
            Write(lbl_f),
            Create(curve_finv),
            Write(lbl_finv),
            FadeIn(dot_p0),
            Write(lbl_p0),
            FadeIn(dot_p0_inv),
            Write(lbl_p0_inv),
            FadeIn(dot_p1),
            Write(lbl_p1),
            FadeIn(dot_p1_inv),
            Write(lbl_p1_inv),
            Create(seg0),
            Create(seg1),
            run_time=2.4
        )
        self.wait(8.0)

        # Cierre institucional
        graph_group = VGroup(
            axes, axes_labels, graph_title,
            line_diag, lbl_diag,
            curve_f, lbl_f,
            curve_finv, lbl_finv,
            dot_p0, lbl_p0,
            dot_p0_inv, lbl_p0_inv,
            dot_p1, lbl_p1,
            dot_p1_inv, lbl_p1_inv,
            seg0, seg1
        )
        self.play(
            FadeOut(graph_group),
            FadeOut(self.active_math),
            FadeOut(self.active_box),
            run_time=1.4
        )
        self.wait(1.0)
