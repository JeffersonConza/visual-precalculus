"""
Clase base reutilizable para ejercicios de precálculo animados.
Controla el ritmo, temporización y estructura visual unificada sin solapamientos.
"""
from manim import *
from .styles import THEME, TIMINGS

class BaseExerciseScene(Scene):
    def setup(self):
        self.camera.background_color = THEME["bg_color"]

    def show_top_bar(self, chapter: str, exercise_num: int, topic: str):
        """Muestra una barra superior compacta y limpia que nunca colisiona con el contenido."""
        bar_text = Text(
            f"Precálculo 2  ·  Capítulo {chapter}  ·  Ejercicio {exercise_num} (Par)  —  {topic}",
            font_size=17,
            color=THEME["header_color"],
            weight=BOLD
        ).to_edge(UP, buff=0.25)
        
        self.play(FadeIn(bar_text, shift=DOWN * 0.2), run_time=0.6)
        return bar_text

    def present_initial_statement(self, statement_content: VMobject, formula_badge: VMobject, read_time: float = 3.5):
        """
        1. Presenta el enunciado completo centrado en pantalla.
        2. Pausa para asimilación.
        3. Sale hacia abajo y la pastilla compacta entra desde arriba hacia abajo.
        """
        box = SurroundingRectangle(
            statement_content,
            color=THEME["statement_box"],
            buff=0.3,
            corner_radius=0.15,
            stroke_width=2.5
        )
        full_group = VGroup(box, statement_content).move_to(ORIGIN)
        
        # Entrada centrada desplazándose hacia abajo
        self.play(FadeIn(full_group, shift=DOWN * 0.4), run_time=1.1)
        self.wait(read_time)
        
        # Posición de la pastilla compacta superior
        formula_badge.to_edge(UP, buff=0.7)
        badge_box = SurroundingRectangle(
            formula_badge,
            color=THEME["statement_box"],
            buff=0.15,
            corner_radius=0.1,
            stroke_width=1.5
        )
        compact_group = VGroup(badge_box, formula_badge)
        
        # Salida del enunciado hacia abajo y entrada de la pastilla compacta hacia abajo
        self.play(
            FadeOut(full_group, shift=DOWN * 0.4),
            FadeIn(compact_group, shift=DOWN * 0.3),
            run_time=0.8
        )
        return compact_group

    def conclude_solution(self, final_answer: VMobject, wait_time: float = 4.0):
        """Destaca la respuesta final con un marco de éxito y pausa antes de cerrar."""
        rect = SurroundingRectangle(
            final_answer,
            color=THEME["success"],
            buff=0.22,
            corner_radius=0.12,
            stroke_width=2.5
        )
        self.play(Create(rect), run_time=TIMINGS["highlight_answer"])
        self.wait(wait_time)
        self.play(FadeOut(*self.mobjects, shift=DOWN * 0.5), run_time=0.9)
