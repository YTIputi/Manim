from manim import *

class LineStyles(Scene):
    def construct(self):
        line = Line(ORIGIN, RIGHT * 4, color=BLUE, stroke_width=10)  # Толщина линии
        dotted_line = DashedLine(LEFT, RIGHT, color=GREEN, dash_length=0.1, stroke_width=5)
        
        self.add(line, dotted_line)
        self.play(line.animate.shift(UP), dotted_line.animate.shift(DOWN))
