from manim import *

class ApplyMethodExample(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        # Используем ApplyMethod для вращения квадрата на 45 градусов
        self.play(ApplyMethod(square.rotate, PI / 4))
