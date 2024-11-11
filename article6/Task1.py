from manim import *

class Basic3DObjects(ThreeDScene):
    def construct(self):
        # Создаем 3D-сферу, куб и конус
        sphere = Sphere(radius=1).shift(LEFT * 3)
        cube = Cube(side_length=1.5).shift(RIGHT * 3)
        cone = Cone(base_radius=1, height=2)

        
        # Добавляем объекты на сцену
        self.add(sphere, cube, cone)
        # Установка начального угла обзора
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        
        # Плавное вращение камеры вокруг сцены
        self.begin_ambient_camera_rotation(rate=1)
        self.wait(10)
