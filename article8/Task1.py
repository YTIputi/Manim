from manim import *

class GraphExample(Scene):
    def construct(self):
        # Создаем оси
        axes = Axes(
            x_range=[-3, 3], 
            y_range=[-5, 5], 
            axis_config={"color": BLUE},
        )
        # Создаем график функции f(x) = x^2
        graph = axes.plot(lambda x: x**3, color=RED)
        # Отображаем оси и график
        self.play(FadeIn(axes), Create(graph))
        self.play(Transform(axes, graph))
