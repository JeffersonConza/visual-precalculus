"""
BaseScene para la Colección Visual Precálculo (Yachay Tech / Editorial Amarun).
Estandariza:
- Identidad visual institucional y paleta de colores.
- Encabezado permanente sin "(Par)".
- Recuadro de enunciado permanente centrado superior [0, 2.5, 0].
- Barra de progreso interactiva inferior (y = -3.55) con n etapas.
- Metamorfosis algebraica 3Blue1Brown (transformación en sitio + justificaciones a la derecha).
- Helpers de tachado explícito, ejes cartesianos, puntos abiertos y cierre suave.
"""
from manim import *
import numpy as np
from .styles import THEME

class AmarunExerciseScene(Scene):
    def setup(self):
        self.camera.background_color = THEME["bg_color"]
        self.header = None
        self.permanent_statement = None
        
        # Barra de progreso
        self.progress_ui = None
        self.prog_dots = []
        self.prog_track = None
        self.prog_label = None
        self.dots_grp = None
        self.step_labels = []
        self.current_step = 0
        
        # Estado algebraico activo
        self.active_math = None
        self.active_just = None
        self.active_box = None

    # ==========================================================
    # 1. Encabezado Permanente
    # ==========================================================
    def setup_header(
        self,
        book: str = "Precálculo 2",
        chapter: str = "Capítulo 5",
        exercise: str = "Ejercicio 5.2",
        topic: str = "Regla del Máximo Dominio (RMD)",
        run_time: float = 0.7
    ) -> Text:
        """Crea el encabezado institucional en la parte superior sin la palabra '(Par)'."""
        self.header = Text(
            f"{book}  ·  {chapter}  ·  {exercise}  —  {topic}",
            font_size=17,
            color=THEME["header_color"],
            weight=BOLD
        ).to_edge(UP, buff=0.25)
        self.play(FadeIn(self.header, shift=DOWN * 0.2), run_time=run_time)
        return self.header

    # ==========================================================
    # 2. Enunciado Permanente
    # ==========================================================
    def setup_statement(
        self,
        desc_text: str,
        math_tex: str,
        read_time: float = 4.5,
        math_font_size: int = 26,
        desc_font_size: int = 18,
        box_pos: np.ndarray = np.array([0.0, 2.5, 0.0])
    ) -> VGroup:
        """Presenta el enunciado permanente en un recuadro rojo poncho en la parte superior."""
        stmt_desc = Text(desc_text, font_size=desc_font_size, color=THEME["statement_text"])
        stmt_math = MathTex(math_tex, font_size=math_font_size, color=THEME["highlight"])
        stmt_content = VGroup(stmt_desc, stmt_math).arrange(RIGHT, buff=0.3)
        
        stmt_box = SurroundingRectangle(
            stmt_content,
            color=THEME["statement_box"],
            buff=0.2,
            corner_radius=0.1,
            stroke_width=2.0
        )
        self.permanent_statement = VGroup(stmt_box, stmt_content).move_to(box_pos)
        self.play(Create(stmt_box), Write(stmt_content), run_time=1.4)
        self.wait(read_time)
        return self.permanent_statement

    # ==========================================================
    # 3. Barra de Progreso Inferior
    # ==========================================================
    def setup_progress_bar(
        self,
        step_labels: list[str],
        y_prog: float = -3.55,
        dot_spacing: float = 1.05,
        run_time: float = 0.8
    ) -> VGroup:
        """Construye la barra de progreso conectada con indicador del paso activo."""
        self.step_labels = step_labels
        num_steps = len(step_labels)
        start_x = - (num_steps - 1) * dot_spacing / 2

        self.prog_dots = []
        self.prog_track = VGroup()
        for i in range(num_steps):
            dot = Dot(point=[start_x + i * dot_spacing, y_prog, 0], radius=0.07, color=THEME["axes"])
            self.prog_dots.append(dot)
            if i > 0:
                seg = Line(self.prog_dots[i-1].get_center(), dot.get_center(), color=THEME["axes"], stroke_width=2)
                self.prog_track.add(seg)

        self.dots_grp = VGroup(*self.prog_dots)
        self.prog_label = Text(step_labels[0], font_size=13, color=THEME["header_color"]).next_to(self.dots_grp, UP, buff=0.14)
        self.progress_ui = VGroup(self.prog_track, self.dots_grp, self.prog_label)

        # Activar el paso 0
        self.prog_dots[0].set_color(THEME["highlight"]).scale(1.25)
        self.current_step = 0
        self.play(FadeIn(self.progress_ui, shift=UP * 0.2), run_time=run_time)
        return self.progress_ui

    def get_advance_progress_anims(self, next_idx: int) -> list:
        """Genera las animaciones necesarias para avanzar el paso en la barra de progreso."""
        current_idx = self.current_step
        new_lbl = Text(self.step_labels[next_idx], font_size=13, color=THEME["header_color"]).next_to(self.dots_grp, UP, buff=0.14)
        anims = [
            self.prog_dots[current_idx].animate.set_color(THEME["success"]).scale(1.0 / 1.25),
            self.prog_dots[next_idx].animate.set_color(THEME["highlight"]).scale(1.25),
            FadeTransform(self.prog_label, new_lbl)
        ]
        self.prog_label = new_lbl
        self.current_step = next_idx
        return anims

    # ==========================================================
    # 4. Helpers de Justificación y Metamorfosis 3B1B
    # ==========================================================
    def create_justification(
        self,
        text_str: str,
        font_size: int = 16,
        pos: list = [3.1, 0.2, 0],
        line_spacing: float = 1.35
    ) -> Text:
        """Crea el bloque de justificación a la derecha con formato uniforme."""
        return Text(
            text_str,
            font_size=font_size,
            color=THEME["statement_text"],
            line_spacing=line_spacing
        ).move_to(pos)

    def morph_step(
        self,
        new_math: VMobject,
        new_just: VMobject,
        box_color: str = None,
        advance_to_step: int = None,
        run_time: float = 1.8,
        wait_time: float = 5.0,
        box_buff: float = 0.15
    ):
        """
        Ejecuta la metamorfosis 3Blue1Brown:
        - Si es el primer paso, introduce fórmula y justificación.
        - Si ya existe un paso, muta la fórmula in situ y renueva la justificación.
        - Avanza automáticamente la barra de progreso si se especifica advance_to_step.
        """
        if box_color is None:
            box_color = THEME["highlight"]

        if self.active_math is None:
            # Primer paso
            self.active_math = new_math
            self.active_just = new_just
            self.play(
                FadeIn(self.active_math, shift=DOWN * 0.3),
                FadeIn(self.active_just, shift=DOWN * 0.3),
                run_time=run_time
            )
            self.active_box = SurroundingRectangle(self.active_math, color=box_color, buff=box_buff, stroke_width=2.0)
            self.play(Create(self.active_box), run_time=0.6)
            self.wait(wait_time)
            return

        # Pasos subsecuentes con metamorfosis
        extra_anims = []
        if advance_to_step is not None:
            extra_anims = self.get_advance_progress_anims(advance_to_step)

        new_box = SurroundingRectangle(new_math, color=box_color, buff=box_buff, stroke_width=2.0)

        self.play(
            FadeOut(self.active_box),
            ReplacementTransform(self.active_math, new_math),
            FadeOut(self.active_just, shift=DOWN * 0.2),
            FadeIn(new_just, shift=DOWN * 0.2),
            *extra_anims,
            run_time=run_time
        )
        self.play(Create(new_box), run_time=0.6)
        self.active_math = new_math
        self.active_just = new_just
        self.active_box = new_box
        self.wait(wait_time)

    # ==========================================================
    # 5. Helpers de Tachado y Gráficos
    # ==========================================================
    def create_strike_line(
        self,
        mobject: VMobject,
        color: str = None,
        stroke_width: float = 3.5,
        pad: float = 0.08
    ) -> Line:
        """Crea una línea diagonal de tachado calculada sobre los bordes del submobject."""
        if color is None:
            color = THEME["poncho_red"]
        return Line(
            mobject.get_corner(DL) + LEFT * pad + DOWN * (pad / 2),
            mobject.get_corner(UR) + RIGHT * pad + UP * (pad / 2),
            color=color,
            stroke_width=stroke_width
        )

    def setup_axes(
        self,
        x_range: list = [-3.2, 3.2, 1],
        y_range: list = [-1.0, 3.2, 1],
        x_length: float = 5.6,
        y_length: float = 3.8,
        center: list = [2.7, -0.45, 0],
        include_numbers: bool = True
    ) -> tuple[Axes, VGroup]:
        """Crea un sistema de ejes coordenados con el estilo y proporciones institucionales."""
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_length,
            y_length=y_length,
            tips=True,
            axis_config={
                "color": THEME["axes"],
                "stroke_width": 2,
                "include_numbers": include_numbers,
                "font_size": 14,
            }
        ).move_to(center)
        labels = axes.get_axis_labels(
            x_label=MathTex("x", font_size=18, color=THEME["statement_text"]),
            y_label=MathTex("y", font_size=18, color=THEME["statement_text"])
        )
        return axes, labels

    def create_open_point(
        self,
        axes: Axes,
        x: float,
        y: float,
        label_tex: str = None,
        color: str = None,
        radius: float = 0.08
    ) -> tuple[Circle, VMobject, VMobject]:
        """Crea un punto abierto (círculo hueco) con flecha y etiqueta LaTeX."""
        if color is None:
            color = THEME["poncho_red"]
        pt = axes.c2p(x, y)
        hole = Circle(
            radius=radius,
            color=color,
            stroke_width=3,
            fill_color=THEME["bg_color"],
            fill_opacity=1.0
        ).move_to(pt)

        if label_tex:
            lbl = MathTex(label_tex, font_size=15, color=color).next_to(hole, UP + LEFT, buff=0.15)
            arrow = Arrow(
                lbl.get_bottom(),
                hole.get_top(),
                buff=0.05,
                stroke_width=2,
                max_tip_length_to_length_ratio=0.25,
                color=color
            )
            return hole, lbl, arrow
        return hole, None, None

    # ==========================================================
    # 6. Cierre Suave
    # ==========================================================
    def finish_exercise(self, extra_mobjects: list = None, run_time: float = 1.4):
        """Desvanece suavemente todos los componentes activos de la escena."""
        to_fade = []
        if self.active_math:
            to_fade.append(self.active_math)
        if self.active_just:
            to_fade.append(self.active_just)
        if self.active_box:
            to_fade.append(self.active_box)
        if extra_mobjects:
            to_fade.extend(extra_mobjects)
        if self.progress_ui:
            to_fade.append(self.progress_ui)
        if self.permanent_statement:
            to_fade.append(self.permanent_statement)
        if self.header:
            to_fade.append(self.header)

        self.play(*[FadeOut(m, shift=DOWN * 0.3) for m in to_fade], run_time=run_time)
