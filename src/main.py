from src.settings import *
import moderngl as mgl
import pygame as pg
import sys
from src.shader_program import ShaderProgram
from src.scene import Scene
from player import Player
from src.textures import Textures


class VoxelEngine:
    """Класс VoxelEngine представляет собой движок для работы с воксельными объектами в графическом приложении"""

    def __init__(self):
        """
        Инициализирует объект VoxelEngine и настраивает окружение для отрисовки с помощью Pygame и ModernGL.
        """
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

        pg.display.set_mode(WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()

        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = 'auto'

        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        self.is_running = True
        self.on_init()

    def on_init(self):
        """
        Вызывается при инициализации VoxelEngine и создает необходимые объекты,
        такие как Textures, Player, ShaderProgram и Scene.
        """
        self.textures = Textures(self)
        self.player = Player(self)
        self.shader_program = ShaderProgram(self)
        self.scene = Scene(self)

    def update(self):
        """Обновляет состояние игровых объектов, ShaderProgram и Scene."""
        self.player.update()
        self.shader_program.update()
        self.scene.update()

        self.delta_time = self.clock.tick()
        self.time = pg.time.get_ticks() * 0.001
        pg.display.set_caption(f'{self.clock.get_fps() :.0f}')

    def render(self):
        """
        Очищает экран, отрисовывает сцену и обновляет дисплей.
        """
        self.ctx.clear(color=BG_COLOR)
        self.scene.render()
        pg.display.flip()

    def handle_events(self):
        """
        Обрабатывает события Pygame, такие как нажатие клавиш или выход из приложения.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False

    def run(self):
        """
        Запускает основной цикл приложения, обрабатывает события,
        обновляет и отрисовывает сцену, пока приложение работает.
        """
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()


if __name__ == '__main__':
    app = VoxelEngine()
    app.run()
