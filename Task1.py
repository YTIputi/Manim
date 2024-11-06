from manim import Scene, Text, Write

class HelloWorld(Scene):
    def construct(self) -> None:
        text = Text("Hello, Sofa")
        self.play(Write(text))
        self.wait(2)
