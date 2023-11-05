from settings import *
import moderngl as mgl
from world_objects.chunk import Chunk
from meshes.block_mesh import Block


class Scene:
    def __init__(self, app):
        self.app = app
        self.chunk = Block(self.app)

    def update(self):
        self.chunk.update()

    def render(self):
        self.chunk.render()
