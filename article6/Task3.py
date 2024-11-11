from manim import *

# class DepthExample(ThreeDScene):
#     def construct(self):
#         # Создаем куб для демонстрации глубины сцены
#         cube = Cube().set_color([RED, BLUE]).set_opacity(0.5)
#         self.add(cube)
        
#         # Устанавливаем начальный угол камеры
#         self.set_camera_orientation(phi=PI/3, theta=PI/4, distance=1)

#         # Анимация вращения камеры
#         self.begin_ambient_camera_rotation(rate=1)
#         self.wait(5)
#         self.stop_ambient_camera_rotation()



class CustomLightingAndDepthScene(ThreeDScene):
    def construct(self):
        # Создание объектов
        sphere = Sphere(radius=1).set_color([RED, ORANGE]).shift(LEFT * 3)
        cube = Cube(side_length=1.5).set_color(GREEN).set_opacity(0.7)
        cone = Cone(base_radius=1, height=2).set_color(BLUE).shift(RIGHT * 3)

        # Позиция "тени" для сферы
        shadow = Sphere(radius=1.05).set_color(BLACK).set_opacity(0.3).shift(LEFT * 3 + DOWN * 0.1)

        # Настройка камеры
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES, distance=8)
        self.add(sphere, shadow, cube, cone)
        self.wait(2)
