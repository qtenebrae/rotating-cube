from src.settings import *


class Camera:
    """Класс Camera представляет камеру в трехмерной сцене и отвечает за управление ее позицией и направлением."""

    def __init__(self, position, yaw, pitch):
        """
        Инициализирует объект Camera с заданной позицией, углами поворота (yaw, pitch)
        и устанавливает начальные векторы направления.

        Parameters:
            position (tuple, optional): позиция камеры в трехмерном пространстве.
            yaw (float, optional): угол поворота камеры по горизонтали.
            pitch (float, optional): угол поворота камеры по вертикали.
        """
        self.position = glm.vec3(position)
        self.yaw = glm.radians(yaw)
        self.pitch = glm.radians(pitch)

        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)

        self.m_proj = glm.perspective(V_FOV, ASPECT_RATIO, NEAR, FAR)
        self.m_view = glm.mat4()

    def update(self):
        """Обновляет векторы направления и матрицу вида камеры."""
        self.update_vectors()
        self.update_view_matrix()

    def update_view_matrix(self):
        """Обновляет матрицу вида камеры на основе текущей позиции и направления."""
        self.m_view = glm.lookAt(self.position, self.position + self.forward, self.up)

    def update_vectors(self):
        """Обновляет векторы направления камеры на основе текущих углов поворота."""
        self.forward.x = glm.cos(self.yaw) * glm.cos(self.pitch)
        self.forward.y = glm.sin(self.pitch)
        self.forward.z = glm.sin(self.yaw) * glm.cos(self.pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def rotate_pitch(self, delta_y):
        """
        Поворачивает камеру по вертикали на заданный угол.

        :param delta_y: изменение угла поворота по вертикали
        """
        self.pitch -= delta_y
        self.pitch = glm.clamp(self.pitch, -PITCH_MAX, PITCH_MAX)

    def rotate_yaw(self, delta_x):
        """
        Поворачивает камеру по горизонтали на заданный угол.

        :param delta_x: изменение угла поворота по горизонтали
        """
        self.yaw += delta_x

    def move_left(self, velocity):
        """Перемещает камеру влево на заданное расстояние."""
        self.position -= self.right * velocity

    def move_right(self, velocity):
        """Перемещает камеру вправо на заданное расстояние."""
        self.position += self.right * velocity

    def move_up(self, velocity):
        """Перемещает камеру вверх на заданное расстояние."""
        self.position += self.up * velocity

    def move_down(self, velocity):
        """Перемещает камеру вниз на заданное расстояние."""
        self.position -= self.up * velocity

    def move_forward(self, velocity):
        """Перемещает камеру вперед на заданное расстояние."""
        self.position += self.forward * velocity

    def move_back(self, velocity):
        """Перемещает камеру назад на заданное расстояние."""
        self.position -= self.forward * velocity
