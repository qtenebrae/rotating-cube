import pygame as pg
import moderngl as mgl


class Textures:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx

        # load textures
        self.textures = [
            self.load('texture.jpg'),
            self.load('texture1.jpg'),
            self.load('cat.jpg'),
            self.load('texture3.jpg'),
            self.load('texture4.jpg'),
            self.load('texture5.jpg')
        ]
        # assign texture units
        for i, texture in enumerate(self.textures):
            texture.use(location=i)

    def load(self, file_name, is_tex_array=False):
        texture = pg.image.load(f'assets/{file_name}')
        texture = pg.transform.flip(texture, flip_x=True, flip_y=False)

        texture = self.ctx.texture(
            size=texture.get_size(),
            components=4,
            data=pg.image.tostring(texture, 'RGBA', False))
        texture.anisotropy = 32.0
        texture.build_mipmaps()
        texture.filter = (mgl.NEAREST, mgl.NEAREST)
        return texture
