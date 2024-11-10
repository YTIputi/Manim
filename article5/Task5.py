from manim import *

class AnimateExample(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        # Используем .animate для плавного перемещения вправо и увеличения масштаба
        self.play(square.animate.shift(RIGHT * 2).scale(1.5).rotate(PI / 4))
        self.wait()
        self.play(square.animate.shift(RIGHT * -2).scale(2 / 3).rotate(-PI / 4))
