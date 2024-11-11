from manim import *

class GradientExample(Scene):
    def construct(self):
        rectangle = Rectangle(width=4, height=2)
        rectangle.set_color([RED, YELLOW, BLUE]).set_fill([RED, YELLOW, BLUE])  # Градиент от красного к синему
        
        self.add(rectangle)
        self.play(rectangle.animate.shift(UP))
