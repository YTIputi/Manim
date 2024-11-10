from manim import *

class BasicExample(Scene):
    def construct(self):
        # Создаем текст
        hello_text = Text("Hello, Manim!")
        formula = MathTex(r"\int_a^b f(x) \, dx")

        # Создаем примитивы
        circle = Circle(color=BLUE).shift(LEFT)
        square = Square(color=GREEN).shift(RIGHT)
        line = Line(LEFT, RIGHT)
        arrow = Arrow(start=LEFT, end=RIGHT, buff=0)

        # Создаем SVG объект
        svg_object = ImageMobject("/home/sb/Downloads/Manim/article2/photo_2024-11-08_00-42-16.jpg").set_color(YELLOW)

        # Анимации
        self.play(Write(hello_text), run_time=2)
        self.play(Write(formula), run_time=2)
        self.play(FadeIn(circle), FadeIn(square))
        self.play(Transform(circle, square), run_time=2)
        self.play(Create(line))
        self.play(GrowArrow(arrow))
        self.play(FadeIn(svg_object))
        self.wait()
