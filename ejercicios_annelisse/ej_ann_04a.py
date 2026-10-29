r"""
Precálculo Universitario · Tutorías Annelisse / Editorial Amarun
Capítulo: Funciones Reales y Gráficas
Ejercicio 4.a: Dominio Máximo, Rango y Gráfica de Función Radical
               f(x) = √(-x² + 6x + 5)

Estructura de la Demostración (100% Precálculo Universitario - Sin Derivadas):
  1. Regla del Máximo Dominio (RMD) para raíces de índice par (u(x) ≥ 0).
  2. Completación canónica de cuadrados del radicando interior: u(x) = 14 - (x - 3)².
  3. Inecuación cuadrática y dominio compacto Dom(f) = [3 - √14, 3 + √14] ≈ [-0.74, 6.74].
  4. Deducción formal del rango mediante cotas de la raíz: Ran(f) = [0, √14] ≈ [0, 3.74].
  5. Cortes con los ejes coordenados (eje Y con punto simétrico y cortes con eje X).
  6. Simetría axial (x = 3) y monotonía formal por herencia del radicando (sin derivadas).
  7. Identidad geométrica de la semicircunferencia (x - 3)² + y² = 14, y ≥ 0 y síntesis.
  8. Trazado cartesiano de precisión: centro C(3, 0), radio R = √14 y proyecciones de Dom y Ran.

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica en 8 pasos con tipografía HD generosa y legible.
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
\usepackage{cancel}
\definecolor{amgold}{HTML}{F6B840}
\definecolor{amteal}{HTML}{5CE1E6}
\definecolor{amred}{HTML}{E53E3E}
\definecolor{amgreen}{HTML}{48BB78}
\definecolor{amorange}{HTML}{DB5A38}
\definecolor{amwhite}{HTML}{FDFBF7}
""")
config.tex_template = AMARUN_TEX_TEMPLATE


