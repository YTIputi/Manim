from manim import *

class AnimationGroupExample(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        triangle = Triangle()
        self.play(AnimationGroup(GrowFromCenter(square), GrowFromCenter(circle), GrowFromCenter(triangle), run_time=2))
        self.wait(1)