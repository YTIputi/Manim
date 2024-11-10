from manim import *

class CameraMovementExample(MovingCameraScene):
    def construct(self):
        circle = Circle()
        square = Square().shift(RIGHT * 3)
        self.add(circle, square)

        self.camera.frame.move_to(circle)
        self.play(self.camera.frame.animate.scale(0.5))

        self.play(self.camera.frame.animate.move_to(square).scale(2))
        self.play(self.camera.frame.animate.scale(0.5))
        self.play(self.camera.frame.animate.scale(2))