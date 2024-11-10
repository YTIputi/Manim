from manim import *

class ThreeDSceneExample(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = Sphere(radius=1, color=BLUE).shift(LEFT * 2)
        cube = Cube().shift(RIGHT * 2)
        self.add(axes, sphere, cube)

        # Установка начального угла обзора
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        
        # Плавное вращение камеры вокруг сцены
        self.begin_ambient_camera_rotation(rate=0.1)
        
        # Плавное приближение камеры к сфере
        self.move_camera(phi=60 * DEGREES, theta=45 * DEGREES, zoom=1.5)
        self.wait(3)
        
        # Возвращение к исходному положению
        self.move_camera(phi=75 * DEGREES, theta=45 * DEGREES, zoom=1)
        self.wait(2)