from manim import *


class ShapesManim(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE).shift(LEFT)
        square = Square(side_length=2, color=GREEN).shift(RIGHT)
        line = Line(LEFT, RIGHT, color=YELLOW).shift(UP)
        rectangle = Rectangle(height=2, width=4).shift(DOWN)
        arrow = Arrow(start=LEFT, end=RIGHT, buff=0)


        self.play(Create(circle))
        self.play(Create(square))
        self.play(Create(line))
        self.play(Create(rectangle))
        self.play(Create(arrow))
