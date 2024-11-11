from manim import *

class ParametricGraph(Scene):
    def construct(self):
        # Создаем оси
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
        ).shift(DOWN)
        # Создаем параметрическую функцию
        parametric_curve = ParametricFunction(
            lambda t: np.array([np.sin(t * 5), np.cos(t * 3), 0]), 
            t_range=[0, 3 * np.pi], 
            color=YELLOW,
        ).shift(DOWN)

        text = Text("Параметрические функции")
        title = MathTex(r"x = sin(t * 5); y = cos(t * 3)").shift(UP * 3)
        # Отображаем оси и график
        self.play(Succession(Write(text), FadeOut(text)))
        self.play(FadeIn(axes), Write(title))
        self.play(Create(parametric_curve), run_time=1)
        self.wait()