class EjercicioAnn_04a(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Annelisse",
            exercise="Ejercicio 4.a",
            topic="Dominio Máximo, Rango y Semicircunferencia",
            font_size=17.0
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 4.a: Halle el dominio máximo y el rango de la función radical real:",
            math_tex=r"{\color{amteal}f(x) = \sqrt{-x^2 + 6x + 5}}, \quad x \in \mathbb{R}",
            desc_font_size=20.0,
            math_font_size=24.0,
            arrange_direction=DOWN,
            buff=0.18,
            box_pos=np.array([0.0, 2.45, 0.0]),
            read_time=3.5
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (8 pasos unificados)
        # ==========================================================
        self.setup_progress_bar([
            "1/8: RMD para Radicales",
            "2/8: Completación del Radicando",
            "3/8: Dominio Máximo Dom(f)",
            "4/8: Rango y Cota Máxima",
            "5/8: Cortes con los Ejes",
            "6/8: Simetría y Monotonía",
            "7/8: Semicircunferencia y Síntesis",
            "8/8: Trazado Cartesiano"
        ], dot_spacing=0.82, label_font_size=14.0)

        # ==========================================================
        # PASO 1: Regla del Máximo Dominio (RMD)
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Regla del Máximo Dominio (RMD) para Radicales:} \\[6pt]"
            r"&\text{Para que la raíz cuadrada principal } \sqrt{u(x)} \in \mathbb{R}, \\[4pt]"
            r"&\text{el radicando subradical debe ser no negativo:} \\[4pt]"
            r"&\quad \mathbf{{\color{amgold}\operatorname{Dom}(f) = \{x \in \mathbb{R} : u(x) \ge 0\}}} \\[6pt]"
            r"&\bullet \ \textbf{Expresión Subradical } u(x): \\[4pt]"
            r"&\quad u(x) = -x^2 + 6x + 5 \ge 0 \\[6pt]"
            r"&\bullet \ \textbf{Extracción del Coeficiente Cuadrático } a = -1: \\[4pt]"
            r"&\quad u(x) = -(x^2 - 6x) + 5"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Condición de Existencia Real:}\\[6pt]"
            r"$\bullet$ En el cuerpo de los números reales $\mathbb{R}$, las raíces de índice par exigen radicando no negativo.\\[5pt]"
            r"$\bullet$ Si $u(x) < 0$, la raíz genera valores no reales $(\mathbb{C} \setminus \mathbb{R})$.\\[5pt]"
            r"$\bullet$ El polinomio cuadrático interior abre hacia abajo ($a = -1 < 0$), lo que acotará el dominio a un intervalo cerrado."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=3.6)

        # ==========================================================
        # PASO 2: Forma Canónica del Radicando Interior
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Forma Canónica del Radicando } u(x): \\[6pt]"
            r"&\quad u(x) = -(x^2 - 6x) + 5 \\[5pt]"
            r"&\bullet \ \textbf{Completando el Trinomio Cuadrado Perfecto:} \\[4pt]"
            r"&\quad \left(\frac{b'}{2}\right)^2 = \left(\frac{-6}{2}\right)^2 = (-3)^2 = 9 \\[5pt]"
            r"&\quad u(x) = -(x^2 - 6x + 9 - 9) + 5 \\[4pt]"
            r"&\quad u(x) = -(x - 3)^2 + 9 + 5 \\[6pt]"
            r"&\therefore \quad \mathbf{{\color{amteal}u(x) = 14 - (x - 3)^2}} \\[6pt]"
            r"&\bullet \ \textbf{Vértice Máximo del Radicando:} \; {\color{amgold}V_u(3, \; 14)}"
            r"\end{aligned}",
            font_size=19.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Transformación Canónica:}\\[6pt]"
            r"$\bullet$ La completación de cuadrados aísla la variable $x$ en un único binomio cuadrático.\\[5pt]"
            r"$\bullet$ La forma $u(x) = 14 - (x - 3)^2$ revela que el radicando alcanza su cota superior absoluta $14$ cuando $x = 3$.\\[5pt]"
            r"$\bullet$ El eje de simetría del radicando es la recta vertical $x = 3$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=3.6)

        # ==========================================================
        # PASO 3: Inecuación Cuadrática y Dominio Máximo
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Resolución de la Inecuación y Dominio Máximo:} \\[6pt]"
            r"&\quad u(x) \ge 0 \iff 14 - (x - 3)^2 \ge 0 \\[5pt]"
            r"&\quad \iff (x - 3)^2 \le 14 \\[5pt]"
            r"&\bullet \ \textbf{Propiedad de Valor Absoluto } (t^2 \le k \iff |t| \le \sqrt{k}): \\[4pt]"
            r"&\quad |x - 3| \le \sqrt{14} \iff -\sqrt{14} \le x - 3 \le \sqrt{14} \\[5pt]"
            r"&\quad \iff \mathbf{3 - \sqrt{14} \le x \le 3 + \sqrt{14}} \\[6pt]"
            r"&\bullet \ \textbf{Aproximación Decimal } (\sqrt{14} \approx 3.74): \\[4pt]"
            r"&\quad x_1 \approx -0.74, \quad x_2 \approx 6.74 \\[6pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}\operatorname{Dom}(f) = [3 - \sqrt{14}, \; 3 + \sqrt{14}] \approx [-0.74, \; 6.74]}}"
            r"\end{aligned}",
            font_size=18.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{3. Dominio Compacto en $\mathbb{R}$:}\\[6pt]"
            r"$\bullet$ El dominio máximo es un intervalo cerrado y acotado (compacto).\\[5pt]"
            r"$\bullet$ Fuera de $[3 - \sqrt{14}, 3 + \sqrt{14}]$, el radicando es negativo y la raíz no existe en $\mathbb{R}$.\\[5pt]"
            r"$\bullet$ Los puntos frontera son los ceros del radicando donde la función se anula: $f(3 \pm \sqrt{14}) = 0$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq3, just3, box_color=THEME["statement_box"], advance_to_step=2, wait_time=3.6)

        # ==========================================================
        # PASO 4: Determinación Formal del Rango
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Determinación Formal del Rango } \operatorname{Ran}(f): \\[6pt]"
            r"&\bullet \ \textbf{Cota Inferior de la Raíz Cuadrada:} \\[4pt]"
            r"&\quad \forall x \in \operatorname{Dom}(f): \quad f(x) = \sqrt{u(x)} \ge 0 \\[4pt]"
            r"&\quad \text{En los extremos } x = 3 \pm \sqrt{14}: \quad f(x) = \sqrt{0} = \mathbf{{\color{amteal}0}} \\[6pt]"
            r"&\bullet \ \textbf{Cota Superior del Radicando:} \\[4pt]"
            r"&\quad \forall x \in \mathbb{R}: \quad (x - 3)^2 \ge 0 \implies u(x) = 14 - (x - 3)^2 \le 14 \\[4pt]"
            r"&\bullet \ \textbf{Monotonía de la Raíz Cuadrada } (0 \le u \le 14): \\[4pt]"
            r"&\quad \sqrt{0} \le \sqrt{u(x)} \le \sqrt{14} \iff \mathbf{{\color{amgreen}0 \le f(x) \le \sqrt{14}}} \\[6pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}\operatorname{Ran}(f) = [0, \; \sqrt{14}] \approx [0, \; 3.74]}} \quad (\text{Intervalo Compacto})"
            r"\end{aligned}",
            font_size=18.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Rango de la Raíz Cuadrada:}\\[6pt]"
            r"$\bullet$ La función raíz cuadrada $t \mapsto \sqrt{t}$ preserva las desigualdades por ser estrictamente creciente para $t \ge 0$.\\[5pt]"
            r"$\bullet$ Como el radicando $u(x)$ varía continuamente de $0$ a $14$, la raíz cubre todos los valores entre $0$ y $\sqrt{14}$.\\[5pt]"
            r"$\bullet$ Cota mínima: $0$; Cota máxima: $\sqrt{14} \approx 3.74$.\\[5pt]"
            r"$\bullet$ Rango final: ${\color{amgreen}\operatorname{Ran}(f) = [0, \sqrt{14}]}$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq4, just4, box_color=THEME["success"], advance_to_step=3, wait_time=3.6)

        # ==========================================================
        # PASO 5: Cortes con los Ejes Coordenados
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Cortes con los Ejes Coordenados:} \\[6pt]"
            r"&\bullet \ \textbf{Corte con el Eje } Y \; (x = 0): \\[4pt]"
            r"&\quad 0 \in \operatorname{Dom}(f) \implies f(0) = \sqrt{-0^2 + 6(0) + 5} = \mathbf{{\color{amteal}\sqrt{5} \approx 2.24}} \\[4pt]"
            r"&\quad \implies \mathbf{{\color{amteal}P_y(0, \; \sqrt{5})}} \\[6pt]"
            r"&\bullet \ \textbf{Punto Simétrico Reflejo } (x = 6): \\[4pt]"
            r"&\quad f(6) = \sqrt{-(6)^2 + 6(6) + 5} = \mathbf{{\color{amteal}\sqrt{5}}} \implies \mathbf{{\color{amteal}P_{\text{sym}}(6, \; \sqrt{5})}} \\[6pt]"
            r"&\bullet \ \textbf{Cortes con el Eje } X \; (y = 0): \\[4pt]"
            r"&\quad f(x) = 0 \iff 14 - (x - 3)^2 = 0 \iff x = 3 \pm \sqrt{14} \\[4pt]"
            r"&\quad \mathbf{{\color{amgreen}P_{x_1}(3 - \sqrt{14}, \; 0)}} \quad \text{y} \quad \mathbf{{\color{amgreen}P_{x_2}(3 + \sqrt{14}, \; 0)}}"
            r"\end{aligned}",
            font_size=18.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Intersecciones Notables:}\\[6pt]"
            r"$\bullet$ El corte con el eje $Y$ se halla evaluando en $x = 0$: $P_y(0, \sqrt{5}) \approx (0, 2.24)$.\\[5pt]"
            r"$\bullet$ Por simetría axial respecto a $x = 3$, el punto a distancia $\Delta x = 3$ a la derecha es $x = 6$, con idéntica altura $\sqrt{5}$.\\[5pt]"
            r"$\bullet$ Los cortes con el eje $X$ coinciden con las fronteras del dominio donde la raíz se anula."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq5, just5, box_color=THEME["error"], advance_to_step=4, wait_time=3.6)

        # ==========================================================
        # PASO 6: Simetría Axial y Monotonía por Inecuaciones (Sin Derivadas)
        # ==========================================================
        eq6 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Simetría Axial y Monotonía (Precálculo):} \\[5pt]"
            r"&\bullet \ \textbf{Simetría Axial Respecto a } x = 3: \\[3pt]"
            r"&\quad \forall h \in [-\sqrt{14}, \sqrt{14}]: \quad f(3 + h) = \sqrt{14 - h^2} = f(3 - h) \\[4pt]"
            r"&\quad \implies \mathbf{{\color{amgold}\text{Eje de Simetría Vertical: } x = 3}} \\[5pt]"
            r"&\bullet \ \textbf{Monotonía por Herencia de la Raíz Cuadrada } g(u) = \sqrt{u}: \\[3pt]"
            r"&\quad \text{Como } \sqrt{u} \text{ es estrictamente creciente } (u_1 < u_2 \iff \sqrt{u_1} < \sqrt{u_2}): \\[4pt]"
            r"&\quad \text{1. Para } 3 - \sqrt{14} \le x_1 < x_2 \le 3 \implies u(x_1) < u(x_2) \implies \mathbf{f(x_1) < f(x_2)} \\[4pt]"
            r"&\quad \quad \therefore \ \mathbf{{\color{amgreen}\text{Estrictamente Creciente en } [3 - \sqrt{14}, \; 3]}} \\[4pt]"
            r"&\quad \text{2. Para } 3 \le x_1 < x_2 \le 3 + \sqrt{14} \implies u(x_1) > u(x_2) \implies \mathbf{f(x_1) > f(x_2)} \\[4pt]"
            r"&\quad \quad \therefore \ \mathbf{{\color{amorange}\text{Estrictamente Decreciente en } [3, \; 3 + \sqrt{14}]}}"
            r"\end{aligned}",
            font_size=17.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{6. Monotonía sin Derivadas:}\\[6pt]"
            r"$\bullet$ La función es perfectamente simétrica respecto al eje vertical $x = 3$.\\[5pt]"
            r"$\bullet$ En Precálculo, la monotonía de $f(x) = \sqrt{u(x)}$ se demuestra porque $\sqrt{u}$ es estrictamente creciente, por lo que $f$ hereda la variación de la parábola interior $u(x)$.\\[5pt]"
            r"$\bullet$ Crece a la izquierda de $x = 3$ y decrece a su derecha.\\[5pt]"
            r"$\bullet$ Máximo absoluto en la cima $V(3, \sqrt{14})$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq6, just6, box_color=THEME["curve"], advance_to_step=5, wait_time=3.6)

        # ==========================================================
        # PASO 7: Identidad Geométrica (Semicircunferencia) y Síntesis
        # ==========================================================
        eq7 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{7. Identidad Geométrica y Resumen Formal:} \\[5pt]"
            r"&\quad y = \sqrt{14 - (x - 3)^2} \iff \mathbf{{\color{amteal}(x - 3)^2 + y^2 = 14}}, \quad y \ge 0 \\[4pt]"
            r"&\text{¡Semicircunferencia superior de centro } C(3, 0) \text{ y radio } R = \sqrt{14}! \\[6pt]"
            r"&\begin{array}{|l|l|} \hline "
            r"\textbf{Propiedad Formal} & \textbf{Resultado Deductivo de Precálculo} \\ \hline "
            r"\text{Dominio Máximo } (\operatorname{Dom}) & [3 - \sqrt{14}, \; 3 + \sqrt{14}] \approx [-0.74, \; 6.74] \\ "
            r"\text{Rango / Imagen } (\operatorname{Ran}) & [0, \; \sqrt{14}] \approx [0, \; 3.74] \\ "
            r"\text{Cúspide / Máximo Global} & V(3, \; \sqrt{14}) \approx (3, \; 3.74) \\ "
            r"\text{Corte con Eje } Y & P_y(0, \; \sqrt{5}) \approx (0, \; 2.24) \\ "
            r"\text{Punto Simétrico} & P_{\text{sym}}(6, \; \sqrt{5}) \approx (6, \; 2.24) \\ "
            r"\text{Cortes con Eje } X & (-0.74, \; 0) \quad \text{y} \quad (6.74, \; 0) \\ "
            r"\text{Eje de Simetría} & \text{Recta vertical } x = 3 \\ "
            r"\text{Monotonía} & \text{Crece en } [3-\sqrt{14}, 3], \ \text{Decrece en } [3, 3+\sqrt{14}] \\ \hline "
            r"\end{array}"
            r"\end{aligned}",
            font_size=16.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{7. Síntesis Geométrica:}\\[6pt]"
            r"$\bullet$ La ecuación $(x - 3)^2 + y^2 = 14$ define la circunferencia con centro en $(3, 0)$ y radio $R = \sqrt{14} \approx 3.74$.\\[5pt]"
            r"$\bullet$ La condición $y = \sqrt{\dots} \ge 0$ toma únicamente la mitad superior del círculo.\\[5pt]"
            r"$\bullet$ El dominio mide el diámetro $2R = 2\sqrt{14} \approx 7.48$, y la altura máxima es el radio $R = \sqrt{14}$.\\[5pt]"
            r"$\bullet$ Todos los datos listos para el trazado cartesiano."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq7, just7, box_color=THEME["statement_box"], advance_to_step=6, wait_time=3.6)

        # ==========================================================
        # PASO 8: Trazado Cartesiano de Precisión
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(7)

        # Panel izquierdo: Resumen geométrico
        t_card = Tex(
            r"\begin{minipage}{5.8cm}\raggedright "
            r"\textbf{{\color{amteal}Verificación Cartesiana:}}\\[6pt]"
            r"$\bullet$ \textbf{Semicircunferencia:}\\[2pt]"
            r"\hspace*{0.8em}$(x - 3)^2 + y^2 = 14, \quad y \ge 0$.\\[5pt]"
            r"$\bullet$ \textbf{Centro y Radio:}\\[2pt]"
            r"\hspace*{0.8em}$C(3, 0), \quad R = \sqrt{14} \approx 3.74$.\\[5pt]"
            r"$\bullet$ \textbf{Máximo Global (Cúspide):}\\[2pt]"
            r"\hspace*{0.8em}$V(3, \; \sqrt{14}) \approx (3, \; 3.74)$.\\[5pt]"
            r"$\bullet$ \textbf{Eje de Simetría:}\\[2pt]"
            r"\hspace*{0.8em}Recta vertical $x = 3$.\\[5pt]"
            r"$\bullet$ \textbf{Corte } $Y$ \textbf{y Simétrico:}\\[2pt]"
            r"\hspace*{0.8em}$P_y(0, \sqrt{5})$ y $P_{\text{sym}}(6, \sqrt{5})$.\\[5pt]"
            r"$\bullet$ \textbf{Rango Proyectado:}\\[2pt]"
            r"\hspace*{0.8em}$[0, \; \sqrt{14}]$ sobre el eje $Y$."
            r"\end{minipage}",
            font_size=17.5,
            color=WHITE
        )
        info_box = SurroundingRectangle(
            t_card,
            color=THEME["statement_box"],
            buff=0.20,
            stroke_width=1.8,
            corner_radius=0.1
        )
        info_grp = VGroup(info_box, t_card).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos
        axes, axes_labels = self.setup_axes(
            x_range=[-1.5, 7.5, 1.0],
            y_range=[-0.5, 4.5, 1.0],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=12,
            labels_font_size=19
        )

        r_val = np.sqrt(14.0)
        x1_val = 3.0 - r_val
        x2_val = 3.0 + r_val

        # Eje de simetría vertical x = 3
        sym_line = DashedLine(
            start=axes.c2p(3.0, -0.45),
            end=axes.c2p(3.0, 4.3),
            color=THEME["highlight"],
            dash_length=0.08,
            stroke_width=2.0
        )
        sym_lbl = MathTex(
            r"x = 3",
            font_size=11.5,
            color=THEME["highlight"]
        ).next_to(axes.c2p(3.0, 4.3), RIGHT, buff=0.08)

        # Curva de la semicircunferencia f(x)
        curve_f = axes.plot(
            lambda x: np.sqrt(max(0.0, 14.0 - (x - 3.0)**2)),
            x_range=[x1_val, x2_val, 0.01],
            color=THEME["amarun_teal"],
            stroke_width=4.0
        )
        lbl_f = MathTex(
            r"f(x) = \sqrt{14 - (x - 3)^2}",
            font_size=12.5,
            color=THEME["amarun_teal"]
        ).next_to(axes.c2p(5.2, 3.2), UR, buff=0.06)

        # Centro C(3, 0)
        p_c = axes.c2p(3.0, 0.0)
        dot_c = Dot(p_c, radius=0.065, color=WHITE)
        lbl_c = MathTex(r"C(3, 0)", font_size=11.5, color=WHITE).next_to(p_c, UL, buff=0.08)

        # Cúspide máxima V(3, √14)
        p_v = axes.c2p(3.0, r_val)
        dot_v = Dot(p_v, radius=0.075, color=THEME["highlight"])
        lbl_v = MathTex(r"V(3, \; \sqrt{14})", font_size=11.5, color=THEME["highlight"]).next_to(p_v, UP, buff=0.08)

        # Radio R = √14 indicado con línea segmentada a 45 grados
        rad_line = DashedLine(
            start=p_c,
            end=axes.c2p(3.0 + r_val * np.cos(np.pi/4), r_val * np.sin(np.pi/4)),
            color=THEME["secondary"],
            dash_length=0.06,
            stroke_width=1.8
        )
        rad_lbl = MathTex(r"R = \sqrt{14}", font_size=11.0, color=THEME["secondary"]).next_to(
            rad_line.get_center(), UR, buff=0.04
        )

        # Cortes con eje X
        p_x1 = axes.c2p(x1_val, 0.0)
        dot_x1 = Dot(p_x1, radius=0.065, color=THEME["success"])
        lbl_x1 = MathTex(r"x_1", font_size=11.5, color=THEME["success"]).next_to(p_x1, UL, buff=0.06)

        p_x2 = axes.c2p(x2_val, 0.0)
        dot_x2 = Dot(p_x2, radius=0.065, color=THEME["success"])
        lbl_x2 = MathTex(r"x_2", font_size=11.5, color=THEME["success"]).next_to(p_x2, UR, buff=0.06)

        # Corte Y (0, √5) y simétrico (6, √5)
        y_int = np.sqrt(5.0)
        p_y = axes.c2p(0.0, y_int)
        dot_y = Dot(p_y, radius=0.065, color=THEME["highlight"])
        lbl_y = MathTex(r"P_y(0, \sqrt{5})", font_size=11.0, color=THEME["highlight"]).next_to(p_y, LEFT, buff=0.06)

        p_sym = axes.c2p(6.0, y_int)
        dot_sym = Dot(p_sym, radius=0.065, color=THEME["highlight"])
        lbl_sym = MathTex(r"P_{\text{sym}}(6, \sqrt{5})", font_size=11.0, color=THEME["highlight"]).next_to(p_sym, UR, buff=0.06)

        # Proyección del rango sobre el borde izquierdo [0, √14]
        range_line = Line(
            axes.c2p(-1.5, 0.0),
            axes.c2p(-1.5, r_val),
            color=THEME["success"],
            stroke_width=5.0
        )
        dot_r_bottom = Dot(axes.c2p(-1.5, 0.0), radius=0.065, color=THEME["success"])
        dot_r_top = Dot(axes.c2p(-1.5, r_val), radius=0.065, color=THEME["success"])
        lbl_range = MathTex(
            r"\operatorname{Ran}=[0, \sqrt{14}]",
            font_size=11.5,
            color=THEME["success"]
        ).next_to(axes.c2p(-1.5, r_val / 2.0), RIGHT, buff=0.08)

        # Transición hacia el paso 8
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

        # Trazado de la curva y eje de simetría
        self.play(
            Create(sym_line), Write(sym_lbl),
            Create(curve_f), Write(lbl_f),
            run_time=2.2
        )

        # Centro, radio y cúspide
        self.play(
            FadeIn(dot_c), Write(lbl_c),
            Create(rad_line), Write(rad_lbl),
            FadeIn(dot_v), Write(lbl_v),
            FadeIn(dot_x1), Write(lbl_x1),
            FadeIn(dot_x2), Write(lbl_x2),
            FadeIn(dot_y), Write(lbl_y),
            FadeIn(dot_sym), Write(lbl_sym),
            Create(range_line), FadeIn(dot_r_bottom), FadeIn(dot_r_top), Write(lbl_range),
            run_time=1.8
        )
        self.wait(4.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            sym_line, sym_lbl, curve_f, lbl_f,
            dot_c, lbl_c, rad_line, rad_lbl, dot_v, lbl_v,
            dot_x1, lbl_x1, dot_x2, lbl_x2, dot_y, lbl_y, dot_sym, lbl_sym,
            range_line, dot_r_bottom, dot_r_top, lbl_range
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
