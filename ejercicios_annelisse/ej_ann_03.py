r"""
Precálculo Universitario · Tutorías Annelisse / Editorial Amarun
Capítulo: Funciones Reales y Gráficas
Ejercicio 3.a: Rango de Función Cuadrática con Dominio Restringido
               f(x) = -2x² - (3/2)x + 5/4,  Dom(f) = ]-3/2, -1/2]

Estructura de la Demostración (8 Pasos):
      1. Coeficientes y concavidad: a = -2 < 0 (parábola cóncava hacia abajo ∩).
      2. Localización analítica del vértice: xv = -3/8 ∉ ]-3/2, -1/2] (vértice exterior a la derecha).
      3. Monotonía en el dominio: al estar a la izquierda del vértice, f es estrictamente creciente.
      4. Evaluación en los extremos: f(-3/2) = -1 (abierto) y f(-1/2) = 3/2 (cerrado, máximo absoluto).
      5. Raíces y signos en el dominio: corte con el eje X en x = -5/4 ∈ ]-3/2, -1/2].
      6. Deducción formal del rango: por monotonía y continuidad, Ran(f) = ]-1, 3/2].
      7. Tabla de valores notables y síntesis institucional de propiedades.
      8. Trazado cartesiano riguroso: arco de curva, extremos abierto/cerrado, raíz y proyección del rango en Y.

Diseño: Metamorfosis 3B1B (Amarun Style), paleta andina institucional,
        animación pedagógica en 8 pasos con tipografía LaTeX HD generosa y legible.
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


class EjercicioAnn_03(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Institucional Permanente
        # ==========================================================
        self.setup_header(
            book="Precálculo Universitario",
            chapter="Tutoría Annelisse",
            exercise="Ejercicio 3.a",
            topic="Rango con Dominio Acotado ]-3/2, -1/2]",
            font_size=17.0
        )

        # ==========================================================
        # 2. Enunciado Institucional en Dos Líneas (Alta Legibilidad)
        # ==========================================================
        self.setup_statement(
            desc_text="Ejercicio 3.a: Determine el rango de la función cuadrática en el dominio acotado:",
            math_tex=r"{\color{amteal}f(x) = -2x^2 - \frac{3}{2}x + \frac{5}{4}}, \quad \operatorname{Dom}(f) = \left]-\frac{3}{2}, -\frac{1}{2}\right]",
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
            "1/8: Coeficientes y Concavidad",
            "2/8: Posición del Vértice",
            "3/8: Monotonía Estricta",
            "4/8: Evaluación en Extremos",
            "5/8: Raíz y Signos en D",
            "6/8: Deducción del Rango",
            "7/8: Tabla y Síntesis",
            "8/8: Trazado Cartesiano y Rango"
        ], dot_spacing=0.82, label_font_size=14.0)

        # ==========================================================
        # PASO 1: Coeficientes y Concavidad
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{1. Coeficientes y Concavidad Polinómica:} \\[6pt]"
            r"&\text{Dada la regla de correspondencia de } f(x) \text{ en } D = \left]-\frac{3}{2}, -\frac{1}{2}\right]: \\[4pt]"
            r"&\quad f(x) = {\color{amred}-2}x^2 + \left({\color{amteal}-\frac{3}{2}}\right)x + {\color{amgold}\frac{5}{4}} \\[6pt]"
            r"&\textbf{Identificación de Parámetros:} \\[4pt]"
            r"&\quad {\color{amred}a = -2}, \quad {\color{amteal}b = -\frac{3}{2}}, \quad {\color{amgold}c = \frac{5}{4}} \\[6pt]"
            r"&\text{Como } {\color{amred}a = -2 < 0} \implies \text{Parábola cóncava hacia abajo } (\cap). \\[4pt]"
            r"&\implies \text{Si el vértice perteneciera a } D, \text{ sería el máximo absoluto}."
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just1 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{1. Coeficientes y Concavidad:}\\[6pt]"
            r"$\bullet$ La función es cuadrática con dominio restringido a un intervalo acotado $D$.\\[5pt]"
            r"$\bullet$ Coeficiente principal: ${\color{amred}a = -2 < 0}$.\\[5pt]"
            r"$\bullet$ Concavidad negativa ($\cap$): las ramas descienden hacia $-\infty$.\\[5pt]"
            r"$\bullet$ Para hallar el rango, es indispensable verificar si el vértice cae dentro o fuera de $D$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=3.6)

        # ==========================================================
        # PASO 2: Posición del Vértice xv
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{2. Localización Analítica del Vértice } x_v: \\[6pt]"
            r"&\text{Abscisa del eje de simetría de la parábola:} \\[4pt]"
            r"&\quad x_v = -\frac{b}{2a} = -\frac{-3/2}{2(-2)} = -\frac{3/2}{4} = \mathbf{{\color{amgold}-\frac{3}{8}}} = \mathbf{-0.375} \\[6pt]"
            r"&\textbf{Comparación de orden con el dominio } D = \left]-\frac{3}{2}, -\frac{1}{2}\right]: \\[4pt]"
            r"&\quad -\frac{3}{2} = -1.5 < -\frac{1}{2} = -0.5 < \mathbf{{\color{amgold}-\frac{3}{8}}} = \mathbf{-0.375} \\[6pt]"
            r"&\therefore \quad \mathbf{{\color{amred}x_v = -\frac{3}{8} \notin \left]-\frac{3}{2}, -\frac{1}{2}\right]}} \quad (\text{Vértice Exterior a la derecha})"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just2 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{2. Vértice Exterior:}\\[6pt]"
            r"$\bullet$ El vértice de la parábola se ubica en $x_v = -3/8 = -0.375$.\\[5pt]"
            r"$\bullet$ El extremo superior del dominio es $-1/2 = -0.500$.\\[5pt]"
            r"$\bullet$ Como $-0.375 > -0.500$, el vértice se halla estrictamente a la derecha del intervalo $D$.\\[5pt]"
            r"$\bullet$ Consecuencia clave: la curva no cambia de dirección dentro de $D$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq2, just2, box_color=THEME["secondary"], advance_to_step=1, wait_time=3.6)

        # ==========================================================
        # PASO 3: Monotonía Estricta en D
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{3. Monotonía Estricta en el Dominio } D: \\[6pt]"
            r"&\text{Para una parábola cóncava hacia abajo } (a = -2 < 0): \\[4pt]"
            r"&\bullet \ \text{Es estrictamente creciente en } \left]-\infty, x_v\right] = \left]-\infty, -\frac{3}{8}\right]. \\[4pt]"
            r"&\bullet \ \text{Es estrictamente decreciente en } \left[x_v, +\infty\right[ = \left[-\frac{3}{8}, +\infty\right[. \\[6pt]"
            r"&\text{Como } D = \left]-\frac{3}{2}, -\frac{1}{2}\right] \subset \left]-\infty, -\frac{3}{8}\right]: \\[5pt]"
            r"&\therefore \quad \mathbf{{\color{amgreen}f(x) \text{ es ESTRICTAMENTE CRECIENTE en todo } D}} \\[6pt]"
            r"&\implies \forall x_1 < x_2 \in D: \quad f(x_1) < f(x_2)."
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just3 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{3. Crecimiento Estricto:}\\[6pt]"
            r"$\bullet$ Todo el intervalo $D$ queda contenido en la rama ascendente de la parábola.\\[5pt]"
            r"$\bullet$ No hay cúspide ni punto de retorno dentro del dominio evaluado.\\[5pt]"
            r"$\bullet$ El valor menor se ubicará en el extremo izquierdo (abierto en $-3/2$).\\[5pt]"
            r"$\bullet$ El valor mayor se alcanzará en el extremo derecho (cerrado en $-1/2$)."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq3, just3, box_color=THEME["statement_box"], advance_to_step=2, wait_time=3.6)

        # ==========================================================
        # PASO 4: Evaluación en los Extremos del Dominio
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{4. Evaluación en los Extremos de Frontera:} \\[6pt]"
            r"&\bullet \ \textbf{Extremo Izquierdo Abierto } (x \to -3/2^+): \\[3pt]"
            r"&\quad f\left(-\frac{3}{2}\right) = -2\left(-\frac{3}{2}\right)^2 - \frac{3}{2}\left(-\frac{3}{2}\right) + \frac{5}{4} \\[4pt]"
            r"&\quad = -2\left(\frac{9}{4}\right) + \frac{9}{4} + \frac{5}{4} = -\frac{18}{4} + \frac{14}{4} = \mathbf{{\color{amred}-1}} \\[6pt]"
            r"&\bullet \ \textbf{Extremo Derecho Cerrado } (x = -1/2): \\[3pt]"
            r"&\quad f\left(-\frac{1}{2}\right) = -2\left(-\frac{1}{2}\right)^2 - \frac{3}{2}\left(-\frac{1}{2}\right) + \frac{5}{4} \\[4pt]"
            r"&\quad = -2\left(\frac{1}{4}\right) + \frac{3}{4} + \frac{5}{4} = -\frac{2}{4} + \frac{8}{4} = \frac{6}{4} = \mathbf{{\color{amgreen}\frac{3}{2}}} = \mathbf{1.5}"
            r"\end{aligned}",
            font_size=20.5,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just4 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{4. Valores de Frontera:}\\[6pt]"
            r"$\bullet$ En $x = -3/2$: la función tiende a $-1$. Como el intervalo es abierto en $-3/2$, este valor es un ínfimo no alcanzable.\\[5pt]"
            r"$\bullet$ En $x = -1/2$: el valor es exactamente $3/2 = 1.5$.\\[5pt]"
            r"$\bullet$ Al ser cerrado en $-1/2$, $y = 3/2$ es el máximo absoluto de la función en $D$.\\[5pt]"
            r"$\bullet$ Los extremos de imagen quedan acotados entre $-1$ y $3/2$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq4, just4, box_color=THEME["curve"], advance_to_step=3, wait_time=3.6)

        # ==========================================================
        # PASO 5: Raíz y Signos en D
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{5. Raíz y Conjuntos de Signos en } D: \\[6pt]"
            r"&\text{Buscando intersección con el eje } X \ (f(x) = 0): \\[4pt]"
            r"&\quad -2x^2 - \frac{3}{2}x + \frac{5}{4} = 0 \iff 8x^2 + 6x - 5 = 0 \\[5pt]"
            r"&\quad (2x - 1)(4x + 5) = 0 \implies x_1 = \frac{1}{2}, \quad \mathbf{{\color{amgold}x_2 = -\frac{5}{4} = -1.25}} \\[6pt]"
            r"&\text{Como } -\frac{3}{2} = -1.5 < \mathbf{-\frac{5}{4}} \le -\frac{1}{2} \implies \mathbf{{\color{amgold}-\frac{5}{4} \in D}} \\[6pt]"
            r"&\textbf{Comportamiento de signos en } D: \\[3pt]"
            r"&\bullet \ \text{En } \left]-\frac{3}{2}, -\frac{5}{4}\right[: \ f(x) < 0 \quad (\text{Negativa}) \\[3pt]"
            r"&\bullet \ \text{En } \left]-\frac{5}{4}, -\frac{1}{2}\right]: \ f(x) > 0 \quad (\text{Positiva})"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just5 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{5. Raíz y Signos:}\\[6pt]"
            r"$\bullet$ La ecuación cuadrática posee dos raíces: $x = 1/2$ y $x = -5/4$.\\[5pt]"
            r"$\bullet$ La raíz $x = -5/4 = -1.25$ cae exactamente en el interior de $D$.\\[5pt]"
            r"$\bullet$ La gráfica cruza el eje $X$ en el punto $(-5/4, 0)$.\\[5pt]"
            r"$\bullet$ La función pasa de ser negativa a positiva dentro de su dominio acotado."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq5, just5, box_color=THEME["error"], advance_to_step=4, wait_time=3.6)

        # ==========================================================
        # PASO 6: Deducción Formal del Rango
        # ==========================================================
        eq6 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{6. Deducción Formal del Rango:} \\[6pt]"
            r"&\text{Por la monotonía estrictamente creciente y la continuidad de } f: \\[4pt]"
            r"&\quad \forall x \in \left]-\frac{3}{2}, -\frac{1}{2}\right]: \quad -\frac{3}{2} < x \le -\frac{1}{2} \\[6pt]"
            r"&\text{Aplicando la función } f \ (\text{al ser creciente, conserva el orden}): \\[4pt]"
            r"&\quad f\left(-\frac{3}{2}\right) < f(x) \le f\left(-\frac{1}{2}\right) \\[6pt]"
            r"&\text{Sustituyendo los valores calculados:} \\[4pt]"
            r"&\quad \mathbf{{\color{amred}-1}} < f(x) \le \mathbf{{\color{amgreen}\frac{3}{2}}} \\[6pt]"
            r"&\therefore \quad \mathbf{\operatorname{Ran}(f) = {\color{amgreen}\left]-1, \frac{3}{2}\right]}} = \mathbf{{\color{amgreen}\left]-1, 1.5\right]}}"
            r"\end{aligned}",
            font_size=21.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just6 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{6. Conclusión Formal del Rango:}\\[6pt]"
            r"$\bullet$ Por el Teorema del Valor Intermedio sobre una función continua y estrictamente creciente en un intervalo:\\[5pt]"
            r"$\bullet$ La imagen cubre todo el intervalo entre el ínfimo y el máximo.\\[5pt]"
            r"$\bullet$ Abierto en $-1$ porque $-3/2$ no pertenece a $D$.\\[5pt]"
            r"$\bullet$ Cerrado en $3/2$ porque $-1/2 \in D$.\\[5pt]"
            r"$\bullet$ Rango final: ${\color{amgreen}\operatorname{Ran}(f) = \left]-1, \frac{3}{2}\right]}$."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq6, just6, box_color=THEME["success"], advance_to_step=5, wait_time=3.6)

        # ==========================================================
        # PASO 7: Tabla de Puntos Notables y Síntesis
        # ==========================================================
        eq7 = MathTex(
            r"\begin{aligned}"
            r"&\textbf{7. Puntos Notables y Tabla de Valores en } D: \\[6pt]"
            r"&\begin{array}{|c|c|c|c|c|c|} \hline "
            r"x & \mathbf{-3/2} & \mathbf{-5/4} & -1 & -3/4 & \mathbf{-1/2} \\ \hline "
            r"f(x) & \mathbf{-1} & \mathbf{0} & 3/4 & 5/4 & \mathbf{{\color{amgreen}3/2}} \\ \hline "
            r"\text{Rol} & \text{Abierto } \circ & \text{Corte } X & \text{Interior} & \text{Interior} & \mathbf{\text{Máximo } \bullet} \\ \hline "
            r"\end{array} \\[8pt]"
            r"&\textbf{Síntesis de Propiedades de } f(x) \text{ en } D: \\[5pt]"
            r"&\bullet \ \mathbf{\text{Dominio: }} D = \left]-3/2, -1/2\right] = \left]-1.5, -0.5\right] \\[4pt]"
            r"&\bullet \ \mathbf{\text{Rango: }} \mathbf{{\color{amgreen}\operatorname{Ran}(f) = \left]-1, 3/2\right]}} = \left]-1, 1.5\right] \\[4pt]"
            r"&\bullet \ \mathbf{\text{Vértice Exterior: }} V(-3/8, 49/32) \notin D \implies \text{Monotonía Creciente}"
            r"\end{aligned}",
            font_size=20.0,
            color=WHITE
        ).move_to([-3.4, -0.45, 0])

        just7 = self.create_justification(
            r"\begin{minipage}{7.6cm}\raggedright "
            r"\textbf{7. Síntesis y Puntos Notables:}\\[6pt]"
            r"$\bullet$ La tabla corrobora que a medida que $x$ crece en $D$, $f(x)$ asciende estrictamente de $-1$ a $1.5$.\\[5pt]"
            r"$\bullet$ La raíz $(-5/4, 0)$ divide los signos dentro de la región.\\[5pt]"
            r"$\bullet$ Extremo izquierdo $(-3/2, -1)$ no alcanzable (punto abierto).\\[5pt]"
            r"$\bullet$ Extremo derecho $(-1/2, 3/2)$ alcanzable (punto cerrado)."
            r"\end{minipage}",
            font_size=18.5,
            pos=[3.35, -0.45, 0]
        )
        self.morph_step(eq7, just7, box_color=THEME["statement_box"], advance_to_step=6, wait_time=3.6)

        # ==========================================================
        # PASO 8: Trazado Cartesiano y Verificación Gráfica
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(7)

        # Panel izquierdo: Resumen geométrico
        t_card = Tex(
            r"\begin{minipage}{5.8cm}\raggedright "
            r"\textbf{{\color{amteal}Verificación Cartesiana:}}\\[6pt]"
            r"$\bullet$ \textbf{Arco de Parábola:}\\[2pt]"
            r"\hspace*{0.8em}$f(x) = -2x^2 - \frac{3}{2}x + \frac{5}{4}$.\\[6pt]"
            r"$\bullet$ \textbf{Frontera Izquierda:}\\[2pt]"
            r"\hspace*{0.8em}$(-1.5, -1)$ \textbf{Punto Abierto} ($\circ$).\\[6pt]"
            r"$\bullet$ \textbf{Frontera Derecha (Máx):}\\[2pt]"
            r"\hspace*{0.8em}$(-0.5, 1.5)$ \textbf{Punto Cerrado} ($\bullet$).\\[6pt]"
            r"$\bullet$ \textbf{Raíz Interna:}\\[2pt]"
            r"\hspace*{0.8em}$(-1.25, 0)$ en dorado.\\[6pt]"
            r"$\bullet$ \textbf{Rango Proyectado:}\\[2pt]"
            r"\hspace*{0.8em}$\left]-1, 1.5\right]$ en el eje vertical $Y$."
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
            x_range=[-2.2, 0.6, 0.5],
            y_range=[-1.6, 2.2, 0.5],
            x_length=5.6,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=True,
            numbers_font_size=13,
            labels_font_size=19
        )

        def f_val(x):
            return -2.0 * (x**2) - 1.5 * x + 1.25

        # Parábola completa referencial (tenue)
        curve_ref = axes.plot(
            f_val,
            x_range=[-1.9, 0.4],
            color=THEME["statement_box"],
            stroke_width=1.5,
            stroke_opacity=0.45
        )

        # Arco de curva restringido en ]-1.5, -0.5]
        curve_dom = axes.plot(
            f_val,
            x_range=[-1.5, -0.5],
            color=THEME["amarun_teal"],
            stroke_width=4.0
        )
        lbl_curve = MathTex(
            r"f(x) \text{ en } D",
            font_size=14.0,
            color=THEME["amarun_teal"]
        ).next_to(axes.c2p(-1.0, 0.8), UP, buff=0.10)

        # Vértice exterior referencial: V(-0.375, 1.531)
        v_ext_pt = axes.c2p(-0.375, f_val(-0.375))
        dot_v_ext = Dot(v_ext_pt, radius=0.05, color=THEME["statement_box"])
        lbl_v_ext = MathTex(
            r"V \notin D",
            font_size=12.0,
            color=THEME["statement_box"]
        ).next_to(v_ext_pt, UR, buff=0.08)

        # Raíz en x = -1.25
        p_root = axes.c2p(-1.25, 0.0)
        dot_root = Dot(p_root, radius=0.06, color=THEME["highlight"])
        lbl_root = MathTex(
            r"-5/4",
            font_size=13.0,
            color=THEME["highlight"]
        ).next_to(p_root, UR, buff=0.08)

        # Extremo izquierdo abierto (-1.5, -1): círculo hueco
        p_open = axes.c2p(-1.5, -1.0)
        dot_open = Circle(radius=0.07, color=THEME["error"], stroke_width=2.5, fill_color=THEME["bg_color"], fill_opacity=1.0).move_to(p_open)
        lbl_open = MathTex(r"\left(-\frac{3}{2}, -1\right)", font_size=13.0, color=THEME["error"]).next_to(p_open, DL, buff=0.08)

        # Extremo derecho cerrado (-0.5, 1.5): punto sólido
        p_closed = axes.c2p(-0.5, 1.5)
        dot_closed = Dot(p_closed, radius=0.075, color=THEME["success"])
        lbl_closed = MathTex(r"\left(-\frac{1}{2}, \frac{3}{2}\right)", font_size=13.0, color=THEME["success"]).next_to(p_closed, UR, buff=0.08)

        # Proyección del rango sobre el eje Y: ]-1, 1.5]
        range_line = Line(
            axes.c2p(0.0, -1.0),
            axes.c2p(0.0, 1.5),
            color=THEME["success"],
            stroke_width=5.0
        )
        dot_r_open = Circle(radius=0.06, color=THEME["error"], stroke_width=2.2, fill_color=THEME["bg_color"], fill_opacity=1.0).move_to(axes.c2p(0.0, -1.0))
        dot_r_closed = Dot(axes.c2p(0.0, 1.5), radius=0.065, color=THEME["success"])
        lbl_range = MathTex(
            r"\left]-1, \frac{3}{2}\right]",
            font_size=13.5,
            color=THEME["success"]
        ).next_to(axes.c2p(0.0, 0.25), RIGHT, buff=0.10)

        # Transición hacia el paso 8
        self.play(
            FadeOut(self.active_box),
            FadeOut(self.active_math, shift=DOWN * 0.2),
            FadeOut(self.active_just, shift=DOWN * 0.2),
            FadeIn(info_grp, shift=DOWN * 0.2),
            Create(axes),
            Write(axes_labels),
            Create(curve_ref),
            FadeIn(dot_v_ext), Write(lbl_v_ext),
            *prog_anims,
            run_time=1.8
        )
        self.active_box = None
        self.active_math = None
        self.active_just = None

        # Trazado del arco restringido y proyección del rango
        self.play(
            Create(curve_dom), Write(lbl_curve),
            Create(range_line),
            FadeIn(dot_r_open), FadeIn(dot_r_closed), Write(lbl_range),
            run_time=2.2
        )

        # Marcado de puntos de frontera y raíz
        self.play(
            FadeIn(dot_open), Write(lbl_open),
            FadeIn(dot_closed), Write(lbl_closed),
            FadeIn(dot_root), Write(lbl_root),
            run_time=1.8
        )
        self.wait(4.5)

        # ==========================================================
        # Cierre suave usando el helper de la clase base
        # ==========================================================
        graph_mobs = [
            info_grp, axes, axes_labels,
            curve_ref, dot_v_ext, lbl_v_ext,
            curve_dom, lbl_curve,
            range_line, dot_r_open, dot_r_closed, lbl_range,
            dot_open, lbl_open, dot_closed, lbl_closed,
            dot_root, lbl_root
        ]
        self.finish_exercise(extra_mobjects=graph_mobs)
        self.wait(0.5)
