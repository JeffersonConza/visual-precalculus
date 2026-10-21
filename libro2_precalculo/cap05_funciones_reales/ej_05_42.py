"""
Precálculo 2 · Colección Yachay Tech / Editorial Amarun
Capítulo 5: Funciones reales
Sección 5.10: Ejercicios propuestos del Capítulo 5
Ejercicio 5.42 (Página 111-112 del libro / Páginas 130-131 del PDF)

Buscamos soluciones (x, y, z) ∈ ℝ³ para 4 sistemas de ecuaciones:
1. Sistema lineal 3x3:
   5x + 3y - 2z = 1
   -x - y + 3z = 2
   4x - 5y + z = -1
   ⟹ Determinado: CS₁ = {(3/13, 4/7, 85/91)}.

2. Sistema semilineal cuadrático:
   5x² + 3y² - 2z = 1
   -x² - y² + 3z = 2
   4x² - 5y² + z = -1
   ⟹ Finitamente determinado: CS₂ = {(±√(39)/13, ±2√(7)/7, 85/91)} (4 soluciones).

3. Sistema bicuadrático:
   5x² + 3y² - 2z² = 1
   -x² - y² + 3z² = 2
   4x² - 5y² + z² = -1
   ⟹ Finitamente determinado: CS₃ = {(±√(39)/13, ±2√(7)/7, ±√(7735)/91)} (8 soluciones).

4. Sistema subdeterminado (2 ecuaciones, 3 incógnitas):
   5x² + 3y² - 2z = 1
   -x² - y² + 3z = 2
   ⟹ Indeterminado: CS₄ = {(±√(7(1-z)/2), ±√((13z-11)/2), z) : z ∈ [11/13, 1]}.
   Proyección en el plano XY: elipse 13x²/7 + y² = 1.
"""
from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from common.base_scene import AmarunExerciseScene
from common.styles import THEME

