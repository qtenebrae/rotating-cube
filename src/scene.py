from settings import *
import moderngl as mgl
from world_objects.chunk import Chunk
from meshes.block_mesh import BlockMesh


class Scene:
    def __init__(self, app):
        self.app = app
        self.block = BlockMesh(self.app)

    def update(self):
        self.block.update()

    def render(self):
        self.block.render()
