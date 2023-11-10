from settings import *


class ShaderProgram:
    """Класс ShaderProgram представляет шейдерную программу в графическом приложении."""

    def __init__(self, app):
        """
        Инициализирует объект ShaderProgram.

        Parameters:
            app (VoxelEngine): Экземпляр VoxelEngine, к которому принадлежит шейдерная программа.
        """
        self.app = app
        self.ctx = app.ctx
        self.player = app.player
        self.block = self.get_program(shader_name='block')
        self.set_uniforms_on_init()

    def set_uniforms_on_init(self):
        """
        Устанавливает значения uniform-переменных шейдерной программы при инициализации.
        """
        self.block['m_proj'].write(self.player.m_proj)
        self.block['m_model'].write(glm.mat4())

        textures = [0, 1, 2, 3, 4, 5]
        self.block['u_textures'].value = textures

    def update(self):
        """
        Обновляет значения uniform-переменных шейдерной программы.
        """
        self.block['m_view'].write(self.player.m_view)

    def get_program(self, shader_name):
        """
        Загружает и компилирует шейдерные программы из файлов вершинного и фрагментного шейдеров.

        Parameters:
            shader_name (str): Имя шейдера.

        Returns:
            moderngl.Program: Объект шейдерной программы.
        """
        with open(f'shaders/{shader_name}.vert', encoding='utf-8') as file:
            vertex_shader = file.read()

        with open(f'shaders/{shader_name}.frag', encoding='utf-8') as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program