class Ejercicio05_42(AmarunExerciseScene):
    def construct(self):
        # ==========================================================
        # 1. Encabezado Permanente (sin "(Par)")
        # ==========================================================
        self.setup_header(
            book="Precálculo 2",
            chapter="Capítulo 5",
            exercise="Ejercicio 5.42",
            topic="Sistemas de Ecuaciones Reales y Clasificación en ℝ³"
        )

        # ==========================================================
        # 2. Enunciado Permanente
        # ==========================================================
        self.setup_statement(
            desc_text="Buscamos soluciones (x, y, z) ∈ ℝ³ para 4 sistemas de ecuaciones (lineales y no lineales):",
            math_tex=r"1.\; \text{Lineal}; \quad 2.\; (x^2, y^2, z); \quad 3.\; (x^2, y^2, z^2); \quad 4.\; \text{2 ecuaciones} \implies \text{Resolver a mano, Maxima y clasificar}.",
            desc_font_size=14,
            math_font_size=13,
            read_time=4.0
        )

        # ==========================================================
        # 3. Barra de Progreso Inferior (6 pasos)
        # ==========================================================
        self.setup_progress_bar([
            "1/6: Núcleo Lineal Común",
            "2/6: Resolución y Maxima",
            "3/6: Sist. 1: Lineal (Determinado)",
            "4/6: Sist. 2: Semilineal (4 sol.)",
            "5/6: Sist. 3: Bicuadrático (8 sol.)",
            "6/6: Sist. 4: Subdeterminado y Geometría"
        ])

        # ==========================================================
        # PASO 1: Núcleo Lineal Común y Sustituciones
        # ==========================================================
        eq1 = MathTex(
            r"\begin{aligned}"
            r"&\text{Matriz de coeficientes común } M \in \mathcal{M}_{3\times 3}(\mathbb{R}): \\[4pt]"
            r"&M \begin{pmatrix} u \\ v \\ w \end{pmatrix} = "
            r"\begin{pmatrix} 5 & 3 & -2 \\ -1 & -1 & 3 \\ 4 & -5 & 1 \end{pmatrix}"
            r"\begin{pmatrix} u \\ v \\ w \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix} \\[6pt]"
            r"&\det(M) = 91 \neq 0 \implies \text{Solución lineal única } (u, v, w) \\[6pt]"
            r"&\mathbf{Sist.\; 1:} \quad (u, v, w) = (x, y, z) \\[2pt]"
            r"&\mathbf{Sist.\; 2:} \quad (u, v, w) = (x^2, y^2, z) \\[2pt]"
            r"&\mathbf{Sist.\; 3:} \quad (u, v, w) = (x^2, y^2, z^2) \\[2pt]"
            r"&\mathbf{Sist.\; 4:} \quad \text{2 ecuaciones en } (x^2, y^2, z)"
            r"\end{aligned}",
            font_size=17,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just1 = self.create_justification(
            "1. Estructura Nuclear Común:\n"
            "• Los 4 problemas comparten la misma\n"
            "  matriz de coeficientes lineal M.\n"
            "• Como det(M) = 91 ≠ 0, el núcleo lineal\n"
            "  posee una terna única (u, v, w).\n"
            "• Cada sistema surge al sustituir variables\n"
            "  lineales por cuadráticas o variar el\n"
            "  número de ligaduras independientes."
        )

        self.morph_step(eq1, just1, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 2: Resolución Analítica y Comparación con Maxima
        # ==========================================================
        eq2 = MathTex(
            r"\begin{aligned}"
            r"&\text{Combinaciones con } E_2: \; -u - v + 3w = 2 \\[4pt]"
            r"&E_1 + 5E_2 \implies -2v + 13w = 11 \\[3pt]"
            r"&4E_2 + E_3 \implies -9v + 13w = 7 \\[4pt]"
            r"&\text{Restando: } 7v = 4 \implies v = \frac{4}{7} \\[4pt]"
            r"&\implies w = \frac{11 + 2(4/7)}{13} = \frac{85}{91} \\[4pt]"
            r"&\implies u = 3w - v - 2 = \frac{3}{13} \\[6pt]"
            r"&\textbf{Maxima:} \; \texttt{linsolve([E1,E2,E3],[u,v,w])} \\[2pt]"
            r"&\implies [u = 3/13, \; v = 4/7, \; w = 85/91]"
            r"\end{aligned}",
            font_size=17,
            color=THEME["secondary"]
        ).move_to([-3.4, 0.2, 0])

        just2 = self.create_justification(
            "2. Resolución Analítica y Maxima:\n"
            "• Eliminación directa: combinamos E₁ y E₃\n"
            "  con E₂ para anular la incógnita u.\n"
            "• El subsistema de 2×2 da v = 4/7 y\n"
            "  w = 85/91; luego u = 3/13.\n"
            "• En Maxima, linsolve corrobora la terna\n"
            "  exacta sin discrepancia analítica."
        )

        self.morph_step(eq2, just2, box_color=THEME["secondary"], wait_time=5.0)

        # ==========================================================
        # PASO 3: Sistema 1 — Caso Lineal Determinado
        # ==========================================================
        eq3 = MathTex(
            r"\begin{aligned}"
            r"&\mathbf{Sistema\; 1:} \quad \begin{cases} 5x + 3y - 2z = 1 \\ -x - y + 3z = 2 \\ 4x - 5y + z = -1 \end{cases} \\[6pt]"
            r"&x = u = \frac{3}{13}, \quad y = v = \frac{4}{7}, \quad z = w = \frac{85}{91} \\[6pt]"
            r"&\text{\textbf{Conjunto Solución:}} \\[4pt]"
            r"&CS_1 = \left\{ \left(\frac{3}{13}, \frac{4}{7}, \frac{85}{91}\right) \right\} \\[6pt]"
            r"&\text{\textbf{Tipo: Determinado}} \quad (\text{Solución única en } \mathbb{R}^3) \\[4pt]"
            r"&\text{Maxima: } \texttt{solve([e1,e2,e3],[x,y,z])} \implies [[x=\frac{3}{13},\dots]]"
            r"\end{aligned}",
            font_size=17,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just3 = self.create_justification(
            "3. Sistema 1 — Caso Lineal:\n"
            "• Identidad directa: u = x, v = y, w = z.\n"
            "• La solución analítica coincide con la única\n"
            "  intersección de los 3 planos afines en ℝ³.\n"
            "• Maxima valida la terna racional única.\n"
            "• Tipo de sistema: Determinado."
        )

        self.morph_step(eq3, just3, box_color=THEME["success"], wait_time=4.8)

        # ==========================================================
        # PASO 4: Sistema 2 — Semilineal Cuadrático (4 Soluciones)
        # ==========================================================
        eq4 = MathTex(
            r"\begin{aligned}"
            r"&\mathbf{Sistema\; 2:} \quad \begin{cases} 5x^2 + 3y^2 - 2z = 1 \\ -x^2 - y^2 + 3z = 2 \\ 4x^2 - 5y^2 + z = -1 \end{cases} \\[6pt]"
            r"&x^2 = u = \frac{3}{13} \implies x = \pm \sqrt{\frac{3}{13}} = \pm \frac{\sqrt{39}}{13} \\[4pt]"
            r"&y^2 = v = \frac{4}{7} \implies y = \pm \sqrt{\frac{4}{7}} = \pm \frac{2\sqrt{7}}{7} \\[4pt]"
            r"&z = w = \frac{85}{91} \\[6pt]"
            r"&CS_2 = \left\{ \left(\pm \frac{\sqrt{39}}{13}, \pm \frac{2\sqrt{7}}{7}, \frac{85}{91}\right) \right\} \\[6pt]"
            r"&\mathbf{Tipo:\; Finitamente\; determinado} \quad (4 \text{ soluciones})"
            r"\end{aligned}",
            font_size=17,
            color=THEME["highlight"]
        ).move_to([-3.4, 0.2, 0])

        just4 = self.create_justification(
            "4. Sistema 2 — Semilineal Cuadrático:\n"
            "• Como u = 3/13 > 0 y v = 4/7 > 0, cada eje\n"
            "  cuadrático aporta 2 raíces simétricas: ±√u, ±√v.\n"
            "• La componente z = 85/91 es lineal y fija.\n"
            "• Total: 2 × 2 × 1 = 4 ternas coplanares.\n"
            "• Tipo de sistema: Finitamente determinado."
        )

        self.morph_step(eq4, just4, box_color=THEME["highlight"], wait_time=4.8)

        # ==========================================================
        # PASO 5: Sistema 3 — Bicuadrático Total (8 Soluciones)
        # ==========================================================
        eq5 = MathTex(
            r"\begin{aligned}"
            r"&\mathbf{Sistema\; 3:} \quad \begin{cases} 5x^2 + 3y^2 - 2z^2 = 1 \\ -x^2 - y^2 + 3z^2 = 2 \\ 4x^2 - 5y^2 + z^2 = -1 \end{cases} \\[6pt]"
            r"&x^2 = \frac{3}{13} \implies x = \pm \frac{\sqrt{39}}{13} \\[3pt]"
            r"&y^2 = \frac{4}{7} \implies y = \pm \frac{2\sqrt{7}}{7} \\[3pt]"
            r"&z^2 = \frac{85}{91} \implies z = \pm \sqrt{\frac{85}{91}} = \pm \frac{\sqrt{7735}}{91} \\[6pt]"
            r"&CS_3 = \left\{ \left(\pm \frac{\sqrt{39}}{13}, \pm \frac{2\sqrt{7}}{7}, \pm \frac{\sqrt{7735}}{91}\right) \right\} \\[6pt]"
            r"&\mathbf{Tipo:\; Finitamente\; determinado} \quad (8 \text{ soluciones})"
            r"\end{aligned}",
            font_size=17,
            color=WHITE
        ).move_to([-3.4, 0.2, 0])

        just5 = self.create_justification(
            "5. Sistema 3 — Bicuadrático Total:\n"
            "• Ahora las tres variables entran al cuadrado.\n"
            "• Con u > 0, v > 0, w > 0, z genera dos ramas: ±√w.\n"
            "• Total de ternas: 2 × 2 × 2 = 8 soluciones.\n"
            "• Vértices de un prisma ortorrómbico centrado\n"
            "  en el origen de ℝ³.\n"
            "• Tipo: Finitamente determinado."
        )

        self.morph_step(eq5, just5, box_color=THEME["statement_box"], wait_time=4.8)

        # ==========================================================
        # PASO 6: Sistema 4 (Subdeterminado) e Ilustración Geométrica
        # ==========================================================
        prog_anims = self.get_advance_progress_anims(5)

        # Panel izquierdo: Resumen geométrico y analítico de Sistema 4
        t_title = Text("Geometría de Sistemas en ℝ³:", font_size=14, color=THEME["header_color"], weight=BOLD)
        eq_s4 = MathTex(
            r"\begin{aligned}"
            r"&\mathbf{Sist.\; 4:} \quad \begin{cases} 5x^2 + 3y^2 - 2z = 1 \\ -x^2 - y^2 + 3z = 2 \end{cases} \\[4pt]"
            r"&x^2 = \frac{7(1-z)}{2} \ge 0 \implies z \le 1 \\[3pt]"
            r"&y^2 = \frac{13z-11}{2} \ge 0 \implies z \ge \frac{11}{13} \\[4pt]"
            r"&\mathbf{CS_4:} \; \left\{\left(\pm\sqrt{\tfrac{7(1-z)}{2}}, \pm\sqrt{\tfrac{13z-11}{2}}, z\right)\right\} \\[4pt]"
            r"&\mathbf{Tipo:\; Indeterminado } \; (\infty \text{ sol.}) \\[4pt]"
            r"&\text{Proyección en } XY: \; \frac{13x^2}{7} + y^2 = 1"
            r"\end{aligned}",
            font_size=15,
            color=WHITE
        )
        info_grp = VGroup(t_title, eq_s4).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        info_box = SurroundingRectangle(info_grp, color=THEME["statement_box"], buff=0.18, stroke_width=1.5, corner_radius=0.08)
        left_grp = VGroup(info_box, info_grp).move_to([-3.4, -0.45, 0])

        # Panel derecho: Ejes cartesianos y proyección en plano XY
        axes, axes_labels = self.setup_axes(
            x_range=[-1.3, 1.3, 0.5],
            y_range=[-1.4, 1.4, 0.5],
            x_length=4.8,
            y_length=3.8,
            center=[2.9, -0.45, 0],
            include_numbers=False
        )

        # Curva elíptica de proyección de CS4: 13x^2 / 7 + y^2 = 1
        a_ell = np.sqrt(7.0 / 13.0)
        b_ell = 1.0
        ellipse_curve = ParametricFunction(
            lambda t: axes.c2p(a_ell * np.cos(t), b_ell * np.sin(t)),
            t_range=[0, TAU],
            color=THEME["curve"],
            stroke_width=2.5
        )

        # Punto de Sist 1: (3/13, 4/7) ≈ (0.2308, 0.5714)
        pt_s1 = axes.c2p(3.0/13.0, 4.0/7.0)
        dot_s1 = Dot(pt_s1, radius=0.065, color=THEME["header_color"])
        lbl_s1 = MathTex(r"CS_1 \; (1 \text{ pto})", font_size=11, color=THEME["header_color"]).next_to(dot_s1, UR, buff=0.08)

        # 4 Puntos de Sist 2: (±sqrt(3/13), ±sqrt(4/7))
        u_val = np.sqrt(3.0 / 13.0)
        v_val = np.sqrt(4.0 / 7.0)
        pts_s2 = [
            axes.c2p(u_val, v_val),
            axes.c2p(-u_val, v_val),
            axes.c2p(-u_val, -v_val),
            axes.c2p(u_val, -v_val)
        ]
        dots_s2 = VGroup(*[Dot(p, radius=0.06, color=THEME["highlight"]) for p in pts_s2])
        lbl_s2 = MathTex(r"CS_2 \subset \text{Elipse} \; (4 \text{ ptos})", font_size=11, color=THEME["highlight"]).next_to(pts_s2[0], UR, buff=0.08)

        graph_title = Text("Proyección en el Plano XY", font_size=13, color=THEME["header_color"]).next_to(axes, UP, buff=0.15)
        ell_label = MathTex(r"\frac{13x^2}{7} + y^2 = 1 \; (CS_4)", font_size=12, color=THEME["curve"]).next_to(axes, DOWN, buff=0.15)

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
            Create(ellipse_curve),
            Write(ell_label),
            run_time=1.4
        )
        self.play(
            FadeIn(dot_s1, scale=1.4),
            Write(lbl_s1),
            FadeIn(dots_s2, scale=1.3),
            Write(lbl_s2),
            run_time=1.2
        )
        self.wait(7.0)

        # Cierre suave
        extra_mobs = [
            left_grp, axes, axes_labels, graph_title,
            ellipse_curve, ell_label,
            dot_s1, lbl_s1, dots_s2, lbl_s2
        ]
        self.finish_exercise(extra_mobjects=extra_mobs)
        self.wait(0.5)
