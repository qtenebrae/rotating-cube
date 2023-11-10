import pygame as pg
import moderngl as mgl


class Textures:
    """Класс Textures отвечает за управление текстурами в графической среде, используемой в приложении или игре."""

    def __init__(self, app):
        """
        Инициализирует объект Textures.

        Parameters:
            app (VoxelEngine): Экземпляр VoxelEngine, к которому принадлежат текстуры.
        """
        self.app = app
        self.ctx = app.ctx

        # load textures
        self.textures = [
            self.load('texture.jpg'),
            self.load('texture1.jpg'),
            self.load('texture2.jpg'),
            self.load('texture3.jpg'),
            self.load('texture4.jpg'),
            self.load('texture5.jpg')
        ]
        # assign texture units
        for i, texture in enumerate(self.textures):
            texture.use(location=i)

    def load(self, file_name, is_tex_array=False):
        """
        Загружает текстуру из файла и выполняет необходимые операции для подготовки ее к использованию.

        Parameters:
            file_name (str): Имя файла текстуры.
            is_tex_array (bool, optional): Флаг, указывающий, является ли текстура массивом текстур. По умолчанию False.

        Returns:
            moderngl.Texture: Объект текстуры.
        """
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
