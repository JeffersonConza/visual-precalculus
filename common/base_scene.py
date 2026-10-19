"""
Clase base reutilizable para ejercicios de precálculo animados.
Controla el ritmo, temporización y estructura visual unificada.
"""
from manim import *
from .styles import THEME, TIMINGS

class BaseExerciseScene(Scene):
    def setup(self):
        self.camera.background_color = THEME["bg_color"]

    def show_header(self, chapter: str, exercise_num: int, topic: str):
        """Muestra la barra superior con el número de ejercicio par y tema."""
        title_text = f"Precálculo 2 · Cap. {chapter} · Ejercicio {exercise_num} (Par)"
        subtitle_text = topic
        
        header = Text(title_text, font_size=22, color=THEME["header_color"], weight=BOLD)
        subtitle = Text(subtitle_text, font_size=18, color=THEME["highlight"])
        
        header_group = VGroup(header, subtitle).arrange(DOWN, buff=0.1).to_edge(UP, buff=0.3)
        self.play(FadeIn(header_group, shift=DOWN * 0.2), run_time=TIMINGS["header_appear"])
        return header_group

    def present_statement(self, statement: VMobject, read_time: float = None):
        """
        Presenta el enunciado centrado en pantalla, ofrece tiempo de lectura
        y luego lo minimiza a la esquina superior izquierda.
        """
        box = SurroundingRectangle(
            statement,
            color=THEME["statement_box"],
            buff=0.3,
            corner_radius=0.15,
            stroke_width=2.5
        )
        statement_group = VGroup(box, statement).move_to(ORIGIN)
        
        # 1. Aparición
        self.play(Create(box), Write(statement), run_time=TIMINGS["statement_write"])
        
        # 2. Pausa prudente para asimilar el enunciado
        duration = read_time if read_time is not None else TIMINGS["statement_read_base"]
        self.wait(duration)
        
        # 3. Minimizar y mover a la esquina
        self.play(
            statement_group.animate.scale(0.65).to_corner(UL, buff=0.6),
            run_time=TIMINGS["statement_minimize"]
        )
        return statement_group

    def conclude_solution(self, final_answer: VMobject, wait_time: float = None):
        """Destaca la respuesta final con un marco de éxito y pausa antes de cerrar."""
        rect = SurroundingRectangle(
            final_answer,
            color=THEME["success"],
            buff=0.2,
            corner_radius=0.1,
            stroke_width=3
        )
        self.play(Create(rect), run_time=TIMINGS["highlight_answer"])
        
        pause = wait_time if wait_time is not None else TIMINGS["final_pause"]
        self.wait(pause)
        
        self.play(FadeOut(*self.mobjects), run_time=1.0)
