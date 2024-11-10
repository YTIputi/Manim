from manim import *

class RotateSphereExample(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = Sphere(radius=1, color=BLUE)
        self.add(axes, sphere)
        
        # Устанавливаем начальный угол
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Анимация вращения сферы
        self.play(Rotate(sphere, angle=PI * 100, axis=RIGHT))
        self.wait(2)
