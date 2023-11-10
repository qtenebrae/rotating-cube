from settings import *
import moderngl as mgl
from world_objects.chunk import Chunk
from meshes.block_mesh import BlockMesh


class Scene:
    """Класс Scene отвечает за управление и отображение объектов, которые находятся в данной сцене."""

    def __init__(self, app):
        """
        Инициализирует объект Scene.

        Parameters:
            app (VoxelEngine): Экземпляр VoxelEngine, к которому принадлежит сцена.
        """
        self.app = app
        self.block = BlockMesh(self.app)

    def update(self):
        """Обновляет состояние сцены."""
        self.block.update()

    def render(self):
        """Отрисовывает сцену."""
        self.block.render()
